# TASC-ADR-010: Adoption of the GA4GH Technical Product Requirements (PDAP Approval Set)

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** pdap, technical-product-requirements, governance, review  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products  

---

## Context

TASC reviewed a candidate document, "GA4GH Technical Product Requirements" listing potential required activities, artifacts, or states a technical product must satisfy to get through PDAP approval. The review considered four candidate requirements: GitHub Repository, Website, Starter Kit, and Conformance Suite. TASC needed to decide, as a set, whether these four items should be adopted as formal PDAP requirements, and to record that decision distinctly from the four individual requirement decisions themselves.

**The Problem:**

- The candidate requirements document identified several potential activities/artifacts/states, but had not yet been formally reviewed and adopted by TASC as binding PDAP requirements.
- Without a record of the review itself, it is unclear which candidate items were considered, which were adopted, and why — separate from the substance of each individual requirement.

**Alternatives Considered:**

1. **Record each requirement decision independently with no umbrella review record**
   - ✅ Simpler — one ADR per requirement
   - ❌ Loses the context of what was reviewed together, in what document, and on what date; harder to trace the origin of the four requirements as a coherent set

2. **Fold the review outcome into a single ADR covering all four requirements**
   - ✅ One document to maintain
   - ❌ Conflates four independently revisable decisions into one ADR, violating the "one ADR per decision" principle (TASC-GOV-02) and making future supersession of a single requirement harder

3. **Record the review as its own ADR, with each requirement recorded as its own ADR (chosen)**
   - ✅ Preserves the review context (source document, date, scope) as a distinct, citable decision
   - ✅ Keeps each requirement independently revisable per TASC-GOV-02's one-decision-per-ADR principle

---

## Decision

TASC formally reviewed the "GA4GH Technical Product Requirements | 2026-07-09" candidate list at its July 2026 workshop and resolved to adopt four of its items as mandatory PDAP approval requirements for all GA4GH technical products: GitHub Repository, Website, Starter Kit, and Conformance Suite. Each requirement is recorded as its own ADR.

**Key Points:**

- The reviewed source document is "GA4GH Technical Product Requirements | 2026-07-09."
- Four requirements were adopted from that document's candidate list:
  - GitHub Repository — see [TASC-ADR-006](TASC-ADR-006.md)
  - Website — see [TASC-ADR-007](TASC-ADR-007.md)
  - Starter Kit — see [TASC-ADR-008](TASC-ADR-008.md)
  - Conformance Suite — see [TASC-ADR-009](TASC-ADR-009.md)
- This ADR records the review and adoption decision itself; the substantive content of each requirement is recorded in its own ADR so each can be revised or superseded independently.

---

## Consequences

### Positive

✅ Establishes a clear, citable record of which candidate requirements were reviewed and adopted, and when  
✅ Keeps the four adopted requirements independently revisable, per the one-decision-per-ADR principle  

### Negative

❌ Any candidate items from the source document not explicitly adopted here remain unresolved and will need a future TASC decision  
❌ Requires cross-referencing five ADRs (this one plus the four requirements) to see the full picture  

### Risks & Mitigations

**Risk:** Future readers may only find one of the four requirement ADRs and miss the broader PDAP context.  
- **Mitigation:** Each requirement ADR ([TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-009](TASC-ADR-009.md)) cross-references this review record in its References section.

---

## References

- **Full Policy:** GA4GH Technical Product Requirements, 2026-07-09
- **Related ADRs:** [TASC-ADR-006](TASC-ADR-006.md) (GitHub Repository), [TASC-ADR-007](TASC-ADR-007.md) (Website), [TASC-ADR-008](TASC-ADR-008.md) (Starter Kit), [TASC-ADR-009](TASC-ADR-009.md) (Conformance Suite), [TASC-ADR-012](TASC-ADR-012.md) (Role of TASC in PDAP Governance)
- **Examples:** n/a

---

## Notes

The source review document referenced here (tracked in this repository as `CLAUDE-PDAP-REVIEW-TASC.md`) was not populated with the full requirements text as part of this ADR set, per an explicit decision at drafting time; this ADR and [TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-009](TASC-ADR-009.md) instead draw directly on the requirements text supplied by Andy Yates during the TASC workshop discussion.

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from source material provided the TASC workshop, July 2026.
