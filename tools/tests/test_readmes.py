import json

from conftest import REPO_ROOT

from tasc_index.readmes import (
    RECENT_END,
    RECENT_START,
    generate,
    latest,
    render_adr_readme,
    render_recent_section,
    render_recommendation_readme,
    splice_recent,
)


def adr(n, status="Accepted", date="2026-01-01", path=None):
    return {
        "id": f"TASC-ADR-{n:03}",
        "type": "adr",
        "name": f"Long title {n}",
        "short_name": f"Short {n}",
        "date": date,
        "status": status,
        "description": "A | B",
        "path": path or f"adr/TASC-ADR-{n:03}.md",
    }


def rec(n, short_name="Short rec", doc_type="recommendation"):
    prefix = "GA4GH-REC" if doc_type == "recommendation" else "TASC-GOV"
    return {
        "id": f"{prefix}-{n:02}",
        "type": doc_type,
        "name": f"Long recommendation title {n}",
        "date": "2026-01-01",
        "status": "Approved",
        "description": "d",
        "path": f"recommendations/{prefix}-{n:02} {short_name}.md",
        "short_name": short_name,
    }


def test_recommendation_readme_links_the_id_and_short_name_for_governance_too():
    text = render_recommendation_readme([rec(1), rec(1, "Charter", doc_type="governance")])
    assert "[GA4GH-REC-01 Short rec](GA4GH-REC-01%20Short%20rec.md)" in text
    assert "[TASC-GOV-01 Charter](TASC-GOV-01%20Charter.md)" in text


def test_recent_recommendations_are_labelled_with_id_and_short_name():
    assert "[GA4GH-REC-01 Short rec]" in render_recent_section([], [rec(1)])


def test_recent_governance_documents_are_approved_ones_with_id_and_short_name():
    docs = [rec(1, "Charter", doc_type="governance"), rec(2, "Draft one", doc_type="governance")]
    docs[1]["status"] = "Draft"
    section = render_recent_section([], docs)
    assert "### Governance" in section
    assert "[TASC-GOV-01 Charter]" in section
    assert "TASC-GOV-02" not in section
    # Governance documents are not listed under Recommendations.
    assert section.index("### Governance") > section.index("### Recommendations")
    assert "TASC-GOV-01" not in section.split("### Governance")[0]


def test_latest_is_newest_first_and_limited():
    docs = [adr(1, date="2026-01-01"), adr(2, date="2026-03-01"), adr(4, date="2026-02-01"),
            adr(5, date="2026-03-01")]  # fmt: skip
    assert [d["id"] for d in latest(docs)] == ["TASC-ADR-005", "TASC-ADR-002", "TASC-ADR-004"]


def test_recent_adrs_are_only_the_accepted_ones():
    docs = [adr(1, status="Accepted"), adr(2, status="Proposed"), adr(3, status="Draft")]
    section = render_recent_section(docs, [])
    assert "TASC-ADR-001" in section
    assert "TASC-ADR-002" not in section
    assert "TASC-ADR-003" not in section
    assert "(2026-01-01)" in section


def test_adr_readme_uses_short_heading_relative_links_and_escapes_pipes():
    text = render_adr_readme([adr(1), adr(2, status="Draft", path="drafts/TASC-ADR-002.md")])
    assert "[TASC-ADR-001 Short 1](TASC-ADR-001.md)" in text
    assert "(../drafts/TASC-ADR-002.md)" in text
    assert "A \\| B" in text


def test_recent_section_says_so_when_nothing_is_approved():
    assert "_None yet._" in render_recent_section([adr(1, status="Draft")], [])


def test_splice_inserts_once_then_replaces():
    readme = "# T\n\n## Table of Contents\n\nx\n"
    once = splice_recent(readme, f"{RECENT_START}\nA\n{RECENT_END}\n")
    twice = splice_recent(once, f"{RECENT_START}\nB\n{RECENT_END}\n")
    assert once.count(RECENT_START) == twice.count(RECENT_START) == 1
    assert "\nB\n" in twice
    assert "\nA\n" not in twice
    assert twice.endswith("## Table of Contents\n\nx\n")


def test_generate_reads_only_the_index_files(repo, tmp_path):
    (repo / "README.md").write_text("## Table of Contents\n")
    docs = [adr(1)]
    (repo / "index" / "adr-index.json").write_text(json.dumps({"documents": docs}))
    (repo / "index" / "recommendation-index.json").write_text(json.dumps({"documents": []}))
    (repo / "index" / "registry-index.json").write_text(json.dumps({"registries": []}))
    generate(repo, repo / "index")
    assert "Short 1" in (repo / "adr" / "README.md").read_text()
    assert "TASC-ADR-001 Short 1" in (repo / "README.md").read_text()


def test_committed_readmes_are_up_to_date():
    """Fails when the indexes changed but the READMEs were not regenerated."""
    root = REPO_ROOT
    adrs = json.loads((root / "index" / "adr-index.json").read_text())["documents"]
    assert (root / "adr" / "README.md").read_text() == render_adr_readme(adrs)
