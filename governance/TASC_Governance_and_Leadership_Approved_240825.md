# TASC Governance and Leadership Charter

**Document Type**: Governance Charter  
**Document ID**: TASC-GOV-01  
**Source**: TASC  
**Title**: TASC Governance and Leadership Charter  
**Description**: The TASC charter: mission, membership, meeting format and the four-step decision-making process, including voting thresholds.  
**Related GitHub issues**: [#65](https://github.com/ga4gh/TASC/issues/65)  
**Authors**: TASC Leadership  
**Date**: 2024-08-25  
**Status**: Approved  
**Keywords**: governance, charter, leadership, decision-making  
**Work Streams Impacted**: All work streams  

## Table of contents

- [Abstract](#abstract)
- [Mission Statement and Scope](#mission-statement-and-scope)
- [TASC Structure](#tasc-structure)
  - [Membership](#membership)
- [Group Meeting Format](#group-meeting-format)
- [Decision-Making Process](#decision-making-process)
  - [Step 1: Collecting and Evaluating Issues](#step-1-collecting-and-evaluating-issues)
  - [Step 2: Working on a Solution](#step-2-working-on-a-solution)
  - [Step 3: Making Decisions](#step-3-making-decisions)
  - [Step 4: Dissemination](#step-4-dissemination)
- [Additional points](#additional-points)
- [Contributors](#contributors)

## Abstract

This charter defines the governance structure, membership, decision-making processes, and operational procedures of the GA4GH Technical Alignment Sub-Committee (TASC). It establishes TASC's mission to harmonize GA4GH technical products, outlines voting and non-voting membership roles, defines meeting formats (open/closed sessions), and specifies the four-step decision-making process from issue collection through dissemination. The charter includes membership term limits, voting thresholds (70% approval), and provisions for reopening decisions through CPO consultation with stakeholder committees.

## Mission Statement and Scope

The mission of the Technical Alignment Sub-Committee (TASC) of the GA4GH Product Steering Committee (PSC) is to aid the harmonisation of GA4GH's technical products to ensure they can be used together effectively. TASC provides outputs and decisions to create internal consistency and technical alignment across GA4GH Work Streams and deliverables.

While TASC functions as a central decision-making body, all of its decisions are informed by relevant stakeholders. The TASC outputs, including all decisions, are regularly and openly communicated back to the GA4GH community. Where appropriate, TASC will action product development related to technical alignment within its structure when a need is identified and would benefit the GA4GH community, the nature of the work does not naturally fit within one of the workstreams, the work requires significant cross-workstream development, and where sufficient interest and resources exist to develop the solution.

## TASC Structure

TASC is responsible for the development and oversight of solutions (including directives and products) to technical alignment issues across GA4GH workstreams. The TASC member network consists of participants to relay technical alignment issues and insights based on product knowledge and expertise, as well as the following voting members, who will make and uphold decisions regarding solutions in the best interest of GA4GH products collectively. This structure can be evaluated and updated on an as-needed basis and can be triggered by the CPO when the need arises.

### Membership

The voting members of TASC are:

* **The TASC Leadership** is composed of two volunteer co-leads who are responsible for convening the group, setting its agenda, facilitating decisions, and serving as the central point of communication for stakeholders. Agenda-setting includes identifying and prioritizing the issues to be addressed by the group. The CPO decides who holds the co-lead positions.
* **The Chief Product Officer (CPO)** ensures that the team creates GA4GH-wide technical alignment and that the needs of GA4GH are appropriately considered in any TASC outputs  
* **Work Stream Representatives.** Two volunteer representatives from each technical Work Stream and Data Security–preferably the Work Stream Co-leads–will provide knowledge and insight for their respective GA4GH products and communicate as liaisons. If they are not the representatives, the Work Stream Co-leads will select these representatives.

The non-voting members (advisory/contributors) are:

* Invited representative(s) from the **Strategic Leadership Committee (SLC)** to provide a strategic lens to TASC and represent TASC initiatives at SLC meetings
* Invited experts from the GA4GH community  
* Other appropriate members of the **GA4GH staff, including the GA4GH Tech Team.**

TASC co-leads and representatives will be expected to serve renewable two-year terms.

## Group Meeting Format

1. The Technical Alignment Sub-Committee (TASC) meets monthly, in either *open* or *closed* sessions, to:
   1. Review unresolved issues in the TASC GitHub repository (*open*)  
   2. Discuss potential unmet needs that could result in the generation of a new issue being added to the TASC GitHub repository (*open*)  
   3. Discuss and review any work being conducted within TASC’s remit, for example, regular updates from TASC working groups (*open*)  
   4. Review all GA4GH technical standards that have been submitted to the PSC for approval (*closed*)
2. Any topics requiring sensitive discussion or voting will be in closed session.  
3. For asynchronous discussion of issues, members can use
   1. Mailing List: Online and in-person meetings will be announced via email using this address: [tasc@ga4gh.org](mailto:tasc@ga4gh.org)  
   2. GitHub: Communication regarding technical contributions and questions is expected in the GitHub repository, found at [https://github.com/ga4gh/TASC](https://github.com/ga4gh/TASC)  
   3. Slack: Additional relevant discussions will happen on the GA4GH Slack Workspace. Use the \#tasc channel.

## Decision-Making Process

### **Step 1: Collecting and Evaluating Issues**

1. Any member of the GA4GH community may raise technical alignment concerns and propose technical alignment solutions as [new Issues in the TASC GitHub repository](https://github.com/ga4gh/TASC/issues). On an operational note, pushing to the [ga4gh/TASC](https://github.com/ga4gh/TASC) repo will be restricted to the TASC co-leads; everyone else will use a fork and pull request approach.  
2. The TASC co-leads and CPO will triage issues. New issues will be presented to the wider TASC group at the next available meeting. The wider TASC group will decide whether to accept IN SCOPE issues or close OUT OF SCOPE issues with a comment on the proposed GitHub issue based on the following criteria:  
   1. Issues that are IN SCOPE should have multiple invested adopters and MUST do one or more of the following:  
      1. Aid the harmonisation of aspects of GA4GH's various products, including the development, documentation, and deployment of said products, e.g., supporting schema alignment
      2. Lower the barriers to organisation-wide harmonisation between GA4GH products.  
      3. Produce directives, policies, and other documents that may enable greater harmonisation, interoperability, or use of specific GA4GH standards.  
   2. Issues may be closed with a comment if they:  
      1. are not feasible, e.g., too onerous to manage  
      2. require significant development, and there is a lack of sufficient resources/interest to develop within TASC  
      3. impose significant operational requirements on existing teams  
3. IN SCOPE issues that would generate outputs that require sufficient levels of cross-work stream development, that can’t realistically be developed in the conventional work streams, may be developed at the discretion of TASC and/or PSC  
   1. Outputs developed and implemented for internal use, including enterprise tools and infrastructure, WILL NOT be subject to the product development and approval process  
   2. Directives and policy statements issued by TASC WILL NOT be subject to the product development and approval process and MUST be reviewed and approved by PSC  
   3. External-facing products (e.g., a standard specification) WILL be subject to the product development and approval process  
      1. Other outputs will be reviewed and governed as per the discretion of TASC

### **Step 2: Working on a Solution**

1. Once an issue has been brought to TASC, it will be added to the [TASC project board](https://github.com/orgs/ga4gh/projects/9/views/1?filterQuery=-status%3ADone) and scoped accordingly, and any proposals that are deemed to be out of scope will be documented with the reason to maintain a decision log and retired. Any issue can be reactivated should interest and resources become available in the future.  
2. For an issue to be in-scope and prioritised, two TASC members (product owners) must be assigned to the issue. In the event that the most appropriate team to work on a solution is a subgroup, the issue will be actioned there. We will also seek adopters to help contribute towards solutions  
3. Owners research the issue, talking to relevant stakeholders and summarising their findings in a brief memo (as a Google document or GitHub repository).
4. GA4GH staff makes the memo available for open comment on the GA4GH website.
5. Any outputs that are proposed for development following the stakeholder consultation are similarly brought to TASC for discussion. Any output approved for development may need larger teams to work on the issue, and the product owner is accountable for creating the development team needed for the work, including the formation of small TASC forces or larger subgroups.  
6. All GA4GH active contributors, including TASC members, have a chance to weigh in on the memo
7. ALL TASC members are expected to have read the memo prior to the scheduled vote

### **Step 3: Making Decisions**

1. To reach a final decision, the two issue owners (see 2.2) must seek a vote from TASC members. The vote will be conducted asynchronously with materials presented at a TASC meeting and seeking to close voting by the next scheduled meeting, i.e., one calendar month.  
2. Notes on Voting  
   1. Members who vote will be given three options: 1\) approve, 2\) reject, 3\) abstain.
   2. The approval threshold is 70% of votes of the total eligible members with a “yes” vote.  
   3. The decision-making and voting process aims to  
      1. Ascertain a high level of consensus rather than unanimity  
      2. Ensure those who have opinions, raised objections, or contributed to development have an opportunity to share their thoughts  
      3. Ensure relevant GA4GH processes have been followed correctly  
   4. Members must ensure that products/outcomes (e.g., data models and specs):  
      1. do what they're designed to do without unduly constraining future development  
      2. are intentionally aligned with other specs at key touchpoints  
      3. do not create unnecessary barriers to interoperability  
3. Where approval is not reached through multiple rounds of votes, TASC Leadership, including the CPO, will make a final decision.  
4. Leadership can take decisions if two consecutive TASC meetings are not quorate — assuming efforts have been made between meetings to collect votes asynchronously  
5. Votes can be requested for approval over email when an issue is simple to close or when a decision must be taken between meetings.  
6. Proposals that have been open for more than 12 months must be taken to vote; if the proposal is rejected, it may be revised and resubmitted as a new issue.  
7. While TASC discussions will occur within GitHub issues, final decisions will be recorded in an [Architectural Decision Record](https://adr.github.io/) (ADR) which will be made publicly available at the TASC GitHub repository.  
8. While TASC decisions are intended to be conclusive, the CPO, in consultation with the PSC, TASC, SLC, or GA4GH Executive Committee, may determine that the issue should be reopened or the decision should be reviewed. The CPO will regularly update the relevant GA4GH committees on progress within any TASC developments to retain alignment with the GA4GH community and its objectives/needs.

### **Step 4: Dissemination**

1. Decisions will be included in the GA4GH communications, reported at the PSC meetings, and published to the GA4GH website.  
2. TASC members and Technical Programme Managers are responsible for maintaining awareness of these decisions within their work streams.  
3. Content-specific indices, repositories, etc., will be created as needed to facilitate the organisation and dissemination of decisions and common components.

## Additional points

* TASC members should help socialise issues by discussing those relevant to their work streams.  
* The proposal here may require an adjustment to the Product Development and Approval Process. Concerning the creation of products from TASC and the use of TASC to review technical products going through approval  
* TASC outputs should be positioned as GA4GH best practice, where we expect conformance on new GA4GH products, but do not expect backwards compatibility with historical outputs
* Any centralised registries or similar structures, if needed, will be managed by GA4GH staff
* Community will be empowered to use TASC and encourage submission of TASC issues, but we will need a mechanism to achieve this  
* TASC will use the Open Calls mechanism from [ga4gh.org](http://ga4gh.org) to raise awareness of solutions requiring input

## Contributors

- TASC Leadership
- GA4GH Product Steering Committee
- GA4GH Work Stream Representatives
