# SSI Final — continuation stopped after seven cases — 2026-10-02

**Run:** `RUN_DOMAIN_20261002T181736Z_f600e74c`  
**Plan:** `DUP_01fe5854e782f647a46351d1`  
**Final runner status:** `STOPPED_INFRASTRUCTURE`  
**Source:** operator-uploaded terminal transcript. Original `run.json`, runtime receipts and signatures were not supplied or independently verified for this publication.

The continuation closed **7 cases: 4 PASS, 3 INCONCLUSIVE, 0 FAIL**, then stopped. The requested limit of 622 was a maximum for the invocation, not a count of completed cases. The starting queue was 614.

The final ISKRA6 case first produced a candidate with `LAB_OUTPUT_MISMATCH`. Its second candidate attempt then reported `NO_CANDIDATE_GENERATED` and `INVALID_WORKER_JSON`. The runner retained INCONCLUSIVE and stopped instead of continuing the queue.

## Case results

| Actor | Case | Final result | Logged reason or outcome |
|---|---|---|---|
| ISKRA2 | S21-01-02 | INCONCLUSIVE | `LAB_EXPRESSION_SHAPE`; tier limit reached |
| ISKRA3 | S22-01-03 | PASS | First candidate verified |
| ISKRA3 | S23-01-01 | INCONCLUSIVE | `LAB_OPERATION_FIELDS:merge:missing=[]:extra=["input_blocks"]`; tier limit reached |
| ISKRA5 | S24-01-01 | PASS | First candidate verified |
| ISKRA3 | S25-01-01 | PASS | First candidate verified |
| ISKRA2 | S26-01-01 | PASS | First candidate verified |
| ISKRA6 | S20-01-01 | INCONCLUSIVE | Candidate 1 output mismatch; candidate 2 invalid/unavailable; runner stopped |

The final case also retained `unparseable_json`, `contract_binding:NO_CANDIDATE_TO_VALIDATE:$` and `rnd_lab_comparison_not_verified`. The event classifier was `VERIFIER_OR_TRANSPORT_UNAVAILABLE`; this is a reported classification, not proof of a provider outage or a specific transport root cause. No `INFLIGHT_LIMIT` explanation is established by this transcript.

## Continuation chronology

| Published observation | Closed cases | PASS | INCONCLUSIVE | FAIL | Runner status |
|---|---:|---:|---:|---:|---|
| Earlier batch: `RUN_DOMAIN_20261002T070948Z_d8652beb` | 7 | 5 | 2 | 0 | DOMAIN_BATCH_COMPLETE |
| This later batch: `RUN_DOMAIN_20261002T181736Z_f600e74c` | 7 | 4 | 3 | 0 | STOPPED_INFRASTRUCTURE |
| Sum of these two distinct case sets | 14 | 9 | 5 | 0 | Not a whole-programme verdict |

Both logs identify the same plan and contain distinct actor/case pairs. This permits recounting their published outcomes together, while retaining their separate run identities. The original historical 1,326-case snapshot is not rewritten or merged into a new qualification score.

The observed queue of 614 confirms the boundary after the earlier batch. Subtracting seven closed cases yields **607**, an arithmetic remainder rather than an observed subsequent queue query. No claim is made about the live process state after the supplied log or later recovery.

## What the log establishes

- All seven Final runtime status checks reported RUNNING; the gateway and Director status checks succeeded before dispatch.
- The ZeroLab readiness preflight reported seven Final executors and Director ready, with no models called by that check.
- Six cases were closed before the final ISKRA6 case; four of those six passed and two remained inconclusive.
- The final case closed INCONCLUSIVE and the runner emitted `STOP_RUN`, followed by `STOPPED_INFRASTRUCTURE`.

The zero-call preflight messages are not the live batch's total model usage. Total paid cost and model-call counts are not established by this transcript.

## Current boundary and next diagnostic target

The terminal log shows invalid or unavailable candidate data at the stop, but it cannot identify whether the underlying cause is model output, response truncation, parsing, transport or another dependency. The next useful diagnostic artifact is the preserved final candidate/transport record linked to this run, together with the contract/reviewer error context. A repair or successful replay is not claimed here.

The recovery runner retains `full_stage_acceptance=false` and `automatic_stage_consolidation=false`. This stop does not change the separate **8/8 local ZeroLab pilot** or the completed first CZARA curriculum. Readiness alone does not prove that these training cases executed through ZeroLab.

## Public evidence

- [Sanitized transcript, CSV, full case-event chronology and hashes](../evidence/SSI_FINAL_RECOVERY_20261002T181736Z/README.md)
- [Machine-readable summary](../evidence/SSI_FINAL_RECOVERY_20261002T181736Z/summary.json)
- [Earlier ZeroLab pilot and first Final batch](../ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Current CZARA status](../CZARA_CURRENT_STATUS.md)
- [Current research roadmap](../CURRENT_RESEARCH_ROADMAP_20261002.md)

The public checker validates export integrity, chronology and counts. It does not authenticate unavailable runtime signatures or reproduce the private execution.
