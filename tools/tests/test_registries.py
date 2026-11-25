import json

import pytest
from conftest import REPO_ROOT, registry_entry, registry_readme, write, write_registry

from tasc_index.builder import IndexBuildError, build_index
from tasc_index.cli import main, validate_against_schema
from tasc_index.readmes import (
    REGISTRIES_END,
    REGISTRIES_START,
    generate,
    render_registries_readme,
    render_registries_section,
    splice_registries,
)
from tasc_index.registries import build_registry_index, render_registry_index

KNOWN = {"GA4GH-REC-01", "TASC-ADR-001"}


def build(repo, known=KNOWN, **kwargs):
    return build_registry_index(repo, known_ids=known, **kwargs)


def errors_of(repo, known=KNOWN):
    with pytest.raises(IndexBuildError) as exc:
        build(repo, known)
    return exc.value.errors


# --- building -------------------------------------------------------------------


def test_entry_has_links_back_to_the_readme_and_data_file(repo):
    (entry,) = build(repo)
    assert entry.slug == "widgets"
    assert entry.path == "registries/widgets/README.md"
    assert entry.url == "https://github.com/ga4gh/TASC/blob/main/registries/widgets/README.md"
    assert entry.data_path == "registries/widgets/widgets.yaml"
    assert entry.data_url.endswith("/blob/main/registries/widgets/widgets.yaml")
    assert entry.hosting == "repository"
    assert entry.defined_by == ("GA4GH-REC-01",)


def test_registry_hosted_elsewhere_needs_no_data_file(repo):
    write_registry(
        repo,
        [
            registry_entry(
                "purls", data_file=None, defined_by="", external_location="https://example.org/x"
            )
        ],
    )
    (entry,) = build(repo)
    assert entry.hosting == "external"
    assert entry.data_path is None
    assert entry.external_url == "https://example.org/x"


def test_entries_are_ordered_by_slug(repo):
    write_registry(repo, [registry_entry("zeta"), registry_entry("alpha")])
    assert [e.slug for e in build(repo)] == ["alpha", "zeta"]


def test_a_registry_directory_without_a_readme_is_an_error(repo):
    """A directory with no README has nothing to index, so it must not slip through."""
    (repo / "registries" / "widgets" / "README.md").unlink()
    assert any("registries/widgets" in e and "README.md" in e for e in errors_of(repo))


def test_registries_are_discovered_from_their_directories(repo):
    write(repo, "registries/extra/README.md", registry_readme(registry_entry("extra")))
    write(repo, "registries/extra/widgets.yaml", "items: []\n")
    assert [e.slug for e in build(repo)] == ["extra", "widgets"]


def test_a_missing_defined_by_line_is_an_error(repo):
    """The field must be stated, even if only to say that nothing defines the registry."""
    write_registry(repo, [registry_entry(defined_by=None)])
    assert any("Defined by" in e for e in errors_of(repo))


@pytest.mark.parametrize("value", ["", "None", "none", "-"])
def test_blank_or_none_defined_by_means_no_document(repo, value):
    write_registry(repo, [registry_entry(defined_by=value)])
    (entry,) = build(repo)
    assert entry.defined_by == ()


def test_several_defining_documents_are_comma_separated(repo):
    write_registry(repo, [registry_entry(defined_by="GA4GH-REC-01, TASC-ADR-001")])
    (entry,) = build(repo)
    assert entry.defined_by == ("GA4GH-REC-01", "TASC-ADR-001")


def test_a_missing_data_file_is_an_error(repo):
    (repo / "registries" / "widgets" / "widgets.yaml").unlink()
    assert any("widgets.yaml" in e for e in errors_of(repo))


def test_defining_document_must_exist(repo):
    write_registry(repo, [registry_entry(defined_by="GA4GH-REC-99")])
    assert any("GA4GH-REC-99" in e for e in errors_of(repo))


def test_a_registry_with_nowhere_to_register_is_an_error(repo):
    write_registry(repo, [registry_entry(data_file=None)])
    assert any("Data file" in e and "External location" in e for e in errors_of(repo))


@pytest.mark.parametrize(
    ("override", "fragment"),
    [
        ({"slug": "Bad Slug"}, "kebab-case"),
        ({"name": ""}, "heading"),
        ({"description": None}, "Description"),
        ({"description": ""}, "Description"),
        ({"description": "x" * 301}, "300"),
        ({"data_file": "../escape.yaml"}, "Data file"),
    ],
)
def test_invalid_fields_are_reported(repo, override, fragment):
    write_registry(repo, [registry_entry(**override)])
    assert any(fragment in e for e in errors_of(repo))


def test_every_problem_is_reported_in_one_run(repo):
    write_registry(
        repo,
        [registry_entry("a", description=None), registry_entry("b", defined_by=None)],
    )
    assert len(errors_of(repo)) == 2


# --- rendering and schema -------------------------------------------------------


def test_rendered_index_satisfies_the_schema(repo):
    rendered = render_registry_index(build(repo), "registry-index.schema.json")
    schema = REPO_ROOT / "index" / "registry-index.schema.json"
    assert validate_against_schema(rendered, schema) == []
    assert json.loads(rendered)["registries"][0]["slug"] == "widgets"


