# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-09-29`  
**Repository role:** public evidence mirror with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

- [Latest S13-S18 routing and crash-recovery evidence](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
- [Machine-readable S13-S18 public summary](RESULTS/SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json)
- [Latest S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [S11 -> S12 quality and efficiency signal](RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md)
- [S11 consolidation + WEB LEGO update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
- [Current machine-readable training progress](RESULTS/SSI_V5_CURRENT_TRAINING_PROGRESS_20260926.json)
- [Preserved S11-named machine-readable update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_PUBLIC_SUMMARY_20260926.json)
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

## Current training front — S13-S18 completed, S19 interrupted/recovery prepared

Current published core-training progression:

| Stage | Executed | PASS | INCONCLUSIVE | FAIL | Consolidation |
|---|---:|---:|---:|---:|---|
| S11 | 210/210 | 196 | 13 | 1 | COMMITTED |
| S12 | 210/210 | 203 | 7 | 0 | COMMITTED |
| S13 | 210/210 | 203 | 6 | 1 | COMMITTED |
| S14 | 210/210 | 208 | 1 | 1 | COMMITTED |
| S15 | 210/210 | 175 | 31 | 4 | COMMITTED |
| S16 | 210/210 | 209 | 1 | 0 | COMMITTED |
| S17 | 210/210 | 206 | 2 | 2 | COMMITTED |
| S18 | 210/210 | 196 | 12 | 2 | COMMITTED |

For S13-S18 together:

```text
unique cases = 1,260
PASS = 1,197 (95.00%)
INCONCLUSIVE = 53
FAIL = 10
```

The unique-case audit counts each `(stage_id, actor, case_id)` once. For all completed S13-S18 cases, `micronetwork_used=true`, `v10_used=true` and `collective_used=true`. Automatic Champion execution is not claimed: `automatic_champion=false` and `no_automatic_champion=true` were recorded across all 1,260 completed cases, while no explicit Champion route execution was found.

The older receipts do not expose a canonical final per-case routing decision that cleanly separates exact reuse from full-flow escalation. Therefore the current bounded routing classification is `MICRONETWORK_V10_USED_ROUTE_UNRESOLVED`, not a claimed reuse/full-flow percentage.

S19 was interrupted after BODY_FROZEN produced 30 cases: **14 PASS, 16 INCONCLUSIVE, 0 FAIL**. Fifteen already-existing S19/BODY_FROZEN case files lacked CASE attestations after the host interruption; only those missing attestations were restored, their original outcomes were preserved, evidence coverage was rechecked, and the source run was sealed as interrupted.

Recovery/readiness checks subsequently reported:

```text
7 BODY/ISKRA runtime sockets = present
Pocket Micro = READY
Doctor = READY_FOR_BOOT
WEB LEGO = READY
WEB LEGO items = 126
WEB templates = 15
WEB stages = 24
WEB cases = 192
WEB runtimes = 7/7
WEB data_policy = SYNTHETIC_ONLY
```

New routing telemetry for future cases is installed to record the effective path more explicitly. Successful post-recovery S19 execution has not yet been published, so no new ISKRA1 result is claimed here.

The configured post-S40 sequence remains:

```text
S19 restart from ISKRA1
-> S20 ... S40
-> S40 execution_complete = true
-> S40 consolidation = COMMITTED
-> WEB01 ... WEB24
```

The actual S40 -> WEB01 live transition remains pending runtime evidence.

- [Detailed S13-S18 routing and recovery report](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
- [Machine-readable S13-S18 public summary](RESULTS/SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json)
- [Previous S12 live report](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)

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

