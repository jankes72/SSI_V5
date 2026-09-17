# SSI V5 — V1 / V2 / V3 / V4 comparison index

**Published:** 2026-09-17  
**Purpose:** public comparison map for four preserved SSI engineering lines.

## Variant map

| Variant | Research role | Distinguishing path |
|---|---|---|
| V1 | lean control/reference | direct `FAST_PASS -> AUTO_EVALUATE_DEEP` |
| V2 | optimized control/observability | `FULL/FALLBACK`, `INCREMENTAL_PARTIAL`, `META_CACHE_REUSE` |
| V3 | intermediate MetaNetwork | MetaNetwork-oriented intermediate architecture |
| V4 | State-Space line | State-Space / uncertainty / adaptive routing extensions |

The numbering reflects historical lineage, not an ordering of quality or performance.

## Shared comparison contract

The four lines are intended to be compared under matched conditions wherever practical:

- same S1-S10 curriculum;
- same task families;
- same acceptance contract;
- same BODY set / source snapshot;
- same hardware class;
- same declared cold/warm condition;
- same evidence boundaries;
- same FAIR protections;
- same regression and rollback discipline.

## Public/private boundary

This repository publishes descriptions, protocols, counts, hashes, pass/fail outcomes, timings where measured, regression evidence and claim boundaries.

It does not publish proprietary implementation source for SSI/V10/S10/Micronetwork/ISKRA/DIRECTOR/ROBERT.

## Version documents

- `VERSIONS/V1_LEAN_CONTROL_20260917.md`
- `VERSIONS/V2_OPTIMIZED_CONTROL_20260917.md`
- `VERSIONS/V3_METANETWORK_20260917.md`
- `VERSIONS/V4_STATE_SPACE_20260917.md`

## Current completed matched-result milestone

V4 has a complete S1-S10 run and post-S10 software-domain evidence published in:

- `RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md`
- `RESULTS/V4_PUBLIC_SUMMARY_20260917.json`

The other variant lines remain separate research baselines and should not inherit V4 outcomes.
