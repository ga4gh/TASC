# Registry index

## Decision

TASC registries are indexed, not numbered. They do not receive `GA4GH-REC-XX` identifiers.

## Why

- Registries are operational data (a YAML or JSON file plus a README on how to add an entry).
  Recommendations are living policy documents with a date, status and authors.
- Some registries are already governed by a recommendation or ADR (for example
  `service-info` by GA4GH-REC-02). A second number for the same thing would be confusing.
- Registry content changes whenever an entry is added, which does not fit the
  Draft / Approved / Superseded lifecycle.
- One registry, `persistent-url`, is maintained in another repository (`ga4gh/w3id.org`).

## How it works

Each registry describes itself in the header of its own README, using the same
`**Field**: value` style as recommendations and ADRs:

```markdown
# Service Info Types

**Description**: One sentence, max 300 characters.  
**Defined by**: GA4GH-REC-02  
**Data file**: ga4gh-service-info.json  
**External location**: https://example.org/where-entries-live  
```

| Field | Required | Meaning |
| ------- | ---------- | --------- |
| Heading | Yes | The registry's name |
| Description | Yes | One-line summary shown in the index |
| Defined by | Yes, but may be blank or `None` | IDs of the ADRs, recommendations or governance documents that define the registry, comma-separated. Blank means no TASC document defines it. The line must still be present so it is never skipped by accident |
| Data file | One of these two | File in the registry directory that holds the entries |
| External location | One of these two | Where the entries are maintained when not in this repository, e.g. `persistent-url` |

```text
registries/<slug>/README.md  (header, the source of truth)
        |  python -m tasc_index
        v
index/registry-index.json    (validated by index/registry-index.schema.json)
        |  python -m tasc_index.readmes
        v
registries/README.md  and the "Registries" block of the root README.md
```

Registries are discovered from the directories under `registries/`, so a new registry
cannot be left out of the index. The generator fails when:

- a directory has no README, or its README has no heading or Description;
- the `Defined by` line is missing, or names an ID that is not an indexed document;
- a `Data file` is named but does not exist, or neither a data file nor an external location is given.

The `tasc-index` workflow runs on changes under `registries/` and commits the regenerated files.

## Adding a registry

1. Create `registries/<slug>/README.md` with the header above, and the data file.
2. Run `uv run python -m tasc_index && uv run python -m tasc_index.readmes` from `tools/`.

## Related

- `governance/TASC-GOV-02 TASC_Document_Standards.md` (repository structure)
- [tools/README.md](../../tools/README.md)
