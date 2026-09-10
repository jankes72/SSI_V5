# SSI V5 — Sequential BODY/ISKRA Training to S3

**Recorded:** `2026-09-10`  
**Status:** `ACTIVE EXECUTION PROTOCOL / BODY_FROZEN S1 CLOSED / S3 QUEUE PREPARED`  
**Scope:** `BODY_FROZEN + 6 BODY ISKRA lines`  
**Current stopping point:** `S3`  
**Public boundary:** `evidence-only / sanitized / no proprietary implementation source`

This document records the canonical execution process for bringing the seven controlled BODY lines to the same pre-experiment maturity level `S3`.

It is an execution and evidence protocol. It does not publish SSI V5 implementation source, Router V10 source, Micronetwork source, private ISKRA internals, credentials, private prompts or reconstructive runtime details.

## 1. Current state

The seven-line technical-readiness gate is already closed in its declared scope:

```text
7-BODY TECHNICAL READINESS = 7/7 PASS
COMMON MATRIX = 147/147 PASS
```

`BODY_FROZEN` has now completed TRAIN-A Foundation:

```text
BODY_FROZEN T0
-> TRAIN01A FOUNDATION
-> FINAL_GATE = PASS
-> 48/48 = PASS
-> BLIND_VALIDATIONS = 16/16 determinate PASS
-> CHECKPOINTS = 16/16
-> T0_INTEGRITY = PASS
-> BODY_FROZEN_FOUNDATION_S1 = CREATED
```

S1 identity:

```text
BODY_FROZEN_FOUNDATION_S1
SHA256 = ed1331e38909db829859ca377e9858ee42fe5528537cf6c9c6d2a5ecc5e253e9
```

The earlier INCONCLUSIVE and FAIL records from TRAIN01A remain preserved as historical evidence. The final S1 result does not erase them.

## 2. Canonical execution order

Training is intentionally sequential by BODY line. The project does not execute Phase A across all bodies first and then Phase B across all bodies.

The canonical order is:

```text
01 BODY_FROZEN
   S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

02 BODY_ISKRA1_NICE
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

03 BODY_ISKRA2_GUARDIAN
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

04 BODY_ISKRA3_JUSTICE
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

05 BODY_ISKRA4_EXPLORER
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

06 BODY_ISKRA5_PRAGMATIST
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY

07 BODY_ISKRA6_SKEPTIC
   T0 -> TRAIN-A -> S1 -> TRAIN-B -> S2 -> TRAIN-C -> S3 -> STOP BODY
```

Only after one BODY reaches a terminal S3 outcome, or is safely marked blocked under the rules below, does execution advance to the next BODY.

## 3. Current research boundary: stop at S3

The active queue deliberately stops at `S3`.

```text
TRAIN-A FOUNDATION -> S1
TRAIN-B LEGO + MICRONETWORK + V10 PRACTICUM -> S2
TRAIN-C CHILD / APPLIED AUTONOMY -> S3
STOP
```

The current queue does **not** authorize:

```text
TRAIN-D
TRAIN-E
S4
S5
held-out mechanism tests
21 cross-domain experiments
post-21 consolidation
```

Those stages remain future work and require a separate owner decision and applicable predeclaration.

## 4. One local queue ZIP per BODY

For operational efficiency, the prepared execution layout uses one local queue archive per BODY rather than forcing the executor to repeatedly rediscover stage packages.

The public repository records only package names and integrity hashes. The executable/local package payloads remain outside this public evidence mirror.

