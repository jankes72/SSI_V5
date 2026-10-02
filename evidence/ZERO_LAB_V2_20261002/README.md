# ZeroLab V2 — public evidence pack — 2026-10-02

> **Subsequent Final continuation:** [4 PASS / 3 INCONCLUSIVE, then STOPPED_INFRASTRUCTURE](../../RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md). This first-pilot/first-batch pack retains its original measurement scope.

This pack publishes **operator-provided terminal evidence**, with derived structured summaries. It contains no proprietary SSI implementation, private prompts, credentials or private runtime state.

| File | Origin and purpose |
|---|---|
| [pilot_terminal_report.json](pilot_terminal_report.json) | Normalized transcription of the operator-pasted readiness and pilot JSON; preserves the eight reported experiment IDs and receipt hashes |
| [final_resume_operator.log](final_resume_operator.log) | Sanitized uploaded terminal transcript for IPC R2 installation and the seven-case Final batch |
| [final_case_results.csv](final_case_results.csv) | Case outcomes and candidate counts extracted from that transcript |
| [public_summary.json](public_summary.json) | Separate readiness, pilot, offline-test and Final-batch totals with provenance and claim boundaries |
| [publication_manifest.json](publication_manifest.json) | SHA-256 hashes of the four data files above; publication integrity only |

The pilot reported 9/9 services READY and 8/8 executor results PASS, `training_pass=false`, `models_called=0`. Director_Czary is not a separate member of that readiness set.

The Final batch `RUN_DOMAIN_20261002T070948Z_d8652beb` reported `DOMAIN_BATCH_COMPLETE`: 5 PASS, 2 INCONCLUSIVE, 0 FAIL. Both unresolved cases retain `LAB_OUTPUT_MISMATCH`. One passing case required a second candidate. The 19 offline resume tests used synthetic transport.

## Provenance and sanitization

The Final transcript was supplied as an uploaded text file. Its original byte hash and the sanitized transcript hash are retained in `public_summary.json`. The public copy replaces local paths, shell user/host, process IDs and internal progress-stack details with placeholders. It retains result lines, ordering, timings, run/plan identifiers and error reasons. No outcomes were changed.

The pilot JSON was pasted into the conversation separately. Its public file adds a provenance wrapper and normalizes formatting. It is not presented as an original on-disk receipt or signed run artifact.

The original Final `run.json`, signatures and pilot receipt files were not supplied for this publication. Therefore:

- receipt hashes are copied references, not independently recomputed receipt proofs;
- the original signed runtime chain has not been verified by the public checker;
- a publication SHA-256 manifest establishes consistency of exported bytes, not the authenticity of the original execution;
- passing the public checker is not independent experimental replication.

## Checking this export

From the repository root:

```bash
python3 tools/verify_zero_lab_public_evidence.py
```

The checker verifies the export manifest, recounts the seven case outcomes from the log and CSV, checks the eight unique pilot actors and reported receipt-hash format, and enforces the declared evidence boundaries. It is offline and makes no model calls.

The existing CZARA first-cycle data remains a separate evidence family. Do not aggregate its results with this pilot or the selected Final recovery cases.

## Reading path

- [First results and limitations](../../ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Architecture and authority](../../SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md)
- [Current research roadmap](../../CURRENT_RESEARCH_ROADMAP_20261002.md)
- [Historical ZeroLab design](../../CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md)
