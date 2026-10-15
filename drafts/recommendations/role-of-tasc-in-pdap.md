# Role of TASC in the PDAP

**Document Type**: Directive  
**Document ID**: *unassigned*  
**Source**: TASC  
**Title**: Role of TASC in the PDAP  
**Related GitHub issues**: [#93](https://github.com/ga4gh/TASC/issues/93), [#90](https://github.com/ga4gh/TASC/issues/90), [#91](https://github.com/ga4gh/TASC/issues/91), [#92](https://github.com/ga4gh/TASC/issues/92)  
**Raised by**: Andy Yates (TASC Co-lead)  
**Authors**: Mamana Mbiyavanga  
**Date:** 2026-07-28  
**Status:** Draft  
**Keywords**: pdap, review, interoperability, risk-tier, conflict-resolution, accountability  
**Work Streams Impacted**: All work streams  
**Products Affected**: All GA4GH Technical Products entering PDAP v2  

## Abstract

Version 2 of the Product Development and Approval Process (PDAP) depends on TASC at two points but does not say what TASC does at either: Section 3.1 gives TASC the Gate 2 interoperability check ("defined and evaluated by TASC"), and Stage 1 has TASC approve a product's technical strategy on behalf of the Product Steering Committee. This directive sets out what TASC does as a product moves through the PDAP — what it reviews and decides, the risk tiers it assigns, where it engages across the lifecycle, where responsibility sits, and how it resolves conflict between products — and what it does not do. It is written for product owners and their teams, and its guidance is surfaced in the README of the PDAP review repository so that a team meets it where the review takes place. It complements the TASC Governance and Leadership Charter (TASC-GOV-01), whose statement of TASC's remit is general, and the operational detail in the PDAP Review Operating Procedure.

## Table of contents

- [Directive](#directive)
- [TASC's Responsibilities](#tascs-responsibilities)
- [Boundaries](#boundaries)
- [Engagement Across the Lifecycle](#engagement-across-the-lifecycle)
- [Risk Tiers](#risk-tiers)
- [Reviews and Responses](#reviews-and-responses)
- [Accountability](#accountability)
- [Cross-Product Conflict Resolution](#cross-product-conflict-resolution)
- [Scope](#scope)
- [References](#references)
- [Contributors](#contributors)
- [Notes](#notes)

## Directive

For every GA4GH Technical Product in PDAP v2:

- TASC MUST review the product's Technical Alignment section of the Product Dossier, assign and maintain a technical-alignment risk tier, and deliver its concerns to the product as a single aggregated response.
- The product team MUST address those concerns and record its decisions as ADRs in its own decision record; TASC MUST NOT write into that record.
- TASC judges whether the product's resolutions are sufficient and MUST give or withhold a technical-alignment sign-off at each gate, as a required input to the Independent Review Panel's determination.
- Where products cannot reach interoperability alignment between themselves, TASC is the venue that arbitrates; a product MAY diverge from another product only with a justification that TASC judges sufficient.

## TASC's Responsibilities

TASC owns the technical-alignment criteria against which a GA4GH product is measured: the definition of interoperability, the technical product requirements, and the technical-alignment section of the Product Dossier. Working from those criteria, TASC:

- reviews a product's Dossier at triage and at each checkpoint, and assigns a technical-alignment tier that reflects the interoperability risk the product carries;
- works its concerns up internally, on its own review repository, and delivers them to the product as a single response agreed at a TASC meeting, rather than as a stream of overlapping comments from individual reviewers;
- reviews the product's responses and judges whether they resolve those concerns sufficiently;
- clears or holds a stage transition on technical-alignment grounds, on the basis of that judgement; and
- arbitrates where two products cannot reach alignment between themselves.

## Boundaries

Several boundaries matter as much as the responsibilities above, because they shape how a product team should work with TASC.

- **TASC does not write entries into a product's decision record.** When it raises a concern, the work of deciding how to address it, and of recording that decision as an ADR, belongs to the product team. TASC supplies the concern; the product produces the response and owns the record of it.
- **TASC does not approve decision records one at a time.** Its review and approval authority is exercised over whether a product's resolutions, taken together, are acceptable at a stage transition, not over each individual record. The gate is the transition, not the record.
- **TASC does not make the gate determination.** The Independent Review Panel reviews the Dossier, the decision records, and the product's responses and determines whether the product is ready to advance; TASC's technical-alignment sign-off is a required input to that determination, not a substitute for it.
- **TASC does not police the PDAP.** The process holds together because several parties must each sign off before a product can advance, and a product cannot pass a gate while any of their conditions are unmet.
- **TASC does not complete the Dossier, or build the conformance suite.** The technical-alignment section is reviewed by TASC, not filled in by it, and a product's conformance suite is the product's to build and operate.

The governing principle is straightforward: TASC sets the framework for what makes a sound, interoperable GA4GH standard, and the product team drives its own product. Where a difficulty is beyond the team's power to resolve, TASC is there to help; short of that, the work and the initiative remain the team's.

## Engagement Across the Lifecycle

TASC's involvement is spread across the lifecycle rather than concentrated in a single review. The table below summarises where it engages and what it does at each point.

| PDAP point | What TASC does | Applies to |
| :-- | :-- | :-- |
| Stage 0 — Triage | Reviews the technical-alignment section of the Dossier, assigns the technical-alignment tier, and raises any concerns as internal issues | All products |
| Stage 1 — Product strategy | Approves technical alignment and overlap on behalf of the PSC | Tier 2 and Tier 3 |
| Checkpoint 1 (Draft) | Reviews the early narrative, reviews the product's responses to its issues, and re-assesses the tier | Mandatory at Tier 2 and Tier 3 |
| Gate 1 | Confirms the product's resolutions are accepted, and gives its technical-alignment sign-off | All products |
| Checkpoint 2 (Candidate) | Reviews progress, agrees the interoperability claims to be demonstrated at Gate 2, and re-assesses the tier | Mandatory at Tier 2 and Tier 3 |
| Gate 2 | Makes the Section 3.1 interoperability determination and gives its alignment sign-off | All products |
| Open comment period | Receives community feedback as issues alongside its own | All products |
| On escalation | Arbitrates a cross-product conflict the parties cannot resolve | As needed |

TASC's initial response is aggregated and delivered after a TASC meeting, which is scheduled no sooner than two weeks after the Dossier is submitted; a product may begin development in the interim, at its own risk. A product carrying a Tier 2 or Tier 3 assignment must complete Checkpoint 1.

A checkpoint and a gate are easily confused, and the distinction matters. A checkpoint records progress; a gate records acceptance. At a checkpoint it is enough for an issue to be addressed rather than closed: a credible plan to resolve it, to be confirmed at the next review, will do. At a gate the resolution must actually be accepted. For that reason a product should not open its public comment period until TASC, the foundational work streams, and the Independent Review Panel have each confirmed that nothing major remains outstanding, since going to the community early risks a second round of resolution and a second consultation.

At Gate 2, TASC makes the interoperability determination that Section 3.1 assigns to it. A technical product is expected to demonstrate at least two working implementations from independent groups, at least one of which is open, so that its interoperability can be observed in practice rather than asserted. A reference implementation is by its nature open; verified implementation is a separate and optional programme covering both open and closed implementations; and the requirement is judged at the time of review, since the implementations that establish a product's readiness need not persist indefinitely afterwards.

## Risk Tiers

At triage TASC assigns a technical-alignment risk tier. The tier reflects the interoperability risk a product carries: how significant the potential for overlap or conflict with existing GA4GH or external products is, and how much alignment effort addressing it will require. A tier is not a verdict on the product, and it can be reassessed as development proceeds.

| Tier | Profile | What it entails |
| :-- | :-- | :-- |
| Tier 1 (low) | Low or no significant risk of overlap with existing GA4GH or external products | TASC monitors the product's progress through the standard PDAP; nothing further is asked of the team |
| Tier 2 (medium) | Potential interoperability concerns; the product's design needs careful integration with existing standards | Potential risks are recorded as issues in the decision record and reviewed at regular check-ins, until the risk is either clarified down to Tier 1 or confirmed as Tier 3 |
| Tier 3 (high) | A confirmed interoperability concern, broad ecosystem impact, or a high potential for conflicting requirements | An active alignment effort: a mitigation plan, tracked review through Draft and Candidate, formal TASC sign-off at Gate 2, and an external audit for interoperability traps |

Tier 2 is best read as a state of insufficient clarity rather than a finding. The mitigation a product provides at Checkpoint 1 should establish why the risk belongs at Tier 1 or at Tier 3. Tiers are revisited as the product develops, since much of the useful interoperability feedback only becomes available once there is a technical specification to examine.

A Tier 3 mitigation plan should set out, at a minimum:

- a regular forum for technical-alignment discussions;
- a defined frequency at which that forum meets; and
- a mechanism for resolving conflict, for which TASC is the de facto venue.

It should also say who the product intends to engage, what it believes a solution looks like, and how much support it is asking of TASC. TASC is not prescriptive about the form a resolution takes; what it requires is that the matter be resolved sufficiently, and that a product not proceed without regard to the other products it affects.

## Reviews and Responses

A product team can expect:

- a single aggregated response agreed by TASC, rather than one set of comments per reviewer, with each point traceable to the TASC review record that produced it and carrying its own tier, since each is resolved on its own terms; and
- a review summary that enumerates what has been raised for the product.

In return, TASC expects the product team to:

- write the decision records that answer its issues, one decision per record and each immutable, so that a changed decision becomes a new record superseding the old one;
- ensure the Dossier summarises the responses and links to those records; and
- notify TASC when it has finished responding, at which point TASC takes a second look.

A team that would rather draft its responses and iterate with TASC before committing decision records, so as to avoid a trail of superseded ones, is free to work that way.

## Accountability

A product's tier is decided by TASC, by consensus of its reviewers, and recorded in the review. Whether a given resolution is sufficient is likewise TASC's to judge, and TASC retains review and approval authority over that judgement. The point at which TASC can hold a product is the stage transition, not the individual decision record. The gate determination itself is made by the Independent Review Panel, with TASC's sign-off as a required input, and the product as a whole is approved by the Product Steering Committee at Stage 3. Should TASC decline to sign off, it states its grounds, and the product may escalate to the PSC, which may accept the position, remit it, or overrule it.

Two limits follow. An objection from TASC is a recorded technical-alignment finding, not a rejection of the product; and the authority delegated to TASC to approve a product's technical strategy carries with it no authority to terminate the product.

## Cross-Product Conflict Resolution

TASC is the venue in which cross-product interoperability conflicts are resolved.

Being the incumbent confers no special authority. A product that happens to be older is not the default standard to which everything else must conform, and where several products are involved the right answer may be none of the positions currently held. A product may deviate from an existing product where that product will not move, provided it justifies the deviation, and that justification comes to TASC to judge sufficient or not. The product leads the conversation first, because it understands its own domain best, and turns to TASC as the escalation path rather than the first port of call. Where a conflict genuinely exceeds the parties' power to resolve, TASC steps in, convening those involved and working towards a resolution itself. It may also say in advance what it believes a resolution should look like, or issue modelling recommendations for a contested area before positions harden.

A product team that finds itself in a collision beyond its power to solve should escalate it.

## Scope

This document applies in the first instance to new products entering PDAP v2, whose interoperability is assessed prospectively. The interoperability framework also provides for products already in existence. An existing product under active development that did not launch under PDAP v2 follows an alignment plan that brings it under PDAP v2 governance and closes interoperability gaps against other GA4GH products. An existing product no longer under active development is instead audited to document where those gaps lie, which is an internal operational exercise and does not call for active TASC participation. Whether and when an existing product enters one of these paths is a judgement for its work stream lead, weighing the product's trajectory, the demand from its community, and its continued fit; some products will have little to gain, while others will need the additional rigour for their credibility.

## References

- [PDAP] [GA4GH Product Development and Approval Process v2.0 draft, 2026-05-19](https://docs.google.com/document/d/1M4rsFHn0u-Qmtf5mdvPj_0J9j4R4tGBxsBTKpB43mag/edit)
- [TASC-INTEROP] [GA4GH 2026 TASC Interoperability](https://docs.google.com/document/d/1_NVRgxqaq_6m0k2Wzjd_7oBwFxlQtsnsxY0t3N_ebIU/edit)
- [DOSSIER] [Technical Product Dossier](https://docs.google.com/document/d/1McYw7Py4SVASDpzj0b5HpoJg_-yT-FE7xf0QXEBekls/edit)
- [TASC-GOV-01] [TASC Governance and Leadership Charter](https://github.com/ga4gh/TASC/blob/main/governance/TASC_Governance_and_Leadership_Approved_240825.md)
- [TASC-GOV-02] [TASC Document Standards](https://github.com/ga4gh/TASC/blob/main/governance/TASC_Document_Standards.md)
- [PROC] [PDAP Review Operating Procedure](pdap-review-operating-procedure.md)
- [TASC-ADR-012] [TASC reviews, judges sufficiency, and arbitrates](../adr/TASC-ADR-012.md)
- [ISSUE-93] <https://github.com/ga4gh/TASC/issues/93>

## Contributors

Participants in the GA4GH 2026 TASC Workshop, 7–10 July 2026:

| Name | Organisation |
| :-- | :-- |
| Andy Yates | EMBL-EBI / TASC Co-lead |
| Mamana Mbiyavanga | University of Cape Town / TASC Co-lead |
| Sasha Siegel | EMBL-EBI / GA4GH Chief Product Officer |
| Alex Wagner | Nationwide Children's Hospital / GKS |
| Larry Babb | Broad Institute / GKS |
| Melissa Cline | UC Santa Cruz / GKS |
| Monica Munoz-Torres | University of Colorado Anschutz / Clin-Pheno |
| Robert Freimuth | Mayo Clinic / GKS |
| Brian O'Connor | Nimbus Informatics / Federated Analysis (Cloud) |
| Miro Cupak | DNAstack / Discovery |
| David Bujold | McGill University / Discovery |
| Jon Turner | Wellcome Sanger Institute / Web Development |
| Jimmy Payyappilly | EMBL-EBI / Technical Team |
| Jeremy Adams | Ontario Institute for Cancer Research / Technical Team |
| Dashrath Chauhan | EMBL-EBI / Technical Team |
| Tom Conner | Broad Institute / Data Security |

## Notes

Drafted with the assistance of Claude Sonnet 5 (Anthropic) via Claude Code, from the TASC Governance and Leadership Charter (TASC-GOV-01), the 2026 TASC Interoperability framework, the PDAP v2 draft, the Technical Product Dossier, and source material from the GA4GH 2026 TASC Workshop, July 2026. All content has been reviewed for accuracy.
