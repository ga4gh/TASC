# TASC-ADR-002: Separate Citation Identifiers from Machine-Readable Standard Identifiers

**Date:** 2026-03-23 | **Status:** Proposed

**Description:** DOIs are used for citing documents only; machine-readable standard identifiers are governed separately.  
**Deciders:** TASC, Technical Team, Architecture Community  
**Keywords:** identifiers, citation, interoperability, APIs, governance  
**Work Streams Impacted:** All  
**Products Affected:** APIs (DRS, TRS, WES, TES, Beacon), data models (VRS) and future standards

---

## Context

During discussions around standard citation, concerns were raised regarding the use of identifiers within APIs, schemas, registries, and machine-readable metadata.

**The Problem:**
- Human citation and machine identification solve different problems
- A DOI is useful for publication and citation
- Software systems often require version-aware and machine-readable identifiers

**Alternatives Considered:**

1. **Use DOIs for all purposes**
   - ✅ Single identifier system
   - ❌ Poor fit for API and protocol interactions

2. **Allow each Work Stream to define its own identifiers**
   - ✅ Maximum flexibility
   - ❌ Inconsistent user experience
   - ❌ Reduced interoperability

3. **Separate citation and technical identification concerns**
   - ✅ Clear governance boundaries
   - ✅ Preserves future architectural flexibility
   - ✅ Supports multiple technical use cases

---

## Decision

GA4GH will use DOIs for documentary citation only. Future machine-readable identifier schemes MAY be developed independently where required for APIs, service registries, metadata models, and protocol implementations.

**Key Points:**
- A DOI MUST NOT be considered the sole identifier mechanism for all standards-related use cases
- Citation requirements and interoperability requirements SHOULD be governed separately
- Future identifier frameworks MAY complement DOI-based citation
- Documentation of this separation of concerns MUST be maintained at both the product level (e.g. in product documentation) and centrally by the GA4GH Technical Team (e.g. as a public listing), so that implementers can find it regardless of where they start looking

---

## Consequences

### Positive

- ✅ Avoids overloading DOI semantics
- ✅ Enables future architectural evolution
- ✅ Better alignment with software interoperability requirements

### Negative

- ❌ Multiple identifier systems may coexist
- ❌ Additional governance may be required

### Risks & Mitigations

**Risk:** Users become confused by multiple identifiers
- **Mitigation:** Clearly document the purpose and scope of each identifier type

**Risk:** Where should documentation of DOIs live
- **Mitigation:** Tech team maintain a registry of registered DOIs
- **Mitigation:** Recommendation suggests using CITATION.cff as a way to organise these data
- **Mitigation:** GA4GH website will also hold some of these

---

## References

- **Full Recommendation:** [Citing GA4GH Documentation Recommendation](../recommendations/Citing%20GA4GH%20Documentation.md)

---

## Notes

This ADR intentionally leaves open the possibility of future GA4GH identifier frameworks for machine-readable use cases.