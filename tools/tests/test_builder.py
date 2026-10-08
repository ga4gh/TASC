import json

import pytest
from conftest import adr_text, rec_text, write

from tasc_index.builder import (
    INDEXES,
    IndexBuildError,
    build_index,
    build_url,
    discover,
    documents_for,
    render_index,
)
from tasc_index.models import DocType


def build(repo, **kwargs):
    return build_index(repo, **kwargs)


def test_indexes_each_type_with_expected_fields(repo):
    docs = {d.id: d for d in build(repo).documents}
    assert set(docs) == {"TASC-ADR-001", "GA4GH-REC-01", "TASC-GOV-01"}

    adr = docs["TASC-ADR-001"]
    assert (adr.type, adr.name, adr.date, adr.status) == (
        DocType.ADR,
        "Use Widgets",
        "2026-01-02",
        "Accepted",
    )
    assert adr.path == "adr/TASC-ADR-001 Widgets.md"

    rec = docs["GA4GH-REC-01"]
    assert (rec.type, rec.name, rec.status) == (DocType.RECOMMENDATION, "Widget guide", "Approved")


def test_order_is_by_type_then_identifier(repo):
    write(repo, "adr/TASC-ADR-002.md", adr_text("002"))
    write(repo, "recommendations/Another.md", rec_text("GA4GH-REC-02"))
    ids = [d.id for d in build(repo).documents]
    assert ids == ["TASC-ADR-001", "TASC-ADR-002", "GA4GH-REC-01", "GA4GH-REC-02", "TASC-GOV-01"]


def test_templates_and_readmes_are_not_indexed(repo):
    # A template has placeholder values that would otherwise fail validation.
    write(
        repo,
        "adr/template.md",
        "# TASC-ADR-XXX: [Title]\n\n**Date:** YYYY-MM-DD | **Status:** [Proposed]\n",
    )
    write(repo, "recommendations/template.md", "# [Title]\n\n**Recommendation**: GA4GH-REC-XX\n")
    write(repo, "adr/README.md", "# ADRs\n")
    paths = [p.name for p, _ in discover(repo)]
    assert "template.md" not in paths and "README.md" not in paths
    assert len(build(repo).documents) == 3


def test_drafts_are_indexed_and_classified_by_content(repo):
    write(repo, "drafts/TASC-ADR-006.md", adr_text("006", status="Draft"))
    write(repo, "drafts/New rec.md", rec_text("GA4GH-REC-09", status="Draft"))
    docs = {d.id: d for d in build(repo).documents}
    assert docs["TASC-ADR-006"].type is DocType.ADR
    assert docs["TASC-ADR-006"].path == "drafts/TASC-ADR-006.md"
    assert docs["GA4GH-REC-09"].type is DocType.RECOMMENDATION


def test_unclassifiable_draft_is_an_error(repo):
    write(repo, "drafts/notes.md", "# Meeting notes\n\n**Status:** Draft\n")
    with pytest.raises(IndexBuildError, match="cannot tell what kind"):
        build(repo)


def test_draft_is_validated_like_its_type(repo):
    write(repo, "drafts/New rec.md", rec_text("GA4GH-REC-09", status="Accepted"))
    with pytest.raises(IndexBuildError, match="status"):
        build(repo)


def test_url_links_back_to_file_and_encodes_spaces(repo):
    rec = next(d for d in build(repo).documents if d.id == "GA4GH-REC-01")
    assert rec.url == "https://github.com/ga4gh/TASC/blob/main/recommendations/Widget%20guide.md"


def test_build_url_honours_repo_and_branch():
    assert (
        build_url("adr/x.md", "https://example.org/r/", "dev")
        == "https://example.org/r/blob/dev/adr/x.md"
    )


@pytest.mark.parametrize("status", ["Approved", "accepted", ""])
def test_adr_rejects_statuses_outside_its_enum(repo, status):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text(status=status))
    with pytest.raises(IndexBuildError, match="status"):
        build(repo)


@pytest.mark.parametrize("status", ["Accepted", "Proposed", "Deprecated"])
def test_recommendation_rejects_adr_only_statuses(repo, status):
    write(repo, "recommendations/Widget guide.md", rec_text(status=status))
    with pytest.raises(IndexBuildError, match="status"):
        build(repo)


@pytest.mark.parametrize("status", ["Draft", "Proposed", "Accepted", "Deprecated", "Superseded"])
def test_adr_accepts_every_adr_status(repo, status):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text(status=status))
    assert any(d.status == status for d in build(repo).documents)


@pytest.mark.parametrize("date", ["YYYY-MM-DD", "2026-13-01", "01/02/2026", ""])
def test_rejects_invalid_dates(repo, date):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text(date=date))
    with pytest.raises(IndexBuildError, match="date"):
        build(repo)


