# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-09-26`  
**Repository role:** public evidence mirror with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

- [Latest S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [S11 consolidation + WEB LEGO update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [Machine-readable latest summary](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
- [Complete previous S11 results: 197 PASS / 12 INCONCLUSIVE / 1 FAIL](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)
- [All 210 case outcomes and source hashes](evidence/S11_20260923/README.md)
- [DEV safeguards and adversarial tests](RESULTS/SSI_V5_DEV_SAFEGUARDS_20260923.md)
- [UAV and permanent R&D laboratory status](SYSTEM/SSI_V5_UAV_AND_RND_LABS_20260923.md)
- [R3 offline test summary](RESULTS/SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json)

The 22 September continuation report is preserved as a separate earlier run.

Earlier milestones and historical evidence:

1. [`RESULTS/SSI_V5_CONTROLLED_EVOLUTION_LIVE_S11_20260920.md`](RESULTS/SSI_V5_CONTROLLED_EVOLUTION_LIVE_S11_20260920.md)
2. [`RESULTS/SSI_V5_IMPLEMENTATION_STATUS_20260920.md`](RESULTS/SSI_V5_IMPLEMENTATION_STATUS_20260920.md)
3. [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
4. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
5. [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
6. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
7. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
8. [`RESULTS/V4_PUBLIC_SUMMARY_20260917.json`](RESULTS/V4_PUBLIC_SUMMARY_20260917.json)
9. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
10. [`docs/index.html`](docs/index.html) — source of the published public research portal.

## Current S11, consolidation and WEB LEGO update — 2026-09-26

Latest observed S11 training run:

```text
RUN = RUN_20260925T163311Z_820718d5
execution_complete = true
PASS = 196
INCONCLUSIVE = 13
FAIL = 1
retry_scope_count = 14
```

The revised learning-mode runner continued through all 210 cases rather than terminating the stage on FAIL/INCONCLUSIVE outcomes. S11 remains **INCONCLUSIVE** as an acceptance status; it is not relabeled PASS.

Only the 196 verified PASS cases were admitted to the subsequent consolidation. Transaction `CC_82dd0b3af825cd8543dcd59835023a5a` completed PASS for BODY_FROZEN and DIRECTOR with the declared identity split preserved: no BODY identity transfer, no Director import of the BODY core, and no weight retraining.

The private WEB LEGO extension is installed and reports:

```text
status = READY
lego_items = 126
templates = 15
stages = 24
cases = 192
actors = 7
data_policy = SYNTHETIC_ONLY
```

This is an installation/readiness claim only. Live WEB01-WEB24 completion is not yet claimed.

The cross-run prerequisite repair for learning-mode stage continuation is now validated by live execution. S12 run `RUN_20260925T223720Z_6e1b1fc8` completed all 210 assignments with **203 PASS, 7 INCONCLUSIVE and 0 FAIL**. The verified subset contained 203 cases; 7 remained excluded. Consolidation transaction `CC_db09484eefd9db783742336b69296eb5` is **COMMITTED** and its request explicitly binds `stage_id=S12` and `training_run_id=RUN_20260925T223720Z_6e1b1fc8`.

### Live S12 result

```text
RUN = RUN_20260925T223720Z_6e1b1fc8
execution_complete = true
PASS = 203
INCONCLUSIVE = 7
FAIL = 0
verified_subset = 203
excluded = 7

CONSOLIDATION = CC_db09484eefd9db783742336b69296eb5
journal.status = COMMITTED
request.stage_id = S12
request.training_run_id = RUN_20260925T223720Z_6e1b1fc8
```

This confirms real cross-run progression from the earlier S11 state into live S12 training and a committed S12 consolidation. S12 remains non-all-PASS because seven cases were unresolved.

- [Detailed S12 live report](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)

### Configured post-S40 training progression

WEB01-WEB24 is now configured as the next SSI training phase after completion of the core S11-S40 sequence. The installed gate requires:

```text
S40 execution_complete = true
AND S40 consolidation = COMMITTED
AND WEB LEGO = READY
-> start WEB01-WEB24
```

This records installed/configured sequencing, not an observed S40 -> WEB01 transition. That transition remains pending future runtime evidence.

- [Detailed 2026-09-26 update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [Machine-readable 2026-09-26 summary](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
- [Preserved 2026-09-23 S11 report](RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md)

## Preserved V4 baseline — 2026-09-17

```text
RUN_ID = RUN_20260917T024400_DCD7FD
FINAL_STAGE = S10
COMPLETE = true

BODY_FROZEN = PASS
ISKRA1 = PASS
ISKRA2 = PASS
ISKRA3 = PASS
ISKRA4 = PASS
ISKRA5 = PASS
ISKRA6 = PASS

CONSOLIDATION / PROMOTION / BRIDGE = PASS
REGRESSION = PASS
ROLLBACK = NOT_REQUIRED
ADVANCE_ALLOWED = true

BODY_FROZEN promoted reload = 144/144 expected entries
POST-S10 DRONE SOFTWARE LAB = PASS / 6 scenarios
POST-S10 HUMANOID SOFTWARE LAB = PASS / 15 scenarios
POST-S10 TOTAL = 21 scenarios
```

## Current milestone — 2026-09-18 — SSI Dual Mother Cross Lab V1

Two independent domain-side controllers were exercised together:

- **DRONE MOTHER** — micro-drone reconnaissance collective.
- **RESCUE ROBOT MOTHER** — specialist non-humanoid rescue robots.

Measured software-lab result:

```text
DRONE MOTHER = 12/12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12/12 paired scenario families PASS
REPEATS PER SCENARIO FAMILY = 60
PAIRED MISSIONS = 720
DOMAIN RESULT ROWS = 1,440

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
= 5.2559 ms across all 12 paired scenario means

PUBLIC RESEARCH PORTAL = PUBLISHED
PUBLIC REVIEWER SURFACE = OBSERVER-ONLY
```

These timings are execution timings of the software laboratory. They are **not** physical drone/robot response times.

## Cross-domain contracts

### M01-M06 — validation before cross consolidation

```text
detect
-> micronetwork sync
-> assess
-> decision
-> action
-> validate
-> cross consolidation
```

### M07-M12 — dynamic invalidation, rollback and second consultation

```text
checkpoint
-> action
-> dynamic evidence
-> current plan invalidated
-> rollback
-> second cross consultation
-> conservative replan
-> validation
```

Dynamic cases include secondary collapse, gas/hazard expansion, contradictory sensor reports, route/drill failure, moving-target reacquisition and Mother-to-Mother link degradation with micronetwork continuity.

## Rescue Robot Mother domain boundary

The rescue domain does **not** use humanoids in this laboratory. Specialist classes represented in the measured scenarios:

```text
MOLE_DRILLER
TRACKED_CRAWLER
SNAKE_SCOUT
QUADRUPED
AMPHIBIOUS_CRAWLER
HEAT_SHIELDED_CRAWLER
```

## Public portal boundary

The published public research portal is a sanitized presentation/observer surface backed by the recorded evidence. It does not provide ROOT execution, private SSI implementation, hidden configuration writes or physical certification.

## Claim boundary

The 2026-09-18 evidence supports a software-laboratory claim that the paired Drone Mother / Rescue Robot Mother harness executed the declared consultation, rollback, replanning, validation and consolidation paths under the recorded scenarios.

It does **not** establish physical drone performance, physical rescue-robot performance, physical humanoid performance, safety certification, production readiness, independent external replication, universal superiority, AGI or consciousness.

Older dated snapshots remain valid historical evidence of what was known, planned or measured at their commit dates.

