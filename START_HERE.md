# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Architecture author:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Development model:** independent solo R&D; designed and integrated by one author outside regular working hours. AI coding/reasoning tools support implementation, analysis and review; they do not constitute a development team. External collaborators are introduced for domain expertise, challenge design and independent validation.  
**Author context:** [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)  
**Updated:** `2026-10-02`  
**Repository role:** public R&D, evidence and external-validation hub with a published observer portal; proprietary implementation remains private.

## Current programme map

The canonical current roadmap is [CURRENT_RESEARCH_ROADMAP_20261002.md](CURRENT_RESEARCH_ROADMAP_20261002.md). It connects core SSI reliability/training, CZARA, Dynamic Mission V6, WEB engineering, Mexico robotics/offline-resilience research and the external partner-defined benchmark strategy while keeping planned work separate from completed evidence.

## Latest SSI Final continuation — infrastructure stop — 2026-10-02

The next operator-provided log records **4 PASS / 3 INCONCLUSIVE / 0 FAIL** across seven closed cases, ending with `STOPPED_INFRASTRUCTURE` in `RUN_DOMAIN_20261002T181736Z_f600e74c`. The last case first reported a LAB output mismatch, then `NO_CANDIDATE_GENERATED` / `INVALID_WORKER_JSON`; the runner preserved INCONCLUSIVE and stopped. The terminal log does not establish the underlying root cause.

Together with the earlier seven-case batch, the two published transcripts contain **14 distinct actor/case outcomes: 9 PASS / 5 INCONCLUSIVE / 0 FAIL**. This is not a whole-stage or whole-queue result, and it does not alter the separate ZeroLab pilot or CZARA curriculum totals.

- [Latest stop, all seven cases and evidence](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md)

## ZeroLab V2 and first post-repair SSI batch — 2026-10-02

Operator-provided terminal evidence reports **9/9 ZeroLab services READY**, followed by an **8/8 PASS local-data pilot** (`training_pass=false`, `models_called=0`). A separate SSI Final recovery batch completed **7 cases: 5 PASS, 2 INCONCLUSIVE, 0 FAIL**. Both unresolved cases retain `LAB_OUTPUT_MISMATCH`; one passing case succeeded after a candidate revision.

The resumed Final batch is a selected S20-S26 recovery measurement after ZeroLab installation, not proof that those seven cases ran through ZeroLab. It does not establish full-stage acceptance or global per-case consolidation. The public export contains terminal evidence and reported receipt hashes; original pilot receipts and the signed Final run bundle have not been independently reverified for this publication.

- [CZARA current status: Director_Czary, BODY 1.0 and ZeroLab](CZARA_CURRENT_STATUS.md)
- [ZeroLab V2 results and provenance](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Architecture, roles and consolidation boundaries](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md)
- [Public evidence and machine-readable results](evidence/ZERO_LAB_V2_20261002/README.md)

## Preserved operator-stop snapshot — 2026-09-30

The following records the earlier stop. The 2026-10-02 result above documents the subsequent limited live restart; historical grades remain unchanged.

Core training progressed through completed S20-S25 stages and into S26. The operator then **manually stopped the run with Ctrl-C** because the number of `INCONCLUSIVE` outcomes and pending cases was increasing and no longer represented a trustworthy training signal.

Latest preserved diagnostic snapshot:

```text
TOTAL = 1,326
PASS = 848
INCONCLUSIVE = 470
FAIL = 8
S20-S25 verified-subset consolidations = PASS for BODY_FROZEN + DIRECTOR
S26 = interrupted / not claimed complete
```

A targeted diagnostic sample of **18 cases** showed that the apparent `unparseable_json` symptom was an **empty response after `INFLIGHT_LIMIT`**. This finding is limited to the inspected sample and is **not** generalized to every unresolved case.

The diagnosis also identified two additional reliability gaps: required task outputs were not always propagated correctly to the reviewer path, and dedicated R&D execution scenarios remain incomplete for parts of S20-S26.

A repair package (`SSI_LAB_REPAIR_20260930.zip`) was prepared and reported **17/17 offline tests PASS**. At that date, a successful live restart was not yet claimed; the separate 2026-10-02 batch above is the later retest. Historical verdicts remain preserved.

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)

