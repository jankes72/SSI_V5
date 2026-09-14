# SSI V5 — Router S10 Variants: V1, V3 and V2

**Originally opened:** `2026-09-13`  
**Updated:** `2026-09-14`  
**Role:** reviewer-facing comparison front door  
**Public boundary:** sanitized evidence only / no proprietary implementation source

## Why multiple variants exist

SSI V5 retains multiple Router S10 engineering lines for controlled comparison rather than treating every architectural change as a silent replacement of the previous configuration.

The current comparison space contains three explicit research lines:

```text
V1 = lean control/reference variant
V3 = intermediate MetaNetwork variant
V2 = richer optimized control/observability variant
```

The numbering is historical lineage, not a performance ranking. V3 is the third explicitly maintained line even though its architectural role is intermediate between the lean V1 line and the richer V2 line.

The purpose is to measure engineering trade-offs among different execution/control architectures while preserving common research boundaries, calibration discipline, provenance and immutable FAIR controls.

## Shared S1–S10 training control

All three variants are intended to receive the **same ten-stage S1–S10 training curriculum**.

```text
V1 = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V3 = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
V2 = S1 -> S2 -> S3 -> S4 -> S5 -> S6 -> S7 -> S8 -> S9 -> S10
```

The curriculum, task families, ordering/randomization rules and acceptance contract are intended to remain matched. The experimental variable is therefore the execution/control architecture, not unequal training exposure.

Current three-variant methodology:

[`S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_V3_20260914.md`](S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_V3_20260914.md)

The earlier two-variant methodology remains preserved as historical evidence:

[`S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md`](S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_20260913.md)

Neither document is proof that all variants have already completed all ten stages.

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

## Variant V3 — intermediate MetaNetwork

V3 is the third explicit SSI V5 S10 engineering line.

Its research role is different from both V1 and V2:

```text
V1 = deliberately lean reference/control path
V3 = intermediate MetaNetwork-oriented path
V2 = richer control/observability/integrity path
```

V3 preserves its own MetaNetwork architecture. It is not being converted into a copy of V2. Where common SSI V5 contracts already have verified implementations, the current V2 line may be used as a reference for repair and compatibility work, but only the shared contract is transferred; V3 retains its distinct architecture.

The current V3 synchronization/validation target includes the common SSI V5 operational boundaries around seven BODY lines, FAIR protection, local ROOT versus public observer separation, runtime/IPC identity, Hermes/S10 integration, training discovery/preflight, evidence/checkpoints and fail-closed handling of unavailable execution capabilities.

Current V3 status document:

[`S10_VARIANT_V3_INTERMEDIATE_METANETWORK_STATUS_20260914.md`](S10_VARIANT_V3_INTERMEDIATE_METANETWORK_STATUS_20260914.md)

V3 timings and final closure claims remain unclaimed until separate evidence is published.

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

## What must stay identical in a fair three-variant benchmark

A formal comparison should keep the following matched wherever practical:

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

The benchmark should compare not only time but also semantic result equivalence, family assignments, Champion/Challenger agreement, false merge/split behavior, wrong promotions, amount of work recomputed or reused, regression outcome, recovery behavior and fail-closed integrity behavior.

## Claim boundary

The current evidence does not justify a universal claim that any one variant is superior.

V2 has scoped measured optimization evidence under declared conditions. V1 has a separately documented control snapshot. V3 is now an explicit active intermediate MetaNetwork comparison line and must receive its own closure and timing evidence before matched performance conclusions are drawn.

The intended scientific value is the controlled comparison itself:

> preserve a lean reference path, preserve an intermediate MetaNetwork path, preserve a richer optimized path, expose all three to matched training and evaluation conditions, and accept performance or efficiency claims only when the resulting decisions remain evidence-backed and integrity boundaries remain intact.
