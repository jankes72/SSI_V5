# SSI V5 — Codex canonical local training execution method

**Recorded:** `2026-09-10`  
**Status:** `METHOD ADOPTED / FIRST BODY_FROZEN LIVE RUN IN PROGRESS`  
**Scope:** `BODY / ISKRA controlled training execution`  
**Final BODY_FROZEN TRAIN01A result:** `NOT YET CLAIMED`

This record documents the transition of controlled BODY/ISKRA training execution to a Codex-driven local procedure that exercises the real running BODY through its canonical local control path rather than treating the training package as an offline checklist.

The purpose of this change is stronger execution provenance: the executor prepares and supervises the run, while the tested BODY remains the system that receives the training tasks, routes them through its live runtime and produces the responses that are preserved as evidence.

## Why this method was adopted

Earlier execution attempts exposed two infrastructure problems before the first valid TRAIN01A step could be credited:

```text
1. local runtime / launch-context mismatch and stale IPC observations
2. executor process-lifecycle limit shorter than the live CHAT fallback window
```

Both were preserved as historical evidence rather than converted into BODY failures.

The live BODY runtime and canonical local IPC were then independently rechecked. Status, CONTINUUM, Micronetwork and capability queries returned through the real running BODY. A separate local status round-trip confirmed the complete local control transport.

The remaining issue was executor lifecycle: a normal Codex shell call could terminate before a long synchronous BODY CHAT request completed. A normal background child process was also not sufficiently durable.

The adopted solution is a durable **user-level system supervisor** for the long-running training execution. Codex creates, starts, inspects and audits that supervisor, while the supervisor remains alive independently of the duration of a single Codex turn.

This is an execution-infrastructure recovery. It is not a modification of the tested BODY competence.

## Canonical execution sequence

For controlled BODY/ISKRA training, the preferred execution sequence is now:

```text
FROZEN / HASH-IDENTIFIED TRAINING PACKAGE
-> VERIFY PACKAGE IDENTITY
-> VERIFY TARGET START STATE / T0 LINEAGE
-> START ONLY THE DECLARED TARGET BODY THROUGH ITS CANONICAL LOCAL LAUNCHER
-> VERIFY LIVE RUNTIME + LOCAL IPC + CONTINUUM + MICRONETWORK AVAILABILITY
-> START DURABLE LOCAL TRAINING SUPERVISOR
-> SEND REAL TASK TO REAL BODY THROUGH AUTHORIZED LOCAL ROOT PATH
-> WAIT FOR REAL BODY RESPONSE / DECLARED FALLBACK COMPLETION
-> PRESERVE RAW INPUT + RAW OUTPUT + ROUTE/PROVENANCE + TIMING
-> APPLY PREDECLARED ACCEPTANCE RULE
-> RECORD PASS / FAIL / INCONCLUSIVE
-> CHECKPOINT
-> CONTINUE TO NEXT STEP
-> FINAL GATE
-> VERSIONED DESCENDANT STATE ONLY IF THE DECLARED GATE PASSES
```

A supervisor start is not itself evidence that a training step passed. A step result exists only after a real BODY response or a formally classified execution outcome has been preserved.

## Executor / target separation

The roles are deliberately separated:

```text
CODEX
= procedural executor / local supervisor / evidence recorder

DURABLE LOCAL SUPERVISOR
= process-lifecycle wrapper for long-running requests and resume

BODY_FROZEN / BODY_ISKRA
= tested target runtime

ROUTER V10 / MICRONETWORKS / CONTINUUM / LIVE BACKENDS
= target-side runtime mechanisms whose reported use is preserved where exposed
```

Codex is not represented as an independent scientific validator and must not manufacture a BODY answer, silently repair a failed result or rewrite acceptance criteria after seeing the output.

## Blind-validation rule

The Foundation Golden Master methodology is preserved.

For each declared blind validation, the executor may instantiate a fresh task inside the declared competence family, but it must freeze the test before exposing it to the BODY:

