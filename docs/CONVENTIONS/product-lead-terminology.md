# Product Lead terminology

GA4GH PDAP v3.0 names the person who guides a product's development the **Product Lead**.
TASC documents use the same term.

## Decision

- GA4GH-REC-03 now describes the **Product Lead** role. It was previously "Product Owner".
- The Recommendation ID (`GA4GH-REC-03`) is unchanged.
- The file moved from `recommendations/GA4GH product owner description.md` to
  `recommendations/GA4GH product lead description.md`. Links to the old path need updating.
- The role's responsibilities, reporting lines and term limits were **not** changed. Only the name was.

## Not renamed

The root `README.md` (Step 2 of the issue process) and `governance/TASC_Governance_and_Leadership_Approved_240825.md`
say "product owners" for the two TASC members assigned to an in-scope issue. That is a TASC working-process
role, not the PDAP role, so it keeps its name. Revisit this if TASC wants one term for both.

## Guard

`tools/tests/test_consistency.py::test_rec_03_uses_pdap_product_lead_terminology` fails if "Product Owner"
or "PO" reappears in REC-03 (apart from the "previously" note) or in its index entry.

## Generated files

`index/recommendation-index.json`, `recommendations/README.md` and the root `README.md` recent-outputs
list are regenerated with `uv run python -m tasc_index` and `uv run python -m tasc_index.readmes`
from `tools/`. Do not edit them by hand.
