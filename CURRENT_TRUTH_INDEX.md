# SSI V5 — CURRENT TRUTH INDEX

**Status:** `CURRENT POINTER / 2026-09-22`  
**Repository role:** public evidence mirror with a published research portal; proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.  
**History rule:** earlier dated truth/status files remain preserved and are not retroactively rewritten.

## Use these current documents first

- [2026-09-22 S11 continuation and LAB report](RESULTS/SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md)
- [LEGO Pocket, META-LEGO and Director-connected laboratories](SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md)
- [Football World implementation boundary](RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md)
- [Sanitized operator excerpt](evidence/SSI_V5_S11_CONTINUATION_20260922_OPERATOR_EXCERPT.md)
- [Offline release tests](RESULTS/SSI_V5_LAB_FIX_OFFLINE_TEST_SUMMARY_20260922.json)

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

## Current implementation milestone — 2026-09-22

```text
SSI V5 Final = IMPLEMENTED / CONTINUATION RUN OBSERVED
BODY_FROZEN + ISKRA1..ISKRA6 = 7/7 runtime/profile readiness reported
DIRECTOR = INDEPENDENT CORE
POCKET readiness = 1 qualified package checked for 7 actors

BODY_FROZEN S11 continuation
inherited prefix = 27 cases verified by the local continuation checker
S11-05-04 = native PASS / CI PASS / CASE_DONE PASS
S11-05-05 = native PASS / CI PASS / CASE_DONE PASS
S11-05-06 = native PASS / CI PASS / CASE_DONE PASS
pending at the last shown CASE_DONE = 0

S11 stage summary = NOT INCLUDED IN THE SUPPLIED EXCERPT
S11 completion for all 7 BODY = NOT ESTABLISHED BY THIS EXCERPT
S12-S40 completion = NOT CLAIMED
PRIVATE LAB FIX = 165/165 offline tests across 14 suites
```

The latest source is an operator-provided excerpt from
`RUN_20260922T182234Z_5ffa1394`. The 27-case prefix was revalidated by the local
continuation checker; the three shown cases then obtained native and CI PASS.
The record ends before a stage or full-run summary.

LEGO Pocket, Pocket Micro, META-LEGO and permanent R&D/controlled-experiment
laboratories are implemented. The independent DIRECTOR can consume laboratory
metadata and has an implemented delegation path. That new end-to-end path and
ŚWIAT PIŁKI — HIPNOZA data/outcome closure retain separate pending validation.

The historical catalog totals and META-LEGO audit remain in the
[2026-09-20 implementation report](RESULTS/SSI_V5_IMPLEMENTATION_STATUS_20260920.md).
The latest preflight's one qualified package is not a new full-catalog audit.

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
