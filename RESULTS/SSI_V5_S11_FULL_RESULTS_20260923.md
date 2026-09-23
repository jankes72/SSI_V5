# SSI V5 — complete recorded S11 results — 23 September 2026

**Run:** `RUN_20260922T221012Z_88df9df1`  
**Run status:** `COMPLETED_WITH_FAILURES`  
**S11 status:** `INCONCLUSIVE`  
**Scope:** software training/evaluation; seven BODY, 30 cases each.

The completed traversal records **197 PASS, 12 INCONCLUSIVE and 1 FAIL out of 210 cases** (93.81% recorded PASS). All outcomes, including unresolved cases, are published in the [complete outcome set](../evidence/S11_20260923/README.md), [CSV](../evidence/S11_20260923/cases.csv) and [JSON](../evidence/S11_20260923/cases.json). This is completion of case traversal, not successful acceptance of S11.

## Results by BODY

| BODY | PASS | INCONCLUSIVE | FAIL |
|---|---:|---:|---:|
| BODY_FROZEN | 29 | 1 | 0 |
| ISKRA1 | 28 | 2 | 0 |
| ISKRA2 | 28 | 2 | 0 |
| ISKRA3 | 29 | 1 | 0 |
| ISKRA4 | 27 | 3 | 0 |
| ISKRA5 | 28 | 2 | 0 |
| ISKRA6 | 28 | 1 | 1 |
| **Total** | **197** | **12** | **1** |

Execution began at 22:10:12 UTC on 22 September and ended at 02:35:13 UTC on 23 September. These timestamps describe the run, not per-model latency. Role prompting was enabled, previous memory was retained, and S10 ancestry was explicitly inherited rather than freshly rerun in this installation. This was not a controlled experiment isolating feelings, learning, role prompts or model-routing effects.

Research flow retained local FAIL/INCONCLUSIVE outcomes and continued independent cases. All **29 stages S12–S40 were DEFERRED_PREREQUISITE**, with zero model calls recorded for those stages. They were not executed. See [all stage dispositions and original aggregate metrics](../evidence/S11_20260923/stage_results.json).

## Every unresolved final case

| BODY | Case | Recorded result | Reason |
|---|---|---|---|
| BODY_FROZEN | S11-05-06 | INCONCLUSIVE | LAB_NONSTRING |
| ISKRA1 | S11-04-06 | INCONCLUSIVE | UNRELATED_EDGE_CHANGED |
| ISKRA1 | S11-05-06 | INCONCLUSIVE | LAB_CONCAT_INPUTS |
| ISKRA2 | S11-05-02 | INCONCLUSIVE | LAB_NONSTRING |
| ISKRA2 | S11-05-04 | INCONCLUSIVE | LAB_OPERATION_FIELDS:b11:missing=[]:extra=["input_blocks"] |
| ISKRA3 | S11-05-05 | INCONCLUSIVE | LAB_NONSTRING |
| ISKRA4 | S11-04-03 | INCONCLUSIVE | UNRELATED_EDGE_CHANGED |
| ISKRA4 | S11-05-01 | INCONCLUSIVE | LAB_CONCAT_INPUTS |
| ISKRA4 | S11-05-06 | INCONCLUSIVE | LAB_NONSTRING |
| ISKRA5 | S11-05-01 | INCONCLUSIVE | LAB_OUTPUT_OR_REPEATABILITY_MISMATCH |
| ISKRA5 | S11-05-06 | INCONCLUSIVE | LAB_NONSTRING |
| ISKRA6 | S11-04-03 | FAIL | {"code": "FAULT_ANALYSIS_NOT_OBSERVED", "path": "$.fault_analysis"} |
| ISKRA6 | S11-05-05 | INCONCLUSIVE | LAB_NONSTRING |

Six final cases rejected non-string input, two lacked concat inputs, one placed operation fields incorrectly, two failed locality preservation, one failed the output comparison and one contradicted the observed fault. The two locality cases changed descriptive `reason` metadata on otherwise unchanged edges; they were not topology failures. The strict contract still rejected those changes. The fault case omitted a supplied sandbox observation of a jam.

## What the additional failure reports established

Thirty full LAB reports cover three candidate attempts in each of ten unresolved S11-05 cases. Replaying them against the unchanged interpreter reproduced their verdicts, issues, test outputs and binding hashes; timing fields were excluded. This is a selected failure sample, not a 0% pass rate for the training run.

| Candidate rejection | Reports |
|---|---:|
| Non-string input | 15 |
| Output/repeatability mismatch | 6 |
| Missing concat inputs | 4 |
| Operation field placement | 3 |
| Invalid graph edge | 2 |

Fifteen runtime exceptions lost the failing test/block/input context in the original report. Together with nine compile/graph failures, **24 of 30 reports provided no failed test row or feedback example**. Four consecutive candidate pairs had the same canonical answer hash across tiers. These findings motivated the R3 diagnostics and no-progress detection; they do not show that model weights learned from a prior failure. The [replay audit](../evidence/S11_20260923/lab_failure_replay.json) preserves the checks without publishing candidate code.

## Response implemented after this run

The private `SSI_V5_LAB_RND_FIX_20260923_R3` package adds detailed execution diagnostics shared by training and registered R&D comparisons, immutable failure fixtures for replay, and detection of unchanged rejected candidates. It keeps the original interpreter, native evaluator, thresholds and historical grades. The intended retry selects the 13 actor-specific unresolved cases after locally revalidating the 197 earlier PASS records; later stages still require accepted prerequisites.

R3 offline validation reports **106 tests: 105 passed and one skipped**. The skipped test concerns a separate-UID signing custodian because Unix sockets were unavailable in the preparation environment. Model/reviewer responses used explicit fixtures, and no paid training or physical pilot ran during this validation. The 197/13 selection test used fixtures; the actual 197 full PASS responses were not provided. See [release summary](SSI_V5_LAB_RND_R3_TEST_SUMMARY_20260923.json) and [every test result](../evidence/S11_20260923/release_test_results.json).

The package raises the existing shared daily model budget from 3 USD to **6 USD across all seven BODY**, preserving spend and reservations. The historical run used the former limit. No complete usage ledger was supplied, so actual spend and savings are not estimated. **Delivery and offline validation of R3 are established; installation on the operator's machine and a post-R3 training result are not yet confirmed.**

## Evidence scope

The upload contains all 210 indexed outcomes and stage aggregates, full case records for the 13 unresolved cases, and 30 failed LAB reports. All uploaded file hashes match their manifest. Full PASS responses were not uploaded, the collector reports `evidence_verified=false`, and the run's signing mode is `LOCAL_DEVELOPMENT`, with `external_pilot_ready=false` and no external timestamp. These facts are retained in the [summary](../evidence/S11_20260923/summary.json).

Historical aggregate metrics and rule checks are published as recorded, even where a favorable metric coexists with unresolved cases. New measurement controls were introduced after this run; they do not retroactively establish that every earlier guard was exercised. There is no independent external replication or hardware validation in this update.

## Related updates

- [DEV feedback, adversarial evidence tests and measurement controls](SSI_V5_DEV_SAFEGUARDS_20260923.md).
- [UAV and R&D laboratory implementation and deployment status](../SYSTEM/SSI_V5_UAV_AND_RND_LABS_20260923.md).
- [Earlier 22 September continuation excerpt](SSI_V5_LAB_AND_S11_CONTINUATION_20260922.md), preserved as a different run.
