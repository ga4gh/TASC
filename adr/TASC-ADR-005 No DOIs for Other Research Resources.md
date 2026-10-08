# TASC-ADR-005: Do Not Extend GA4GH DOIs to Other Research Resources

**Date:** 2026-07-07 | **Status:** Proposed

**Description:** GA4GH DOIs are limited to documentary outputs and are not extended to datasets, tools or other research resources.  
**Deciders:** TASC, GA4GH Technical Team, Chief Product Officer  
**Keywords:** doi, persistent-identifier, datasets, scope, governance  
**Work Streams Impacted:** All  
**Products Affected:** None directly (policy)

---

## Context

While developing the GA4GH DOI citation mechanism for documentary outputs (standards, technical specifications, protocols, products, white papers, selected blog posts), the question was raised as to whether the same mechanism should also be used to mint persistent identifiers for GA4GH-related datasets and other research resources.

**The Problem:**

- Datasets and other research resources also benefit from stable, citable, persistent identifiers
- Extending GA4GH's DOI program to cover datasets would significantly broaden its scope beyond documentary citation
- GA4GH does not operate data hosting or curation functions
- Established persistent identifier ecosystems for datasets already exist and are maintained by organisations with the relevant data governance responsibilities
- Some products bundle test data within an official release's test suite. Such bundled test data is considered part of that product's documentary output (and therefore in scope for a DOI covering the release), rather than a standalone research dataset. Edge cases MUST be resolved case-by-case by the originating group together with the Technical Team

**Alternatives Considered:**

1. **Extend the GA4GH DOI mechanism to cover datasets**
   - ✅ Single, consistent identifier mechanism across all outputs
   - ❌ Expands GA4GH's minting and metadata-maintenance obligations well beyond documentary outputs
   - ❌ GA4GH is not the natural steward of dataset identity or availability, unlike its role for its own documentary outputs
   - ❌ Duplicates existing, better-suited dataset identifier ecosystems

2. **Do not extend the GA4GH DOI mechanism to datasets; leave dataset identification out of scope**
   - ✅ Keeps the GA4GH DOI program focused and operationally manageable
   - ✅ Avoids duplicating existing dataset persistent-identifier infrastructure
   - ❌ GA4GH datasets remain reliant on whatever identifier scheme their hosting repository provides

---

## Decision

GA4GH will not use, or extend, its DOI mechanism to serve as the persistent identifier scheme for datasets, tools, or other research resources. The scope of GA4GH-minted DOIs is restricted to documentary outputs.

**Key Points:**

- GA4GH-minted DOIs MUST NOT be used as a general-purpose persistent identifier mechanism for datasets, tools, or other research resources
- Datasets requiring persistent identifiers SHOULD use established dataset-identifier mechanisms appropriate to where they are hosted or governed
- This decision bounds the scope of the Citing GA4GH Documentation Recommendation, which applies only to documentary outputs
- Due to the nature of some documentary outputs they may contain data supporting testing. This is a consequence of minting said DOI

---

## Consequences

### Positive

- ✅ Keeps the GA4GH DOI program scoped to what GA4GH can realistically govern and maintain
- ✅ Avoids duplicating or competing with existing dataset persistent-identifier ecosystems
- ✅ Reduces ongoing metadata-maintenance burden on GA4GH's Technical Team

### Negative

- ❌ GA4GH datasets do not gain a consistent, GA4GH-controlled citation mechanism analogous to documentary outputs
- ❌ Work Streams must look to external or repository-specific mechanisms for dataset persistent identification

### Risks & Mitigations

**Risk:** Confusion arises over whether a GA4GH DOI can be used to cite a dataset
- **Mitigation:** State explicitly in the Citing GA4GH Documentation Recommendation that the recommendation does not apply to datasets, tools, or other research resources

---

## References

- **Full Recommendation:** [Citing GA4GH Documentation Recommendation](../recommendations/Citing%20GA4GH%20Documentation.md)