**Preserved continuation requirement:** a new post-repair provenance boundary was required. The later recovery batch uses a separate plan/run and preserves earlier verdicts; it does not certify completion through S40.


## CZARA first internal training cycle complete — 2026-10-01

`CZARA-RND-1.0.0` completed its first internal training, frozen validation and frozen Champion benchmark cycle.

```text
UNIQUE STAGES = 160
FINAL CHECKPOINT = 160 / 160 PASS
FINAL QUALIFIED SKILLS = 520 / 520

TRAINING
  120 unique stages
  497 attempts
  120 PASS attempts
  377 intermediate INCONCLUSIVE attempts
  0 FAIL
  learning_applied = true

FROZEN VALIDATION
  24 / 24 PASS
  24 / 24 REUSE
  skill coverage = 1.0
  learning_applied = false

FROZEN CHAMPION BENCHMARK
  16 / 16 PASS
  16 / 16 REUSE
  skill coverage = 1.0
  learning_applied = false

AUTHORITY ERRORS = 0
```

The **377 INCONCLUSIVE records are preserved intermediate training/retry attempts**, not unresolved final curriculum stages. The final checkpoint records all 160 unique stages as PASS.

This is internal SSI evidence for the planned Poland-Mexico research workflow. It is **not** an independent Mexico benchmark, physical robotics validation, safety certification or external replication.

