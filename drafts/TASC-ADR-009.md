# TASC-ADR-009: Every GA4GH Technical Product Must Have a Conformance Suite

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** conformance, testing, traceability, pdap, technical-product-requirements  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products  

---

## Context

As part of TASC's review of the "GA4GH Technical Product Requirements", TASC needed to decide whether a conformance suite should be mandatory for every technical product, and to define what a conformance suite is. Without a repeatable, traceable basis for assessing conformance, adopters and other GA4GH products cannot reliably know whether a given implementation actually satisfies a product's specification, undermining the interoperability goals described in the TASC interoperability framework (see [TASC-ADR-011](TASC-ADR-011.md)).

**The Problem:**

- Not all technical products currently have a defined, traceable conformance suite.
- Without one, "conformance" claims for an implementation cannot be independently verified against the specification.

**Alternatives Considered:**

1. **No requirement — leave conformance testing to each product team's discretion**
   - ✅ No additional deliverable burden on teams
   - ❌ No repeatable basis for verifying interoperability claims; undermines the interoperability mandate

2. **Recommend, but do not require, a conformance suite**
   - ✅ Lower burden on teams
   - ❌ A non-mandatory recommendation does not give PDAP a reliable gate to check against, and conformance claims remain unverifiable

3. **Require a conformance suite for every technical product, traceable to the specification's requirements and behaviours (chosen)**
   - ✅ Gives PDAP and adopters a repeatable, verifiable basis for conformance claims
   - ✅ Directly supports the GA4GH interoperability mandate

---

## Decision

A conformance suite is a defined set of tests, derived from a product specification, that is traceable to the product's requirements and behaviours. It provides a repeatable basis for assessing whether an implementation can claim conformance to a specified version of a GA4GH product. Passing a conformance suite means an implementation conforms to that version of the product, subject to the stated scope, optional features, and limitations. All GA4GH technical products MUST have a conformance suite.

**Key Points:**

- Every technical product MUST have a conformance suite.
- The suite MUST be traceable to the product specification's requirements and behaviours.
- The suite MUST state its scope, optional features, and limitations, so that a "pass" result has a clear, bounded meaning.
- This requirement is one of the four PDAP artifact/state requirements TASC agreed at its July 2026 workshop (see [TASC-ADR-006](TASC-ADR-006.md), [TASC-ADR-007](TASC-ADR-007.md), [TASC-ADR-008](TASC-ADR-008.md), and the umbrella review record [TASC-ADR-010](TASC-ADR-010.md)).

---

## Consequences

### Positive

✅ Conformance claims become independently verifiable and repeatable  
✅ Directly supports GA4GH's interoperability mandate (see [TASC-ADR-011](TASC-ADR-011.md))  

### Negative

❌ Product teams without an existing conformance suite must build and maintain one  
❌ Suites must be kept in sync with specification versions, adding ongoing maintenance burden  

### Risks & Mitigations

**Risk:** Conformance suites of inconsistent rigour or scope across products could give a false sense of comparable conformance.  
- **Mitigation:** TASC to define minimum expectations for conformance-suite traceability and scope documentation as part of the PDAP review checklist (see [TASC-ADR-010](TASC-ADR-010.md)).

---

## References

- **Full Policy:** GA4GH Technical Product Requirements, 2026-07-09
- **Related ADRs:** [TASC-ADR-006](TASC-ADR-006.md) (GitHub Repository), [TASC-ADR-007](TASC-ADR-007.md) (Website), [TASC-ADR-008](TASC-ADR-008.md) (Starter Kit), [TASC-ADR-010](TASC-ADR-010.md) (PDAP Technical Product Requirements Review), [TASC-ADR-011](TASC-ADR-011.md) (Interoperability Framework), [TASC-ADR-012](TASC-ADR-012.md) (Role of TASC in PDAP Governance)
- **Examples:** Existing GA4GH product conformance suites

---

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from source material provided the TASC workshop, July 2026.
