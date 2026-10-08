import json

from conftest import adr_text, write

from tasc_index.cli import main


def run(repo, *extra):
    return main(["--root", str(repo), *extra])


def load(repo, name):
    return json.loads((repo / "index" / name).read_text())


def test_writes_separate_schema_valid_indexes(repo, capsys):
    assert run(repo) == 0
    adr = load(repo, "adr-index.json")
    rec = load(repo, "recommendation-index.json")
    assert [d["id"] for d in adr["documents"]] == ["TASC-ADR-001"]
    assert [d["id"] for d in rec["documents"]] == ["GA4GH-REC-01", "TASC-GOV-01"]
    assert adr["$schema"] == "adr-index.schema.json"
    assert rec["$schema"] == "recommendation-index.schema.json"
    assert "Wrote 1 documents" in capsys.readouterr().out


def test_description_is_copied_from_document(repo):
    run(repo)
    assert load(repo, "adr-index.json")["documents"][0]["description"] == "An ADR about widgets."


def test_invalid_document_fails_without_writing(repo, capsys):
    write(repo, "adr/TASC-ADR-001 Widgets.md", adr_text(status="Nope"))
    assert run(repo) == 1
    assert not (repo / "index" / "adr-index.json").exists()
    assert not (repo / "index" / "recommendation-index.json").exists()
    assert "adr/TASC-ADR-001 Widgets.md" in capsys.readouterr().err


def test_strict_flag_fails_on_missing_description(repo):
    write(
        repo,
        "adr/TASC-ADR-001 Widgets.md",
        adr_text().replace("**Description:** An ADR about widgets.\n", ""),
    )
    assert run(repo, "--strict") == 1
    assert run(repo) == 0
