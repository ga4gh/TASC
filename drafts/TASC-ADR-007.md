# TASC-ADR-007: GA4GH Product and Topic Websites Must Be Served from a ga4gh.org Subdomain

**Date:** 2026-08-14 | **Status:** Draft  

**Deciders:** TASC (agreed at TASC workshop, July 2026)  
**Keywords:** website, domain, branding, pdap, technical-product-requirements  
**Work Streams Impacted:** All work streams  
**Products Affected:** All GA4GH technical products with a public-facing website  

---

## Context

As part of TASC's review of the "GA4GH Technical Product Requirements", we defined the candidate set of required activities, artifacts, or states a technical product must satisfy to get through PDAP approval (see [TASC-ADR-010](TASC-ADR-010.md)). TASC needed to decide where product and topic websites should be hosted.

Standalone or third-party domains for GA4GH products create inconsistent branding, make it harder for adopters to trust that a site is an official GA4GH resource, and create risk if a third-party domain lapses, changes ownership, or is not maintained under GA4GH's control.

**The Problem:**

- Some products and topics have historically been represented by standalone or third-party domains rather than a `ga4gh.org` subdomain.
- This creates inconsistent branding and a governance/continuity risk for domains not controlled by GA4GH.

**Alternatives Considered:**

1. **No requirement — allow any domain**
   - ✅ No migration effort for existing standalone sites
   - ❌ Inconsistent branding; GA4GH has no control over domain continuity or content
   - ❌ Already observed issues in current structures

2. **Recommend, but do not require, a `ga4gh.org` subdomain**
   - ✅ Lower burden on teams with existing standalone domains
   - ❌ A non-mandatory recommendation does not give PDAP a reliable gate to check against

3. **Require any website representing a GA4GH product or topic to be served from a `ga4gh.org` subdomain (chosen)**
   - ✅ Consistent branding and clear signal of official GA4GH status
   - ✅ GA4GH retains control over domain continuity, security, and content governance

---

## Decision

Any website representing a GA4GH product or topic MUST be served from a `ga4gh.org` subdomain (e.g., `product.ga4gh.org`). Standalone or third-party domains are NOT permitted.

**Key Points:**

- Product and topic websites MUST use a `ga4gh.org` subdomain.
- Standalone domains (e.g., `product.org`) and third-party-hosted domains are not permitted for representing a GA4GH product or topic.
- This requirement is one of the four PDAP artifact/state requirements TASC agreed at its July 2026 workshop (see [TASC-ADR-006](TASC-ADR-006.md), [TASC-ADR-008](TASC-ADR-008.md), [TASC-ADR-009](TASC-ADR-009.md), and the umbrella review record [TASC-ADR-010](TASC-ADR-010.md)).

---

## Consequences

### Positive

✅ Consistent, recognisable branding for all GA4GH product/topic websites  
✅ GA4GH retains operational control and continuity over the hosting domain  

### Negative

❌ Products with an existing standalone or third-party domain will need to migrate to a `ga4gh.org` subdomain  
❌ Adds a DNS/hosting coordination step with GA4GH staff for every new product website  

### Risks & Mitigations

**Risk:** Migrating an established standalone domain may break existing inbound links, bookmarks, or citations.  
- **Mitigation:** Require redirects from the old domain to the new `ga4gh.org` subdomain during migration, and communicate the change via the standard TASC dissemination process (TASC-GOV-01).

---

## References

- **Full Policy:** GA4GH Technical Product Requirements, 2026-07-09
- **Related ADRs:** [TASC-ADR-006](TASC-ADR-006.md) (GitHub Repository), [TASC-ADR-008](TASC-ADR-008.md) (Starter Kit), [TASC-ADR-009](TASC-ADR-009.md) (Conformance Suite), [TASC-ADR-010](TASC-ADR-010.md) (PDAP Technical Product Requirements Review), [TASC-ADR-012](TASC-ADR-012.md) (Role of TASC in PDAP Governance)
- **Examples:** Existing `*.ga4gh.org` product subdomains

---

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic), via Claude Code, from source material provided the TASC workshop, July 2026.
