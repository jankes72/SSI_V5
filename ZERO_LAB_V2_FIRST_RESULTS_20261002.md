# ZeroLab V2 — first runtime results and SSI Final recovery batch

**Date:** 2026-10-02  
**Version:** `SSI_ZERO_LAB_V2_20261002`  
**Evidence:** operator-provided terminal output; public export consistency can be checked locally. Original runtime receipts and the signed Final run bundle have not been independently reverified for this publication.

ZeroLab V2 reached **9/9 checked services READY** and completed its first **8/8 PASS local-data pilot**. A separate post-repair SSI Final batch then completed seven selected recovery cases: **5 PASS, 2 INCONCLUSIVE, 0 FAIL**.

These are three different measurements:

| Measurement | Observed result | What it establishes |
|---|---|---|
| Resume IPC R2 offline tests | 19/19 PASS; synthetic transport; 0 model calls | Regression checks for the resume/install path |
| ZeroLab local pilot | 8/8 executor results PASS; 0 model calls | Execution of the demonstration through the installed local ZeroLab routes |
| SSI Final recovery batch | 5 PASS / 2 INCONCLUSIVE / 0 FAIL | A completed seven-case batch in the existing training runner after installation |

The counts are not combined into one benchmark score. ZeroLab readiness before the Final batch does not establish that its seven training cases executed through ZeroLab.

## What ZeroLab adds

ZeroLab turns an experiment request into a versioned, executable local software protocol when sufficient inputs and a supported adapter exist. The Director identifies the objective, BODY checks missing inputs, and the protocol's criteria remain separate from the candidate method. Missing resources or measurements stay explicit.

The same engine serves two separate scopes:

| Scope | Director | Executors |
|---|---|---|
| CZARA | Director_Czary | BODY_FROZEN_1_0 |
| FINAL | Director_Final | BODY_FROZEN and ISKRA1–ISKRA6 |

Czara can observe authorized research conversation and prepare shadow alternatives. A professor/operator selects any change to the main direction, which creates a new main execution rather than relabeling a shadow result. This workflow is implemented in the reviewed source; the pilot below tests a narrower local execution path.

See [architecture and authority](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md). The [2026-10-01 LAB_ARCHITECT definition](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md) remains the historical, broader research design.

## First ZeroLab pilot

The operator ran the installed startup check and local pilot. All eight executors and Director_Final reported the same V2 version. Director_Czary was not a separate member of this nine-service readiness check.

```text
READINESS = 9 / 9 READY
PILOT EXECUTORS = 8 / 8 PASS
SCOPE = DEMONSTRATION_LOCAL_DATA_ONLY
training_pass = false
models_called = 0
```

The reviewed pilot fixture uses local record ordering with a baseline, an empty-input control and an out-of-order example, configured for two repetitions. It exercises the record-transformation adapter. It is not a held-out research benchmark, a micronetwork-adapter performance result or a hardware experiment.

Reported executor results:

| Executor | Pilot result |
|---|---|
| BODY_FROZEN_1_0 | PASS |
| BODY_FROZEN | PASS |
| ISKRA1 | PASS |
| ISKRA2 | PASS |
| ISKRA3 | PASS |
| ISKRA4 | PASS |
| ISKRA5 | PASS |
| ISKRA6 | PASS |

The public [pilot report](evidence/ZERO_LAB_V2_20261002/pilot_terminal_report.json) preserves all eight experiment IDs and operator-reported receipt hashes. These hashes are references copied from the terminal output; the original receipt files were not supplied to this publication and their hashes were not recomputed.

## First post-repair Final batch

Run: `RUN_DOMAIN_20261002T070948Z_d8652beb`  
Plan: `DUP_01fe5854e782f647a46351d1`  
Final runner status: `DOMAIN_BATCH_COMPLETE`

| Actor | Case | Final result | Candidate history shown in the log |
|---|---|---|---|
| ISKRA2 | S21-01-01 | INCONCLUSIVE | `LAB_OUTPUT_MISMATCH`; stopped at tier limit |
| ISKRA1 | S22-01-03 | PASS | First candidate verified |
| ISKRA1 | S23-01-01 | PASS | First candidate mismatched; second candidate verified |
| ISKRA4 | S24-01-01 | PASS | First candidate verified |
| BODY_FROZEN | S25-01-01 | PASS | First candidate verified |
| ISKRA1 | S26-01-01 | PASS | First candidate verified |
| ISKRA5 | S20-01-01 | INCONCLUSIVE | `LAB_OUTPUT_MISMATCH`; stopped at tier limit |

Both unresolved cases retain `rnd_lab_comparison_not_verified`. The batch finished without the infrastructure-stop condition seen in earlier attempts. One local candidate revision succeeded; this is not evidence of general performance improvement or cross-agent learning.

The queue was 621 before the batch. Subtracting seven closed attempts gives **614 remaining at that boundary**; this is derived arithmetic, not a later queue-status observation. Closed INCONCLUSIVE attempts are preserved, not silently retried or promoted to PASS. No result from the subsequently requested continuation is included here.

The log's zero-call preflight messages apply to those checks. Total model calls and paid cost for the live training batch are not established by the supplied transcript. The reported configuration was one capacity slot for CZARA/Director_Czary/BODY 1.0 and another for Director_Final/Final BODY/Iskras, under a shared USD 6/day budget.

## Repair and retest context

Earlier installed files were newer than the running processes; those processes returned unknown-action responses for ZeroLab. After the operator's reboot and startup, the V2 readiness and pilot checks passed.

The initial resume checks also hit short status-read timeouts. IPC R2 permits bounded status reads up to 30 seconds while retaining process ownership, profile and RUNNING-status checks. The retest recorded several healthy status responses taking 3.88–7.87 seconds. The 19 offline tests used synthetic transport and are separate from the live batch results. This change concerns readiness checks, not a blanket retry of paid training requests.

The earlier [operator-stop and repair record](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md) remains preserved. The new seven-case batch does not replace its historical 848 PASS / 470 INCONCLUSIVE / 8 FAIL snapshot.

## Consolidation and acceptance boundary

The selected S20-S26 recovery runner declares `full_stage_acceptance=false` and `automatic_stage_consolidation=false`. The ordinary full-stage Final workflow has a separate verified-subset consolidation path; that does not turn this recovery batch into a stage consolidation.

There is no evidence here of automatic joint consolidation after every case across Czara, Director_Czary, Director_Final, BODY_FROZEN_1_0 and Final actors. A common engine, storage or budget does not establish shared learned state.

This publication establishes bounded local software results. It does not establish completed S20-S40 training, complete professor-chat/shadow/promotion validation, new learned-skill qualification from the pilot, physical validation or independent external replication.

## Evidence and verification

- [Public evidence pack and provenance](evidence/ZERO_LAB_V2_20261002/README.md)
- [Machine-readable public summary](evidence/ZERO_LAB_V2_20261002/public_summary.json)
- [Seven case outcomes](evidence/ZERO_LAB_V2_20261002/final_case_results.csv)
- [Sanitized operator transcript](evidence/ZERO_LAB_V2_20261002/final_resume_operator.log)
- [Current roadmap](CURRENT_RESEARCH_ROADMAP_20261002.md)

From a repository checkout, run `python3 tools/verify_zero_lab_public_evidence.py`. It checks export hashes, recounts the transcript/CSV and verifies the published scope boundaries. It does not call models, execute SSI, verify unavailable runtime signatures or independently reproduce the experiments.