```text
01 SSI_S3_QUEUE_01_BODY_FROZEN_ONE_ZIP_V1_20260910.zip
   SHA256 = 1f3da18544d322ef1723d91858944090baa02b6677836ce82298485f0ad88737
   stages = TRAIN-B + TRAIN-C

02 SSI_S3_QUEUE_02_ISKRA1_NICE_ONE_ZIP_V1_20260910.zip
   SHA256 = 070894d16cebcd3ff44971f2df465c305cc79260cfc7e44a218fa76a533d6e4f
   stages = TRAIN-A + TRAIN-B + TRAIN-C

03 SSI_S3_QUEUE_03_ISKRA2_GUARDIAN_ONE_ZIP_V1_20260910.zip
   SHA256 = e9261eeeebe165c99091b88a077ad2439e46ccfc5a33339c33004dde69046137
   stages = TRAIN-A + TRAIN-B + TRAIN-C

04 SSI_S3_QUEUE_04_ISKRA3_JUSTICE_ONE_ZIP_V1_20260910.zip
   SHA256 = f63e920b764d280d96798a34a3b6e50880ec1d971de8aa2749b31adc06142458
   stages = TRAIN-A + TRAIN-B + TRAIN-C

05 SSI_S3_QUEUE_05_ISKRA4_EXPLORER_ONE_ZIP_V1_20260910.zip
   SHA256 = 886f3a5908b4d5901d961b909a51065b9bd73db04653a8ab155a37feb02038e6
   stages = TRAIN-A + TRAIN-B + TRAIN-C

06 SSI_S3_QUEUE_06_ISKRA5_PRAGMATIST_ONE_ZIP_V1_20260910.zip
   SHA256 = 28a971ad7a08e2a5838b99fb6e89586601c3bb704f95f7928ff4f4b39d858807
   stages = TRAIN-A + TRAIN-B + TRAIN-C

07 SSI_S3_QUEUE_07_ISKRA6_SKEPTIC_ONE_ZIP_V1_20260910.zip
   SHA256 = a22ffcbd14dc4e2970eb5a1929d261209cd9175ca7b534cc1b484c6fa2206a7c
   stages = TRAIN-A + TRAIN-B + TRAIN-C
```

A hash proves package identity/integrity relative to that artifact. It does not prove scientific correctness.

## 5. Gate rule inside each BODY

Each transition requires its own predecessor state and terminal evidence:

```text
T0 -> TRAIN-A -> S1
S1 -> TRAIN-B -> S2
S2 -> TRAIN-C -> S3
```

Before a stage starts, the executor must verify at minimum:

```text
target BODY identity
predecessor state identity
package identity/hash
frozen task/curriculum identity
continuity/checkpoint state
```

After a stage finishes, the executor records:

```text
PASS / FAIL / INCONCLUSIVE
checkpoint(s)
state identity/hash if a descendant state is created
runtime-reported route where available
elapsed/call evidence where available
failure/interruption/recovery history
```

No descendant state may be created by inference when its gate has not actually passed.

## 6. Unattended execution policy

The intended execution mode is unattended for normal, previously authorized training operations. The owner should not be required to click a logical confirmation between ordinary training steps.

For a **BODY-local** problem:

```text
FAIL
INCONCLUSIVE
ambiguous local critical error
body-specific backend/task/evaluator problem
```

the executor must:

```text
1. preserve the exact outcome;
2. write evidence and checkpoint;
3. mark that BODY/stage BLOCKED or INCOMPLETE;
4. NOT repair the BODY automatically;
5. NOT change frozen acceptance criteria;
6. NOT change Router V10, Micronetworks, CONTINUUM or curriculum;
7. NOT retry until success in a loop;
8. move to the next BODY in the declared queue.
```

This prevents one difficult BODY from blocking collection of evidence from all later BODY lines.

## 7. Global-stop boundary

A failure that can invalidate or contaminate later runs is not treated as a local BODY failure.

Examples include:

```text
package/hash mismatch
shared package corruption
shared runtime/state corruption
loss of evidence persistence
unsafe disk/storage condition
wrong BODY identity mapping
shared configuration mutation that changes later test conditions
security/disclosure boundary violation
```

For such a global integrity problem:

```text
GLOBAL_STOP
-> preserve evidence
-> do not continue into later BODY lines
-> do not self-repair unless separately authorized
```

