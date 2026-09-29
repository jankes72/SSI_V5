# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** `2026-09-30`  
**Development model:** independent solo R&D. SSI V5 is designed and integrated by one author outside regular working hours. AI coding/reasoning tools support implementation, analysis and review; they do not represent a development team. External collaborators are introduced for domain expertise, challenge design and independent validation.  
**Author context:** [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)  
**Repository role:** `PUBLIC EVIDENCE / REVIEW MIRROR + PUBLISHED RESEARCH PORTAL`  
**Proprietary implementation:** private by design.

## Current training snapshot — 2026-09-30

The operator reports that core SSI training continues alongside CZARA. The public S20 log is a partial capture of `RUN_20260929T212837Z_92e516e1`, not a final stage report.

| Track | Latest published state | Evidence scope |
|---|---|---|
| Core S20-S40 | S20 started; core training reported ongoing | S20 excerpt: 116 unique completed cases, 79 PASS, 37 INCONCLUSIVE, 0 FAIL; full-stage completion not established |
| S19 recovery / pre-S20 hardening | Startup banner reports hardening PASS and S19 COMMITTED | Operator-supplied log; transaction journal and detailed gate reports are not included in this excerpt |
| CZARA Live Training | Running alongside core training | Internal integration snapshot; 160-item curriculum = 120 training + 24 frozen validation + 16 frozen Champion benchmark; final completion not published |
| Dynamic Mission V6 | Installed; scheduler active; waiting for CZARA completion | 0/72 live missions at the recorded snapshot; 48 training + 12 frozen validation + 12 frozen blind Champion |
| WEB01-WEB24 | Installed / READY; gated after S40 | Requires S40 execution completion and COMMITTED consolidation; live completion not published |
| Mexico external benchmark | Planned | Internal simulations do not establish Mexico-side execution or independent validation |

The S20 excerpt covers BODY_FROZEN, ISKRA1, ISKRA2 and part of ISKRA3. It declares seven actors and 210 assignments, but does not include results for the entire stage. All captured verdicts remain visible, including the 37 INCONCLUSIVE rows. The excerpt contains no FAIL rows; the final stage outcome is not established.

V6 adds complete evolving experiments with a simulated professor and four experts, DIRECTOR-managed MAIN/SHADOW branches and explicit formal promotion. Installer self-tests are recorded separately from live mission results. The planned 48-stage Mexico robotics curriculum, the 160-item CZARA curriculum and the 72-mission V6 curriculum are distinct programmes.

Current sources:

- [Latest public status and source map](LATEST_PUBLIC_STATUS_20260930.md)
- [Machine-readable current snapshot](RESULTS/SSI_V5_CURRENT_PUBLIC_STATUS_20260930.json)
- [Supplied S20 runtime log](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)
- [Parallel core/CZARA integration simulation](MEXICO_PARALLEL_INTEGRATION_SIMULATION_20260929.md)
- [V6 installation, self-tests and post-CZARA gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)

The earlier S19 incident and pre-S20 preregistration remain historical evidence. S20 startup is now recorded; the excerpt does not independently audit all prerequisite gates or the S19 commit.

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
+ CZARA (research context / translation)
+ DYNAMIC MISSION V6 (installed / post-CZARA gate)
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

1. [Latest public status](LATEST_PUBLIC_STATUS_20260930.md)
2. [S20 runtime source excerpt](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)
3. [V6 installation and post-CZARA gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)
4. [Parallel core/CZARA integration simulation](MEXICO_PARALLEL_INTEGRATION_SIMULATION_20260929.md)
5. [Current grant-reviewer summary](GRANT_REVIEWER_CURRENT_STATUS_20260930.md)
6. [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
7. [Mexico team interface and CZARA controls](MEXICO_TEAM_INTERFACE_AND_CZARA_CONTROLS_20260928.md)
8. [External review attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
9. [S13-S18 routing and recovery results](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
10. [Preserved Dual Mother results](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
11. [Author context](AUTHOR_CONTEXT.md)
12. [Collaboration and IP boundary](COLLABORATION_AND_PARTNER_ENTRY.md)

Older dated records retain their original results and scope. Current pointers summarize the latest published sources; they do not monitor the private runtime.


Older dated files remain preserved as historical evidence. Use the current-state documents above for the latest implementation and continuation status; measured domain results retain their original dates and scope.

