# SSI V5 — S10 Variant V1 Control Baseline and V1/V2 Comparison

**Date:** `2026-09-13`  
**Variant:** `V1 / lean control-baseline configuration`  
**Status:** `SANITIZED ENGINEERING EVIDENCE / COMPARISON BASELINE`  
**Implementation:** proprietary / not published

## 1. Purpose

This document defines **S10 VARIANT V1** as the deliberately leaner control/reference line used for comparison with the richer **S10 VARIANT V2** configuration.

The purpose of V1 is not to replace V2 and not to represent an older or invalid Router S10. V1 preserves the current calibrated S10 decision profile and integrity gates while using a more direct evaluation path with less cache/reuse infrastructure around the execution.

The two variants are therefore intended to answer a controlled engineering question:

> What changes when the same S10 competence-selection logic is executed in a leaner control configuration versus a richer configuration with incremental reuse, whole-state cache reuse and additional control/observability infrastructure?

The variants must not be mixed in one timing claim. Any performance comparison must use the same declared hardware, BODY source set, source state, cache condition and evaluation mode.

## 2. Variant identity

```text
VARIANT V1
= lean control/reference configuration
= direct FAST_PASS -> DEEP evaluation path
= full explicit deep-comparison evidence in the recorded snapshot
= calibrated GRID_SAFETY_MAX profile active
= PRE_S10 integrity gate preserved
= immutable enforcement preserved

VARIANT V2
= richer control / observability / integrity configuration
= FULL/FALLBACK available
= INCREMENTAL_PARTIAL available
= META_CACHE_REUSE available
= optimized repeated evaluation on unchanged or partially changed state
= separate measured timing record
```

V1 and V2 are comparison lines, not competing truth records.

## 3. V1 evidence snapshot

The current sanitized V1 snapshot was inspected from the retained local engineering data bundle.

Recorded S10 evaluation state:

```text
MODE = AUTO_EVALUATE_DEEP
STATUS = EVALUATION_COMPLETE
SOURCE_BODIES = ISKRA4 + ISKRA5
SKILL_VARIANTS = 144
S10_FAMILIES = 13
DEEP_COMPARE_COMPLETED = 13 / 13 families
DEEP_PAIR_COUNT = 1890
CHAMPION_PROPOSALS = 13
```

This specific snapshot is therefore **not** claimed as a seven-BODY V1 benchmark. It is a scoped V1 control snapshot based on the declared `ISKRA4 + ISKRA5` source set.

## 4. V1 integrity and calibration state

The V1 snapshot preserves the current S10 calibration and integrity controls.

Recorded state:

```text
ACTIVE_PROFILE = GRID_SAFETY_MAX
PRE_S10_GATE = PASS
IMMUTABLE_ENFORCEMENT = TRUE
CONSOLIDATION_BLOCKED = FALSE
RUNTIME_PROFILE_CONFIRMED = TRUE
CONFIG_HASH_MATCH = TRUE
POST_ACTIVATION_SMOKE = PASS
REGRESSION_FOUND = FALSE
```

Final calibration evidence associated with the active profile:

| Metric | GRID_SAFETY_MAX | CONTROL |
|---|---:|---:|
| Precision | 0.696921 | 0.693975 |
| Recall | 1.000000 | 1.000000 |
| False merge rate | 0.055458 | 0.056235 |
| False split rate | 0.000000 | 0.000000 |
| 3-class accuracy | 0.817016 | 0.816239 |
| Champion agreement | 1.000000 | 1.000000 |
| Wrong champion promotion rate | 0.000000 | 0.000000 |

The calibration improvement is modest but measurable. No large-breakthrough claim is made from these deltas alone.

## 5. V1 execution character

The practical character of V1 is a direct evaluation path:

```text
SOURCE STATE
-> FAIR / PRE_S10 INTEGRITY CHECK
-> FAST_PASS FAMILY FORMATION
-> DEEP EVALUATION
-> EVIDENCE RANKING
-> CHAMPION / CHALLENGER PROPOSALS
-> CONSOLIDATION OUTPUT
```

In the current snapshot, all 13 declared S10 families completed deep comparison and the evaluation recorded 1,890 deep pair comparisons.

This makes V1 useful as a transparent control/reference line because the evaluation evidence shows the work being explicitly recomputed rather than primarily reused from an optimized whole-state cache.

## 6. What V1 intentionally does not claim

V1 is described as **leaner**, not featureless.

It still includes the important S10 research mechanisms around:

- Hermes competence memory;
- FAST_PASS family grouping;
- deep comparison;
- evidence-based Champion / Challenger proposals;
- consolidation planning;
- versioned upgrade/descendant workflow;
- calibrated S10 thresholds;
- negative-memory preservation;
- immutable FAIR baseline protection;
- PRE_S10 gate enforcement;
- post-activation profile verification;
- retained audit/evidence history.

The distinction from V2 is primarily the surrounding execution/control optimization, not removal of the central S10 competence logic.

## 7. V2 comparison line

The richer V2 line is documented separately in:

[`S10_VARIANT_V2_PERFORMANCE_AND_INTEGRITY_EVIDENCE_20260913.md`](S10_VARIANT_V2_PERFORMANCE_AND_INTEGRITY_EVIDENCE_20260913.md)

