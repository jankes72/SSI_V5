# SSI V5 — Router S10 Variants: V1 vs V2

**Date:** `2026-09-13`  
**Role:** reviewer-facing comparison front door  
**Public boundary:** sanitized evidence only / no proprietary implementation source

## Why two variants exist

SSI V5 retains two Router S10 engineering lines for controlled comparison rather than treating every optimization as a silent replacement of the previous configuration.

```text
V1 = lean control/reference variant
V2 = richer optimized control/observability variant
```

The purpose is to measure the engineering trade-off between explicit recomputation and safe reuse while preserving the same research boundaries, calibration discipline and immutable FAIR controls.

## Shared S1–S10 training control

Both variants are predeclared to receive the **same ten-stage S1–S10 training curriculum**.

```text
V1 = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V2 = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
```

The curriculum, task families, ordering/randomization rules and acceptance contract are intended to remain matched. The experimental variable is therefore the S10 execution/control variant, not unequal training exposure.

The ten stages progress from foundation and routing practice through autonomy, robustness, multiple-solution reasoning, rerouting, cross-domain abstraction, novel recombination and a final generalization-readiness gate.

Detailed shared-training methodology:

[`S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md`](S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md)

This shared curriculum is a predeclared methodology. It does not claim that both variants have already completed all ten stages.

## Variant V1 — control/reference

V1 is the lean comparison baseline.

Current retained V1 evidence records:

```text
MODE = AUTO_EVALUATE_DEEP
SOURCE_BODIES = ISKRA4 + ISKRA5
SKILL_VARIANTS = 144
S10_FAMILIES = 13
DEEP_COMPARE_COMPLETED = 13 / 13
DEEP_PAIR_COUNT = 1890
ACTIVE_PROFILE = GRID_SAFETY_MAX
PRE_S10_GATE = PASS
IMMUTABLE_ENFORCEMENT = TRUE
RUNTIME_PROFILE_CONFIRMED = TRUE
REGRESSION_FOUND = FALSE
```

This is a scoped two-BODY V1 snapshot, not a seven-BODY benchmark.

Detailed V1 evidence and comparison protocol:

[`S10_VARIANT_V1_CONTROL_BASELINE_AND_V1_V2_COMPARISON_20260913.md`](S10_VARIANT_V1_CONTROL_BASELINE_AND_V1_V2_COMPARISON_20260913.md)

## Variant V2 — optimized control/observability

V2 adds richer execution optimization and integrity-aware reuse around the S10 workflow.

Documented V2 modes include:

```text
FULL / FALLBACK
INCREMENTAL_PARTIAL
META_CACHE_REUSE
```

Published V2 evidence includes a localized-change run where 12 of 13 families were reused and only one family was recomputed, and an unchanged-state run where all 13 families were reused with zero current deep-pair computations.

Measured V2 timing evidence currently published:

```text
WARM META_CACHE_REUSE = ~1.48–1.51 s
COLD INIT + EVALUATION = ~3.60 s
```

Detailed V2 evidence:

[`S10_VARIANT_V2_PERFORMANCE_AND_INTEGRITY_EVIDENCE_20260913.md`](S10_VARIANT_V2_PERFORMANCE_AND_INTEGRITY_EVIDENCE_20260913.md)

## What must stay identical in a fair V1/V2 benchmark

A formal comparison should keep the following matched:

- S1–S10 training curriculum;
- task-family identities;
- acceptance contract;
- hardware class;
- selected BODY source set;
- source-state snapshot;
- S10 profile;
- cold/warm condition;
- declared evaluation mode;
- measurement boundaries.

The benchmark should compare not only time but also semantic result equivalence, family assignments, Champion/Challenger agreement, false merge/split behavior, wrong promotions, amount of work recomputed or reused, regression outcome and fail-closed integrity behavior.

## Claim boundary

The current evidence does not justify a universal claim that V1 is slower or that V2 is superior in every condition. V2 has measured optimization evidence under its declared conditions; V1 now has a separately documented control snapshot and must receive matched timing runs before timing claims are made across variants.

The shared S1–S10 curriculum is predeclared as the same for both variants, but this document does not claim that both variants have already completed the ten training stages.

The intended scientific value is the controlled comparison itself:

> preserve a lean reference path, introduce an optimized path, give both variants the same training exposure, hold the research invariants fixed, and accept performance or efficiency improvements only when the resulting decisions remain evidence-equivalent and integrity gates remain intact.
