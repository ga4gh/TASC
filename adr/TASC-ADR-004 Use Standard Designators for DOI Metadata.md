# TASC-ADR-004: Use Standard Designators for DOI Metadata Classification

**Date:** 2026-03-23 | **Status:** Proposed

**Description:** Every GA4GH DOI registration must carry a std_designator metadata value naming the originating group and document.  
**Deciders:** TASC, Technical Team, Work Stream Leads
**Keywords:** metadata, governance, taxonomy, classification, doi
**Work Streams Impacted:** All
**Products Affected:** All categories

---

## Context

GA4GH requires a consistent mechanism to classify and manage DOI registrations across Work Streams. While DOI metadata provides rich descriptive information, a standardized classification mechanism is required to support governance, reporting, administration, and discovery. Without a common convention, Work Streams may independently adopt different naming patterns, making DOI registrations more difficult to manage consistently across the organization.

**The Problem:**

- DOI registrations need a standardized mechanism for identifying their context within GA4GH
- Work Streams require a common taxonomy for documentary outputs
- Administrative and reporting processes benefit from consistent classification
- Classification conventions must be simple enough to apply consistently across all Work Streams

**Alternatives Considered:**

1. **No standard classification mechanism**
   - ✅ Minimal process overhead
   - ✅ Maximum flexibility for Work Streams
   - ❌ Inconsistent metadata
   - ❌ Difficult organizational reporting and governance

2. **Work Stream-specific classification schemes**
   - ✅ Allows local flexibility
   - ✅ Can be optimized for individual Work Stream needs
   - ❌ Inconsistent user experience
   - ❌ Difficult cross-Work Stream reporting

3. **Adopt a common standard designator convention**
   - ✅ Consistent metadata across GA4GH
   - ✅ Simplified governance and administration
   - ✅ Improved discoverability and reporting
   - ✅ Supports future automation

---

## Decision

GA4GH will require all DOI registrations to include a standard designator (`std_designator`) that identifies the originating group and the associated documentary output. The standard designator will be used as a metadata classification mechanism and will not form part of the DOI itself.

**Key Points:**

- Every DOI registration MUST include a `std_designator`
- Standard designators MUST follow the format:

  ```text
  <ORIGINATING_GROUP_ACRONYM>_<DOCUMENT_NAME>
  ```

Standard designators SHOULD remain stable over the lifetime of the referenced documentary output and therefore link items together.

Examples:

```text
TASC_TS
FEDANALYSIS_WES
CLINPHENO_PHEN
DISCOVERY_BEACON
REWS_GDPRPRIMER
```

---

## Consequences

### Positive

- ✅ Consistent classification of DOI registrations across GA4GH
- ✅ Improved metadata quality and discoverability
- ✅ Simplified reporting, governance, and administration
- ✅ Enables future automation and metadata analysis
- ✅ Provides human-readable context independent of DOI identifiers

### Negative

- ❌ Requires governance of naming conventions
- ❌ Requires coordination across Work Streams
- ❌ Existing registrations may require metadata updates if conventions evolve

### Risks & Mitigations

**Risk:** Different originating groups adopt inconsistent naming patterns
- **Mitigation:** Publish and maintain a controlled naming convention managed through the DOI registration process. Document the naming convention and index its subcomponents (`<ORIGINATING_GROUP_ACRONYM>`, `<DOCUMENT_NAME>`) in the Technical Team's central register — see [originating-group-acronyms.yaml](../registries/group-acronyms/originating-group-acronyms.yaml) for the authoritative list of `<ORIGINATING_GROUP_ACRONYM>` values — so clashes and inconsistencies can be checked before registration

**Risk:** Designators become overly detailed or unstable
- **Mitigation:** Require concise, durable naming aligned with long-term product and document identity

**Risk:** Proposed designators clash with existing registrations or diverge from convention
- **Mitigation:** As all DOI requests are routed through the Technical Team, the Technical Team MUST check proposed `<std_designator>` values against the central register before registration

---

## References

- **Full Recommendation:** [Citing GA4GH Documentation Recommendation](../recommendations/Citing%20GA4GH%20Documentation.md)