- [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
- [Machine-readable public summary](evidence/CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
- [Sanitized run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [Historical S120 checkpoint — preserved](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)
- [ZeroLab V2 — first runtime results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)

## Preserved earlier software results

```text
V4 S1-S10 BASELINE = COMPLETE / PASS under one run ID
7 BODY final state = 7/7 PASS
CONSOLIDATION / PROMOTION / BRIDGE = PASS
REGRESSION = PASS
BODY_FROZEN promoted reload = 144/144 expected entries

POST-S10 DRONE = 6/6 software scenarios PASS
POST-S10 HUMANOID = 15/15 software scenarios PASS
POST-S10 TOTAL = 21 software-domain scenarios

SSI DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
REPEATS PER SCENARIO FAMILY = 60
PAIRED MISSIONS = 720
DOMAIN RESULT ROWS = 1,440

CROSS CONSULTATION = 6 scenario families / 360 missions / 720 measured rounds
CROSS CONSOLIDATION = 6 scenario families / 360 measured merges
ROLLBACK = 6 scenario families / 360 measured executions

mean cross consultation = 2.4896 ms
mean rollback = 0.1170 ms
mean cross consolidation = 0.0369 ms
mean total software flow = 5.2559 ms

PUBLIC RESEARCH PORTAL = PUBLISHED
PUBLIC REVIEWER INTERFACE = observer-only
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

All timing values above are software-lab execution measurements, not physical drone or robot response times.

## What SSI is

SSI V5 is a persistent multi-agent software ecosystem built around:

```text
DIRECTOR
+ BODY_FROZEN
+ ISKRA1..ISKRA6
+ HERMES
+ CONTINUUM
+ ROUTER V10
+ ROUTER S10
+ MICRONETWORKS / BLOCKS / POCKET
+ WORLD / DOMAIN LAYERS
+ LOCAL ROOT CONTROL
+ PUBLIC OBSERVER INTERFACE
+ EVIDENCE / CHECKPOINT / PROVENANCE
```

S1-S10 is one controlled training/evaluation process inside that larger ecosystem.

## Preserved V4 baseline

```text
RUN_ID = RUN_20260917T024400_DCD7FD
TRACE_ROOT = TRACE_5EE50008986B
FINAL_STAGE = S10
COMPLETE = true
```

All seven BODY lines reached PASS in the final state. Consolidation, promotion, bridge and regression completed, rollback was not required, and the promoted BODY_FROZEN state reloaded with complete accounting of 144/144 expected competence entries.

After S10, the promoted state was executed in two software-domain harnesses:

```text
DRONE / SWARM = 6 scenarios PASS
HUMANOID MOTION / STABILITY = 15 scenarios PASS
TOTAL = 21 post-S10 software-domain scenarios
```

These remain the preserved 2026-09-17 baseline results.

## Preserved cross-domain milestone — 2026-09-18

SSI Dual Mother Cross Lab V1 exercises two independent domain sides:

- **Drone Mother** — micro-drone reconnaissance collective.
- **Rescue Robot Mother** — specialist non-humanoid rescue collective.

Stable scenarios M01-M06 require validation before cross consolidation:

```text
detect -> micronetwork sync -> assess -> decision -> action -> validate -> cross consolidation
```

Dynamic scenarios M07-M12 require failure-aware recovery:

```text
checkpoint -> action -> dynamic evidence -> invalidate current plan
-> rollback -> second cross consultation -> conservative replan -> validation
```

Rescue specialists represented in the measured scenarios: `MOLE_DRILLER`, `TRACKED_CRAWLER`, `SNAKE_SCOUT`, `QUADRUPED`, `AMPHIBIOUS_CRAWLER`, `HEAT_SHIELDED_CRAWLER`.

## Published public research portal

The public portal is published as a sanitized research front door. Its source is [`docs/index.html`](docs/index.html). It presents recorded evidence and claim boundaries and remains separate from LOCAL ROOT execution authority.

```text
OBSERVE != CONTROL
```

## Four preserved engineering configurations

```text
V1 = lean control/reference
V2 = optimized control/observability and reuse
V3 = intermediate MetaNetwork line
V4 = State-Space / uncertainty / adaptive-routing line
```

The numbering is historical lineage, not a ranking.

## Research / collaboration surface

SSI is ready for controlled external work around:

- agentic AI and multi-agent systems;
- continual / lifelong learning;
- persistent competence and memory;
- cross-agent competence comparison and consolidation;
- adaptive routing, rollback and recovery;
- cross-domain consultation and transfer;
- external falsification / unseen challenge design;
- drone/swarm autonomy in software and later physical validation;
- specialist rescue robotics in software and later physical validation;
- humanoid motion/stability in software and later physical validation;
- independent replication;
- grant and consortium collaboration.

Preferred collaboration model:

```text
EXTERNAL PARTNER DEFINES PROBLEM
-> ACCEPTANCE CRITERIA FROZEN BEFORE RUN
-> SSI RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE AND TIMINGS RECORDED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
-> RESULT RETURNED TO PARTNER
```

## Reviewer and control boundary

```text
LOCAL ROOT = execution authority
PUBLIC PORTAL / REVIEWER INTERFACE = sanitized observer-only access
OBSERVE != CONTROL
```

## Read these first

1. [Current research roadmap — 2026-10-02](CURRENT_RESEARCH_ROADMAP_20261002.md)
2. [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
3. [CZARA sanitized run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
4. [S20-S26 operator stop and LAB repair](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
5. [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
6. [REVIEWER_INDEX.md](REVIEWER_INDEX.md)
7. [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
8. [COLLABORATION_AND_PARTNER_ENTRY.md](COLLABORATION_AND_PARTNER_ENTRY.md)
9. [ZeroLab V2 — first results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
10. [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)
11. [Historical S19 observability incident](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
12. [Dual Mother Cross Lab V1](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
13. [Complete ecosystem architecture](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)

## Claim boundary

Current public evidence supports the narrow claim that SSI is a persistent, evidence-oriented multi-agent software ecosystem with seven BODY development lines, organizational control, persistent memory/state, competence routing, cross-line consolidation, regression/rollback discipline, software-domain execution and a measured Dual Mother cross-domain software laboratory.

It does **not** establish:

- physical drone performance;
- physical rescue-robot performance;
- physical humanoid performance;
- safety certification;
- live autonomous financial-account execution;
- independent external replication;
- universal superiority over other AI architectures;
- production readiness;
- AGI or consciousness.

## Publication boundary

```text
PUBLIC = evidence, protocols, results, lineage, counts, timings, QA, hashes, provenance, claim boundaries, published observer portal
PRIVATE = proprietary source code, ROOT internals, private state, reconstructive implementation details, credentials
```

Older dated files remain historical evidence and are not rewritten to imitate the newest state.



