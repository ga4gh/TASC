# TASC-ADR-001: Use Crossref as the DOI Registration Authority for GA4GH

**Date:** 2026-03-23 | **Status:** Proposed

**Description:** GA4GH registers all of its DOIs through Crossref, using the GA4GH DOI prefix.  
**Deciders:** TASC, GA4GH Technical Team, Chief Product Officer
**Keywords:** doi, crossref, governance, publishing, metadata
**Work Streams Impacted:** All
**Products Affected:** All categories

---

## Context

GA4GH elected to adopt Digital Object Identifiers (DOIs) as the mechanism for creating persistent citations for documentary outputs, including standards, technical specifications, white papers, and product documentation. To support DOI creation and long-term management, GA4GH required a registration authority capable of issuing DOI prefixes, supporting metadata registration, and providing ongoing DOI resolution services.

**The Problem:**

- GA4GH required an authoritative mechanism for DOI registration
- DOI registrations require long-term stewardship and metadata management
- Work Streams require a consistent registration process
- DOI assignment should be governed centrally across the organization

**Alternatives Considered:**

1. **Allow Work Streams to use different registration providers**
   - ✅ Maximum flexibility
   - ❌ Inconsistent governance
   - ❌ Inconsistent metadata practices
   - ❌ Fragmented user experience

2. **Use repository-managed DOI services (e.g. publication repositories)**
   - ✅ Minimal operational overhead
   - ✅ Existing DOI support
   - ❌ Citation ownership resides outside GA4GH
   - ❌ Inconsistent management across Work Streams

3. **Use a single registration authority for all GA4GH DOI registrations**
   - ✅ Consistent governance
   - ✅ Common metadata practices
   - ✅ Centralized lifecycle management
   - ✅ Uniform experience for all Work Streams

Any issuer must be able to support the release of standards based DOI records.

---

## Decision

GA4GH will use Crossref as the registration authority for DOI issuance and management. All GA4GH DOI registrations MUST be created through Crossref.

**Key Points:**

- Crossref is the authoritative registration authority for GA4GH DOI registrations
- All GA4GH-managed DOI registrations MUST use the assigned GA4GH DOI prefix
- DOI metadata MUST be deposited through Crossref

---

## Consequences

### Positive

- ✅ Consistent DOI management across all Work Streams
- ✅ Support for required record types to achieve the citation policy

### Negative

None aware of

### Risks & Mitigations

**Risk:** DOI registration becomes an operational bottleneck

---

## References

- **Full Recommendation:** [Citing GA4GH Documentation Recommendation](../recommendations/Citing%20GA4GH%20Documentation.md)
- \[CROSSREF_RECORDS\] \- [Crossref Supported Record Types](https://www.crossref.org/documentation/schema-library/markup-guide-record-types/)
