# TASC-ADR-012: TASC reviews, judges sufficiency, and arbitrates

**Decided:** GA4GH 2026 TASC Workshop (7–10 July 2026) | **Recorded:** 2026-07-28 | **Status:** Proposed

**Deciders:** TASC, GA4GH Technical Team, Chief Product Officer  
**Keywords:** pdap, review, authority, sufficiency, arbitration, interoperability  
**Work Streams Impacted:** All  
**Products Affected:** All GA4GH Technical Products entering PDAP v2  

---

## Context

PDAP v2 assigns TASC a role at two points without stating what authority that role carries. Section 3.1 makes the Gate 2 interoperability check something to be defined and evaluated by TASC, and Stage 1 has TASC approve a product's technical strategy on behalf of the Product Steering Committee. In neither case does the process say what happens when TASC is not satisfied, nor who resolves an interoperability conflict between two products that the products cannot resolve themselves.

**The Problem:**

- "Evaluated by TASC" and "approved by TASC on behalf of the PSC" are undefined; the extent of TASC's authority over a product's technical alignment is unclear
- Product teams do not know how they are expected to interact with TASC, what TASC is accountable for, or where a technical-alignment decision finally rests
- The PDAP places the burden of resolving an interoperability collision on the product moving through the process, even where the other product is established and unwilling to change
- Two readings are both undesirable: a TASC that only advises, leaving the technical-alignment gates without effect, and a TASC that must approve every individual decision record, which does not scale

**Alternatives Considered:**

1. **TASC advises only, with no authority**
   - ✅ Minimal load on TASC; TASC is never a gating factor
   - ❌ The technical-alignment gates carry no weight
   - ❌ Cross-product interoperability conflicts have no venue and no arbiter

2. **TASC reviews and approves each ADR in a product's decision record**
   - ✅ Fine-grained oversight of every decision
   - ❌ A single review can produce many decision records; approving each one does not scale
   - ❌ TASC would be editing the product's decision record, which is the product's to own

3. **TASC owns the criteria, reviews, judges the sufficiency of a product's resolutions, and arbitrates, exercising its authority at the stage transition**
   - ✅ Accountability is clear, and a product knows where a decision rests
   - ✅ A product receives one consolidated review rather than many independent ones
   - ✅ Cross-product conflict resolution has a defined venue
   - ✅ The product's decision record remains the product's to write

---

## Decision

TASC reviews a product's technical alignment, judges whether the product's resolutions are sufficient, and arbitrates interoperability conflicts between products. TASC holds review and approval authority for this purpose, and exercises it at the stage transition rather than over individual decision records.

**Key Points:**

- TASC owns the technical-alignment criteria (the interoperability definition, the technical product requirements, and the technical-alignment section of the Product Dossier) and reviews the Dossier at triage and at each checkpoint, assigning a technical-alignment tier
- TASC works its concerns up internally, on its own review repository, and delivers them to the product as a single aggregated response; the product writes the decision records that answer them, and TASC does not enter anything into the product's decision record
- TASC judges whether the product's resolutions are sufficient and retains review and approval authority over that judgement, exercised at the stage transition and not over any individual record
- TASC does not make the gate determination; the Independent Review Panel does, with TASC's technical-alignment sign-off as a required input
- TASC is the venue for resolving cross-product interoperability conflicts, and steps in where a conflict exceeds the parties' ability to resolve it; an established product is not the default standard to which others must conform
- TASC is not prescriptive about the form of a resolution, but a product may not proceed without regard to the other products it affects

---

## Consequences

### Positive

- ✅ A product team can see what TASC is accountable for and where a technical-alignment decision rests
- ✅ A product receives one consolidated review rather than separate reviews from individual reviewers
- ✅ Cross-product interoperability conflict resolution has a defined venue
- ✅ The product's decision record remains the product's to own

### Negative

- ❌ TASC becomes a gating factor in the PDAP and carries the associated review load
- ❌ Responsibility for technical-alignment decisions is concentrated on a volunteer body

### Risks & Mitigations

**Risk:** TASC becomes a bottleneck on every product going through the PDAP
- **Mitigation:** consolidate the review into a single aggregated response. The interoperability framework already schedules TASC's discussion meeting no sooner than two weeks after a Dossier is submitted, with the aggregated response following it, and a product may continue development in the interim at its own risk. No maximum turnaround was agreed, so any tighter target TASC publishes is a self-imposed best-effort commitment

**Risk:** Delegated approval authority is taken to include the authority to reject or terminate a product
- **Mitigation:** an objection from TASC is a recorded technical-alignment finding, not a product rejection; the PSC approves the product and hears escalations

---

## References

- **Directive:** [Role of TASC in the PDAP](../recommendations/role-of-tasc-in-pdap.md)
- **PDAP:** [GA4GH Product Development and Approval Process v2.0 draft](https://docs.google.com/document/d/1M4rsFHn0u-Qmtf5mdvPj_0J9j4R4tGBxsBTKpB43mag/edit) (Section 3.1)
- **Charter:** [TASC Governance and Leadership Charter (TASC-GOV-01)](https://github.com/ga4gh/TASC/blob/main/governance/TASC_Governance_and_Leadership_Approved_240825.md)
- **Issue:** <https://github.com/ga4gh/TASC/issues/93>

---

## Notes

Numbered 012 to match the reference carried in the role-of-TASC directive. The `adr/` directory currently holds TASC-ADR-001 to 005; numbers 006 to 011 are assumed reserved for the other decisions taken at the same workshop. If they are not, this record should be renumbered to the next free number and the two references in the directive updated. On acceptance, this record moves from `drafts/` to `adr/` per TASC-GOV-02.
