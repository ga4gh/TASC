"""Discover TASC documents and turn them into validated index entries."""

from __future__ import annotations

import datetime
import json
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

from tasc_index.descriptions import MAX_LENGTH, derive_description
from tasc_index.models import ID_PATTERNS, STATUS_ENUMS, DocType, Document
from tasc_index.parsing import ParseError, parse_adr_title, parse_h1, parse_metadata

DEFAULT_REPO_URL = "https://github.com/ga4gh/TASC"
DEFAULT_BRANCH = "main"
MAX_SHORT_NAME = 60

# Directory -> document type. `drafts/` holds work in progress of any type, so
# its files are classified from their content instead (see `infer_type`).
SOURCES: dict[str, DocType | None] = {
    "adr": DocType.ADR,
    "recommendations": DocType.RECOMMENDATION,
    "governance": DocType.GOVERNANCE,
    "drafts": None,
}

# Files that live beside real documents but are not documents themselves.
EXCLUDED_FILENAMES = {"template.md", "readme.md"}


@dataclass(frozen=True)
class IndexSpec:
    """One generated index file: which document types it lists."""

    name: str
    types: frozenset[DocType]

    @property
    def filename(self) -> str:
        return f"{self.name}-index.json"

    @property
    def schema_filename(self) -> str:
        return f"{self.name}-index.schema.json"


# ADRs are immutable decision records; recommendations and governance documents
# are living policy (see TASC_Document_Standards.md), so they share an index.
INDEXES = (
    IndexSpec("adr", frozenset({DocType.ADR})),
    IndexSpec("recommendation", frozenset({DocType.RECOMMENDATION, DocType.GOVERNANCE})),
)

# Metadata field holding the identifier for non-ADR documents (ADRs use the H1).
_ID_FIELDS = {
    DocType.RECOMMENDATION: "recommendation",
    DocType.GOVERNANCE: "document id",
}


class IndexBuildError(Exception):
    """One or more documents are invalid. ``errors`` lists every problem found."""

    def __init__(self, errors: list[str]):
        super().__init__("\n".join(errors))
        self.errors = errors


@dataclass
class BuildResult:
    documents: list[Document] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def infer_type(text: str) -> DocType:
    """Classify a draft by its identifying marker; raises ParseError if none is found."""
    meta = parse_metadata(text)
    if parse_h1(text).startswith("TASC-ADR-"):
        return DocType.ADR
    for doc_type, field_name in _ID_FIELDS.items():
        if field_name in meta:
            return doc_type
    raise ParseError(
        "cannot tell what kind of document this is: expected a 'TASC-ADR-NNN:' title, "
        "a 'Recommendation' field or a 'Document ID' field"
    )


def discover(root: Path) -> list[tuple[Path, DocType | None]]:
    """Return (path, type) for every indexable markdown file, in stable order.

    The type is None for files whose type must be inferred from their content.
    """
    found = []
    for directory, doc_type in SOURCES.items():
        for path in sorted((root / directory).glob("*.md")):
            if path.name.lower() not in EXCLUDED_FILENAMES:
                found.append((path, doc_type))
    return found


def build_url(rel_path: str, repo_url: str = DEFAULT_REPO_URL, branch: str = DEFAULT_BRANCH) -> str:
    return f"{repo_url.rstrip('/')}/blob/{branch}/{quote(rel_path)}"


def parse_document(
    path: Path,
    doc_type: DocType | None,
    root: Path,
    *,
    repo_url: str = DEFAULT_REPO_URL,
    branch: str = DEFAULT_BRANCH,
) -> tuple[Document, list[str]]:
    """Parse one file. Returns the entry and any warnings; raises ParseError."""
    text = path.read_text(encoding="utf-8")
    meta = parse_metadata(text)
    warnings: list[str] = []
    if doc_type is None:
        doc_type = infer_type(text)

    if doc_type is DocType.ADR:
        title = parse_adr_title(text)
        doc_id, name = title.id, title.name
        if path.stem != doc_id and not path.stem.startswith(f"{doc_id} "):
            raise ParseError(
                f"file name '{path.name}' must be '{doc_id} Short Name.md' (or '{doc_id}.md')"
            )
    else:
        doc_id = meta.get(_ID_FIELDS[doc_type], "")
        name = meta.get("title", "")
        if not doc_id:
            raise ParseError(f"missing '{_ID_FIELDS[doc_type]}' metadata field")
        if not name:
            raise ParseError("missing 'Title' metadata field")

    if not ID_PATTERNS[doc_type].match(doc_id):
        raise ParseError(f"identifier '{doc_id}' does not match {ID_PATTERNS[doc_type].pattern}")

    date = meta.get("date", "")
    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        raise ParseError(f"date '{date}' is not a valid YYYY-MM-DD date") from None

    status = meta.get("status", "")
    allowed = [s.value for s in STATUS_ENUMS[doc_type]]
    if status not in allowed:
        raise ParseError(f"status '{status}' is not one of {allowed}")

    description = meta.get("description", "")
    if not description:
        description = derive_description(doc_type, text)
        warnings.append(f"{doc_id}: no Description field, derived from document text")
    if not description:
        raise ParseError("no description available (add a 'Description' metadata field)")
    if len(description) > MAX_LENGTH:
        raise ParseError(f"description is longer than {MAX_LENGTH} characters")

    short_name = None
    if doc_type is DocType.ADR:
        short_name = path.stem[len(doc_id) :].strip()
        if not short_name:
            short_name = name
            warnings.append(f"{doc_id}: no short name in the file name, using the full title")
        elif len(short_name) > MAX_SHORT_NAME:
            raise ParseError(f"short name is longer than {MAX_SHORT_NAME} characters")

    rel_path = path.relative_to(root).as_posix()
    document = Document(
        id=doc_id,
        type=doc_type,
        name=name,
        date=date,
        status=status,
        description=description,
        path=rel_path,
        url=build_url(rel_path, repo_url, branch),
        short_name=short_name,
    )
    return document, warnings


def build_index(
    root: Path,
    *,
    strict: bool = False,
    repo_url: str = DEFAULT_REPO_URL,
    branch: str = DEFAULT_BRANCH,
) -> BuildResult:
    """Build the index for every document under ``root``.

    All problems are collected before raising so a contributor can fix them in
    one pass. With ``strict``, a missing ``Description`` field or ADR short name is an error.
    """
    result = BuildResult()
    errors: list[str] = []
    seen: dict[str, str] = {}

    for path, doc_type in discover(root):
        rel = path.relative_to(root).as_posix()
        try:
            document, warnings = parse_document(
                path, doc_type, root, repo_url=repo_url, branch=branch
            )
        except ParseError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if document.id in seen:
            errors.append(
                f"{rel}: duplicate identifier '{document.id}' (also in {seen[document.id]})"
            )
            continue
        seen[document.id] = rel
        result.documents.append(document)
        result.warnings.extend(warnings)

    if strict:
        errors.extend(
            w for w in result.warnings if "no Description field" in w or "no short name" in w
        )
    if errors:
        raise IndexBuildError(errors)

    type_order = list(DocType)
    result.documents.sort(key=lambda d: (type_order.index(d.type), d.id))
    return result


def documents_for(documents: list[Document], types: frozenset[DocType]) -> list[Document]:
    return [d for d in documents if d.type in types]


def render_index(documents: list[Document], schema_ref: str | None = None) -> str:
    """Serialise deterministically (no timestamps) so unchanged input gives an unchanged file."""
    payload: dict[str, object] = {}
    if schema_ref:
        payload["$schema"] = schema_ref
    payload["documents"] = [d.to_dict() for d in documents]
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
