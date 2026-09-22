# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** `2026-09-22`  
**Repository role:** `PUBLIC EVIDENCE / REVIEW MIRROR + PUBLISHED RESEARCH PORTAL`  
**Proprietary implementation:** private by design.

## Preserved software evidence in one view

```text
V4 S1-S10 BASELINE = COMPLETE / PASS under one run ID
7 BODY final state = 7/7 PASS
CONSOLIDATION / PROMOTION / BRIDGE = PASS
REGRESSION = PASS
BODY_FROZEN final promoted reload = 144/144 expected entries

POST-S10 DRONE SOFTWARE LAB = 6/6 scenarios PASS
POST-S10 HUMANOID SOFTWARE LAB = 15/15 scenarios PASS
POST-S10 TOTAL = 21 scenarios

SSI DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
60 deterministic repeats per scenario family
720 paired missions / 1,440 domain result rows

CROSS CONSULTATION = 6 scenario families / 360 missions / 720 measured rounds
CROSS CONSOLIDATION = 6 scenario families / 360 measured merges
ROLLBACK = 6 scenario families / 360 measured executions

mean cross consultation = 2.4896 ms
mean rollback = 0.1170 ms
mean cross consolidation = 0.0369 ms
mean total software flow = 5.2559 ms

PUBLIC RESEARCH PORTAL = PUBLISHED
PUBLIC REVIEWER ACCESS = observer-only
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

All timings above are execution timings of the software laboratory and must not be interpreted as physical drone or robot response times.

## SSI V5 implementation update — 2026-09-22

```text
SSI V5 Final = IMPLEMENTED / CONTINUATION RUN OBSERVED
BODY_FROZEN + ISKRA1..ISKRA6 = 7/7 runtime/profile readiness reported
DIRECTOR = INDEPENDENT CORE
POCKET readiness = 1 qualified package checked for 7 actors

BODY_FROZEN S11 continuation
inherited prefix = 27 cases verified by the local continuation checker
S11-05-04 = native PASS / CI PASS / CASE_DONE PASS
S11-05-05 = native PASS / CI PASS / CASE_DONE PASS
S11-05-06 = native PASS / CI PASS / CASE_DONE PASS
pending at the last shown CASE_DONE = 0

