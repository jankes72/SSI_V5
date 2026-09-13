# SSI V5 — S10 Variant V2 Performance and Integrity Evidence

**Date:** `2026-09-13`  
**Variant:** `V2 / richer control-and-observability configuration`  
**Status:** `INTERNAL ENGINEERING CLOSURE / SANITIZED PUBLIC EVIDENCE`  
**Implementation:** proprietary / not published

## Variant identity — important

This document describes **S10 VARIANT V2 only**.

A second comparison line, **VARIANT V1**, will be documented separately as a deliberately leaner configuration. V1 is intended to provide a useful control/comparison point rather than replace V2.

The variants must not be mixed in one timing claim.

```text
VARIANT V1
= leaner configuration
= separate evidence record
= timings / behavior NOT YET CLAIMED in this document

VARIANT V2
= richer control / observability / integrity configuration
= this document
= current measured timings below
```

When V1 evidence is added, the repository should compare V1 and V2 under the same declared conditions wherever possible: same hardware class, same selected BODY set, same source state, same cache condition and same evaluation mode.

## Why two variants are useful

The purpose of keeping both variants is not to create competing truth records. The purpose is to show the engineering trade-off between a leaner path and a richer path with more supervision, evidence and integrity infrastructure.

A useful comparison should answer:

- what each variant contains at a high level;
- which safeguards and observability features are enabled;
- which evaluation path was exercised;
- whether the state was cold or warm;
- whether the run was FULL/FALLBACK, INCREMENTAL_PARTIAL or META_CACHE_REUSE;
- real measured time under that exact condition;
- whether the scientific/engineering result remained equivalent where equivalence is expected.

No implementation recipe, private scoring logic, hidden Micronetwork construction or source code is required for this comparison.

## Purpose of this V2 closure

This record documents a real engineering optimization cycle in the Router S10 / Hermes / FAIR control path without publishing source code, private data structures, exact scoring logic, hidden Micronetwork construction or executable control mechanisms.

The goal was not to make S10 appear faster by disabling checks. The goal was to identify repeated work on an unchanged state and remove only work that could be safely reused while preserving the same result, provenance boundary and FAIR controls.

## Problem observed

A repeated S10 evaluation on an unchanged seven-BODY state was spending most of its time repeating verification and state-processing work that had already produced the same result.

The engineering investigation identified several broad classes of avoidable cost:

- repeated memory-state inspection;
- duplicate snapshot work inside one evaluation cycle;
- repeated processing of unchanged large state material;
- repeated FAIR integrity work after process restart;
- a runtime-integration defect that was not detectable by syntax compilation alone.

The public lesson is the engineering method, not the private implementation.

## V2 performance evidence

Observed warm evaluation time during the V2 optimization sequence:

```text
~9.15 s
-> ~7.46 s
-> ~4.75 s
-> ~3.19 s
-> ~1.48–1.51 s
```

Observed cold path after process restart:

```text
previously observed: ~19–23 s
final V2 cold init + evaluation: ~3.60 s
```

These are scoped local engineering measurements on the current development machine and current seven-BODY dataset. They are not universal performance claims and must not later be attributed to V1 without separate V1 evidence.

## Evaluation-mode matrix for V2

### FULL / FALLBACK

Used when the system cannot safely reuse prior state or when broader change requires broader re-evaluation.

Public claim: V2 retains a full fallback path rather than forcing reuse.

### INCREMENTAL_PARTIAL

A controlled partial-change test demonstrated:

```text
13 S10 families total
12 families reused
1 family recomputed
1 deep pair computed in that run
semantic equivalence to an independent full modified evaluation = PASS
```

This demonstrates selective re-evaluation for a localized change.

### META_CACHE_REUSE

For an unchanged clean V2 state:

```text
13 / 13 families reused
0 families recomputed
0 deep pairs computed in the current run
source scan skipped
whole-state cache reuse active
```

