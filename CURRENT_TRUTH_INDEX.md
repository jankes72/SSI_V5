# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-10-01`  
**Repository role:** public R&D, evidence and external-validation hub with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

- [Canonical current research roadmap — 2026-09-30](CURRENT_RESEARCH_ROADMAP_20261001.md)

- [CZARA first training cycle — final results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md)
- [Machine-readable CZARA final public summary](evidence/CZARA_FIRST_TRAINING_CYCLE_PUBLIC_SUMMARY_20261001.json)
- [Sanitized CZARA run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md)
- [ZERO-LAB / LAB_ARCHITECT next module](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)
- [Historical CZARA S120 checkpoint](RESULTS/CZARA_RND_1_0_0_TRAINING_CHECKPOINT_S120_20260930.md)

- [S20-S26 operator stop and LAB repair incident](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md)
- [Machine-readable S20-S26 stop/repair summary](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_PUBLIC_SUMMARY_20260930.json)

- [S19 observability incident and pre-S20 status](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 observability/evidence hardening preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review feedback and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
- [Latest S13-S18 routing and crash-recovery evidence](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
- [Machine-readable S13-S18 public summary](RESULTS/SSI_V5_S13_S18_ROUTING_PUBLIC_SUMMARY_20260929.json)
- [Latest S12 live training + committed consolidation](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md)
- [S11 -> S12 quality and efficiency signal](RESULTS/SSI_V5_S11_S12_QUALITY_EFFICIENCY_SIGNAL_20260926.md)
- [S11 consolidation + WEB BLOCKS update](RESULTS/SSI_V5_S11_CONSOLIDATION_AND_WEB_LEGO_UPDATE_20260926.md)
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
- [ZERO-LAB / LAB_ARCHITECT next module](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)

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

