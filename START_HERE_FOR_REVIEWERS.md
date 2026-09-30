# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** `2026-09-30`  
**Development model:** independent solo R&D. SSI V5 is designed and integrated by one author outside regular working hours. AI coding/reasoning tools support implementation, analysis and review; they do not represent a development team. External collaborators are introduced for domain expertise, challenge design and independent validation.  
**Author context:** [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)  
**Repository role:** `PUBLIC R&D / EVIDENCE / EXTERNAL-VALIDATION HUB + PUBLISHED RESEARCH PORTAL`  
**Proprietary implementation:** private by design.

## Current programme roadmap

Use [CURRENT_RESEARCH_ROADMAP_20260930.md](CURRENT_RESEARCH_ROADMAP_20260930.md) for the current programme-level sequence across core SSI training, CZARA, Dynamic Mission V6, WEB engineering, Mexico robotics/offline-resilience research and external partner-defined validation.

## Current training status — operator stop and LAB repair boundary — 2026-09-30

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

A repair package (`SSI_LAB_REPAIR_20260930.zip`) was prepared and reported **17/17 offline tests PASS**. The public hub does **not** yet claim that the live private runtime has been repaired/restarted successfully. Historical verdicts remain preserved.

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)

**Continuation boundary:** do not treat the old S20-S40 launcher as authorized for restart. The next continuation must preserve a new post-repair runtime/provenance boundary and support frozen-case replay.


## CZARA active internal training — 2026-09-30

`CZARA-RND-1.0.0` has reached its 120-case TRAINING checkpoint:

```text
22 PASS / 98 INCONCLUSIVE / 0 FAIL
120 / 120 training cases reached
24 validation cases = not yet claimed
16 Champion Benchmark cases = not yet claimed
```

The track exercises multilingual research-context handling, role/authority separation, benchmark freeze/revision control, evidence provenance and controlled professor-role -> CZARA -> DIRECTOR routing.

This is internal simulated training for the planned Mexico collaboration, not a completed live external benchmark.

- [CZARA S120 training checkpoint](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)
- [Machine-readable CZARA checkpoint](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.json)

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
+ MICRONETWORKS / BLOCKS / POCKET
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

1. [`RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md`](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
2. [`RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json`](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)
3. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
4. [`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md)
5. [`RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md`](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
6. [`SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md`](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
7. [`EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md`](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
8. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
9. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
10. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)

Older dated files remain preserved as historical evidence. Use the current-state documents above for the latest implementation and continuation status; measured domain results retain their original dates and scope.

