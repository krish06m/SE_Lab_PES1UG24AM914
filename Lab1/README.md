# SE Lab 1: Requirements Engineering and UML Use-Case Modelling

**Problem Statement #63: Community Solar Credit Allocation Manager**
Department of CSE, PES University

Name: Krish Mathur
SRN: PES1UG24AM914
Section: F

## Scenario

A clean energy sharing portal for a neighbourhood microgrid. It ingests rooftop solar
generation from smart meters, lets prosumers transfer surplus credits to neighbours,
and turns those credits into offsets on the monthly utility bill.

## Actors

| Actor | Type | Role in the system |
|---|---|---|
| Prosumer Resident | Human, primary | Transfers surplus credits, views their dashboard, raises disputes |
| Co-op Manager | Human, primary | Manages microgrid membership, resolves disputes |
| Smart Meter Gateway | External system | Pushes hourly generation readings into the portal |
| Utility Billing System | External system | Receives the monthly offset statements |

## Use cases

| ID | Use case | Notes |
|---|---|---|
| UC-01 | Record Solar Generation | includes UC-06 |
| UC-02 | Transfer Surplus Credits | includes UC-07 |
| UC-03 | View Credit Dashboard | |
| UC-04 | Generate Monthly Offset Statement | |
| UC-05 | Raise / Resolve Transfer Dispute | |
| UC-06 | Validate Meter Data Integrity | «include» target of UC-01 |
| UC-07 | Verify Available Credit Balance | «include» target of UC-02 |
| UC-08 | Flag Anomalous Meter Reading | «extend» on UC-01 |
| UC-09 | Apply Co-op Priority Allocation | «extend» on UC-02 |
| UC-10 | Manage Microgrid Membership | |

## Files

| File | Deliverable |
|---|---|
| `Requirements_Table.docx` / `.pdf` | 5 FRs and 2 NFRs with ID, type, description, priority, acceptance criteria, rationale |
| `UseCase_Diagram.pdf` | Use-case diagram with all four actors, system boundary, associations, two «include» and two «extend» relations |
| `UseCase_Flow.docx` / `.pdf` | One page flow for UC-02 Transfer Surplus Credits, with two alternate flows |

## Tool used

Diagram drawn to UML use-case notation: stick figure actors outside the boundary,
ovals for use cases, solid lines for associations, dashed arrows with the stereotype
label for the include and extend dependencies.
