# S11 public outcome set — 23 September 2026

Run: `RUN_20260922T221012Z_88df9df1`. All **210 recorded outcomes** are included. There are **197 PASS, 12 INCONCLUSIVE and 1 FAIL**. Stage S11 remained INCONCLUSIVE; the run finished as COMPLETED_WITH_FAILURES.

## Files and verification scope

- [cases.csv](cases.csv) and [cases.json](cases.json): every actor/case outcome and original report hash.
- [summary.json](summary.json): totals, per-BODY counts, provenance and limits.
- [stage_results.json](stage_results.json): all reported S11 actor metrics/rules, plus every S12–S40 deferral.
- [unresolved_cases.json](unresolved_cases.json): all 13 final non-PASS outcomes and recorded reasons.
- [lab_failure_replay.json](lab_failure_replay.json): replay checks for the 30 supplied failed LAB candidates; selected failure sample.
- [release_test_results.json](release_test_results.json): separate R3 offline test list, 105 PASS and 1 SKIPPED.
- [SHA256SUMS.txt](SHA256SUMS.txt): hashes of this public export and the accompanying dated reports.

The supplied collection contains the complete outcome index and aggregate stage reports, but full raw case records for only the 13 unresolved cases. The 197 PASS case hashes are collector-reported; their full responses were not uploaded or independently revalidated here. The local installer must verify them before reuse. All supplied source file bytes match the collection manifest; its `evidence_verified` field is **false**. Byte consistency is not independent authentication. The run records LOCAL_DEVELOPMENT trust and no external timestamp.

This public export excludes private prompts, raw candidate programs, source code, credentials and operational paths. It permits recomputing totals and auditing published test claims; it is not sufficient to independently rerun the proprietary evaluator. Later repairs do not rewrite this history.

## Complete outcome matrix

| Case | BODY_FROZEN | ISKRA1 | ISKRA2 | ISKRA3 | ISKRA4 | ISKRA5 | ISKRA6 |
|---|---|---|---|---|---|---|---|
| S11-01-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-01-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-01-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-01-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-01-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-01-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-02-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-03-06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-04-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-04-02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-04-03 | PASS | PASS | PASS | PASS | INCONCLUSIVE | PASS | FAIL |
| S11-04-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-04-05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-04-06 | PASS | INCONCLUSIVE | PASS | PASS | PASS | PASS | PASS |
| S11-05-01 | PASS | PASS | PASS | PASS | INCONCLUSIVE | INCONCLUSIVE | PASS |
| S11-05-02 | PASS | PASS | INCONCLUSIVE | PASS | PASS | PASS | PASS |
| S11-05-03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| S11-05-04 | PASS | PASS | INCONCLUSIVE | PASS | PASS | PASS | PASS |
| S11-05-05 | PASS | PASS | PASS | INCONCLUSIVE | PASS | PASS | INCONCLUSIVE |
| S11-05-06 | INCONCLUSIVE | INCONCLUSIVE | PASS | PASS | INCONCLUSIVE | INCONCLUSIVE | PASS |

