# TASC-ADR-011: Adoption of the TASC Interoperability Framework

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** interoperability, pdap, risk-tiering, governance  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products  

---

## Context

TASC developed a draft interoperability framework ("GA4GH 2026 TASC Interoperability") to advance the interoperability mandate identified in the GA4GH Gap Analysis report, which called for "an interconnected suite of standards that are compatible and interoperable with each other and hardened for real-world use". TASC needed to decide whether to formally adopt this framework (definitions, development paths, and risk-tiering model) as the basis for how TASC assesses and manages interoperability during product development and PDAP review.

**The Problem:**

- GA4GH products have historically been developed without a shared, structured definition of "interoperability" or a consistent process for assessing interoperability risk.
- Without an agreed framework, TASC has no repeatable way to triage new products for interoperability risk, or to manage alignment work for existing products.

**Alternatives Considered:**

1. **No formal framework — assess interoperability ad hoc, case by case**
   - ✅ No process overhead
   - ❌ Inconsistent assessment; no shared vocabulary or risk-tiering; does not scale across a growing product portfolio

2. **Adopt only the three-layer definition (syntactic/semantic/behavioural) without the risk-tiering or development-path process**
   - ✅ Establishes shared vocabulary with minimal process change
   - ❌ Leaves PDAP without an actionable mechanism for triaging and managing interoperability risk

3. **Adopt the full framework — definitions, three development paths, PDAP v2 triage process, and risk-tier model (chosen)**
   - ✅ Provides both a shared vocabulary and an operational process integrated with PDAP v2
   - ✅ Directly traceable to the GA4GH 2020 Gap Analysis interoperability mandate

---

## Decision

TASC adopts the interoperability framework set out in "GA4GH 2026 TASC Interoperability" as its basis for assessing and managing interoperability across GA4GH technical products.

**Key Points:**

- **Definition:** Interoperability is the ability of two or more autonomous systems, applications, or components to securely, reliably, and efficiently exchange data and subsequently utilise that information without requiring custom, ad-hoc integrations, operating across three layers: syntactic (format/protocol), semantic (shared meaning), and behavioural/pragmatic (workflow/execution alignment)
- **Three development paths** govern how interoperability is assessed depending on product status:
  1. New products (or products entering a major change cycle): forward-looking risk assessment through PDAP v2.
  2. Existing active products not yet on the newest PDAP: backward-looking alignment and gap closure to bring them under PDAP v2 governance.
  3. Existing inactive products: gap documentation only; does not require active TASC participation.
- **PDAP triage process** for new products includes: GA4GH CSO initial scope review within 1 week; Work Stream representatives identifying potential conflicts ahead of a TASC discussion meeting (at least 2 weeks out); issues tracked on a GitHub repository; an aggregated singular TASC response following discussion. This final response MUST come from "TASC" and a machine user on GitHub should be used to convey the final message.
- Policy questions for existing active and inactive products (audit ownership, communication of gaps, defining success) remain open and are not resolved by this ADR

---

## Consequences

### Positive

✅ Gives TASC and product teams a shared vocabulary and a repeatable process for assessing interoperability risk  
✅ Integrates interoperability assessment directly into the PDAP v2 approval process, rather than treating it as a separate activity  

### Negative

❌ Adds triage overhead (scope review, WS conflict-checking, discussion meetings) to the PDAP v2 timeline for new products  
❌ Existing active and inactive products face additional alignment or audit work to come under, or be assessed against, this framework  

### Risks & Mitigations

**Risk:** Several sections of the source framework (interoperability-by-standard-type categories, and the policy approach for existing active/inactive products) remain placeholders or open questions.  
- **Mitigation:** Treat this ADR as adopting the framework's definitions, development paths, and risk-tiering model as currently specified; unresolved sections (standard-type guidance, existing-product audit ownership) require follow-up TASC decisions before those parts of the framework are binding.

---

## References

- **Full Policy:** `2026 TASC Interoperability.md` (TASC internal framework document); GA4GH Strategic Road Map / 2020 Gap Analysis report, <https://www.ga4gh.org/about-us/strategic-road-map/>
- **Related ADRs:** [TASC-ADR-009](TASC-ADR-009.md) (Conformance Suite), [TASC-ADR-010](TASC-ADR-010.md) (PDAP Technical Product Requirements Review), [TASC-ADR-012](TASC-ADR-012.md) (Role of TASC in PDAP Governance)
- **Examples:** n/a

---

## Notes

The source framework document contains several open policy questions not resolved by this ADR: audit ownership and communication mechanisms for existing active and inactive products, and unfilled "interoperability by standard type" guidance (Data Model/Ontology, APIs, File Formats, Policy, Protocols, Technical implementation guidance). These remain tracked for future TASC decisions and may result in superseding or supplementary ADRs.

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from `2026 TASC Interoperability.md` and source material provided the TASC workshop, July 2026.