def test_rejects_adr_file_name_that_disagrees_with_identifier(repo):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text("002"))
    with pytest.raises(IndexBuildError, match="file name .* must be"):
        build(repo)


@pytest.mark.parametrize("doc_id", ["GA4GH-REC-XX", "REC-01", "TASC-ADR-001"])
def test_rejects_malformed_recommendation_identifier(repo, doc_id):
    write(repo, "recommendations/Widget guide.md", rec_text(doc_id))
    with pytest.raises(IndexBuildError, match="identifier"):
        build(repo)


def test_rejects_missing_identifier_field(repo):
    write(repo, "recommendations/Widget guide.md", rec_text(id_field="Something else"))
    with pytest.raises(IndexBuildError, match="missing 'recommendation'"):
        build(repo)


def test_rejects_duplicate_identifiers(repo):
    write(repo, "recommendations/Copy.md", rec_text("GA4GH-REC-01"))
    with pytest.raises(IndexBuildError, match="duplicate identifier 'GA4GH-REC-01'"):
        build(repo)


def test_reports_every_problem_in_one_pass(repo):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text(status="Nope"))
    write(repo, "recommendations/Widget guide.md", rec_text(date="never"))
    with pytest.raises(IndexBuildError) as excinfo:
        build(repo)
    assert len(excinfo.value.errors) == 2


def test_description_comes_from_the_document_header(repo):
    docs = {d.id: d for d in build(repo).documents}
    assert docs["TASC-ADR-001"].description == "An ADR about widgets."
    assert docs["GA4GH-REC-01"].description == "A recommendation about widgets."
    assert build(repo).warnings == []


def test_missing_description_is_derived_with_warning(repo):
    write(
        repo,
        "adr/TASC-ADR-001 Widgets.md",
        adr_text().replace("**Description:** An ADR about widgets.\n", ""),
    )
    result = build(repo)
    adr = next(d for d in result.documents if d.id == "TASC-ADR-001")
    assert adr.description == "We will use widgets."
    assert any("TASC-ADR-001" in w and "derived" in w for w in result.warnings)


def test_strict_mode_requires_a_description_field(repo):
    write(
        repo,
        "adr/TASC-ADR-001 Widgets.md",
        adr_text().replace("**Description:** An ADR about widgets.\n", ""),
    )
    with pytest.raises(IndexBuildError, match="no Description field"):
        build(repo, strict=True)


def test_strict_mode_passes_when_all_described(repo):
    assert build(repo, strict=True).warnings == []


def test_overlong_description_is_rejected(repo):
    write(
        repo, "adr/TASC-ADR-001 Widgets.md", adr_text().replace("An ADR about widgets.", "x" * 301)
    )
    with pytest.raises(IndexBuildError, match="longer than"):
        build(repo)


def test_documents_for_splits_adrs_from_recommendations_and_governance(repo):
    docs = build(repo).documents
    adr_spec, rec_spec = INDEXES
    assert [d.id for d in documents_for(docs, adr_spec.types)] == ["TASC-ADR-001"]
    assert [d.id for d in documents_for(docs, rec_spec.types)] == ["GA4GH-REC-01", "TASC-GOV-01"]
    assert (adr_spec.filename, rec_spec.schema_filename) == (
        "adr-index.json",
        "recommendation-index.schema.json",
    )


def test_render_is_deterministic_and_has_no_timestamp(repo):
    docs = build(repo).documents
    first, second = render_index(docs, "s.json"), render_index(docs, "s.json")
    assert first == second and first.endswith("\n")
    payload = json.loads(first)
    assert payload["$schema"] == "s.json"
    assert list(payload) == ["$schema", "documents"]
    assert list(payload["documents"][0]) == [
        "id",
        "type",
        "name",
        "date",
        "status",
        "description",
        "path",
        "url",
        "short_name",
    ]


def test_adr_short_name_comes_from_the_file_name_and_only_adrs_have_one(repo):
    docs = {d.id: d for d in build(repo).documents}
    assert docs["TASC-ADR-001"].short_name == "Widgets"
    assert docs["GA4GH-REC-01"].short_name is None


def test_adr_file_name_without_short_name_falls_back_to_title_and_fails_strict(repo):
    (repo / "adr" / "TASC-ADR-001 Widgets.md").rename(repo / "adr" / "TASC-ADR-001.md")
    result = build(repo)
    assert result.documents[0].short_name == "Use Widgets"
    assert any("no short name" in w for w in result.warnings)
    with pytest.raises(IndexBuildError, match="no short name"):
        build(repo, strict=True)


def test_overlong_short_name_is_rejected(repo):
    (repo / "adr" / "TASC-ADR-001 Widgets.md").rename(repo / "adr" / f"TASC-ADR-001 {'x' * 61}.md")
    with pytest.raises(IndexBuildError, match="short name is longer"):
        build(repo)
