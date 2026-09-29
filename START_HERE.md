# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Architecture author:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Development model:** independent solo R&D; designed and integrated by one author outside regular working hours. AI coding/reasoning tools support implementation, analysis and review; they do not constitute a development team. External collaborators are introduced for domain expertise, challenge design and independent validation.  
**Author context:** [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)  
**Updated:** `2026-09-30`  
**Repository role:** public research/evidence mirror with a published observer portal; proprietary implementation remains private.

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
+ CZARA (research context / translation)
+ DYNAMIC MISSION V6 (installed / post-CZARA gate)
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

