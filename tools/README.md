# TASC index generator

Generates two machine-readable indexes of this repository's documents. The TASC
pages on the GA4GH website read them from `main`:

| File                                 | Lists                                  | Schema                                    |
|--------------------------------------|----------------------------------------|-------------------------------------------|
| `index/adr-index.json`               | ADRs                                   | `index/adr-index.schema.json`             |
| `index/recommendation-index.json`    | Recommendations and governance documents | `index/recommendation-index.schema.json` |

```text
https://raw.githubusercontent.com/ga4gh/TASC/main/index/adr-index.json
https://raw.githubusercontent.com/ga4gh/TASC/main/index/recommendation-index.json
```

## What is indexed

| Directory          | Type             | Identifier source                      | Statuses                                  |
|--------------------|------------------|----------------------------------------|-------------------------------------------|
| `adr/`             | `adr`            | H1: `# TASC-ADR-NNN: Title`            | Draft, Proposed, Accepted, Deprecated, Superseded |
| `recommendations/` | `recommendation` | `**Recommendation**: GA4GH-REC-NN`     | Draft, Approved, Superseded               |
| `governance/`      | `governance`     | `**Document ID**: TASC-GOV-NN`         | Draft, Approved, Superseded               |

`drafts/` is also indexed; a draft's type is inferred from its content (a
`TASC-ADR-NNN:` title, a `Recommendation` field or a `Document ID` field), and its
`path`/`url` point into `drafts/`. `template.md` and `README.md` files are never indexed.

Each entry has `id`, `type`, `name`, `date`, `status`, `description`, `path` and
`url` (a permanent GitHub link back to the source file). The shape is defined by
the two schemas above. Each has its own status enum: ADRs use one, recommendations
and governance documents share another.

## Usage

```bash
cd tools
uv sync                                  # once; installs the locked dependencies
uv run python -m tasc_index              # writes both files in ../index
uv run python -m tasc_index.readmes      # then the READMEs, from those files
uv run pytest
uv run ruff check . && uv run ruff format --check .
```

Dependencies are declared in `tools/pyproject.toml` and locked in `tools/uv.lock`; use
`uv add <package>` (or `uv add --dev <package>`) to change them and commit the lock file.

Options: `--strict` (fail when a document has no `Description` field),
`--branch`, `--repo-url`, `--root`, `--index-dir`.

A malformed document (bad ID, date or status, duplicate ID, ADR file name that
disagrees with its ID) fails generation. Every problem is listed in one run.

## READMEs

`python -m tasc_index.readmes` (run from `tools/`, after the indexes are generated) reads
`index/*.json`, never the markdown, and writes:

- `adr/README.md` and `recommendations/README.md`: a table of every indexed document;
- the "Recently Approved" block of the root `README.md` (between the `tasc-recent`
  markers): the latest 3 `Accepted` ADRs and the latest 3 `Approved` recommendations, newest `Date` first.

Do not edit these by hand; the workflow regenerates and commits them.

## ADR short names

ADR headings in listings read `TASC-ADR-001 Use Crossref for DOI`. The short part lives in
the ADR's file name, so the files are easy to browse: `adr/TASC-ADR-001 Use Crossref for DOI.md`
(up to 60 characters after the ID). It is emitted as `short_name` in `adr-index.json`. A file named
only `TASC-ADR-NNN.md` falls back to the full title with a warning, and `--strict` (and the test
suite) fails.

## Descriptions

Each document carries its own one-line summary in its metadata header, as
`**Description:**` (ADRs) or `**Description**:` (recommendations and governance),
up to 300 characters. Edit it in the document. If the field is missing the
generator derives one from the first sentence of the Decision (ADRs) or Abstract
and prints a warning; `--strict` turns that into an error.

## Automation

[`.github/workflows/tasc-index.yml`](../.github/workflows/tasc-index.yml) runs lint,
tests and generation on pull requests, and on every push/merge to `main` it also
commits the regenerated indexes. That commit is made with
`GITHUB_TOKEN`, so it does not retrigger the workflow. If `main` is protected, the
bot must be allowed to push to it.

## Changing statuses or adding a document type

1. Update the enums in `tasc_index/models.py`.
2. Update the relevant `index/*-index.schema.json` and `template.md`.

`tests/test_consistency.py` fails until all three agree.

## Layout

| File                      | Responsibility                                    |
|---------------------------|---------------------------------------------------|
| `tasc_index/models.py`    | Document types, status enums, ID formats, entry model |
| `tasc_index/parsing.py`   | Markdown metadata header and heading parsing      |
| `tasc_index/descriptions.py` | Fallback description when a document has none  |
| `tasc_index/builder.py`   | Discovery, validation, ordering, index split, JSON rendering |
| `tasc_index/cli.py`       | Command line and schema validation of the output  |
| `tasc_index/readmes.py`   | README generation from the index JSON             |
