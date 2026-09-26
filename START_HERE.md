# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Architecture author:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Development model:** independent solo R&D; designed and integrated by one author outside regular working hours. AI coding/reasoning tools support implementation, analysis and review; they do not constitute a development team. External collaborators are introduced for domain expertise, challenge design and independent validation.  
**Author context:** [AUTHOR_CONTEXT.md](AUTHOR_CONTEXT.md)  
**Updated:** `2026-09-26`  
**Repository role:** public research/evidence mirror with a published observer portal; proprietary implementation remains private.

## Current training front — S12 consolidated, S13 next — 2026-09-26

The current evidenced core-training progression is:

| Stage | Executed | Verified PASS | Unresolved | FAIL | Consolidation |
|---|---:|---:|---:|---:|---|
| S11 | 210/210 | 196 | 14 | 1 | COMMITTED |
| S12 | 210/210 | 203 | 7 | 0 | COMMITTED |
| S13 | not run | — | — | — | NEXT |

Latest S11 run:

```text
RUN = RUN_20260925T163311Z_820718d5
execution_complete = true
PASS = 196
INCONCLUSIVE = 13
FAIL = 1
verified_subset = 196
CONSOLIDATION = CC_82dd0b3af825cd8543dcd59835023a5a
status = COMMITTED
```

Only the 196 verified PASS cases were admitted to the recorded S11 consolidation. The unresolved cases remained excluded rather than being relabeled.

Live S12 then traversed all 210 assignments:

```text
RUN = RUN_20260925T223720Z_6e1b1fc8
execution_complete = true
PASS = 203
INCONCLUSIVE = 7
FAIL = 0
verified_subset = 203
CONSOLIDATION = CC_db09484eefd9db783742336b69296eb5
status = COMMITTED
```

This provides live cross-run evidence of:

```text
S11 execution
-> verified-subset consolidation
-> S12 execution
-> verified-subset consolidation
-> S13 NEXT
```

Observed S11 -> S12 quality delta:

```text
verified:   196 -> 203
unresolved:  14 -> 7
FAIL:         1 -> 0
```

The operator additionally reports approximately 3x lower wall-clock time and approximately 3x lower model-token use for S12 relative to the comparable S11 work. These efficiency observations are not yet backed by a complete public provider usage ledger and are therefore published as an operator-observed signal, not an audited cost benchmark or causal proof of Champion routing.

Current evidence links:

- [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
- [S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [S11 -> S12 quality and efficiency signal](RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md)
- [Current machine-readable training progress](RESULTS/SSI_V5_CURRENT_TRAINING_PROGRESS_20260926.json)
- [S11 consolidation + WEB LEGO update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [DEV safeguards and adversarial tests](RESULTS/SSI_V5_DEV_SAFEGUARDS_20260923.md)

S12 is not presented as all-PASS: seven cases remain unresolved. S13-S40 completion, physical validation and independent external replication are not claimed.

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
+ MICRONETWORKS / LEGO / POCKET
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

1. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
2. [`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md)
3. [`RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md`](RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md)
4. [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
5. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
6. [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
7. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
8. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
9. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
10. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md)
11. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)

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

