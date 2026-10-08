"""Guards against drift between code, schema, templates and the real documents."""

import json
import re
from enum import Enum

import pytest
from conftest import REPO_ROOT

from tasc_index.builder import build_index
from tasc_index.models import AdrStatus, RecommendationStatus

INDEX_DIR = REPO_ROOT / "index"
ADR_SCHEMA = json.loads((INDEX_DIR / "adr-index.schema.json").read_text())
REC_SCHEMA = json.loads((INDEX_DIR / "recommendation-index.schema.json").read_text())


def values(enum: type[Enum]) -> list[str]:
    return [member.value for member in enum]


def template_statuses(rel_path: str) -> list[str]:
    """Read the '[A | B | C]' list on the template's Status line."""
    text = (REPO_ROOT / rel_path).read_text()
    match = re.search(r"\*\*Status:\*\*\s*\[([^\]]+)\]", text)
    assert match, f"{rel_path} has no '**Status:** [...]' placeholder"
    return [s.strip() for s in match[1].split("|")]


def test_schema_adr_statuses_match_code():
    assert ADR_SCHEMA["$defs"]["adrStatus"]["enum"] == values(AdrStatus)


def test_schema_recommendation_statuses_match_code():
    assert REC_SCHEMA["$defs"]["recommendationStatus"]["enum"] == values(RecommendationStatus)


def test_adr_template_lists_the_adr_statuses():
    assert template_statuses("adr/template.md") == values(AdrStatus)


def test_recommendation_template_lists_the_recommendation_statuses():
    assert template_statuses("recommendations/template.md") == values(RecommendationStatus)


@pytest.mark.parametrize("schema", [ADR_SCHEMA, REC_SCHEMA])
def test_schemas_are_valid_json_schemas(schema):
    from jsonschema import Draft202012Validator

    Draft202012Validator.check_schema(schema)


ENTRY = {
    "name": "n",
    "date": "2026-01-01",
    "description": "d",
    "path": "x.md",
    "url": "https://example.org/x",
}


@pytest.mark.parametrize(
    ("schema", "bad"),
    [
        (ADR_SCHEMA, {"type": "adr", "id": "TASC-ADR-001", "status": "Approved"}),
        (ADR_SCHEMA, {"type": "adr", "id": "GA4GH-REC-01", "status": "Accepted"}),
        (ADR_SCHEMA, {"type": "recommendation", "id": "GA4GH-REC-01", "status": "Approved"}),
        (
            ADR_SCHEMA,
            {
                "type": "adr",
                "id": "TASC-ADR-001",
                "status": "Accepted",
                "short_name": "x",
                "extra": "x",
            },
        ),
        (REC_SCHEMA, {"type": "recommendation", "id": "GA4GH-REC-01", "status": "Accepted"}),
        (REC_SCHEMA, {"type": "governance", "id": "TASC-GOV-01", "status": "Proposed"}),
        (REC_SCHEMA, {"type": "adr", "id": "TASC-ADR-001", "status": "Accepted"}),
    ],
)
def test_schemas_reject_inconsistent_entries(schema, bad):
    from jsonschema import Draft202012Validator

    assert not Draft202012Validator(schema).is_valid({"documents": [{**ENTRY, **bad}]})


@pytest.mark.parametrize(
    ("schema", "good"),
    [
        (ADR_SCHEMA, {"type": "adr", "id": "TASC-ADR-001", "status": "Draft", "short_name": "x"}),
        (REC_SCHEMA, {"type": "recommendation", "id": "GA4GH-REC-01", "status": "Approved"}),
        (REC_SCHEMA, {"type": "governance", "id": "TASC-GOV-01", "status": "Draft"}),
    ],
)
def test_schemas_accept_valid_entries(schema, good):
    from jsonschema import Draft202012Validator

    assert Draft202012Validator(schema).is_valid({"documents": [{**ENTRY, **good}]})


def test_real_repository_documents_are_all_valid():
    """Fails a PR that adds a malformed ADR, recommendation or governance document."""
    result = build_index(REPO_ROOT)
    assert result.documents
    assert not any(d.id.endswith(("XX", "XXX")) for d in result.documents), "template was indexed"


def test_every_real_document_has_a_description_field():
    """New documents must carry their own Description (the templates include the field)."""
    assert build_index(REPO_ROOT, strict=True)


@pytest.mark.parametrize("template", ["adr/template.md", "recommendations/template.md"])
def test_templates_include_a_description_field(template):
    assert "**Description" in (REPO_ROOT / template).read_text()
