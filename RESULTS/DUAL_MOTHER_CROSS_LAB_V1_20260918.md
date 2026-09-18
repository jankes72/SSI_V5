# SSI Dual Mother Cross Lab V1 — Measured Public Report — 2026-09-18

## Scope

- Software-only validation.
- No claim of physical robot/drone performance or safety certification.
- DRONE MOTHER: **12/12** paired scenario families passed.
- RESCUE ROBOT MOTHER: **12/12** paired scenario families passed.
- **60 deterministic repetitions** per scenario family.
- **720 paired missions / 1,440 domain result rows**.
- Cross consultation: **6 scenario families, 360 missions, 720 measured consultation rounds**.
- Cross consolidation: **6 scenario families, 360 measured merge executions**.
- Rollback: **6 scenario families, 360 measured rollback executions**.

## Paired scenario timing table

The recorded public table contains one row for each domain side. For each scenario ID the measured cross-event and total-flow values are identical across the two domain-side rows, so the paired summary is shown once below.

| ID | Mode | Dynamic event / purpose | Rescue specialist | Consult ms | Rollback ms | Consolidation ms | Total flow ms | P95 total ms |
|---|---|---|---|---:|---:|---:|---:|---:|
| M01 | cross_consolidation | mine shaft mapping | SNAKE_SCOUT | 0.0000 | 0.0000 | 0.0315 | 3.9578 | 4.4151 |
| M02 | cross_consolidation | collapsed building voids | TRACKED_CRAWLER | 0.0000 | 0.0000 | 0.0340 | 3.7020 | 4.1117 |
| M03 | cross_consolidation | fire thermal search | HEAT_SHIELDED_CRAWLER | 0.0000 | 0.0000 | 0.0640 | 4.5906 | 8.2597 |
| M04 | cross_consolidation | GNSS + communications blackout | QUADRUPED | 0.0000 | 0.0000 | 0.0281 | 3.9550 | 4.2779 |
| M05 | cross_consolidation | unit loss reassignment | TRACKED_CRAWLER | 0.0000 | 0.0000 | 0.0318 | 3.8851 | 4.2117 |
| M06 | cross_consolidation | flooded tunnel access | AMPHIBIOUS_CRAWLER | 0.0000 | 0.0000 | 0.0322 | 4.6240 | 8.2848 |
| M07 | cross_consultation | secondary collapse / aftershock | MOLE_DRILLER | 2.4026 | 0.1280 | 0.0000 | 6.2446 | 6.5414 |
| M08 | cross_consultation | gas explosion / hazard expansion | SNAKE_SCOUT | 2.4840 | 0.1151 | 0.0000 | 6.4093 | 6.6476 |
| M09 | cross_consultation | contradictory sensor reports | SNAKE_SCOUT | 2.6337 | 0.1078 | 0.0000 | 6.6351 | 6.9155 |
| M10 | cross_consultation | drill resistance / route failure | MOLE_DRILLER | 2.3963 | 0.1194 | 0.0000 | 6.2316 | 6.4829 |
| M11 | cross_consultation | moving target / reacquisition | QUADRUPED | 2.4873 | 0.1162 | 0.0000 | 6.3497 | 6.6442 |
| M12 | cross_consultation | Mother-to-Mother link degradation | TRACKED_CRAWLER | 2.5336 | 0.1156 | 0.0000 | 6.4862 | 6.7482 |

## Aggregate software timings

Derived from the scenario means above:

```text
mean cross consultation across M07-M12 = 2.4896 ms
range = 2.3963 .. 2.6337 ms

mean rollback across M07-M12 = 0.1170 ms
range = 0.1078 .. 0.1280 ms

mean cross consolidation across M01-M06 = 0.0369 ms
range = 0.0281 .. 0.0640 ms

mean total software flow across M01-M12 = 5.2559 ms
range = 3.7020 .. 6.6351 ms
```

These are software execution measurements, not real-world robot/drone response times.

## Cross consolidation contract — M01-M06

The stable/validated cases use the path:

```text
detect
-> micronetwork sync
-> assess
-> decision
-> action
-> validate
-> cross consolidation
```

Only validated knowledge is eligible for the recorded cross-domain merge step.

## Dynamic cross-consultation contract — M07-M12

```text
checkpoint
-> action
-> dynamic evidence
-> plan invalidation
-> rollback
-> second cross consultation
-> conservative replan
-> validation
```

Dynamic cases:

- **M07** — secondary collapse / aftershock.
- **M08** — gas explosion / hazard expansion.
- **M09** — contradictory sensor reports.
- **M10** — drill resistance / route failure.
- **M11** — moving target / reacquisition.
- **M12** — Mother-to-Mother link degradation with micronetwork continuity.

## Domain boundary

RESCUE ROBOT MOTHER is a non-humanoid specialist-rescue domain in this lab. Tested specialist classes:

- MOLE_DRILLER
- TRACKED_CRAWLER
- SNAKE_SCOUT
- QUADRUPED
- AMPHIBIOUS_CRAWLER
- HEAT_SHIELDED_CRAWLER

## Claim boundary

PASS means the declared deterministic software-lab acceptance path passed under this harness and recorded repetitions. It does not mean physical certification, independent replication, or production readiness.