The semantic cache identity remained stable through the V2 optimization series.

## Required comparison format when V1 is added

V1 and V2 should be compared in a table similar to this, filled only with measured evidence:

| Condition | V1 | V2 |
|---|---:|---:|
| Cold process start | TBD | ~3.60 s total init + evaluation |
| Warm META_CACHE_REUSE | TBD | ~1.48–1.51 s |
| Incremental partial | TBD | 12 reused / 1 recomputed / 1 deep pair |
| Full/fallback | TBD | available as safe fallback; timing must be tied to a specific measured run |
| FAIR baseline | must remain protected | UNTOUCHED |
| Observer boundary | document separately | READ_ONLY public observer |

`TBD` means **not yet measured / not yet claimed**, not failure.

## FAIR integrity behavior in V2

The FAIR baseline remained immutable throughout the work.

The high-level integrity rule remains:

```text
UNCHANGED VERIFIED STATE
-> verified reusable result may be used

DETECTED CHANGE
-> stronger verification path is required

MISMATCH / UNSAFE STATE
-> fail closed / block
```

A persistent FAIR optimization cache was tested for corruption handling. When its integrity fingerprint was deliberately invalidated, the controller rejected the cache and returned to the safe path rather than accepting it as a FAIR PASS.

After byte-for-byte restoration, the valid cache loaded again successfully.

This is a fail-safe cache-integrity test. It is not a claim that the cache is tamper-proof against an attacker with unrestricted host write access.

## Runtime integration lesson

One intermediate V2 patch compiled successfully but failed at runtime because an expected runtime element was missing.

The failure was preserved because it demonstrates an important rule:

```text
SYNTAX / COMPILE PASS
!=
RUNTIME INTEGRATION PASS
```

The defect was repaired, re-tested and followed by full regression.

## V2 verification-harness closure

After the final V2 changes, the full interface/integration verification harness completed successfully.

Verified public-facing categories include:

- Python compilation;
- central self-tests;
- controlled training/experiment queue behavior;
- multi-BODY / Meta readiness;
- import/reload contract checks;
- sibling BODY preflight;
- reviewer observer boundary;
- preserved FAIR baseline;
- seven-BODY discovery/readiness.

Final V2 result:

```text
FULL_INTERFACE_VERIFY = PASS
FAIR baseline = UNTOUCHED
BODY discovery = 7 / 7
public observer = READ_ONLY
```

## Why this matters for DIRECTOR learning

This evidence is intentionally more useful as a problem-solving record than as source code.

The transferable lesson is:

```text
OBSERVE THE BOTTLENECK
-> FORM A TESTABLE HYPOTHESIS
-> CHANGE THE SMALLEST NECESSARY PART
-> PRESERVE INVARIANTS
-> MEASURE AGAIN
-> RUN REGRESSION
-> KEEP FAILURE HISTORY
-> ACCEPT ONLY EVIDENCE-BACKED IMPROVEMENT
```

A future DIRECTOR or BODY_FROZEN 2.0 should not be trained to copy this implementation. It should learn to recognize the engineering pattern and solve an analogous problem in a different architecture using its own evidence.

## Public / private boundary

### Public

- variant identity;
- problem class;
- measurement history;
- evaluation-mode behavior;
- pass/fail outcomes;
- regression result;
- FAIR preservation;
- high-level lessons;
- scoped performance measurements.

### Private

- source code;
- exact internal functions;
- exact fingerprint construction;
- private state layout;
- hidden Micronetwork structure and layer construction;
- private thresholds / scoring;
- exact optimization implementation;
- executable ROOT-control and S10 internals.

## Claim boundary

This closure demonstrates a scoped engineering improvement and integrity-preserving fast path for **Variant V2** on the current SSI V5 installation. It does not prove universal S10 superiority, complete scientific validation of seven-line competence consolidation, production security, external independent replication, or any result for Variant V1 that has not yet been separately measured.
