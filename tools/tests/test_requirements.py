import json

import pytest
from conftest import REPO_ROOT

from tasc_index.readmes import generate
from tasc_index.requirements import (
    CATEGORIES,
    load_requirements,
    render_requirements_readme,
    validate_requirements,
)

DOCS = {
    "TASC-ADR-001": {"id": "TASC-ADR-001", "status": "Accepted", "date": "2026-03-23",
                     "path": "adr/TASC-ADR-001.md"},
    "TASC-ADR-002": {"id": "TASC-ADR-002", "status": "Accepted", "date": "2026-07-07",
                     "path": "adr/TASC-ADR-002.md"},
    "TASC-ADR-003": {"id": "TASC-ADR-003", "status": "Draft", "date": "2026-08-01",
                     "path": "drafts/TASC-ADR-003.md"},
    "GA4GH-REC-01": {"id": "GA4GH-REC-01", "status": "Approved", "date": "2025-01-01",
                     "path": "recommendations/Rec.md"},
}  # fmt: skip
REGISTRIES = {"service-info": {"slug": "service-info", "path": "registries/service-info/README.md"}}


def req(**overrides):
    base = {
        "name": "Widgets",
        "category": "ownership",
        "details": "Every product has a widget.",
        "applies": "On approval",
        "documents": ["TASC-ADR-001"],
    }
    return {**base, **overrides}


def errors(*reqs):
    return validate_requirements(list(reqs), DOCS, REGISTRIES)


def test_a_valid_requirement_has_no_errors():
    assert errors(req()) == []


def test_unknown_category_is_rejected():
    assert any("category" in e for e in errors(req(category="vibes")))


def test_unknown_document_id_is_rejected():
    assert any("TASC-ADR-099" in e for e in errors(req(documents=["TASC-ADR-099"])))


def test_unknown_registry_is_rejected():
    assert any("nope" in e for e in errors(req(registries=["nope"])))


def test_requirement_needs_all_core_fields():
    bad = req()
    del bad["applies"]
    assert any("applies" in e for e in errors(bad))


def test_requirement_with_no_document_must_state_its_own_status():
    assert any("status" in e for e in errors(req(documents=[], references=["PDAP v3.0 §7.3"])))
    assert errors(req(documents=[], references=["PDAP v3.0 §7.3"], status="Approved")) == []


def test_requirement_with_nothing_to_cite_is_rejected():
    assert errors(req(documents=[], status="Approved"))


def test_duplicate_names_are_rejected():
    assert any("duplicate" in e.lower() for e in errors(req(), req()))


def render(*reqs):
    return render_requirements_readme(list(reqs), list(DOCS.values()), list(REGISTRIES.values()))


def test_status_and_date_come_from_the_referenced_documents():
    text = render(req(documents=["TASC-ADR-001", "TASC-ADR-002"]))
    row = next(line for line in text.splitlines() if line.startswith("| Widgets"))
    assert "| Approved |" in row
    assert "2026-07-07" in row  # the latest of the two documents


def test_a_document_still_in_draft_shows_as_draft_adr():
    row = next(
        line
        for line in render(req(documents=["TASC-ADR-003"])).splitlines()
        if line.startswith("| Widgets")
    )
    assert "Draft ADR" in row


def test_explicit_status_overrides_the_derived_one():
    assert "| Recommended | " in render(req(status="Recommended"))


def test_date_always_comes_from_the_documents_and_cannot_be_set_on_a_requirement():
    assert any("date" in e for e in errors(req(date="2020-02-02")))
    row = next(line for line in render(req()).splitlines() if line.startswith("| Widgets"))
    assert row.endswith("| 2026-03-23 |")


def test_documentation_column_links_documents_registries_and_plain_references():
    text = render(req(documents=["TASC-ADR-001"], registries=["service-info"],
                      references=["PDAP v3.0 §7.3"]))  # fmt: skip
    assert "[TASC-ADR-001](../adr/TASC-ADR-001.md)" in text
    assert "[service-info/](../registries/service-info/README.md)" in text
    assert "PDAP v3.0 §7.3" in text


def test_requirements_are_grouped_under_their_category_in_the_fixed_order():
    text = render(req(name="B", category="citation"), req(name="A", category="repository-website"))
    headings = [line for line in text.splitlines() if line.startswith("## ")]
    assert headings == ["## 1. Repository and website", "## 5. Citation"]
    assert [c.slug for c in CATEGORIES][:2] == ["repository-website", "starter-kit-conformance"]


def test_pipes_in_cells_are_escaped():
    assert "a \\| b" in render(req(details="a | b"))


def test_generate_writes_the_requirements_page_when_a_source_exists(repo):
    (repo / "README.md").write_text("## Table of Contents\n")
    (repo / "index" / "adr-index.json").write_text(
        json.dumps({"documents": [{**DOCS["TASC-ADR-001"], "type": "adr", "name": "n",
                                   "short_name": "s", "description": "d"}]})
    )  # fmt: skip
    (repo / "index" / "recommendation-index.json").write_text(json.dumps({"documents": []}))
    (repo / "index" / "registry-index.json").write_text(json.dumps({"registries": []}))
    (repo / "requirements").mkdir()
    (repo / "requirements" / "requirements.json").write_text(json.dumps({"requirements": [req()]}))
    generate(repo, repo / "index")
    assert "Widgets" in (repo / "requirements" / "README.md").read_text()


def test_generate_fails_on_an_invalid_requirement(repo):
    (repo / "README.md").write_text("## Table of Contents\n")
    for name, key in [("adr", "documents"), ("recommendation", "documents")]:
        (repo / "index" / f"{name}-index.json").write_text(json.dumps({key: []}))
    (repo / "index" / "registry-index.json").write_text(json.dumps({"registries": []}))
    (repo / "requirements").mkdir()
    (repo / "requirements" / "requirements.json").write_text(
        json.dumps({"requirements": [req(documents=["TASC-ADR-099"])]})
    )
    with pytest.raises(ValueError, match="TASC-ADR-099"):
        generate(repo, repo / "index")


def test_committed_requirements_are_valid_and_up_to_date():
    root = REPO_ROOT
    docs = []
    for name in ("adr", "recommendation"):
        docs += json.loads((root / "index" / f"{name}-index.json").read_text())["documents"]
    registries = json.loads((root / "index" / "registry-index.json").read_text())["registries"]
    reqs = load_requirements(root / "requirements" / "requirements.json")
    assert validate_requirements(reqs, {d["id"]: d for d in docs},
                                 {r["slug"]: r for r in registries}) == []  # fmt: skip
    assert (root / "requirements" / "README.md").read_text() == render_requirements_readme(
        reqs, docs, registries
    )
