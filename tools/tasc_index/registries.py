"""Index of the registries TASC maintains under ``registries/``.

Registries are operational data (a YAML/JSON file plus a README on how to change
it), not documents: they have no identifier, date or status, so they are not
numbered and are not part of the ADR/recommendation indexes.

Each registry describes itself in its own README, using the same bold-key header
as the other TASC documents::

    # Service Info Types

    **Description**: One sentence, max 300 characters.
    **Defined by**: GA4GH-REC-02
    **Data file**: ga4gh-service-info.json
    **External location**: https://example.org/where-entries-live

``Defined by`` is mandatory but may be blank or ``None`` when no TASC document
defines the registry. A registry needs a ``Data file`` (entries live in its
directory), an ``External location`` (entries live elsewhere), or both.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from tasc_index.builder import DEFAULT_BRANCH, DEFAULT_REPO_URL, IndexBuildError, build_url
from tasc_index.descriptions import MAX_LENGTH
from tasc_index.parsing import ParseError, parse_h1, parse_metadata

REGISTRIES_DIR = "registries"
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
NO_DOCUMENT = {"", "none", "n/a", "-"}


@dataclass(frozen=True)
class RegistryEntry:
    """One entry in the generated registry index."""

    slug: str
    name: str
    description: str
    path: str  # the registry's README
    url: str
    hosting: str  # "repository": data lives here; "external": maintained elsewhere
    defined_by: tuple[str, ...] = ()
    data_path: str | None = None
    data_url: str | None = None
    external_url: str | None = None

    def to_dict(self) -> dict[str, object]:
        data: dict[str, object] = {
            "slug": self.slug,
            "name": self.name,
            "description": self.description,
            "path": self.path,
            "url": self.url,
            "hosting": self.hosting,
            "defined_by": list(self.defined_by),
        }
        for key in ("data_path", "data_url", "external_url"):
            if getattr(self, key) is not None:
                data[key] = getattr(self, key)
        return data


def _parse_defined_by(value: str) -> tuple[str, ...]:
    if value.strip().lower() in NO_DOCUMENT:
        return ()
    return tuple(part.strip() for part in value.split(",") if part.strip())


def _parse_registry(
    root: Path, directory: Path, known_ids: set[str], repo_url: str, branch: str
) -> tuple[RegistryEntry | None, list[str]]:
    slug = directory.name
    label = f"{REGISTRIES_DIR}/{slug}"
    readme_rel = f"{label}/README.md"
    readme = directory / "README.md"
    errors: list[str] = []

    if not SLUG_PATTERN.match(slug):
        errors.append(f"{label}: directory name must be lower-case kebab-case")
    if not readme.is_file():
        return None, [*errors, f"{label}: needs a README.md describing the registry"]

    text = readme.read_text(encoding="utf-8")
    meta = parse_metadata(text)
    try:
        name = parse_h1(text)
    except ParseError:
        name = ""
        errors.append(f"{readme_rel}: needs a level-1 heading naming the registry")

    description = meta.get("description", "")
    if not description:
        errors.append(f"{readme_rel}: missing 'Description' header field")
    elif len(description) > MAX_LENGTH:
        errors.append(f"{readme_rel}: Description is longer than {MAX_LENGTH} characters")

    if "defined by" not in meta:
        errors.append(
            f"{readme_rel}: missing 'Defined by' header field (leave it blank or write None "
            "if no ADR, recommendation or governance document defines the registry)"
        )
    defined_by = _parse_defined_by(meta.get("defined by", ""))
    errors.extend(
        f"{readme_rel}: Defined by '{doc_id}' is not an indexed ADR, recommendation or "
        "governance document"
        for doc_id in defined_by
        if doc_id not in known_ids
    )

    data_file = meta.get("data file") or None
    external_url = meta.get("external location") or None
    data_path = None
    if data_file:
        if PurePosixPath(data_file).name != data_file or data_file.startswith("."):
            errors.append(f"{readme_rel}: Data file must be a file name inside {label}/")
        else:
            data_path = f"{label}/{data_file}"
            if not (root / data_path).is_file():
                errors.append(f"{readme_rel}: Data file {data_path} does not exist")
    if not data_file and not external_url:
        errors.append(
            f"{readme_rel}: needs a 'Data file' or an 'External location' (where entries live)"
        )

    if errors:
        return None, errors
    return (
        RegistryEntry(
            slug=slug,
            name=name,
            description=description,
            path=readme_rel,
            url=build_url(readme_rel, repo_url, branch),
            hosting="external" if external_url and not data_file else "repository",
            defined_by=defined_by,
            data_path=data_path,
            data_url=build_url(data_path, repo_url, branch) if data_path else None,
            external_url=external_url,
        ),
        [],
    )


def build_registry_index(
    root: Path,
    *,
    known_ids: set[str],
    repo_url: str = DEFAULT_REPO_URL,
    branch: str = DEFAULT_BRANCH,
) -> list[RegistryEntry]:
    """Index every directory under ``registries/``, in slug order.

    Every problem is collected before raising. ``known_ids`` are the identifiers of
    the indexed documents that a registry may name in ``Defined by``.
    """
    entries: list[RegistryEntry] = []
    errors: list[str] = []
    for directory in sorted((root / REGISTRIES_DIR).iterdir()):
        if not directory.is_dir():
            continue
        entry, problems = _parse_registry(root, directory, known_ids, repo_url, branch)
        errors.extend(problems)
        if entry:
            entries.append(entry)
    if errors:
        raise IndexBuildError(errors)
    return entries


def render_registry_index(entries: list[RegistryEntry], schema_ref: str | None = None) -> str:
    """Serialise deterministically (no timestamps), like the document indexes."""
    payload: dict[str, object] = {}
    if schema_ref:
        payload["$schema"] = schema_ref
    payload["registries"] = [e.to_dict() for e in entries]
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
