# SSI V5 — Public Evidence Index

**Current index sync:** `2026-09-23`  
**Latest update:** complete recorded S11 outcomes, DEV safeguards and laboratory status, `2026-09-23`; historical domain measurements retain their original dates.

This directory preserves sanitized evidence, lineage, failure/repair history, integrity references and claim boundaries. Historical files are intentionally retained.

> For the shortest reviewer path, start with [../REVIEWER_INDEX.md](../REVIEWER_INDEX.md).

## Complete S11 outcomes and safeguards — 2026-09-23

[All 210 outcomes](S11_20260923/README.md): 197 PASS, 12 INCONCLUSIVE, one FAIL. S11 is INCONCLUSIVE and S12–S40 are deferred. Full case records were reviewed for the 13 unresolved cases; the 197 PASS source hashes are collector-reported. The export records provenance limits.

- [Full report](../RESULTS/SSI_V5_S11_FULL_RESULTS_20260923.md).
- [DEV safeguards and attack results](../RESULTS/SSI_V5_DEV_SAFEGUARDS_20260923.md).
- [UAV / R&D implementation status](../SYSTEM/SSI_V5_UAV_AND_RND_LABS_20260923.md).
- [R3 offline validation](../RESULTS/SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json): 105 passed, one skipped; distinct from live training.

## Earlier continuation and LAB evidence — 2026-09-22

- [Operator-supplied S11 continuation excerpt](SSI_V5_S11_CONTINUATION_20260922_OPERATOR_EXCERPT.md): 27 checked inherited cases and three new BODY_FROZEN native/CI passes; no stage summary supplied.
- [Current report](../RESULTS/SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md): implementation changes and evidence boundaries.
- [Offline release summary](../RESULTS/SSI_V5_LAB_FIX_OFFLINE_TEST_SUMMARY_20260922.json): 165 tests across 14 suites, zero paid model calls in that suite.
- [Component overview](../SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md): LEGO Pocket, META-LEGO and Director-connected laboratories.
- [Football World boundary](../RESULTS/FOOTBALL_WORLD_IMPLEMENTATION_BOUNDARY_20260922.md): implementation retained; full data-path validation pending.

The operator excerpt and offline summary have different origins. Neither is
presented as a full public raw training archive or an independent replication.

## Preserved verified milestone

```text
V4 S1-S10 = COMPLETE / PASS
7 BODY final state = 7/7 PASS
BODY_FROZEN promoted reload = 144/144

POST-S10 DRONE = 6/6 software scenarios PASS
POST-S10 HUMANOID = 15/15 software scenarios PASS

DUAL MOTHER CROSS LAB V1
DRONE MOTHER = 12/12 PASS
RESCUE ROBOT MOTHER = 12/12 PASS
720 paired missions
1,440 domain result rows
720 cross-consultation rounds
360 cross-consolidation executions
360 rollback executions
```

Latest result references:

- [../CURRENT_TRUTH_INDEX_20260918.md](../CURRENT_TRUTH_INDEX_20260918.md)
- [../RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md](../RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md)
- [../RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json](../RESULTS/DUAL_MOTHER_PUBLIC_SUMMARY_20260918.json)
- [../RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md](../RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md)

## Evidence policy

```text
PASS
FAIL
INCONCLUSIVE
SUPERSEDED
ROOT CAUSE
REPAIR
RETEST
```

A later PASS does not erase an earlier failure, weak contract or superseded state.

Official evidence should preserve, where applicable:

```text
DECLARED SCOPE
-> FROZEN ACCEPTANCE CRITERIA
-> VERSION / RUN IDENTITY
-> EXECUTION
-> CHECKPOINTS
-> FAILURE / RECOVERY
-> RESULT
-> SANITIZED EXPORT
```

## Major evidence families

### BODY / ISKRA baselines
- [BODY_FROZEN_T0_20260905/README.md](BODY_FROZEN_T0_20260905/README.md)
- [BODY_ISKRA_6X_T0_20260906/README.md](BODY_ISKRA_6X_T0_20260906/README.md)
- [7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md](7BODY_TECHNICAL_READINESS_FINAL_CLOSURE_20260909.md)

### Director / training lineage
- [DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md](DIRECTOR_TRAIN08A_FINAL_CLOSURE_20260909.md)
- [DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md](DIRECTOR_TRAIN08A_REBUILD_INTEGRITY_RECORD_20260909.md)
- [BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md](BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md)

### Runtime / routing / recovery
- [ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md](ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md)
- [RUNTIME_RESTART_20X_20260902.md](RUNTIME_RESTART_20X_20260902.md)
- [TEST5_FINAL_CONVERGENCE_20260903.md](TEST5_FINAL_CONVERGENCE_20260903.md)

### Football World
- [FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md](FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)

## Historical material

This directory intentionally contains older dated evidence. Historical records may describe an earlier status that is no longer current.

Rule:

```text
CURRENT STATUS
= newest dated current-state document

HISTORICAL EVIDENCE
= preserved older record
```

Do not rewrite old evidence to imitate a later state.

## Publication firewall

Public evidence may contain:

```text
protocols
package IDs
SHA256 references
PASS / FAIL / INCONCLUSIVE / SUPERSEDED
sanitized lifecycle / routing state
counts and benchmark summaries
hardware/model context
claim boundaries
lineage
repair/retest chronology
```

It must not intentionally publish:

```text
private SSI source code
private V10 / S10 / Micronetwork / ISKRA / DIRECTOR / ROBERT internals
secrets / tokens
private local paths
raw private memory
private prompts / configuration
operational control endpoints
```

The repository is an evidence mirror, not a source-code distribution.

