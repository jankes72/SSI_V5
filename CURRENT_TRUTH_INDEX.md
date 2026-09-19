# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-09-18`  
**Repository role:** public evidence mirror with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

1. [`CURRENT_TRUTH_INDEX_20260918.md`](CURRENT_TRUTH_INDEX_20260918.md)
2. [`RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md`](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
3. [`RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json`](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
4. [`SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md`](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)
5. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
6. [`RESULTS/V4_PUBLIC_SUMMARY_20260917.json`](RESULTS/V4_PUBLIC_SUMMARY_20260917.json)
7. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
8. [`docs/index.html`](docs/index.html) — source of the published public research portal.

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