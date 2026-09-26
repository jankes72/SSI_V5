# SSI V5 — S11 to S12 quality and efficiency signal

**Date:** 2026-09-26  
**Status:** `PUBLIC RESEARCH NOTE / LIVE TRAINING COMPARISON`  
**Evidence boundary:** software/runtime evidence only.  
**Repository role:** public evidence mirror; proprietary implementation remains private.

## 1. Why this comparison matters

S12 is the first live stage after the evidenced S11 consolidation. This makes the S11 -> S12 transition useful for checking whether continued training is associated not only with preserved execution, but also with a better verified-case yield and lower practical execution cost.

The comparison must keep two evidence classes separate:

1. repository-backed run/consolidation facts;
2. operator-observed efficiency measurements that are not yet backed by a complete public provider usage ledger.

## 2. Repository-backed outcome comparison

| Metric | S11 | S12 | Change |
|---|---:|---:|---:|
| Executed cases | 210 | 210 | 0 |
| Verified PASS | 196 | 203 | +7 |
| Unresolved | 14 | 7 | -7 (-50%) |
| FAIL | 1 | 0 | -1 |
| Consolidation | COMMITTED | COMMITTED | retained |

S11 run:

```text
RUN = RUN_20260925T163311Z_820718d5
execution_complete = true
PASS = 196
INCONCLUSIVE = 13
FAIL = 1
verified_subset = 196
CONSOLIDATION = CC_82dd0b3af825cd8543dcd59835023a5a
status = COMMITTED
```

S12 run:

```text
RUN = RUN_20260925T223720Z_6e1b1fc8
execution_complete = true
PASS = 203
INCONCLUSIVE = 7
FAIL = 0
verified_subset = 203
CONSOLIDATION = CC_db09484eefd9db783742336b69296eb5
status = COMMITTED
```

The repository therefore supports a bounded claim that verified-case yield improved from S11 to S12 while unresolved outcomes were reduced by half and FAIL outcomes fell from one to zero.

## 3. Operator-observed efficiency signal

The operator reports that the live S12 stage completed at approximately **3x lower wall-clock time** than the comparable S11 stage and used approximately **3x fewer model tokens**.

The operator also reports cumulative paid-model expenditure through the current training/loading work at approximately **USD 7 total**, including approximately:

- **USD 1.50** attributed to Luna;
- **USD 5** attributed to the other primary paid provider;
- the remaining difference is treated as rounding and/or other usage and is not assigned here.

These cost and token observations are currently classified as:

```text
SOURCE_CLASS = OPERATOR_OBSERVED
PUBLIC_FULL_USAGE_LEDGER = NOT_AVAILABLE
PROVIDER_BILLING_RECONCILIATION = NOT_COMPLETE
```

They should therefore be interpreted as an efficiency signal, not as a fully audited cost benchmark.

## 4. Interpretation: competence reuse / Champion hypothesis

The joint pattern is notable:

```text
verified outcomes       UP
unresolved outcomes     DOWN
FAIL outcomes           DOWN
observed runtime        DOWN ~3x
observed token use      DOWN ~3x
```

This pattern is **consistent with increased reuse of previously consolidated competence**, including Champion / LEGO / micronetwork paths, rather than repeatedly solving every case through the most expensive full-flow path.

However, the S11 -> S12 comparison alone does **not** establish that Champion routing caused the runtime/token reduction. Other factors may contribute, including case mix, provider/model routing, cache/reuse behavior, prompt differences, runtime conditions or other implementation changes.

The correct current claim is therefore:

> S12 provides the first live multi-metric signal consistent with practical competence reuse: verified-case yield improved while operator-observed execution time and token consumption fell substantially.

It is **not yet** a causal proof of Champion-first routing efficiency.

## 5. Required telemetry for S13 and later

To turn the efficiency signal into a stronger causal result, future stages should record per-case routing data such as:

```text
stage_id
case_id
actor_id
route_mode
champion_id / competence_id
champion_match_score
reuse_hit
partial_flow_invoked
full_flow_invoked
provider
model
input_tokens
output_tokens
wall_clock_ms
provider_cost
verdict
```

The following aggregate metrics should then be published for each stage:

- Champion Hit Rate;
- % cases solved without FULL FLOW;
- verified PASS rate;
- unresolved rate;
- FAIL rate;
- median and total token usage;
- median and total wall-clock time;
- paid-provider cost;
- cost per verified PASS;
- FULL FLOW fallback rate.

A controlled comparison of `Champion-first enabled` versus `forced FULL FLOW` on matched cases would provide substantially stronger evidence of causality.

## 6. What this update establishes

This update establishes:

- an evidenced S11 -> S12 increase from 196 to 203 verified PASS cases;
- a reduction from 14 to 7 unresolved cases;
- a reduction from one FAIL to zero;
- committed consolidation after both stages;
- an operator-observed approximately 3x runtime reduction;
- an operator-observed approximately 3x token reduction;
- an operator-observed cumulative paid-model spend of approximately USD 7 through the current training/loading work.

## 7. What this update does not establish

It does **not** establish:

- that Champion routing alone caused the efficiency improvement;
- an audited provider-level cost benchmark;
- general performance improvement outside the S11/S12 training distributions;
- S13-S40 completion;
- successful WEB01-WEB24 live training;
- physical validation;
- independent external replication;
- production readiness;
- AGI or consciousness.

The next important evidence point is S13. If S13 preserves or improves verified outcomes while maintaining lower token/time cost, the project will have a stronger multi-stage progression signal rather than a single S11 -> S12 comparison.