V2 adds optimized evaluation modes around the same broad S10 research workflow.

### V2 — INCREMENTAL_PARTIAL

A controlled localized-change test recorded:

```text
13 S10 families total
12 families reused
1 family recomputed
1 deep pair computed in that run
semantic equivalence to independent full modified evaluation = PASS
```

### V2 — META_CACHE_REUSE

For an unchanged verified V2 state:

```text
13 / 13 families reused
0 families recomputed
0 deep pairs computed in the current run
source scan skipped
whole-state cache reuse active
```

### V2 — measured performance evidence

The currently published V2 evidence records:

```text
WARM META_CACHE_REUSE = ~1.48–1.51 s
COLD INIT + EVALUATION = ~3.60 s
```

These timing values belong to V2 only. They must not be attributed to V1 until a V1 timing run is executed under matched declared conditions.

## 8. Professional V1/V2 comparison matrix

| Dimension | Variant V1 | Variant V2 |
|---|---|---|
| Role | control/reference line | optimized richer line |
| Core S10 research logic | present | present |
| Active calibrated profile | GRID_SAFETY_MAX | must be compared under matched profile/state |
| FAIR / immutable boundary | preserved | preserved |
| Direct full deep recomputation evidence | yes in current snapshot | available through full/fallback path |
| Incremental family reuse | not established as V1 feature | yes |
| Whole-state META cache reuse | not established as V1 feature | yes |
| Partial recomputation | not established as V1 feature | yes |
| Current recorded deep work | 13/13 families, 1890 pairs | mode-dependent; can reuse 13/13 with 0 current deep pairs |
| Current snapshot source set | ISKRA4 + ISKRA5 | seven-BODY performance evidence documented separately |
| Cold timing | not yet measured under comparison protocol | ~3.60 s in published V2 evidence |
| Warm reuse timing | not yet measured under comparison protocol | ~1.48–1.51 s in published V2 evidence |
| Intended research value | transparent control / recomputation baseline | engineering optimization / reuse / observability |

## 9. Why the comparison is scientifically useful

A useful V1/V2 experiment should not ask only which variant is faster.

The stronger comparison is:

```text
SAME INPUT STATE
+ SAME BODY SET
+ SAME S10 PROFILE
+ SAME ACCEPTANCE CONTRACT
+ SAME HARDWARE CLASS
+ DECLARED COLD/WARM CONDITION

-> V1 RESULT
vs
-> V2 RESULT
```

The comparison should then measure:

- semantic result equivalence;
- family assignment equivalence;
- Champion / Challenger proposal agreement;
- false-merge / false-split behavior;
- wrong promotion rate;
- amount of work recomputed versus reused;
- cold execution time;
- warm execution time;
- incremental-change execution time;
- regression behavior;
- integrity/fail-closed behavior.

The expected engineering hypothesis is that V2 should reduce repeated work while preserving the decision result and safety boundaries. That hypothesis must be tested rather than assumed.

## 10. Recommended matched benchmark protocol

A future formal V1/V2 comparison should execute at least three matched scenarios.

### A. Full / cold

```text
same process-start condition
same BODY source set
same S10 profile
same source snapshot
no reusable V2 meta cache assumed
```

Measure total time, family count, pair count, proposals and result hash/equivalence.

### B. Unchanged / warm

Repeat the exact same verified source state.

Expected comparison question:

> Does V2 safely reuse verified state while V1 recomputes more work, and do both produce an equivalent scientific result?

### C. Localized change

Modify one controlled competence family while preserving the experiment contract.

Expected comparison question:

> Can V2 recompute only the affected portion and still match an independent full evaluation result?

All timing claims should include the exact condition and source-set identity.

## 11. Public/private boundary

### Public

This repository may expose:

- variant identities;
- high-level execution modes;
- sanitized counts;
- family/pair totals;
- calibration metrics;
- integrity status;
- timing evidence;
- pass/fail outcomes;
- comparison methodology;
- claim boundaries.

### Private

The following remain proprietary unless separately authorized:

- implementation source code;
- exact internal scoring implementation;
- private thresholds not already intentionally published;
- hidden Micronetwork construction;
- private memory/state layouts;
- executable ROOT-control internals;
- credentials, tokens and local secrets;
- reconstructive private prompts or operational paths.

## 12. Claim boundary

This document establishes a **scoped V1 engineering control baseline** and a professional comparison framework against V2.

It does **not** claim:

- that V1 is universally better, safer or slower than V2;
- that V2 is universally superior to V1;
- that the current V1 snapshot represents seven-BODY evaluation;
- that V1 cold/warm timings have already been measured under the matched comparison protocol;
- that cache reuse proves scientific correctness;
- that full recomputation automatically proves scientific correctness;
- complete external independent replication;
- production security;
- AGI, consciousness or universal transfer.

The current evidence supports the narrower statement:

> Variant V1 is a lean S10 control/reference configuration with the calibrated GRID_SAFETY_MAX profile and preserved PRE_S10/immutable safeguards. In the retained V1 snapshot, 144 skill variants from ISKRA4 and ISKRA5 were organized into 13 S10 families and evaluated through 1,890 deep pair comparisons, with all 13 families completing deep comparison. Variant V2 is the richer optimization line that adds incremental and whole-state reuse paths and must be compared against V1 only under matched declared conditions.