S11 stage summary = NOT INCLUDED IN THE SUPPLIED EXCERPT
S11 completion for all 7 BODY = NOT ESTABLISHED BY THIS EXCERPT
S12-S40 completion = NOT CLAIMED
PRIVATE LAB FIX = 165/165 offline tests across 14 suites
```

The newly published [component overview](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md) explains LEGO Pocket,
Pocket Micro, META-LEGO and the permanent laboratories available to the independent
DIRECTOR. The [current report](RESULTS/SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md) distinguishes native/CI case results,
operator-supplied evidence and offline software tests.

A private experiment panel supports frozen protocols, retained results and expert
review/stop controls. Public access remains observational. The
[Football World](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md) is implemented and previously operator-observed;
complete data ingress, identity and outcome validation still require evidence.

## Why this project is now collaboration-ready

The preserved 2026-09-17 V4 run established a complete controlled software cycle with seven BODY development lines, S1-S10 progression, consolidation/promotion/bridge gates, regression verification, rollback accounting, promoted-state reload verification and post-training domain execution.

The 2026-09-18 Dual Mother milestone adds a separate cross-domain evidence layer:

- two independent domain-side controllers;
- paired scenario execution with deterministic repetition;
- validation-gated cross consolidation;
- dynamic plan invalidation;
- checkpoint rollback;
- second cross-domain consultation;
- conservative replanning followed by validation;
- recorded timings and explicit claim boundaries.

This makes externally defined falsification, replication and cross-domain challenge design more concrete than a roadmap-only collaboration.

## Dual Mother scenario split

### M01-M06 — validation followed by cross consolidation

```text
detect
-> micronetwork sync
-> assess
-> decision
-> action
-> validate
-> cross consolidation
```

### M07-M12 — dynamic failure, rollback and second consultation

```text
checkpoint
-> action
-> dynamic evidence
-> plan invalidation
-> rollback
-> second cross consultation
-> conservative replan
-> validation
```

Rescue Robot Mother is non-humanoid in this laboratory. Measured specialist classes include `MOLE_DRILLER`, `TRACKED_CRAWLER`, `SNAKE_SCOUT`, `QUADRUPED`, `AMPHIBIOUS_CRAWLER` and `HEAT_SHIELDED_CRAWLER`.

## Research areas relevant to partners

```text
AGENTIC AI
MULTI-AGENT SYSTEMS
CONTINUAL / LIFELONG LEARNING
PERSISTENT COMPETENCE AND MEMORY
ADAPTIVE ROUTING
CROSS-AGENT COMPETENCE CONSOLIDATION
FAILURE-AWARE RECOVERY / ROLLBACK
CROSS-DOMAIN CONSULTATION
AUTONOMOUS SYSTEMS
DRONES / MULTI-ROBOT SYSTEMS
SPECIALIST RESCUE ROBOTICS
HUMANOID MOTION / STABILITY
AUDITABLE / EVIDENCE-ORIENTED AGENT WORKFLOWS
CROSS-DOMAIN TRANSFER
```

## External collaboration model

Preferred model:

```text
EXTERNAL PARTNER DEFINES A PREVIOUSLY UNSEEN PROBLEM
-> ACCEPTANCE CRITERIA FROZEN BEFORE RUN
-> SSI EXECUTION
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> EVIDENCE / TIMINGS / FAILURES RETAINED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
-> RESULT RETURNED TO PARTNER
```

Possible partner roles include:

- research collaborator;
- consortium partner / beneficiary where programme rules permit;
- external challenge designer;
- independent replication / validation partner;
- continual-learning or multi-agent methods reviewer;
- drone/swarm research laboratory;
- specialist rescue-robotics laboratory;
- humanoid/robotics research laboratory;
- later physical validation partner.

## Current architecture summary

SSI is a persistent multi-agent software ecosystem containing:

```text
DIRECTOR
+ BODY_FROZEN
+ ISKRA1..ISKRA6
+ HERMES
+ CONTINUUM
+ ROUTER V10
+ ROUTER S10
+ MICRONETWORKS / LEGO / POCKET
+ WORLD / DOMAIN LAYERS
+ EVIDENCE / CHECKPOINT / PROVENANCE
```

S1-S10 is one controlled training/evaluation process inside this ecosystem, not the entire system.

## Preserved V4 system milestone

```text
RUN_ID = RUN_20260917T024400_DCD7FD
TRACE_ROOT = TRACE_5EE50008986B
FINAL_STAGE = S10
COMPLETE = true

BODY_FROZEN = PASS
ISKRA1 = PASS
ISKRA2 = PASS
ISKRA3 = PASS
ISKRA4 = PASS
ISKRA5 = PASS
ISKRA6 = PASS
CONSOLIDATION = PASS
REGRESSION = PASS
ROLLBACK = NOT_REQUIRED
ADVANCE_ALLOWED = true

expected_count = 144
loaded_count = 144
complete_accounting = true
fresh_process = true
```

## Published public research portal

The public portal is published as a sanitized research front door. The repository source is [`docs/index.html`](docs/index.html). It exposes recorded evidence and claim boundaries, not ROOT execution or private implementation.

## Reviewer access boundary

```text
PUBLIC PORTAL / REVIEWER
= sanitized status / evidence / allowed questions
!= ROOT
!= arbitrary mission execution
!= runtime configuration write access
```

## What reviewers should not infer

Do not infer:

- physical drone validation;
- physical rescue-robot validation;
- physical humanoid validation;
- safety certification;
- live autonomous financial-account execution;
- independent external replication;
- universal superiority of SSI, V10, S10 or any V1-V4 configuration;
- production readiness;
- AGI or consciousness.

## Recommended reading order

1. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
2. [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
3. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
4. [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
5. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
6. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
7. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
8. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)
9. [`EXTERNAL_CHALLENGE_ENTRY_20260914.md`](EXTERNAL_CHALLENGE_ENTRY_20260914.md)

Older dated files remain preserved as historical evidence. Use the current-state documents above for the latest implementation and continuation status; measured domain results retain their original dates and scope.
