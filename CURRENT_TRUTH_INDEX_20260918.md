# SSI V5 — Current Truth Index — 2026-09-18

**Repository role:** public evidence mirror. Proprietary implementation remains private.  
**Evidence boundary:** software-only unless a document explicitly states otherwise.

## Current verified software state

### V4 S1-S10 baseline retained from 2026-09-17

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

CONSOLIDATION = PASS
REGRESSION = PASS
ROLLBACK = NOT_REQUIRED
ADVANCE_ALLOWED = true

BODY_FROZEN promoted reload = 144 / 144 expected entries
POST-S10 DRONE SOFTWARE LAB = PASS / 6 scenarios
POST-S10 HUMANOID SOFTWARE LAB = PASS / 15 scenarios
```

### New 2026-09-18 milestone — SSI Dual Mother Cross Lab V1

Two independent domain-side controllers were exercised together:

- **DRONE MOTHER** — micro-drone reconnaissance collective.
- **RESCUE ROBOT MOTHER** — specialist non-humanoid rescue robots.

Measured software-lab result:

```text
DRONE MOTHER = 12 / 12 paired scenario families PASS
RESCUE ROBOT MOTHER = 12 / 12 paired scenario families PASS
REPEATS PER SCENARIO FAMILY = 60
PAIRED MISSIONS = 720
DOMAIN RESULT ROWS = 1,440

CROSS CONSULTATION:
  6 scenario families
  360 paired missions
  720 measured consultation rounds

CROSS CONSOLIDATION:
  6 scenario families
  360 measured merge executions

ROLLBACK:
  6 scenario families
  360 measured rollback executions
```

Across the 6 consultation scenario means:

```text
mean cross consultation = 2.4896 ms
mean rollback = 0.1170 ms
```

Across the 6 consolidation scenario means:

```text
mean cross consolidation = 0.0369 ms
```

Across all 12 paired scenario means:

```text
mean total software flow = 5.2559 ms
```

These timings are execution timings of the software laboratory. They are **not** physical drone/robot response times.

## Cross consolidation — M01-M06

Validated knowledge is consolidated only after the scenario-side validation step.

- M01 — mine shaft mapping
- M02 — collapsed building voids
- M03 — fire thermal search
- M04 — GNSS + communications blackout
- M05 — unit loss reassignment
- M06 — flooded tunnel access

## Cross consultation + rollback — M07-M12

The dynamic contract is:

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

Cases:

- M07 — secondary collapse / aftershock
- M08 — gas explosion / hazard expansion
- M09 — contradictory sensor reports
- M10 — drill resistance / route failure
- M11 — moving target / reacquisition
- M12 — Mother-to-Mother link degradation with micronetwork continuity

## Rescue Robot Mother boundary

The rescue domain does **not** use humanoids in this laboratory.

Specialist classes represented in the measured scenarios:

```text
MOLE_DRILLER
TRACKED_CRAWLER
SNAKE_SCOUT
QUADRUPED
AMPHIBIOUS_CRAWLER
HEAT_SHIELDED_CRAWLER
```

## Public showcase

A sanitized GitHub Pages research front door is stored in `docs/index.html`. It exposes recorded evidence and claim boundaries only; it does not provide ROOT execution or private SSI implementation.

## Evidence references

- [Dual Mother Cross Lab V1 report](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
- [Dual Mother public summary JSON](RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
- [V4 S1-S10 + post-S10 results](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
- [Complete ecosystem architecture](SYSTEM/SSI_COMPLETE_ECOSYSTEM_ARCHITECTURE_20260917.md)

## Claim boundary

The 2026-09-18 evidence supports a software-laboratory claim that the paired Drone Mother / Rescue Robot Mother harness executed the declared consultation, rollback, replanning, validation and consolidation paths under the recorded scenarios.

It does **not** establish physical robot/drone performance, safety certification, production readiness, independent external replication, universal superiority, AGI or consciousness.
