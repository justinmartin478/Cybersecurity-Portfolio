# Key Deliverables and Project Methodologies

*Deliverables for the Gatorware Software systems upgrade and methodology selection for three business scenarios*

**Course:** IT295 CompTIA Project+ Cert Prep &nbsp;·&nbsp; **Module:** 4 &nbsp;·&nbsp; **Type:** Report

> The full assignment is rendered below. The original and a formal copy are available for download: [**Word document**](./IT295_Module4_Key_Deliverables_and_Methodologies_Portfolio_Justin_Martin.docx) · [**PDF**](./IT295_Module4_Key_Deliverables_and_Methodologies_Portfolio_Justin_Martin.pdf)

| Team Member | Course | Assignment | Parts |
| --- | --- | --- | --- |
| Justin Martin | IT295 | Module 4 | A and B |

---

| Key Deliverables | Deliverable Groups | Scenarios | Methodologies |
| --- | --- | --- | --- |
| 12 | 5 | 3 | 3 |

## Methodology Selections at a Glance

|  | Scenario | Selection | Deciding factors |
| --- | --- | --- | --- |
| A | FDIC insured bank | WATERFALL | Mature systems, minor predictable changes, audit documentation |
| B | Java and C# software company | AGILE + XP | Reusable libraries, faster releases, XP testing and refactoring |
| C | Medical AI startup | HYBRID | Evolving requirements with doctors, formal validation before clinical use |

## A. Gatorware Software Key Deliverables

The main goal of this project is to give Gatorware the infrastructure and development capabilities it needs to expand its operations. I would identify the following key deliverables because each one is a completed result that supports the new environment described in the scenario.

### Cloud and Platform

**01. AWS development QA and production environments**

Separate, configured AWS environments for development, quality assurance, and production. Existing applications and required data would be migrated from the current environment and tested for compatibility. This includes addressing any dependencies on AIX before the cloud environments are accepted.

**02. Container platform using Docker and Kubernetes**

Applications packaged in Docker containers, with Kubernetes configured to deploy and manage them. The completed platform should support consistent deployments across the cloud environments and be tested to confirm that applications can run and recover as expected.

**03. Cloud hosted SaaS service**

A working subscription service that lets customers securely log in and access their own container configured to their specifications. Customer access, subscription handling, and separation of customer environments should be tested before the service is made available. Since the customers include HMOs and banks, a documented security and compliance review would also be part of accepting this deliverable.

### Onsite Systems and Team Tools

**04. Dell servers and workstations**

Installed and configured Dell PowerEdge servers and Dell Windows workstations to replace the onsite mainframe and thin client environment. The workstations should support the tools employees need and connect successfully to the approved company services.

**05. GitHub source code repositories**

Company source code migrated from Subversion to GitHub, with repository permissions and a documented process for managing changes. The migration should preserve needed history and confirm that authorized developers can retrieve code and collaborate without losing existing work.

**06. Slack collaboration workspace**

A configured Slack workspace with channels and access rules for the development teams and approved consultants. The workspace should give teams a shared place to communicate about development work and coordinate changes across locations.

### Development Process

**07. In house AI development agents**

Developed and deployed AI agents that assist with agreed software development tasks. The agents should be tested for useful results, with controls over access to company code and data and human review before generated changes are accepted.

**08. Agile development process using Extreme Programming**

A documented and adopted Agile process that emphasizes Extreme Programming practices such as pair programming, automated testing, refactoring, and frequent releases. Team training and a pilot iteration would help demonstrate that the new process is ready to use.

### Connectivity and Access

**09. Network connectivity for the expanded organization**

A configured network solution connecting the two main campuses, satellite offices, and AWS environments. The completed connections should be tested for reliable communication and sufficient capacity for the company's development and business activities.

**10. Secure VPN access and consultant permissions**

A working VPN service that allows approved IT employees and third party vendors to access authorized environments remotely. User authentication, access restrictions, and logging should be configured and tested so users receive only the access needed for their work.

**11. BYOD policy and supporting controls**

An approved Bring Your Own Device policy with the technical controls needed to support it. The deliverable should define eligible devices, security requirements, enrollment, access limits, and how company access is removed when a device or user is no longer authorized.

### Transition

**12. Validated migration and operational handoff**

Documented test results, operating procedures, and a completed handoff to IT staff. Backup and recovery arrangements should be validated for the new cloud and GitHub environment, since the existing tape process may not cover them. The old systems should be retired only after the replacements are accepted.

I would confirm the detailed acceptance criteria with the stakeholders before work begins. The deliverables above define what the project should produce without assuming a budget, schedule, or additional features that the scenario does not provide.

## B. Selecting a Project Methodology

### A. FDIC Insured Bank

**Selection:** WATERFALL

**Scenario:** *A FDIC insured bank where written documentation is very important for compliance audits. Applications and systems are very mature, usually only minor very predictable changes made using legacy languages and technologies.*

I would choose Waterfall for the bank because its systems are mature and the changes are minor and predictable. That makes it easier to define the requirements upfront and move through planning, design, implementation, testing, and deployment in a controlled sequence. The team is maintaining established systems rather than trying to discover an entirely new product.

The need for written documentation also makes Waterfall a good fit. Requirements, approvals, test results, and change records can be documented at each stage for compliance audits. The legacy languages and technologies support a careful approach where the team reviews dependencies before making changes. This choice follows the conditions in the scenario; the bank's industry alone would not determine the methodology.

### B. Software Company

**Selection:** AGILE + XP

**Scenario:** *A software company that creates applications using Java and C#. Applications are somewhat mature and creating program libraries that can be reused for multiple applications is extremely important to reduce cost and the time required to bring new versions of their applications to market.*

I would choose Agile with Extreme Programming practices for the software company. Its applications are somewhat mature, but the company still needs to release new versions quickly and build reusable program libraries. Short development iterations would let the team improve those libraries, use them in applications, and get feedback without waiting for a large release.

Extreme Programming supports this approach through automated testing, refactoring, pair programming, and frequent integration. Those practices would help developers keep shared Java and C# libraries reliable as they change. Reuse needs clear interfaces and documentation as well, so other teams can use the libraries correctly. The company's emphasis on reuse and faster delivery supports this choice more than the programming languages themselves.

### C. Medical AI Startup

**Selection:** HYBRID

**Scenario:** *A software startup that is trying to produce an AI software application to help doctors diagnose patients. The startup is working closely with teams of doctors in emergency rooms at several local hospitals to develop the product.*

I would choose a hybrid approach for the startup. The product is still being developed, and the doctors' feedback will likely change what the team builds. Agile iterations would let developers test prototypes with the doctors, refine requirements, and address problems as they learn more about emergency room workflows.

I would combine that flexibility with planned reviews and formal validation before clinical deployment. Because the application is intended to help doctors diagnose patients, the team needs documented requirements, careful testing, data protection controls, and clear approval criteria. Software that supports diagnosis may also be regulated by the FDA as a medical device, and any patient data from the hospitals brings HIPAA into the project, so those checkpoints need records an auditor could follow. Frequent feedback can guide development, while controlled review points help determine whether the product is ready to move forward. A prototype that gets positive feedback would still need validation before being used for patient care.

## Outcome

I defined twelve key deliverables for the Gatorware Software systems upgrade and grouped them into five areas, each with clear acceptance conditions. I then selected a project methodology for three business scenarios. I chose Waterfall for the bank, Agile with XP for the software company, and a hybrid approach for the medical AI startup, based on each scenario's requirements and compliance needs.