```text
CREATE FRESH BLIND CASE
-> RECORD TASK
-> RECORD ACCEPTANCE CRITERIA
-> RECORD EXPECTED PROPERTIES
-> HASH / FREEZE CASE
-> SEND TO BODY
-> PRESERVE BODY RESPONSE
-> EVALUATE ONLY AGAINST THE PRE-FROZEN CRITERIA
```

The blind case or acceptance rule must not be changed after the BODY response is known.

## Long-running execution and resume

A training run may outlive a single Codex turn. Therefore the durable supervisor is required to preserve execution continuity.

The run must be resumable from evidence and checkpoint state rather than from chat memory:

```text
PROGRESS
+ STEP EVIDENCE
+ CHECKPOINTS
+ RAW RUNTIME OUTPUT
= RESUME SOURCE OF TRUTH
```

If Codex reconnects later, completed steps are not repeated merely because a new interactive turn started. The executor resumes from the first genuinely unfinished step.

A normal timeout, backend delay or executor-turn ending must not be silently converted into a BODY `FAIL`.

## Current hardware constraint is part of the evidence context

The first BODY_FROZEN Foundation execution under this method is intentionally running on a materially smaller local node than the previously executed Director Foundation reference.

Current BODY_FROZEN execution context:

```text
RAM = 8 GB
GPU VRAM = 4 GB
LOCAL MODEL CLASS = approximately 4B
```

Previously used stronger Director-side local context included:

```text
RAM = 16 GB
GPU VRAM = 6 GB
LOCAL MODEL CLASS = approximately 7B
```

This difference is useful as an engineering stress condition because the same Foundation competence family can be observed under different resource/model constraints.

However, hardware/model differences are **not** by themselves proof that Router V10 is better or worse, and a routing difference between nodes cannot automatically be attributed to hardware. Possible causes must remain separated, including target configuration, local model capability, backend availability, resource pressure and Router V10 classification behavior.

## Evidence requirements

For each executed step, the public-safe evidence model should preserve, where available:

```text
STEP ID
MODULE / PHASE
TARGET IDENTITY
INPUT HASH
RAW RESPONSE HASH
START / END TIME
ELAPSED TIME
REPORTED ROUTE / BACKEND / PROVENANCE
ACCEPTANCE RULE ID
PASS / FAIL / INCONCLUSIVE
RECOVERY / RETRY HISTORY
CHECKPOINT REFERENCE
```

Private source, credentials, secrets, reconstructive internal configuration and unsafe infrastructure details remain outside the public repository.

## Current BODY_FROZEN TRAIN01A boundary

The first BODY_FROZEN run using this execution method is currently an **open live run**.

The repository does not claim its final result in advance.

Historical infrastructure interruptions and inconclusive observations remain part of the evidence chain. A later PASS, if achieved, does not erase those events.

The valid lineage remains:

```text
BODY_FROZEN_T0
-> TRAIN01A FOUNDATION / LIVE EXECUTION
-> BODY_FROZEN_FOUNDATION_S1 ONLY IF FINAL GATE PASSES
```

## Adoption for subsequent BODY / ISKRA packages

This Codex + durable-local-supervisor method is now the preferred canonical execution procedure for the upcoming controlled BODY/ISKRA training packages unless a later execution-method version is explicitly recorded before use.

Each target still requires its own:

```text
target identity
canonical launcher binding
start-state verification
package/hash verification
live-runtime verification
evidence chain
PASS / FAIL / INCONCLUSIVE closure
```

No result from BODY_FROZEN may be copied to an ISKRA line by inference.

## Claim boundary

This execution-method record establishes a **procedure**, not a successful training result.

It does not claim that:

- BODY_FROZEN TRAIN01A has already passed;
- any ISKRA Foundation run has passed;
- the smaller hardware node is scientifically superior or inferior;
- Router V10 caused every route difference observed across machines;
- Codex is an independent external validator;
- a durable supervisor changes or improves BODY competence;
- local execution evidence alone establishes production readiness, AGI, consciousness or universal transfer.

The intended standard is:

> Run the declared package against the real target, keep the target and executor roles separate, preserve the complete failure/recovery chronology, and make the result claim only after the final gate actually closes.