def test_schema_rejects_an_entry_with_unknown_hosting(repo):
    payload = json.loads(render_registry_index(build(repo)))
    payload["registries"][0]["hosting"] = "somewhere"
    schema = REPO_ROOT / "index" / "registry-index.schema.json"
    assert validate_against_schema(json.dumps(payload), schema)


def index_json(repo):
    return json.loads(render_registry_index(build(repo)))["registries"]


DOCS = [
    {
        "id": "GA4GH-REC-01",
        "name": "Widget guide",
        "path": "recommendations/GA4GH-REC-01 Widget guide.md",
    },
    {"id": "TASC-ADR-001", "name": "Widgets", "path": "adr/TASC-ADR-001 Widgets.md"},
]


def test_registries_readme_links_are_relative_to_the_registries_directory(repo):
    text = render_registries_readme(index_json(repo), DOCS)
    assert "[Widget Registry](widgets/README.md)" in text
    assert "[widgets.yaml](widgets/widgets.yaml)" in text
    assert "[GA4GH-REC-01](../recommendations/GA4GH-REC-01%20Widget%20guide.md)" in text


def test_registries_readme_flags_externally_hosted_registries(repo):
    write_registry(
        repo,
        [
            registry_entry(
                "purls", data_file=None, defined_by="", external_location="https://example.org/x"
            )
        ],
    )
    text = render_registries_readme(index_json(repo), DOCS)
    assert "[example.org/x](https://example.org/x)" in text or "https://example.org/x" in text
    assert "outside this repository" in text


def test_unknown_governing_ids_degrade_to_plain_text(repo):
    text = render_registries_readme(index_json(repo), [])
    assert "GA4GH-REC-01" in text
    assert "](../recommendations" not in text


def test_registries_readme_escapes_pipes(repo):
    write_registry(repo, [registry_entry(description="A | B")])
    assert "A \\| B" in render_registries_readme(index_json(repo), DOCS)


def test_root_readme_section_links_to_each_registry(repo):
    section = render_registries_section(index_json(repo))
    assert section.startswith(REGISTRIES_START) and section.rstrip().endswith(REGISTRIES_END)
    assert "[Widget Registry](registries/widgets/README.md)" in section
    assert "(registries/README.md)" in section


def test_splice_registries_inserts_once_then_replaces():
    readme = "# T\n\n## Table of Contents\n\nx\n"
    once = splice_registries(readme, f"{REGISTRIES_START}\nA\n{REGISTRIES_END}\n")
    twice = splice_registries(once, f"{REGISTRIES_START}\nB\n{REGISTRIES_END}\n")
    assert once.count(REGISTRIES_START) == twice.count(REGISTRIES_START) == 1
    assert "\nB\n" in twice and "\nA\n" not in twice
    assert twice.endswith("## Table of Contents\n\nx\n")


# --- CLI and README generation --------------------------------------------------


def test_cli_writes_a_schema_valid_registry_index(repo, capsys):
    assert main(["--root", str(repo)]) == 0
    payload = json.loads((repo / "index" / "registry-index.json").read_text())
    assert payload["$schema"] == "registry-index.schema.json"
    assert [r["slug"] for r in payload["registries"]] == ["widgets"]
    assert "Wrote 1 registries" in capsys.readouterr().out


def test_cli_fails_without_writing_when_a_registry_is_invalid(repo, capsys):
    write(repo, "registries/hidden/README.md", "# Hidden\n")
    assert main(["--root", str(repo)]) == 1
    assert not (repo / "index" / "registry-index.json").exists()
    assert not (repo / "index" / "adr-index.json").exists()
    assert "registries/hidden" in capsys.readouterr().err


def test_generate_writes_registries_readme_and_root_block(repo):
    assert main(["--root", str(repo)]) == 0
    (repo / "README.md").write_text("## Table of Contents\n")
    generate(repo, repo / "index")
    assert "widgets/README.md" in (repo / "registries" / "README.md").read_text()
    assert "registries/widgets/README.md" in (repo / "README.md").read_text()


# --- the real repository --------------------------------------------------------


def test_every_real_registry_directory_is_indexed():
    result = build_index(REPO_ROOT)
    entries = build_registry_index(REPO_ROOT, known_ids={d.id for d in result.documents})
    on_disk = {p.name for p in (REPO_ROOT / "registries").iterdir() if p.is_dir()}
    assert {e.slug for e in entries} == on_disk


def test_committed_registry_index_and_readme_are_up_to_date():
    result = build_index(REPO_ROOT)
    entries = build_registry_index(REPO_ROOT, known_ids={d.id for d in result.documents})
    committed = (REPO_ROOT / "index" / "registry-index.json").read_text()
    assert committed == render_registry_index(entries, "registry-index.schema.json")
    docs = []
    for name in ("adr", "recommendation"):
        docs += json.loads((REPO_ROOT / "index" / f"{name}-index.json").read_text())["documents"]
    rows = json.loads(committed)["registries"]
    assert (REPO_ROOT / "registries" / "README.md").read_text() == render_registries_readme(
        rows, docs
    )
