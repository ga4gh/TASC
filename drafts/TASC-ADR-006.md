# TASC-ADR-006: Every GA4GH Technical Product Must Have a Conformant GitHub Repository

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** github, repository, pdap, technical-product-requirements  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products  

---

## Context

As part of TASC's review of the "GA4GH Technical Product Requirements" (2026-07-09) the candidate set of required activities, artifacts, or states a technical product must satisfy to get through PDAP approval (see [TASC-ADR-010](TASC-ADR-010.md)). TASC needed to decide whether a GitHub repository, conforming to a shared template and policy set, should be a mandatory artifact for every technical product.

Without a consistent, policy-conformant home for a product's source and collaboration activity, work streams create repositories with inconsistent structure, licensing, ownership, and access-control practices. This makes it harder for TASC and the PSC to assess a product, and harder for external adopters to know what to expect when engaging with a GA4GH product's codebase.

**The Problem:**

- Technical products currently vary in whether, where, and how they maintain a GitHub repository, and in what structure/policies that repository follows.
- PDAP approval needs a reliable, checkable artifact confirming a product has an accessible, well-governed code repository.

**Alternatives Considered:**

1. **No requirement — leave repository practice to each product team**
   - ✅ Maximum flexibility for teams
   - ❌ Inconsistent structure and governance makes PDAP review and cross-product alignment difficult
   - ❌ Already observed issues in current structures

2. **Recommend, but do not require, a GitHub repository**
   - ✅ Lower burden on teams
   - ❌ A non-mandatory recommendation does not give PDAP a reliable gate to check against

3. **Require at least one GitHub repository per product, conforming to a TASC repository template and referenced GitHub policies (chosen)**
   - ✅ Gives PDAP a concrete, checkable requirement
   - ✅ Standardises repository structure and policy conformance across all GA4GH technical products

---

## Decision

All GA4GH technical products MUST have at least one GitHub repository. Each repository MUST conform to the TASC repository template and comply with all GitHub policies referenced within it.

**Key Points:**

- At least one GitHub repository is required per technical product.
- The repository MUST conform to the TASC repository template.
- The repository MUST comply with all GitHub policies referenced within that template.
- This requirement is one of the four PDAP artifact/state requirements TASC agreed at its July 2026 workshop (see [TASC-ADR-007](TASC-ADR-007.md), [TASC-ADR-008](TASC-ADR-008.md), [TASC-ADR-009](TASC-ADR-009.md), and the umbrella review record [TASC-ADR-010](TASC-ADR-010.md)).

---

## Consequences

### Positive

✅ PDAP reviewers have a single, checkable artifact confirming a product has a governed code repository  
✅ Repository structure, licensing, and access-control practices become consistent across GA4GH products  

### Negative

❌ Existing products with non-conformant repositories will need remediation work to meet the template and policies  
❌ Adds an upfront checklist item for new products entering PDAP  

### Risks & Mitigations

**Risk:** The TASC repository template or referenced GitHub policies are not yet finalised or widely known.  
- **Mitigation:** TASC to publish and maintain the repository template and referenced policies as living recommendation documents, and communicate them via the standard TASC dissemination process (TASC-GOV-01).

---

## References

- **Full Policy:** GA4GH Technical Product Requirements, 2026-07-09
- **Related ADRs:** [TASC-ADR-007](TASC-ADR-007.md) (Website), [TASC-ADR-008](TASC-ADR-008.md) (Starter Kit), [TASC-ADR-009](TASC-ADR-009.md) (Conformance Suite), [TASC-ADR-010](TASC-ADR-010.md) (PDAP Technical Product Requirements Review), [TASC-ADR-012](TASC-ADR-012.md) (Role of TASC in PDAP Governance)
- **Examples:** TASC repository template (to be published under `recommendations/`)

---

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from source material provided the TASC workshop, July 2026.
