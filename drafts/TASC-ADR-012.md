# TASC-ADR-012: The Role of TASC in PDAP Technical Alignment and Interoperability Governance

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** governance, role, pdap, technical-alignment, interoperability  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products  

---

## Context

TASC-GOV-01 establishes TASC's role to aid the harmonisation of GA4GH's technical products so they can be used together and its decision-making structure. With the adoption of the PDAP technical product requirements ([TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-010](TASC-ADR-010.md)) and the interoperability framework ([TASC-ADR-011](TASC-ADR-011.md)), TASC needed to formally record its specific operational role within the PDAP v2 process itself, rather than leaving that role implicit across several separate documents.

**The Problem:**

- TASC's general mission and decision-making process are documented (TASC-GOV-01), but TASC's specific operational role within PDAP (triage, risk-tiering, conflict resolution, sign-off) was only described piecemeal across the interoperability framework and the individual requirement decisions
- Without a single decision record naming TASC's role in PDAP, it is unclear to product teams and the PSC where TASC's authority and responsibilities sit within the approval pipeline.

**Alternatives Considered:**

1. **Leave TASC's PDAP role implicit, inferred from TASC-GOV-01 plus the interoperability framework**
   - ✅ No new document to maintain
   - ❌ Product teams and PSC lack a single, explicit reference for what TASC does within PDAP v2

2. **Expand TASC-GOV-01 (the general charter) to include PDAP-specific role detail**
   - ✅ Keeps all governance content in one charter
   - ❌ Conflates TASC's general governance charter with PDAP-specific operational detail that may evolve independently and faster

3. **Record TASC's PDAP role as its own ADR, referencing TASC-GOV-01 and the interoperability framework (chosen)**
   - ✅ Gives PDAP stakeholders a single, explicit, independently revisable record of TASC's role
   - ✅ Keeps the general charter (TASC-GOV-01) stable while allowing PDAP-specific role detail to evolve via ADR supersession

---

## Decision

TASC's role in PDAP is to perform technical-alignment review and interoperability risk-tiering during product approval, and to act as the venue for resolving cross-product technical alignment conflicts. This role builds on TASC's general mission (TASC-GOV-01) and is exercised through the PDAP requirements ([TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-010](TASC-ADR-010.md)) and the interoperability framework ([TASC-ADR-011](TASC-ADR-011.md)).

**Key Points:**

- TASC's mission (per TASC-GOV-01) is to aid harmonisation of GA4GH's technical products so they can be used together effectively, producing outputs and decisions for internal consistency and technical alignment across Work Streams.
- Within PDAP, TASC specifically:
  - Reviews new products' anticipated domains and data types at triage, and sets/adjusts interoperability risk tiers.
  - Aggregates Work Stream representatives' conflict identification and TASC's holistic response following discussion.
  - Provides structured touch-points and mitigation review for at-risk (Tier 2/3) products at PDAP checkpoints and gates, including formal sign-off for Tier 3 products.
  - Acts as the *de facto* venue for resolving cross-product technical alignment conflicts.
  - Reviews and adopts PDAP artifact/state requirements (GitHub Repository, Website, Starter Kit, Conformance Suite) that products must satisfy ([TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-009](TASC-ADR-009.md)).

---

## Consequences

### Positive

✅ Gives product teams, Work Streams, and the PSC a single, explicit reference for TASC's role and authority within PDAP v2  
✅ Clarifies that PDAP-specific role detail can evolve via ADR supersession without reopening the general TASC charter  

### Negative

❌ Adds one more document product teams must be aware of alongside TASC-GOV-01 and the interoperability framework  
❌ Overlap between this ADR and TASC-GOV-01 / TASC-ADR-011 requires care to avoid drift if one is updated without the others  

### Risks & Mitigations

**Risk:** This ADR's description of TASC's PDAP role could drift out of sync with TASC-GOV-01 or the interoperability framework if either is revised independently.  
- **Mitigation:** Any future revision to TASC's general mission (TASC-GOV-01) or the interoperability framework ([TASC-ADR-011](TASC-ADR-011.md)) that materially changes TASC's PDAP responsibilities should be accompanied by a superseding ADR to this one.

---

## References

- **Full Policy:** `governance/TASC_Governance_and_Leadership_Approved_240825.md` (TASC-GOV-01); `2026 TASC Interoperability.md`
- **Related ADRs:** [TASC-ADR-006](TASC-ADR-006.md)–[TASC-ADR-009](TASC-ADR-009.md) (PDAP requirements), [TASC-ADR-010](TASC-ADR-010.md) (PDAP Technical Product Requirements Review), [TASC-ADR-011](TASC-ADR-011.md) (Interoperability Framework)
- **Examples:** n/a

---

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from `governance/TASC_Governance_and_Leadership_Approved_240825.md`, `2026 TASC Interoperability.md`, and source material provided the TASC workshop, July 2026.
