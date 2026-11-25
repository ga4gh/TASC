# Technical product requirements table

The GA4GH Technical Product Requirements table is generated, not written by hand. It lives at
[requirements/README.md](../../requirements/README.md).

## Sources

| Input | Role |
| --- | --- |
| `requirements/requirements.json` | One entry per requirement: name, category, details, when it applies, and the documents and registries that define it. |
| `index/adr-index.json`, `index/recommendation-index.json` | Supply each referenced document's status, date and path. |
| `index/registry-index.json` | Supplies each referenced registry's path. |

`python -m tasc_index.readmes` (run by the `TASC index` workflow) writes
`requirements/README.md` from these.

## Why a separate file

A document does not map to one requirement. TASC-ADR-001 to 005 and GA4GH-REC-05 together
define "DOIs", one ADR may define several requirements, and some requirements (for example
"Retired status shown") come from the PDAP and have no TASC document. A header field on each
document could not express that.

## Fields of a requirement

| Field | Required | Notes |
| --- | --- | --- |
| `name`, `details`, `applies` | yes | Shown as-is. |
| `category` | yes | One of the six slugs in `CATEGORIES` in `tools/tasc_index/requirements.py`; this sets the section. |
| `documents` | no | ADR, recommendation or governance IDs. They must exist in the index. |
| `registries` | no | Registry slugs. They must exist in the registry index. |
| `references` | no | Plain-text citations for sources outside this repository. |
| `status` | only without `documents` | Overrides the derived status, for example `Recommended`. |

Every requirement must cite at least one document, registry or reference.

## How the date is derived

The date is the latest date among the referenced documents. It cannot be set on a requirement
(`date` is rejected). A requirement with no document has a blank date; fix that by adding the
date to the source document or registry, not to `requirements.json`.

## How status is derived

- All referenced documents Accepted (ADRs) or Approved (recommendations, governance): `Approved`.
- Otherwise, if any referenced ADR is not yet accepted: `Draft ADR`.
- Otherwise: `Draft`.

Generation fails with the list of problems if a category, document ID or registry slug is
unknown, so a renamed or removed document cannot silently leave a stale row.

## Not generated

Section 7 (artefacts by product type) and section 8 (proposed additions) of the source document
are drafts for TASC discussion and remain prose. Add them here once agreed.
