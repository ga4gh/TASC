![](https://www.ga4gh.org/wp-content/themes/ga4gh-theme/gfx/GA-logo-horizontal-tag-RGB.svg)

# GA4GH Technical Alignment Sub Committee (TASC) [![](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://raw.githubusercontent.com/ga4gh-discovery/ga4gh-service-registry/develop/LICENSE)

The Technical Alignment Sub-Committee (TASC) of the GA4GH Product Steering Committee (PSC) aids the harmonisation of GA4GH's technical products to ensure they can be used together effectively. TASC provides outputs and decisions to create internal consistency and technical alignment across GA4GH Work Streams and deliverables.

While TASC functions as a central decision-making body, all of its decisions are informed by relevant stakeholders. The TASC outputs, including all decisions, are regularly and openly communicated back to the GA4GH community. Where appropriate, TASC will action product development related to technical alignment within its structure when a need is identified and would benefit the GA4GH community, the nature of the work does not naturally fit within one of the workstreams, the work requires significant cross-workstream development, and where sufficient interest and resources exist to develop the solution.

TASC organizes and monitors its technical alignment activities through a [GitHub Project board](https://github.com/orgs/ga4gh/projects/9/views/1), where you can find and track the progress of current issues and initiatives.

## Table of Contents
- [TASC Structure](#tasc-structure)
- [TASC Members](#tasc-members)   
- [Group Meeting Format](#group-meeting-format)
- [Decision-Making Process](#decision-making-process)   
- [Issue labels](#issue-labels)   

## TASC Structure

TASC is responsible for the development and oversight of solutions (including directives and products) to technical alignment issues across GA4GH workstreams. The TASC member network consists of participants to relay technical alignment issues and insights based on product knowledge and expertise, as well as voting members who will make and uphold decisions regarding solutions in the best interest of GA4GH products collectively.

## TASC members

### Voting Members

#### TASC Leadership
- **Mamana Mbiyavanga** - Co-lead
- **Andy Yates** - Co-lead

The TASC Leadership is composed of two volunteer co-leads who are responsible for convening the group, setting its agenda, facilitating decisions, and serving as the central point of communication for stakeholders. The CPO decides who holds the co-lead positions.

#### Chief Product Officer (CPO)
- **Sasha Siegel** - Chief Product Officer

The CPO ensures that the team creates GA4GH-wide technical alignment and that the needs of GA4GH are appropriately considered in any TASC outputs.

#### Work Stream Representatives

| Member | Work Stream |
|--------|-------------|
| **Michael Baudis** | Discovery |
| **Venkat Malladi & Alex Kanitz** | Cloud |
| **John Marshall** | Large Scale Genomics |
| **Jaime Guidry Auvil & Jonathan Lawson** | DURI |
| **Bob Freimuth & Alex Wagner** | GKS |
| **Francesca Frexia** | Clin/Pheno |
| **David Bernick** | Data Security |

Two volunteer representatives from each technical Work Stream and Data Security–preferably the Work Stream Co-leads–provide knowledge and insight for their respective GA4GH products and communicate as liaisons.

#### DaMaSC Sub-group Representative
- **Kathy Reinold** - DaMaSC

A representative from the DaMaSC sub-group participates in TASC decisions as a voting member.

### Non-Voting Members (Advisory/Contributors)

#### GA4GH Staff Technical Team
TASC also enlists support from the GA4GH Staff Technical Team to encourage technical alignment across the Work Streams.

| Member | Email | Role |
|--------|-------|------|
| **Reggan Thomas** | reggan.thomas@ga4gh.org | Staff Technical Team Support |
| **Jimmy Payyappilly** | | Staff Technical Team |
| **Angela Page** | | Staff Technical Team |
| **Chen Chen** | | Staff Technical Team |
| **Jon Turner** | | Staff Technical Team |

#### Other Non-Voting Members
- Invited representative(s) from the Strategic Leadership Committee (SLC)
- Invited experts from the GA4GH community
- Other appropriate members of the GA4GH staff

## Group Meeting Format

TASC meets monthly in either *open* or *closed* sessions to review unresolved issues, discuss unmet needs, review TASC work, and review GA4GH technical standards submitted to PSC for approval. Topics requiring sensitive discussion or voting are conducted in closed sessions.

For asynchronous discussion, members use:
- **Mailing List**: [tasc@ga4gh.org](mailto:tasc@ga4gh.org)
- **GitHub**: [https://github.com/ga4gh/TASC](https://github.com/ga4gh/TASC)
- **Slack**: GA4GH Slack Workspace, #tasc channel

## Decision-Making Process

### **Step 1: Collecting and Evaluating Issues**
1. Any GA4GH community member may raise technical alignment concerns as [new Issues](https://github.com/ga4gh/TASC/issues)
2. TASC co-leads and CPO triage issues and present them to the wider TASC group
3. TASC group decides whether to accept IN SCOPE issues or close OUT OF SCOPE issues based on criteria:
   - **IN SCOPE**: Multiple invested adopters AND must do one or more of the following:
     - Aid the harmonisation of aspects of GA4GH's various products, including the development, documentation, and deployment of said products (e.g., supporting schema alignment via DaMaSC)
     - Lower the barriers to organisation-wide harmonisation between GA4GH products
     - Produce directives, policies, and other documents that may enable greater harmonisation, interoperability, or use of specific GA4GH standards
   - **OUT OF SCOPE**: Issues may be closed if they:
     - Are not feasible (e.g., too onerous to manage)
     - Require significant development with lack of sufficient resources/interest to develop within TASC
     - Impose significant operational requirements on existing teams

4. **TASC Product Development Criteria**: TASC will action product development when:
   - A need is identified and would benefit the GA4GH community
   - The nature of the work does not naturally fit within one of the workstreams
   - The work requires significant cross-workstream development
   - Sufficient interest and resources exist to develop the solution

5. **Cross-Workstream Development**: IN SCOPE issues that would generate outputs requiring sufficient levels of cross-work stream development, that can't realistically be developed in the conventional work streams, may be developed at the discretion of TASC and/or PSC

6. **Output Types and Approval Process**:
   - Internal-use outputs (enterprise tools, infrastructure) WILL NOT be subject to product development and approval process
   - Directives and policy statements WILL NOT be subject to product development and approval process but MUST be reviewed and approved by PSC
   - External-facing products (e.g., standard specifications) WILL be subject to product development and approval process
   - Other outputs will be reviewed and governed as per the discretion of TASC

### **Step 2: Working on a Solution**
1. **Project Board Management**: Issues are added to the [TASC project board](https://github.com/orgs/ga4gh/projects/9/views/1?filterQuery=-status%3ADone) and scoped accordingly. Any proposals deemed out of scope are documented with reasons to maintain a decision log and retired. Any issue can be reactivated should interest and resources become available in the future.

2. **Product Owner Assignment**: Two TASC members (product owners) must be assigned to in-scope issues. In the event that the most appropriate team to work on a solution is a subgroup, the issue will be actioned there. TASC will also seek adopters to help contribute towards solutions.

3. **Research and Stakeholder Consultation**: Product owners research the issue, talking to relevant stakeholders and summarising their findings in a brief memo (as a Google document or GitHub repository).

4. **Open Community Review**: GA4GH staff makes the memo available for open comment on the GA4GH website.

5. **Development Planning**: Any outputs proposed for development following stakeholder consultation are brought to TASC for discussion. Any output approved for development may need larger teams, and the product owner is accountable for creating the development team needed for the work, including the formation of subgroups.

6. **Community Input**: All GA4GH active contributors, including TASC members, have a chance to weigh in on the memo.

7. **Pre-Vote Preparation**: ALL TASC members are expected to have read the memo prior to the scheduled vote.

### **Step 3: Making Decisions**
1. Two issue owners seek a vote from TASC members (asynchronous, one calendar month)
2. Voting options: approve, reject, or abstain
3. Approval threshold: 70% of total eligible members with "yes" vote
4. **Voting Process Aims**:
   - Ascertain high level of consensus rather than unanimity
   - Ensure those with opinions, objections, or contributions have opportunity to share thoughts
   - Ensure relevant GA4GH processes have been followed correctly
5. **Product Requirements**: Members must ensure products/outcomes:
   - Do what they're designed to do without unduly constraining future development
   - Are intentionally aligned with other specs at key touchpoints
   - Do not create unnecessary barriers to interoperability
6. If approval not reached through multiple rounds, TASC Leadership makes final decision
7. Leadership can take decisions if two consecutive meetings are not quorate
8. Proposals open for more than 12 months must be taken to vote
9. Final decisions recorded in [Architectural Decision Records](https://adr.github.io/)
10. CPO may reopen issues or review decisions in consultation with PSC, TASC, SLC, or GA4GH Executive Committee

### **Step 4: Dissemination**
1. Decisions included in GA4GH communications and published to website
2. TASC members maintain awareness within their work streams
3. Content-specific indices and repositories created as needed

## Issue labels
### By Status (Open)
- **CRITICAL**: Decision needs to be made soon

### By Status (Closed)
- **Duplicate**: This issue or pull request already exists
- **Approach Resolved**: Consensus reached or final decision taken by TASC leadership
- **Out of Scope**: Issue or pull request not a TASC task and will not be looked at

### By Area
- **Documentation**: Improvements or additions to documentation
- **Product Approval Process**: Going through GA4GH approval's process
- **Update to existing TASC managed process**: Improvements or additions to TASC managed process

