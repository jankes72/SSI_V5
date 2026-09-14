# SSI V5 — S10 Variant V3 Intermediate MetaNetwork Status

**Date:** `2026-09-14`  
**Variant:** `V3 / intermediate MetaNetwork configuration`  
**Status:** `ACTIVE ENGINEERING LINE / VALIDATION IN PROGRESS`  
**Implementation:** proprietary / not published

## Purpose

Variant V3 is the third explicit SSI V5 S10 engineering line. It is not defined as better or worse than V1 or V2. Its role is to test a different architectural trade-off between the deliberately lean V1 control/reference line and the richer V2 control/observability line.

The numeric label is a lineage identifier, not a performance ranking. In terms of architectural position, the intended comparison can be read as:

```text
V1 = lean control/reference
V3 = intermediate MetaNetwork
V2 = richer optimized control/observability
```

## Variant identity

V3 preserves its own MetaNetwork-oriented architecture instead of being converted into a copy of V2. Where common SSI V5 contracts are shared, verified behavior from the richer line may be used as a reference implementation for repair and compatibility work, but the V3 line retains its distinct architecture.

The current V3 engineering target includes the same high-level operational boundaries expected across the active seven-BODY research lines:

- BODY_FROZEN plus six ISKRA lines;
- immutable FAIR baseline protection;
- local owner/ROOT control separated from reviewer observation;
- runtime and IPC identity checks;
- Hermes/S10 integration;
- BODY-specific training discovery and preflight;
- evidence/checkpoint preservation;
- fail-closed behavior when an execution capability is not verified.

## Research role

V3 exists to make the comparison space broader than a two-point choice. The project can therefore evaluate three different control/architecture styles rather than silently replacing one configuration with another:

```text
LEAN
<->
INTERMEDIATE METANETWORK
<->
RICHER CONTROL / OBSERVABILITY
```

This does not assume that measured behavior will fall numerically between V1 and V2. Timing, correctness, reuse, robustness and integrity behavior must be measured separately.

## Shared S1-S10 training control

V3 is intended to receive the same S1-S10 curriculum used as the comparison-control training programme for the other S10 variants. The current three-variant training methodology is documented in:

[`S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_V3_20260914.md`](S1_S10_SHARED_TRAINING_PROTOCOL_FOR_S10_V1_V2_V3_20260914.md)

The presence of local training packages or a predeclared stage does not itself mean that the stage was executed or passed.

## Current validation boundary

V3 is an active implementation line. Its common contracts are being synchronized and tested against the current SSI V5 operational standard while preserving its distinct MetaNetwork architecture.

Until a final V3 closure record is published, this document does **not** claim:

- completed S1-S10 execution;
- matched timing results against V1 or V2;
- universal superiority or inferiority;
- complete seven-line S10 scientific validation;
- completed held-out mechanism tests;
- completed 21 cross-domain experiment outcomes;
- production readiness.

## Public / private boundary

### Public

- variant identity and research role;
- high-level architecture class;
- validation status;
- training-control methodology;
- sanitized counts, pass/fail outcomes and timing evidence once separately measured;
- FAIR and observer boundaries.

### Private

- source code;
- exact internal scoring logic;
- private thresholds;
- hidden Micronetwork construction;
- private state and memory layouts;
- executable ROOT/S10 internals;
- credentials, tokens and local filesystem details.

## Claim boundary

The evidence-backed current claim is intentionally narrow:

> SSI V5 now maintains a third explicit S10 engineering line, Variant V3, using an intermediate MetaNetwork-oriented architecture. It is being synchronized to the shared SSI V5 operational and evidence contracts without being converted into V2. V3 is a separate research configuration for controlled comparison, not a declaration that it is better or worse than V1 or V2.
