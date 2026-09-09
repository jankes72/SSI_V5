# DIRECTOR TRAIN08A — Live Execution Record

**Date:** 2026-09-09  
**Target baseline:** `DIRECTOR_FROZEN_C0`  
**Training package:** `SSI_TRAIN08A_DIRECTOR_FOUNDATION_V1_20260909_REBUILT_FOR_KILO`  
**Planned steps:** `48`  
**Public status:** `IN PROGRESS / INTERRUPTED EXTERNALLY / CONTINUATION STARTED`  
**Final TRAIN08A result:** `NOT YET CLAIMED`

## Purpose of this record

This file is a same-day public record of what actually happened during execution of DIRECTOR TRAIN08A. It is intentionally published before the experiment is complete so that the interruption, executor change and already-produced evidence are not rewritten later as if execution had been uninterrupted.

This is an evidence-oriented status record, not a claim that TRAIN08A has passed in full.

## What was executed

TRAIN08A execution started against the previously identified `DIRECTOR_FROZEN_C0` baseline.

The local execution procedure created and used the following evidence/state surfaces:

```text
state/PRE_RUN_IDENTITY.json
state/PROGRESS.json
evidence/TRAIN08A_EVENTS.jsonl
EVIDENCE/DIRECTOR_FROZEN_C0_FULL.zip
```

The pre-run record identified the frozen baseline, checked key-file hashes and created a full frozen archive before training continued.

The captured execution transcript shows real step-by-step work rather than a single final declaration. Records contain, depending on phase, fields such as:

```text
step_id
module
phase
start_ts
end_ts
elapsed_s
outcome
acceptance_rule
observed_result_summary
model/executor
tool_call_count
evidence_paths
```

Mandatory checkpoints were written every three steps in the captured run.

## Observed partial results before the service interruption

The captured record shows successful completion of the early Foundation modules and their blind-validation phases. In the available transcript:

```text
M01 / steps 01-03 = PASS / checkpoint written
M02 / steps 04-06 = PASS / checkpoint written
M03 / steps 07-09 = PASS / checkpoint written
```

Further recorded work includes dependency/DAG reasoning, schema validation/repair, machine-checked output and entry into the programming/transformation section.

The transcript contains a BLIND_VALIDATION record for step 15 marked `PASS` and then shows execution entering M06, including a machine-executed `run_length_encode` task with visible passing examples.

These are partial execution facts only. They do **not** establish a final `48/48 PASS` result and do **not** establish `DIRECTOR_FOUNDATION_S1`.

## Interruption

The first executor for this run was:

```text
Kiro / kiro-cli / Auto cloud model
```

During the live run, Kiro stopped accepting further requests because the account reached its monthly usage limit. The interruption was therefore external to the DIRECTOR training target and was not triggered by a TRAIN08A acceptance failure.

The execution is **not** being rewritten as uninterrupted.

The historical Kiro-produced evidence is to remain preserved as produced, including any future-discovered `PASS`, `FAIL`, `INCONCLUSIVE`, interruption or recovery records.

## Executor handoff

To avoid waiting for the next Kiro billing/usage cycle, continuation is being handed to:

```text
Kilo
```

The continuation rule is:

```text
DO NOT restart TRAIN08A from step 1
DO NOT erase or rewrite Kiro history
READ state/PROGRESS.json
READ state/PRE_RUN_IDENTITY.json
READ evidence/TRAIN08A_EVENTS.jsonl
RESUME from the authoritative next_step
WRITE an explicit EXECUTOR_HANDOFF / recovery record
CONTINUE under the same acceptance and evidence rules
```

The exact numerical handoff boundary is intentionally not guessed in this public note. The authoritative boundary is the local `state/PROGRESS.json` plus `evidence/TRAIN08A_EVENTS.jsonl` at handoff time. That boundary should be published from the final preserved evidence after Kilo completes or stops.

## Why the executor change does not become a hidden methodology change

The subject being trained remains the same DIRECTOR lineage. The executor/orchestrator changes because of an external service-usage limit.

For the final report, the run must therefore be represented as two auditable execution segments:

```text
SEGMENT A = Kiro
SEGMENT B = Kilo
```

Timing and executor-dependent metrics must not be silently merged. Any speed comparison must preserve the executor/model identity for each segment.

The executor change must not be used to remove, regrade or replace earlier outcomes.

## Claim boundary

At publication time, the strongest supported public statement is:

> DIRECTOR TRAIN08A has begun real execution against the recorded DIRECTOR_FROZEN_C0 baseline. Partial step-level evidence and checkpoints exist. Execution was interrupted by exhaustion of Kiro's monthly usage allowance and is being continued by Kilo from preserved state. The final 48-step result is not yet known and no DIRECTOR_FOUNDATION_S1 completion claim is made.

Not claimed:

```text
TRAIN08A = COMPLETE
TRAIN08A = 48/48 PASS
DIRECTOR_FOUNDATION_S1 = CREATED / VALIDATED
TRAIN08B = STARTED
executor-independent speed equivalence between Kiro and Kilo
```

## Public-source boundary

This repository remains a public research/evidence mirror. This record documents procedure, state transitions, results and claim boundaries. Proprietary implementation source and private operational code are not required for this public status record.

## Next publication step

After Kilo continuation closes or reaches a genuine blocker, publish a final TRAIN08A execution record containing at minimum:

```text
exact Kiro -> Kilo handoff boundary
steps completed / 48
PASS count
FAIL count
INCONCLUSIVE count
all interruption/recovery records
checkpoint consistency result
PROGRESS.json vs event-log consistency result
final evidence integrity references
whether DIRECTOR_FOUNDATION_S1 may legitimately be claimed
```

Until then, this file is the canonical public same-day interruption/handoff record for DIRECTOR TRAIN08A.
