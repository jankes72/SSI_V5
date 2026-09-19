# SSI V5 — Research Front Door

**Experimental persistent-competence architecture for adaptive multi-agent AI systems**  
**Current public status:** `2026-09-18`  
**Repository role:** evidence-indexed public R&D mirror with a published research portal; proprietary implementation remains private.

SSI V5 investigates whether a long-running adaptive system can build, validate, preserve, reuse, compare, revise and consolidate competence across tasks using persistent state, experience, Micronetworks, Candidate -> Challenger -> Champion lifecycle, Router V10, Router S10, LEGO composition, Hermes memory and CONTINUUM persistence.

This repository publishes **evidence, protocols, status, failures, repairs, retests, timings, hashes, provenance and claim boundaries**. It does not distribute the proprietary SSI/V10/S10/Micronetwork/ISKRA/DIRECTOR/ROBERT implementation.

## Current state — 2026-09-18

```text
V4 S1-S10 BASELINE
= COMPLETE / PASS under one run ID
= 7 BODY final state: 7/7 PASS
= CONSOLIDATION / PROMOTION / BRIDGE: PASS
= REGRESSION: PASS
= BODY_FROZEN promoted reload: 144/144 expected entries

POST-S10 SOFTWARE DOMAINS
= DRONE: 6/6 scenarios PASS
= HUMANOID: 15/15 scenarios PASS
= TOTAL: 21 scenarios

SSI DUAL MOTHER CROSS LAB V1
= DRONE MOTHER: 12/12 paired scenario families PASS
= RESCUE ROBOT MOTHER: 12/12 paired scenario families PASS
= 60 deterministic repeats per scenario family
= 720 paired missions
= 1,440 domain result rows

CROSS CONSULTATION
= 6 scenario families
= 360 paired missions
= 720 measured consultation rounds
= mean 2.4896 ms across scenario means

CROSS CONSOLIDATION
= 6 scenario families
= 360 measured merge executions
= mean 0.0369 ms across scenario means

ROLLBACK
= 6 scenario families
= 360 measured executions
= mean 0.1170 ms across scenario means

MEAN TOTAL SOFTWARE FLOW
= 5.2559 ms across 12 scenario means

PUBLIC RESEARCH PORTAL = PUBLISHED
PUBLIC REVIEWER INTERFACE = observer-only
PHYSICAL VALIDATION = not claimed
INDEPENDENT EXTERNAL REPLICATION = not claimed
```

These timings are execution timings of the software laboratory. They are **not** physical drone or robot response times.

## Latest public evidence

