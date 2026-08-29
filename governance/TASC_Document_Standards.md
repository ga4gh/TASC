# TASC Document Standards

**Document Type**: Governance Charter  
**Document ID**: TASC-GOV-02  
**Source**: TASC  
**Title**: TASC Document Standards: Format, Placement, and Communication Standards for TASC Outputs  
**Related GitHub issues**: [#76](https://github.com/ga4gh/TASC/pull/76)  
**Raised by**: Mamana Mbiyavanga (TASC)  
**Authors**: Mamana Mbiyavanga, Andy Yates, Sasha Siegel, Jinny Park  
**Date**: 2026-02-01  
**Status**: Draft  
**Keywords**: governance, document-standards, templates, numbering, placement, communication  
**Work Streams Impacted**: All work streams  

## Abstract

This document formalizes the format, placement, and communication standards for all TASC outputs. It establishes two document types (living policies and immutable decision records), standard metadata templates, a numbering convention, the GitHub repository as the canonical source of truth, and a communication workflow to ensure approved outputs reach the GA4GH community.

## Table of contents

- [Background](#background)
- [Document Types](#document-types)
- [Metadata Templates](#metadata-templates)
- [Numbering Convention](#numbering-convention)
- [Repository Structure](#repository-structure)
- [Document Lifecycle](#document-lifecycle)
- [Communication Workflow](#communication-workflow)
- [Website and Airtable Integration](#website-and-airtable-integration)
- [References](#references)
- [Contributors](#contributors)

## Background

TASC has produced a growing number of approved outputs -- recommendations, governance charters, and architectural decision records. Without standardized format and placement, outputs were scattered across Google Docs, GitHub, emails, and meeting notes. Stakeholders could not easily find or reference decisions, leading to duplication, version confusion, and inconsistent formats across authors and time periods. New members had no efficient way to catch up on past decisions.

This document formalizes the structure that has been adopted in the `ga4gh/TASC` GitHub repository, drawing on practices from other standards organizations (HL7 FHIR, W3C, IETF) that separate living specifications from decision rationale.

## Document Types

TASC outputs fall into two categories with distinct characteristics:

### Recommendations and Governance Documents (Living)

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Ongoing rules, procedures, standards, and guidance |
| **Nature** | Living, prescriptive, comprehensive |
| **Length** | Typically 10-50+ pages |
| **Scope** | Broad domain or process |
| **Key Question** | "What are the rules?" |

These documents define processes and standards that apply broadly and MAY evolve over time through a formal revision process. Examples include the API Pagination Guide (GA4GH-REC-01) and the TASC Governance Charter (TASC-GOV-01).

### Architectural Decision Records (Immutable)

| Attribute | Description |
|-----------|-------------|
| **Purpose** | Single decision + rationale |
| **Nature** | Immutable, explanatory, focused |
| **Length** | 1-2 pages |
| **Scope** | Single architectural choice |
| **Key Question** | "Why did we decide this way?" |

ADRs follow the Michael Nygard template and capture the context, alternatives considered, decision made, and consequences. Once accepted, ADRs MUST NOT be edited. If a decision changes, a new ADR supersedes the original.

### When to Use Which

- **Write a Recommendation/Governance document when**: Defining ongoing rules, procedures, or standards that apply broadly and may evolve.
- **Write an ADR when**: The decision could have gone another way and the rationale matters for future reference.

The policy tells the process. The ADR records when that process was used to make a specific choice.

## Metadata Templates

### Recommendation / Governance Metadata Header

All recommendations and governance documents MUST include the following metadata header:

```markdown
**Source**: TASC  
**Recommendation**: GA4GH-REC-XX (or **Document ID**: TASC-GOV-XX)  
**Title**: [Full descriptive title]  
**Related GitHub issues**: [#N](https://github.com/ga4gh/TASC/issues/N)  
**Raised by**: [Name (Work Stream/Role)]  
**Authors**: [Author names, comma-separated]  
**Date:** YYYY-MM-DD  
**Status:** [Draft | Approved | Superseded]  
**Keywords**: [comma-separated keywords]  
**Work Streams Impacted**: [affected work streams]  
**Products Affected**: [affected GA4GH products]  
```

### ADR Metadata Header

All ADRs MUST include the following metadata header and follow the Nygard template structure:

```markdown
# TASC-ADR-XXX: [Short Decision Title]

**Decided:** [when the decision was taken, e.g. a meeting or workshop] | **Recorded:** YYYY-MM-DD | **Status:** [Proposed | Accepted | Deprecated | Superseded]  
**Deciders:** [List key decision-makers]  
**Keywords:** [comma-separated keywords]  
**Work Streams Impacted:** [affected work streams]  
**Products Affected:** [affected GA4GH products]  

## Context
## Decision
## Consequences
```

### Metadata Field Definitions

| Field | Description |
|-------|-------------|
| **Source** | Always "TASC" |
| **Raised by** | The person and work stream/role that originally raised the issue (recommendations only) |
| **Authors** | Those who wrote the document |
| **Deciders** | Those who made the decision (ADRs only) |
| **Decided** | The date the decision was taken, e.g. at a meeting or workshop (ADRs only) |
| **Recorded** | The date the ADR document was written (ADRs only) |
| **Keywords** | Searchable tags for discoverability (e.g., api, pagination, governance, maturity-model) |
| **Work Streams Impacted** | GA4GH work streams affected by the document |
| **Products Affected** | Specific GA4GH products impacted |
| **Status** | Current state: Draft, Approved/Accepted, Superseded/Deprecated |

Each metadata line MUST end with two trailing spaces for proper Markdown line breaks.

## Numbering Convention

| Document Type | ID Format | Example |
|---------------|-----------|---------|
| Recommendations | `GA4GH-REC-XX` | GA4GH-REC-01 |
| Governance documents | `TASC-GOV-XX` | TASC-GOV-01 |
| Architectural Decision Records | `TASC-ADR-XXX` | TASC-ADR-001 |

- Recommendations use the `GA4GH-` prefix as they represent organization-wide guidance.
- Governance documents and ADRs use the `TASC-` prefix as they are scoped to the sub-committee.
- Numbers are zero-padded and assigned sequentially.

## Repository Structure

The `ga4gh/TASC` GitHub repository is the canonical source of truth for all TASC outputs:

```text
ga4gh/TASC/
├── README.md
├── adr/
│   ├── README.md          (index table)
│   ├── template.md
│   └── NNN-short-title.md (accepted ADRs)
├── governance/
│   └── TASC-GOV-XX_Title.md
├── recommendations/
│   ├── template.md
│   └── [Recommendation Title].md
├── drafts/                (work in progress)
├── service-info/
│   └── ga4gh-service-info.json
└── data/                  (supporting materials, not committed)
```

- **`adr/`** -- Immutable decision records. ADR files use the naming convention `NNN-short-kebab-title.md` with zero-padded 3-digit numbers.
- **`governance/`** -- TASC operating charters and leadership rules.
- **`recommendations/`** -- Approved policy documents and guidance.
- **`drafts/`** -- Work-in-progress documents that graduate to their respective directories upon approval.
- **`service-info/`** -- The GA4GH Service Info Type Registry.

## Document Lifecycle

Documents follow the TASC charter's four-step decision-making process:

1. **GitHub Issue** -- Anyone in the GA4GH community can raise a technical alignment concern.
2. **Discussion** -- TASC meetings and asynchronous discussion on GitHub/Slack.
3. **Draft** -- Work in progress, placed in `drafts/`.
4. **Review / Vote** -- 70% approval threshold per the TASC Governance Charter (TASC-GOV-01).
5. **Approved** -- Placed in the appropriate directory:
   - Recommendations go to `recommendations/`
   - ADRs go to `adr/`
   - Governance documents go to `governance/`

## Communication Workflow

When a new output is approved, the following communication steps SHOULD be followed:

| Step | Action | Channel |
|------|--------|---------|
| 1 | Merge PR | GitHub repository (source of truth) |
| 2 | Update Airtable | Metadata registry |
| 3 | Post announcement | TASC mailing list + Slack #tasc |
| 4 | Update website | GA4GH website cards |
| 5 | Present at GA4GH Connect | If the output is significant |

This ensures no approved output "goes dark" -- every output reaches the people who need to know.

## Website and Airtable Integration

All approved outputs SHOULD appear as cards on the GA4GH website, linking back to the GitHub source document. The Airtable metadata registry SHOULD contain the following fields for each output:

| Field | Description |
|-------|-------------|
| Title | Document name |
| Description | Brief summary |
| Alignment Scope | GA4GH alignment area |
| Work Streams | Affected work streams |
| Products | Related GA4GH products |
| Tags | Searchable keywords |
| Directive (Y/N) | Mandatory vs. guidance |
| Link | URL to GitHub source |

## References

- [TASC Governance and Leadership Charter (TASC-GOV-01)](TASC_Governance_and_Leadership_Approved_240825.md)
- [Michael Nygard's ADR template](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [TASC Placement Proposal Presentation](https://docs.google.com/presentation/d/1zc4VeoZVaU2fIr6dP9VSFhHxIceWzglt/edit) (February 2026)
- [GA4GH TASC GitHub Project Board](https://github.com/orgs/ga4gh/projects/9/views/1)

## Contributors

| Name | Organisation |
|------|-------------|
| Mamana Mbiyavanga | University of Cape Town / TASC Co-lead |
| Andy Yates | EMBL-EBI / TASC Co-lead |
| Sasha Siegel | GA4GH / CPO |
| Jinny Park | GA4GH / Technical Team |
