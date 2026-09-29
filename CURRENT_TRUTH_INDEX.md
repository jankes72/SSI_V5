# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-09-29`  
**Repository role:** public evidence mirror with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

- [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 observability/evidence hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review feedback and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
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

## Current training front — S19 fully executed; consolidation hardening before S20

Current evidenced progression:

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
| **S19** | **210/210** | **182** | **24** | **4** | **NOT YET COMMITTED** |

S19 full execution run:

```text
RUN = RUN_20260929T005550Z_a356e86c
execution_complete = true
PASS = 182
INCONCLUSIVE = 24
FAIL = 4
verified subset = 182
excluded = 28
```

The S19 case workload completed. The subsequent cross-consolidation transaction `CC_09eae1705906e8acaa653eb28123fc84` did not commit.

### Why consolidation stopped

The stop is not classified as a case-level capability failure. It occurred after routing observability was expanded to resolve an earlier evidence gap: S13-S18 receipts showed Micronetwork/V10 participation but could not prove whether a Champion was actually selected/executed or when Full Flow actually ran.

The current root-cause classification is:

```text
OBSERVABILITY_INDUCED_INTEGRATION_REGRESSION
```

The observability/continuation integration altered the runtime/bootstrap path used by post-stage consolidation. Recovery also exposed a stale pending-mission condition in BODY_FROZEN. The stage results remain preserved; S19 is not being relabeled.

### Pre-S20 hardening is now preregistered

Before continuation, SSI will gate:

- observer non-interference using matched A/B execution;
- explicit Champion available/selected/executed/result evidence;
- explicit exact-reuse / Full-Flow / provider-fallback evidence;
- model/provider correlation;
- seven-actor failure overlap;
- 7/7 actor+transaction SNAPSHOT validation;
- chain-specific previous-hash and missing-sequence tests;
- a hash-chain negative control;
- explicit notary/signing outage behavior;
- explicit unsigned-attestation buffer-limit safe mode.

The evidence-chain additions are materially informed by external DEV review from **Hamid Ahmadian**. His feedback is attributed separately rather than presented as an SSI-originated requirement.

### Current continuation boundary

```text
S19 execution = complete
S19 consolidation = not yet claimed COMMITTED
S20 = not yet claimed started
WEB01-WEB24 = READY package, not yet claimed live-complete
```

Target sequence:

```text
pre-S20 hardening PASS
-> S19 consolidation COMMITTED
-> S20 ... S40
-> S40 consolidation COMMITTED
-> WEB01 ... WEB24
-> final diagnostic report
```

Current primary records:

- [S19 incident / current stop point](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
- [Machine-readable pre-S20 summary](RESULTS/SSI_V5_PRE_S20_HARDENING_PUBLIC_SUMMARY_20260929.json)
- [S13-S18 routing evidence](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)

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

