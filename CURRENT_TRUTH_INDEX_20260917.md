# SSI V5 — Current Truth Index — 2026-09-17

**Role:** newest evidence-backed status index.  
**Repository boundary:** public evidence/protocol mirror; proprietary implementation remains private.

## Newest completed milestone

A complete V4 S1-S10 run finished under one run ID:

```text
RUN_ID = RUN_20260917T024400_DCD7FD
TRACE_ROOT = TRACE_5EE50008986B
FINAL_STAGE = S10
COMPLETE = true
```

Final V4 state:

```text
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
```

Final promoted BODY_FROZEN reload accounting:

```text
expected_count = 144
loaded_count = 144
artifact_count = 4
complete_accounting = true
fresh_process = true
```

Post-S10 software-domain execution:

```text
DRONE = PASS / 6 scenarios
HUMANOID = PASS / 15 scenarios
TOTAL = 21 scenarios
```

## Four preserved comparison lines

| Variant | Role |
|---|---|
| V1 | lean control/reference; direct FAST_PASS -> AUTO_EVALUATE_DEEP |
| V2 | optimized control/observability; FULL/FALLBACK + INCREMENTAL_PARTIAL + META_CACHE_REUSE |
| V3 | intermediate MetaNetwork line |
| V4 | State-Space / uncertainty / adaptive routing line |

The numbering is historical lineage, not a ranking.

## Read these first

1. [`VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md`](VERSIONS/V1_V2_V3_V4_COMPARISON_INDEX_20260917.md)
2. [`VERSIONS/V1_LEAN_CONTROL_20260917.md`](VERSIONS/V1_LEAN_CONTROL_20260917.md)
3. [`VERSIONS/V2_OPTIMIZED_CONTROL_20260917.md`](VERSIONS/V2_OPTIMIZED_CONTROL_20260917.md)
4. [`VERSIONS/V3_METANETWORK_20260917.md`](VERSIONS/V3_METANETWORK_20260917.md)
5. [`VERSIONS/V4_STATE_SPACE_20260917.md`](VERSIONS/V4_STATE_SPACE_20260917.md)
6. [`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)
7. [`RESULTS/V4_PUBLIC_SUMMARY_20260917.json`](RESULTS/V4_PUBLIC_SUMMARY_20260917.json)

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

## Claim boundary

The current evidence supports completion of the stated V4 software training/evaluation run and the stated software-domain post-S10 scenarios.

It does not establish physical drone or humanoid validation, independent external replication, universal superiority over V1/V2/V3, production readiness, AGI or consciousness.

Older dated files remain historical records. When an older status conflicts with this newer evidence-backed status, this 2026-09-17 index is the current-state reference without rewriting the historical record.
