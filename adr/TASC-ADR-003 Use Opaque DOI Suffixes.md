# TASC-ADR-003: Use Opaque DOI Suffixes

**Date:** 2026-03-23 | **Status:** Proposed

**Description:** GA4GH DOI suffixes are opaque and must not encode work stream, product, specification or version information.  
**Deciders:** TASC, Technical Team, Work Stream Leads
**Keywords:** metadata, governance, taxonomy, doi, identifiers
**Work Streams Impacted:** All
**Products Affected:** All categories

---

## Context

DOIs require both a unique identifier and sufficient metadata to support discovery and management. A key design consideration was whether information about a standard should be embedded directly within the DOI suffix itself or maintained separately in metadata. Embedding semantic meaning within identifiers can improve readability but creates governance, maintenance, and lifecycle management challenges as standards evolve. Crossref guidance also recommends avoiding meaningfully encoded identifiers wherever possible.

**The Problem:**

- Users need a way to understand what a DOI references
- DOI identifiers must remain stable over time
- Standard names, Work Stream names, and product branding may change
- GA4GH requires a consistent mechanism to classify registrations without creating identifier maintenance burdens

**Alternatives Considered:**

Alternative 1. **Use semantic DOI suffixes**

Example:

```text
10.59756/wes/1.0.0
```

- ✅ Human readable
- ✅ Easy to understand
- ❌ Difficult to change when standards evolve
- ❌ Creates governance challenges around naming
- ❌ Introduces risk of identifier instability

Alternative 2. **Use opaque DOI suffixes without additional classification**

Example:

```text
10.59756/ab12-x7yz
```

- ✅ Stable
- ✅ Easy to generate
- ❌ Difficult to manage administratively
- ❌ Limited discoverability

---

## Decision

GA4GH will generate DOI suffixes as opaque, non-semantic identifiers

**Key Points:**

- DOI suffixes MUST be generated as opaque identifiers
- DOI suffixes MUST NOT encode Work Stream names, product names, specification names, versions, or other semantic information

---

## Consequences

### Positive

- ✅ DOI identifiers remain stable even when document names change
- ✅ Naming and branding changes do not require identifier changes
- ✅ Alignment with DOI best practices
- ✅ Lean on metadata for human readable information

### Negative

- ❌ DOI identifiers are less intuitive for human readers
- ❌ Administrative systems must rely on metadata rather than identifier inspection

### Risks & Mitigations

**Risk:** Users attempt to infer meaning from DOI values
- **Mitigation:** Publish guidance stating that meaning is carried through metadata and standard designators rather than the DOI suffix

**Risk:** Opaque suffixes reduce administrative discoverability of registrations
- **Mitigation:** The Technical Team maintains a central register indexing assigned suffixes against their `<std_designator>` values, restoring discoverability without encoding meaning in the DOI itself

---

## References

- **Full Recommendation:** [Citing GA4GH Documentation Recommendation](../recommendations/Citing%20GA4GH%20Documentation.md)
- **Related ADRs:** [TASC-ADR-001: Use Crossref as the DOI Registration Authority for GA4GH](./TASC-ADR-001%20Use%20Crossref%20for%20DOI.md)

---

## Notes

The decision to separate identifier generation from human-readable classification was made to ensure long-term identifier stability. Metadata is considered the authoritative mechanism for describing the meaning and context of a DOI registration.
