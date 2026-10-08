# TASC-ADR-008: Every GA4GH Technical Product Must Provide a Starter Kit

**Date:** 2026-08-14 | **Status:** Draft  

**Description:** Every GA4GH technical product must provide a Starter Kit giving users minimal scaffolding to build their own implementation.  
**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** starter-kit, reference-implementation, scaffolding, pdap, technical-product-requirements  
**Work Streams Impacted:** All work streams  
**Products Affected:** API, data model/ontology, file format, protocol, technical implementation guide

---

## Context

As part of TASC's review of the "GA4GH Technical Product Requirements", TASC needed to define what a "Starter Kit" is and decide whether, and how, product teams must provide one. Without minimal, extensible scaffolding, downstream adopters must build an implementation entirely from the specification, which raises the barrier to adoption and produces inconsistent first implementations across the community.

**The Problem:**

- Product teams do not consistently provide content that lets a new adopter begin building a custom implementation of the product.
- It was unclear whether a full reference implementation could satisfy this need, or whether a separate, purpose-built artifact was required.

**Alternatives Considered:**

1. **No requirement — leave onboarding content to each product team**
   - ✅ No additional deliverable burden on teams
   - ❌ Inconsistent, or absent, adoption pathway across products

2. **Require a dedicated, standalone Starter Kit artifact distinct from any reference implementation**
   - ✅ Purpose-built for onboarding, potentially lighter-weight
   - ❌ Duplicates effort where a reference implementation already exists and is well suited to the role

3. **Require a Starter Kit, and permit a Product Development team's reference implementation to satisfy the requirement (chosen)**
   - ✅ Guarantees every product has adoptable scaffolding
   - ✅ Avoids duplicate effort where a suitable reference implementation already exists

---

## Decision

A Starter Kit is content needed to enable users to begin building their own custom implementation of a product. It offers minimal scaffolding that can be readily extended for use in a variety of downstream workflows or applications. Every GA4GH technical product MUST provide a Starter Kit. A reference implementation built by the Product Development team MAY serve as the Starter Kit.

**Key Points:**

- Every technical product MUST provide a Starter Kit satisfying the above definition.
- A Product Development team's reference implementation MAY be used to satisfy this requirement where it meets the minimal-scaffolding, readily-extensible criteria.
- This requirement is one of the four PDAP artifact/state requirements TASC agreed at its July 2026 workshop (see [TASC-ADR-006](TASC-ADR-006%20Require%20a%20Conformant%20GitHub%20Repository.md), [TASC-ADR-007](TASC-ADR-007%20Serve%20Websites%20from%20ga4gh.org.md), [TASC-ADR-009](TASC-ADR-009%20Require%20a%20Conformance%20Suite.md), and the umbrella review record [TASC-ADR-010](TASC-ADR-010%20Adopt%20Technical%20Product%20Requirements.md)).

---

## Consequences

### Positive

✅ Every product provides a concrete, reusable starting point for downstream implementers  
✅ Product teams with an existing reference implementation avoid duplicate work  

### Negative

❌ Product teams without a reference implementation must produce a dedicated Starter Kit  
❌ PDAP reviewers must judge whether an offered reference implementation genuinely meets the "minimal, readily extensible" bar, which is somewhat subjective  

### Risks & Mitigations

**Risk:** A reference implementation submitted as a Starter Kit may be too complex, opinionated, or tightly coupled to one workflow to be "readily extended" for varied downstream use.  
- **Mitigation:** TASC to define concrete acceptance criteria for what counts as adequate Starter Kit scaffolding as part of the PDAP review checklist (see [TASC-ADR-010](TASC-ADR-010%20Adopt%20Technical%20Product%20Requirements.md)).

---

## References

- **Full Policy:** GA4GH Technical Product Requirements, 2026-07-09
- **Related ADRs:** [TASC-ADR-006](TASC-ADR-006%20Require%20a%20Conformant%20GitHub%20Repository.md) (GitHub Repository), [TASC-ADR-007](TASC-ADR-007%20Serve%20Websites%20from%20ga4gh.org.md) (Website), [TASC-ADR-009](TASC-ADR-009%20Require%20a%20Conformance%20Suite.md) (Conformance Suite), [TASC-ADR-010](TASC-ADR-010%20Adopt%20Technical%20Product%20Requirements.md) (PDAP Technical Product Requirements Review), [TASC-ADR-012](TASC-ADR-012%20TASC%20Role%20in%20PDAP%20Governance.md) (Role of TASC in PDAP Governance)
- **Examples:** Product reference implementations submitted as Starter Kits

---

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from source material provided the TASC workshop, July 2026.
