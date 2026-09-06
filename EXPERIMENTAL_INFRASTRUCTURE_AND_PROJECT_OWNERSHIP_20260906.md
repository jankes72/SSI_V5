# SSI V5 — Experimental Infrastructure & Project Ownership

**Recorded:** `2026-09-06`  
**Project status:** `INDEPENDENT / SOLO-DEVELOPED / AUTHOR-OWNED COMPUTE / AFTER-HOURS DEVELOPMENT`  
**Purpose:** document the actual compute context and scaling plan without implying institutional, team or grant-funded infrastructure.

## 1. Current ownership and team boundary

SSI V5 is currently developed as a **one-person independent project** by Paweł Jankiewicz (`jankes72`).

The project is developed outside the author's regular employment, primarily in personal time / after working hours.

The compute resources described in this document are the author's own equipment, or equipment currently being personally acquired by the author. They are not presented as university, school, company, laboratory or grant-funded infrastructure.

As of this record:

```text
CURRENT SSI V5 DEVELOPMENT TEAM = 1 person
DEVELOPMENT MODE = independent / after-hours
CURRENT INSTITUTIONAL COMPUTE SPONSOR = none claimed
CURRENT GRANT-FUNDED COMPUTE = none claimed
LISTED COMPUTERS = private author-owned / personally acquired equipment
```

This statement is about the present SSI V5 project and the infrastructure described here. Future collaborators, sponsors or funded compute should be recorded separately if they actually join the project.

## 2. Actual early compute context — primarily one laptop

The current project was not developed from the beginning on a three-node lab or research cluster.

Up to the current stage, practical SSI development and experimentation has been carried out primarily on a **single personal laptop**, under constrained resources and limited after-hours development time.

A further personal computer only entered the author's available setup approximately **three weeks before this record**, so later/current hardware availability must not be retroactively attributed to earlier project stages.

Preserved constrained experimental node:

```text
LENOVO LAPTOP
SYSTEM RAM = 8 GB
GPU VRAM = 4 GB
OWNERSHIP = private / author-owned
ROLE = constrained experimental laboratory / agent-world node
```

The Lenovo environment remains useful as a historical and experimental comparison point. Moving later work to stronger hardware must not retroactively change the hardware context of earlier evidence.

## 3. Current transition toward three role-separated personal nodes

The author is now expanding the private environment into a three-node setup. This is a **recent personal infrastructure expansion**, not the infrastructure on which the entire project history was originally produced.

### Node A — Agent / World Laboratory

```text
PLATFORM = Lenovo laptop
RAM = 8 GB
VRAM = 4 GB
ROLE = Football World / agents / Teachers / laboratory / controlled experiments
STATUS = preserved personal experimental node
```

The intent is to keep the agent/world environment resource-constrained and comparable rather than silently moving every experiment to stronger hardware.

### Node B — ROBERT execution body

```text
PLATFORM = desktop
CPU CLASS = Intel i5
RAM = 16 GB
VRAM = 4 GB
ROLE = ROBERT / Eyes / Hands / execution / tools
OWNERSHIP = private / personally acquired by author
STATUS = recent / near-term infrastructure expansion
```

### Node C — DIRECTOR

```text
PLATFORM = desktop
CPU CLASS = Intel i7
RAM = 16 GB
VRAM = 6 GB
ROLE = DIRECTOR / coordination / memory / evidence / routing / comparison
OWNERSHIP = private / personally acquired by author
STATUS = recent / near-term infrastructure expansion
```

The Director is intended to use the strongest of the three personal nodes because it is expected to accumulate the broadest cross-world state, evidence and coordination workload.

## 4. Why the roles are separated

The intended topology is:

```text
                 DIRECTOR
                    |
          +---------+---------+
          |                   |
          v                   v
 AGENT / WORLD LAB         ROBERT
   constrained node       execution node
```

This is not presented as one combined GPU or one shared-memory supercomputer. The nodes remain separate machines with separate local resources. Any distributed coordination must be measured as distributed execution rather than by adding VRAM/RAM figures together.

## 5. Experimental reporting rule

Hardware changes can materially affect latency, throughput and model capacity. Therefore future public experiment records should, where relevant, identify the execution platform or hardware class used for a run.

The intended comparison rule is:

```text
SYSTEM VERSION
+ EXPERIMENT VERSION
+ EXECUTION PLATFORM
+ MODEL / PROVIDER CLASS WHERE RELEVANT
+ RESULT / TIMING / EVIDENCE
```

This helps distinguish improvement caused by SSI architecture or learned competence from improvement caused only by stronger hardware.

## 6. Future funded scaling

If SSI V5 later receives sponsorship, grant funding or institutional collaboration, stronger compute may be introduced as a **new infrastructure generation**. That future state must not be described as if it existed during the earlier single-laptop / Lenovo-era experiments.

Possible future scaling may include substantially larger RAM/VRAM resources and greater parallelism, but no specific future hardware performance claim is made by this document.

The preserved research logic is:

```text
PRIMARY SINGLE-LAPTOP / AFTER-HOURS DEVELOPMENT
-> RECENT PERSONAL HARDWARE EXPANSION
-> ROLE-SEPARATED PERSONAL THREE-NODE LAB
-> FUTURE FUNDED INFRASTRUCTURE, IF OBTAINED
```

## 7. Claim boundary

This document supports only the following infrastructure statements:

- SSI V5 is currently a solo-developed independent project;
- development is performed primarily outside the author's regular employment, in personal time;
- the project was developed primarily on one personal laptop through much of its current history;
- additional personal compute entered the setup only recently, with one additional computer becoming available approximately three weeks before this record;
- the listed compute is private author-owned or personally acquired equipment;
- the project is not presented as currently backed by school, university, company or grant-funded compute;
- the Lenovo environment is preserved as a constrained historical/experimental node;
- the current direction is a three-node separation for Agent/World, ROBERT and DIRECTOR roles;
- future stronger compute is a scaling plan, not a current capability claim.

This document does **not** claim that modest hardware proves the scientific validity of SSI. Scientific claims must come from experiment design, evidence and independent evaluation rather than from the cost or size of the machines used.