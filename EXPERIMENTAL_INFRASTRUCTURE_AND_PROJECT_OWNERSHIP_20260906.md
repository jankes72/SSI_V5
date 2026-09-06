# SSI V5 — Experimental Infrastructure & Project Ownership

**Recorded:** `2026-09-06`  
**Project status:** `INDEPENDENT / SOLO-DEVELOPED / AUTHOR-OWNED COMPUTE`  
**Purpose:** document the current compute context and scaling plan without implying institutional or grant-funded infrastructure.

## 1. Current ownership and team boundary

SSI V5 is currently developed as a **one-person independent project** by Paweł Jankiewicz (`jankes72`).

The compute resources described in this document are the author's own equipment, or equipment currently being personally acquired by the author. They are not presented as university, school, company, laboratory or grant-funded infrastructure.

As of this record:

```text
CURRENT SSI V5 DEVELOPMENT TEAM = 1 person
CURRENT INSTITUTIONAL COMPUTE SPONSOR = none claimed
CURRENT GRANT-FUNDED COMPUTE = none claimed
LISTED COMPUTERS = private author-owned / personally acquired equipment
```

This statement is about the present SSI V5 project and the infrastructure described here. Future collaborators, sponsors or funded compute should be recorded separately if they actually join the project.

## 2. Constrained original experimental environment

The project has been developed and tested on modest personal hardware rather than on a research cluster.

Current preserved experimental node:

```text
LENOVO LAPTOP
SYSTEM RAM = 8 GB
GPU VRAM = 4 GB
OWNERSHIP = private / author-owned
ROLE = constrained experimental laboratory / agent-world node
```

The Lenovo environment is intentionally useful as a historical and experimental comparison point. Moving later work to stronger hardware must not retroactively change the hardware context of earlier evidence.

## 3. Near-term three-node role separation

The author is expanding the private lab with two additional personally acquired desktop computers.

### Node A — Agent / World Laboratory

```text
PLATFORM = Lenovo laptop
RAM = 8 GB
VRAM = 4 GB
ROLE = Football World / agents / Teachers / laboratory / controlled experiments
STATUS = existing personal experimental node
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
STATUS = near-term infrastructure expansion
```

### Node C — DIRECTOR

```text
PLATFORM = desktop
CPU CLASS = Intel i7
RAM = 16 GB
VRAM = 6 GB
ROLE = DIRECTOR / coordination / memory / evidence / routing / comparison
OWNERSHIP = private / personally acquired by author
STATUS = near-term infrastructure expansion
```

The Director is assigned the strongest of the three current/planned personal nodes because it is expected to accumulate the broadest cross-world state, evidence and coordination workload.

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

If SSI V5 later receives sponsorship, grant funding or institutional collaboration, stronger compute may be introduced as a **new infrastructure generation**. That future state must not be described as if it existed during the earlier Lenovo-era experiments.

Possible future scaling may include substantially larger RAM/VRAM resources and greater parallelism, but no specific future hardware performance claim is made by this document.

The preserved research logic is:

```text
CONSTRAINED PERSONAL LAB
-> ROLE-SEPARATED PERSONAL THREE-NODE LAB
-> FUTURE FUNDED INFRASTRUCTURE, IF OBTAINED
```

## 7. Claim boundary

This document supports only the following infrastructure statements:

- SSI V5 is currently a solo-developed independent project;
- the listed compute is private author-owned or personally acquired equipment;
- the project is not presented as currently backed by school, university, company or grant-funded compute;
- the Lenovo environment is a constrained historical/experimental node;
- two additional private desktops are being added for separate ROBERT and DIRECTOR roles;
- future stronger compute is a scaling plan, not a current capability claim.

This document does **not** claim that modest hardware proves the scientific validity of SSI. Scientific claims must come from experiment design, evidence and independent evaluation rather than from the cost or size of the machines used.