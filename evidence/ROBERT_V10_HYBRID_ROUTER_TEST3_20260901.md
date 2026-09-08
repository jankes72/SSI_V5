# ROBERT V10 Hybrid Router — Test 3 / Adaptive Routing Validation

**Validation date:** 2026-09-01  
**Scope:** ROBERT / Micronetwork full stack / V10 adaptive routing  
**Status:** `DEVELOPMENT_VALIDATED — scoped adaptive routing test`  
**Comparison geometry:** 600 cases / 40 rounds / 15 cases per round

## Why there are three tests

These three runs are not repeated attempts at the same performance target. Each stage had a different experimental purpose, and together they form the evidence sequence.

### Test 1 — earlier / lighter flow

Public 600X baseline:

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 67.85
PASS:             true
```

This stage demonstrated stability of the earlier, lighter lifecycle path.

### Test 2 — full expanded Micronetwork flow

Test 2 deliberately executed a broader path: a larger Experience state and a fuller Candidate -> Challenger -> persistence -> replay/retry/restart/concurrency lifecycle.

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 126.65
start experiences: 5195
end experiences:   5195
PASS:             true
```

Within this research sequence, Test 2 should be interpreted as **evidence that the full path exists and remains consistent**, not as a target speed benchmark. Its longer duration compared with the earlier lighter path is consistent with doing more work. Timing alone is not the evidence for layer use; state counters, replay, restart, persistence, concurrency and lifecycle checks are also part of the evidence.

Test 2 was necessary before routing: the full path first had to be shown to work before the system could be evaluated for selectively avoiding it when unnecessary.

### Test 3 — full Micronetwork system with V10 Hybrid Router

Test 3 preserves the same main stress-test geometry:

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 57.61
PASS:             true
```

Routing:

```text
REUSE_TOP1:          534
VERIFY_TOPK:          66
ESCALATE_FULL_FLOW:    0
CREATE_SKILL_PATH:     0
fallback_count:        0
```

Known-case correctness check:

```text
correctness_matched:     100
correctness_total_known: 100
correctness_rate:        1.0
```

Foreground latency:

```text
p50: 20.612 ms
p95: 23.902 ms
```

V10 counters:

```text
lookups:             600
cache_exact_hits:    100
similarity_hits:     434
route_compilations:  133
errors:                0
```

## Timing comparison

| Stage | 600 cases | Time | Interpretation |
|---|---:|---:|---|
| Test 1 | PASS | 67.85 s | earlier, lighter flow |
| Test 2 | PASS | 126.65 s | full expanded Micronetwork flow |
| Test 3 | PASS | 57.61 s | full system with V10 selective routing |

Test 3 was:

- approximately **2.20x faster than Test 2**;
- approximately **54.5% shorter in duration than Test 2**;
- approximately **15.1% faster than Test 1**, despite being recorded after the system had been expanded with routing and a fuller structure.

## What the result supports

Within the tested scope, the result supports the following model:

```text
INPUT
-> V10 ROUTER
-> EXACT CACHE / SIMILARITY ROUTE
-> REUSE_TOP1 or VERIFY_TOPK
-> CANONICAL MICRONETWORK RESULT
-> FEEDBACK / ROUTE COMPILATION
```

The full path remains part of the architecture, but recognized cases need not execute the entire path unnecessarily.

The important result is not timing alone, but the combined observation:

```text
SAME TEST GEOMETRY
+ 100/100 KNOWN CORRECTNESS
+ 0 FALLBACKS
+ 534 DIRECT REUSE ROUTES
+ 66 VERIFY ROUTES
+ LOWER TOTAL DURATION
```

## Why Test 2 was necessary

Without Test 2, the faster Test 3 would be difficult to interpret. It would not be clear whether the system actually possessed the full expanded path or simply never executed it.

The sequence is therefore intentional:

```text
TEST 1
older / lighter flow

-> TEST 2
full expanded Micronetwork flow

-> TEST 3
full system + dynamic routing
```

Test 2 shows that the full path exists and remains consistent. Test 3 shows that after adding V10, the system can use shorter paths for recognized cases while preserving measured correctness in the tested scope.

## Important limitations

This result does not prove that V10 will be faster for every workload or that SSI is production-ready.

In particular:

- the measurement concerns this specific 600-case set and current data state;
- `100/100 correctness` applies to the controlled known-case subset measured in this test;
- the absence of `FULL_FLOW` in this run does not prove that escalation is never required;
- `background_stats.completed = 599` with `submitted = 600` means the final snapshot was written while one background task had not yet been marked complete; this is not hidden;
- future tests should deliberately include novel, conflicting and adversarial cases requiring escalation.

The appropriate interpretation is:

**`DEVELOPMENT_VALIDATED — adaptive routing produced a faster scoped 600-case run while preserving measured known-case correctness.`**

## Public evidence references

- earlier 600X: `evidence/robert_600x/HARDCORE_600X_SUMMARY.json`
- full Test 2: `evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`
- Test 3 raw summary: `evidence/router_v10_test3/H_TEST3_RESULTS.json`
- Test 3 baseline snapshot: `evidence/router_v10_test3/A_BASELINE.json`

An older V10 beta run that exposed routing errors remains part of the local engineering history. It is not presented as the final Test 3 result. Its existence is methodologically important: the current PASS followed detection and repair of a real routing regression rather than being the result of the first attempt.
