# SSI Final — stopped continuation evidence

**Run:** `RUN_DOMAIN_20261002T181736Z_f600e74c`  
**Plan:** `DUP_01fe5854e782f647a46351d1`  
**Result:** `STOPPED_INFRASTRUCTURE`; 4 PASS / 3 INCONCLUSIVE / 0 FAIL across seven closed cases.

| File | Purpose |
|---|---|
| [operator.log](operator.log) | Sanitized operator-uploaded terminal transcript |
| [cases.csv](cases.csv) | Seven case outcomes, final event reasons and candidate counts |
| [case_events.json](case_events.json) | Candidate and training-event chronology, including the final two-candidate sequence |
| [summary.json](summary.json) | Counts, identity, queue observation, stop condition and evidence boundaries |
| [publication_manifest.json](publication_manifest.json) | SHA-256 integrity references for the four exported data files |

The source text contained the completed stop message and returned shell prompt. This is a stopped-run observation, not a claim that the 622 requested maximum cases or the whole 614-case starting queue were completed.

## Provenance

The original uploaded file's SHA-256 and the public sanitized log's SHA-256 are retained in the summary. Sanitization replaces the user's local paths, shell identity, process IDs and internal progress-stack details. Case identities, verdicts, error reasons, ordering and timing markers remain intact.

No original `run.json`, receipt files or signed runtime evidence bundle were supplied for this export. Its hash manifest checks exported bytes; it is not an independent signature or proof of runtime authenticity. The published totals can be independently recounted from the terminal transcript, but the experiment has not been independently reproduced.

The first case ended with `LAB_EXPRESSION_SHAPE`; another had an unsupported `input_blocks` field for `merge`. The final case's first candidate had `LAB_OUTPUT_MISMATCH`; its second had `NO_CANDIDATE_GENERATED` / `INVALID_WORKER_JSON`, followed by `STOP_RUN`. All remain visible.

## Offline consistency check

From the repository root:

```bash
python3 tools/verify_final_recovery_public_evidence.py
```

This recounts the transcript, CSV and event JSON, verifies hashes and reported stop semantics, and checks that the two published recovery case sets are distinct. It does not call models or run SSI.

- [Result and limitations](../../RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md)
- [Earlier batch and ZeroLab pilot evidence](../ZERO_LAB_V2_20261002/README.md)
- [Current CZARA status](../../CZARA_CURRENT_STATUS.md)
