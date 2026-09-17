# SSI V5 — V4 State-Space Line

**Published:** 2026-09-17  
**Role:** State-Space / richer adaptive routing research line  
**Public boundary:** evidence and architecture description only; proprietary implementation remains private.

## Identity

V4 is the later SSI comparison line that extends the earlier S10 architecture with State-Space-oriented components and additional adaptation/uncertainty infrastructure.

```text
V4 = State-Space line
```

## Architectural additions

The V4 research line includes the newer components documented in the private implementation and public evidence boundary, including:

- DomainAdapter;
- StateEncoder;
- RegionEstimator;
- TransitionEstimator;
- UncertaintyGate;
- V10-SS / S10-SS path;
- State-Space shadow integration;
- Diana / Recursio integration path;
- atomic rollback / promotion safety boundaries;
- reuse-safety and anti-loop controls.

These additions are kept separate from the V1, V2 and V3 identities for controlled comparison.

## Shared operational skeleton

For fair comparison, V4 uses the same broad execution discipline as the other lines:

- seven BODY runtimes;
- S1-S10 shared curriculum;
- FAIR protection;
- local ROOT / public observer separation;
- stage barriers;
- consolidation;
- promotion;
- regression testing;
- rollback on failure;
- evidence and provenance preservation.

## Current V4 validated run

A complete V4 S1-S10 run completed on 2026-09-17 under run ID:

```text
RUN_20260917T024400_DCD7FD
```

The detailed public result is published separately in:

`RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`

The numbering is lineage, not a performance ranking.