- [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
- [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
- [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
- [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
- [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
- [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
- [`docs/index.html`](docs/index.html) — source of the published public research portal.

## Latest cross-domain milestone — Dual Mother

Two independent domain-side controllers were exercised together:

- **DRONE MOTHER** — micro-drone reconnaissance collective.
- **RESCUE ROBOT MOTHER** — specialist non-humanoid rescue robots.

The measured software-lab split is intentional:

```text
M01-M06
detect -> micronetwork sync -> assess -> decision -> action -> validate -> cross consolidation

M07-M12
checkpoint -> action -> dynamic evidence -> plan invalidation -> rollback
-> second cross consultation -> conservative replan -> validation
```

Only validated knowledge is eligible for the recorded cross-domain merge step. Dynamic failure is not counted as success: the current plan is invalidated, state returns through rollback, the domains consult again and a new plan must pass validation.

Rescue Robot Mother uses specialist non-humanoid classes in this laboratory:

```text
MOLE_DRILLER
TRACKED_CRAWLER
SNAKE_SCOUT
QUADRUPED
AMPHIBIOUS_CRAWLER
HEAT_SHIELDED_CRAWLER
```

## SSI is a complete persistent ecosystem

SSI is not only an S1-S10 training pipeline. The training curriculum is one controlled process inside a broader persistent software ecosystem:

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

DIRECTOR is the organizational/management layer. BODY_FROZEN is the stable/reference and controlled consolidation target. ISKRA1-6 preserve independent developmental histories. Hermes retains competence identity, provenance and experience. CONTINUUM preserves missions, checkpoints and operational continuity. V10 routes competence within task execution; S10 compares competence across BODY histories and controls promotion/consolidation.

## Verified V4 system baseline — 2026-09-17

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
artifact_count = 4
complete_accounting = true
fresh_process = true
```

That baseline remains the preserved system-level evidence under its original run ID. The 2026-09-18 Dual Mother laboratory is the newer cross-domain milestone built on the public evidence line.

## Four preserved engineering configurations

```text
V1 = lean control/reference
V2 = optimized control/observability and reuse
V3 = intermediate MetaNetwork line
V4 = State-Space / uncertainty / adaptive-routing line
```

The numbering is historical lineage, not a ranking. See [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md).

## Research questions

Current collaboration-relevant questions include:

- persistent competence across long-running agent histories;
- continual / lifelong learning without silent state loss;
- functional identity of competence across independent agents;
- false merge / false split in cross-agent consolidation;
- evidence-backed Champion / Challenger / Specialist / Hold decisions;
- selective re-evaluation after local change;
- failure-aware routing, rollback and recovery;
- cross-domain consultation and transfer;
- whether consolidation improves later performance without increasing false reuse;
- externally supplied unseen challenge cases;
- specialist rescue-robot and drone/swarm validation in software and later physical systems;
- later physical validation in humanoid motion/stability.

## Collaboration

SSI V5 is open to controlled collaboration with researchers, laboratories, universities, startups, companies and grant consortia.

Preferred model:

```text
EXTERNAL PARTNER DEFINES PROBLEM
-> ACCEPTANCE CRITERIA FROZEN BEFORE RUN
-> SSI RUN
-> PASS / FAIL / INCONCLUSIVE PRESERVED
-> FAILURES / TIMINGS / EVIDENCE RECORDED
-> OPTIONAL CONSOLIDATION
-> TARGET-SPECIFIC RE-VALIDATION
-> RESULT RETURNED TO PARTNER
```

Possible roles include research collaborator, consortium partner, challenge designer, independent validation/replication partner, continual-learning or multi-agent methods reviewer, drone/swarm lab, specialist rescue-robot lab, humanoid/robotics lab and later physical-validation partner.

See [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md).

## Reviewer access

```text
LOCAL ROOT
= execution authority
= mission/control actions
= runtime changes
= promotion / recovery operations

PUBLIC RESEARCH PORTAL / REVIEWER INTERFACE
= published sanitized observation surface
= evidence/status inspection
= no arbitrary ROOT execution
= no hidden configuration writes
```

Principle:

```text
OBSERVE != CONTROL
```

## Evidence volume

The local sanitization pass over the completed V4 run identified:

```text
TRAINING_JSON_COUNT = 229
EXPERIMENT_FILES = 373
PASS-status training JSONs = 76
FAIL-status training JSONs = 0
OTHER training JSONs = 153
```

`OTHER` is a structural category for metadata/state/report records without a top-level PASS/FAIL field; it is not a failure count.

## Public/private boundary

```text
PUBLIC
= architecture descriptions
+ protocols
+ test results
+ run identifiers
+ evidence counts
+ timings
+ hashes / provenance where safe
+ PASS / FAIL / rollback records
+ claim boundaries
+ comparative version descriptions
+ published research portal

PRIVATE
= proprietary source code
+ Router V10 implementation internals
+ Router S10 implementation internals
+ reconstructive Micronetwork details
+ private Hermes memory
+ ROOT execution internals
+ prompts / private configuration
+ credentials / endpoints
+ complete private state / descendant trees
```

## Claim boundary

The current evidence supports describing SSI as a persistent multi-agent software ecosystem with organizational control, seven BODY development lines, memory, mission continuity, competence routing, cross-line consolidation, software-domain execution, cross-domain consultation/rollback/consolidation and evidence preservation.

It does **not** establish:

- physical drone validation;
- physical rescue-robot validation;
- physical humanoid validation;
- safety certification;
- live autonomous financial-account execution;
- independent external replication;
- universal superiority over other architectures;
- production readiness;
- AGI or consciousness.

## Recommended reading order

1. [`START_HERE.md`](START_HERE.md)
2. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
3. [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
4. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
5. [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
6. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
7. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
8. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
9. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md)
10. [`COLLABORATION_AND_PARTNER_ENTRY.md`](COLLABORATION_AND_PARTNER_ENTRY.md)

Older dated files remain historical records. When an older status conflicts with the newer evidence-backed state, use the newest dated current-state document without rewriting the historical record.