This distinction is intended to maximize unattended progress without sacrificing comparability or evidence integrity.

## 8. No silent repair rule

During the sequential S3 queue, the executor is an execution/evidence operator, not an unrestricted repair agent.

Without separate owner authorization it must not:

```text
rewrite a frozen task
weaken acceptance
replace an oracle merely to obtain PASS
modify BODY reasoning logic
modify Router V10
modify Micronetworks
modify CONTINUUM semantics
change ISKRA identity/personality baseline
erase historical FAIL or INCONCLUSIVE events
```

If a defect is found, preserve it and continue only when the local/global rules above permit continuation.

## 9. TRAIN01A methodological precedent

BODY_FROZEN TRAIN01A established an important precedent for later runs:

- original unresolved outcomes were preserved;
- infrastructure problems were separated from BODY reasoning;
- Kilo model selection was repaired without changing BODY reasoning;
- CHAT fallback was shown to execute through its configured providers;
- backend availability/configuration was repaired separately from the frozen task;
- the step-24 retest then produced a determinate acceptance failure;
- forensic audit proved that the evaluator enforced an undeclared `loader` condition;
- the existing BODY output and parser were not rewritten;
- owner-authorized re-adjudication used the actual frozen contract without a new LLM execution;
- the historical FAIL remained preserved;
- only after full gate verification was `BODY_FROZEN_FOUNDATION_S1` created.

Detailed sanitized closure record:

- [`evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md`](evidence/BODY_FROZEN_TRAIN01A_FINAL_CLOSURE_20260910.md)

## 10. Public/private publication firewall

The public GitHub repository is an evidence mirror, not the execution repository.

Allowed public material includes:

```text
sanitized protocols
package names and hashes
stage/gate status
PASS / FAIL / INCONCLUSIVE accounting
safe checkpoint/state hashes
route/time/call measurements where disclosure-safe
failure -> diagnosis -> repair -> retest lineage
claim boundaries
reviewer-oriented summaries
```

Do **not** publish:

```text
proprietary SSI implementation source
Router V10 implementation source
Micronetwork implementation source
ISKRA private implementation
DIRECTOR/ROBERT private implementation
API keys/tokens/credentials
private local secrets
raw private prompts/data that reconstruct the system
sensitive operational endpoints
```

Any automated publication step must sanitize first and fail closed if it cannot determine whether material is safe for public disclosure.

## 11. Training/experiment firewall

TRAIN-A/B/C must train general mechanism/competence and must not leak held-out experiment answers.

The later drones, humanoid and self-selected third-domain experiment answers remain outside the training material.

The project therefore separates:

```text
TRAINING COMPETENCE ACQUISITION
!=
HELD-OUT EXPERIMENT ANSWER REHEARSAL
```

## 12. Target end state of this queue

A fully successful current queue would end with:

```text
BODY_FROZEN S3
ISKRA1 NICE S3
ISKRA2 GUARDIAN S3
ISKRA3 JUSTICE S3
ISKRA4 EXPLORER S3
ISKRA5 PRAGMATIST S3
ISKRA6 SKEPTIC S3
```

This is a target state, **not a result claimed in advance**.

At the time this protocol is recorded, only BODY_FROZEN S1 is claimed as completed within this new training sequence. S2/S3 and the six ISKRA A/B/C outcomes remain unknown until execution evidence exists.

## 13. Claim boundary

This protocol does not claim:

- that BODY_FROZEN has already reached S2 or S3;
- that any ISKRA has already completed TRAIN-A/B/C;
- that all seven S3 states will be created;
- that future S4/S5 training will pass;
- that held-out mechanism or cross-domain experiments will pass;
- that local executor tools are independent scientific validators;
- that hashes prove scientific correctness;
- AGI, consciousness, universal transfer or production readiness.

The governing rule is:

> Execute one BODY line through the authorized maturity boundary, preserve every outcome, continue past local blockers without self-repair, stop on global integrity threats, and publish only sanitized evidence.