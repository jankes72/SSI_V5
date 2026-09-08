# SSI V5 — Canonical Experiment Package Standard

**Recorded:** `2026-09-08`  
**Status:** `PREDECLARED / REQUIRED FORMAT FOR SSI EXPERIMENTS`  
**Applies to:** internal SSI experiments, BODY_FROZEN, BODY ISKRA 1-6, later ROBERT/DIRECTOR experiments, and externally proposed reviewer challenges  
**Primary objectives:** reproducible execution, minimal live author steering, crash-safe resume, evidence preservation, and zero publication of private SSI source code

## 1. Canonical rule

SSI V5 experiments are not treated as informal one-shot prompts. Each official experiment must use a versioned experiment package with a frozen contract, integrity references, small execution steps, persistent checkpoints and an append-oriented evidence history.

The canonical pattern is:

```text
EXPERIMENT IDEA / EXTERNAL CHALLENGE
-> DECLARED SCOPE
-> FROZEN CONTRACT
-> ACCEPTANCE CRITERIA
-> MICROSTEP PLAN
-> MANIFEST
-> SHA256 / INTEGRITY DIGEST
-> KILO PRE-RUN VERIFICATION
-> REAL SSI BODY EXECUTION
-> STEP RECEIPT
-> CHECKPOINT
-> NEXT STEP
-> FAILURE / INTERRUPTION / RECOVERY PRESERVED
-> FINAL PASS / FAIL / INCONCLUSIVE
-> SANITIZED PUBLIC EXPORT
-> PUBLICATION FIREWALL
-> VERSIONED EVIDENCE
```

This format is intended to remain usable on constrained author-owned hardware where Kilo, Ollama, the reviewer interface, local models or other runtime components may occasionally stop because of memory pressure, process failure or other infrastructure problems.

## 2. One BODY = one independent experiment package

Where multiple SSI BODY lines are compared, they should not be collapsed into one execution artifact.

The intended structure is:

```text
BODY_FROZEN -> independent frozen package + independent evidence chain
NICE        -> independent frozen package + independent evidence chain
GUARDIAN    -> independent frozen package + independent evidence chain
JUSTICE     -> independent frozen package + independent evidence chain
EXPLORER    -> independent frozen package + independent evidence chain
PRAGMATIST  -> independent frozen package + independent evidence chain
SKEPTIC     -> independent frozen package + independent evidence chain
```

A later cross-BODY analysis may compare already closed results, but it must not rewrite or silently rerun the underlying BODY experiments.

## 3. Atomic execution and checkpoint rule

Kilo should execute the declared package in small, auditable steps rather than one large opaque action.

Conceptually:

```text
STEP_0001
-> execute declared action
-> record evidence
-> write receipt
-> update checkpoint

STEP_0002
-> execute declared action
-> record evidence
-> write receipt
-> update checkpoint

...
```

The experiment state must make it possible to identify at least:

```text
CURRENT_STEP
LAST_COMPLETED_STEP
LAST_VALID_RECEIPT
CURRENT_BODY_ID
PACKAGE_ID
PACKAGE_HASH
RUN_ID
RUN_STATUS
```

A later resume starts from the first step that does not have a valid completed receipt rather than starting the entire experiment again or relying on memory of where execution stopped.

## 4. Infrastructure interruption is not automatically experimental intervention

The methodology distinguishes a technical restart from author steering.

### Infrastructure interruption

Examples:

```text
KILO_PROCESS_CRASH
OLLAMA_FAILURE
INTERFACE_FAILURE
OUT_OF_MEMORY
OPERATING_SYSTEM_FREEZE
POWER / PROCESS INTERRUPTION
OTHER DOCUMENTED INFRASTRUCTURE FAILURE
```

If the author only restores the required environment without changing the frozen experiment, SSI decision, acceptance criteria, tested source logic or intended answer, the event should be recorded as infrastructure/operator recovery, for example:

```text
EVENT_TYPE = INFRASTRUCTURE_INTERRUPTION
RECOVERY_TYPE = OPERATOR_RESTART
EXPERIMENT_INPUT_CHANGED = NO
ACCEPTANCE_CHANGED = NO
TESTED_LOGIC_CHANGED = NO
ANSWER_SUPPLIED_BY_AUTHOR = NO
RESUME_FROM = <recorded checkpoint>
```

Before continuation, Kilo should re-verify the relevant package and protected-artifact integrity references where technically available.

### Manual intervention

A materially different category is:

```text
MANUAL_INTERVENTION
```

This includes actions such as:

- changing the task after observing an outcome;
- changing acceptance criteria;
- editing tested SSI logic to rescue the active run;
- telling SSI which route, Champion or answer to use;
- replacing an unfavorable result;
- changing a frozen package component without creating a new package version.

A material intervention must be recorded. If it changes the frozen experimental input or tested mechanism, the current run cannot silently continue under the original package identity.

## 5. Resume contract

After an interruption, the allowed resume sequence is:

```text
1. record the interruption if it was not already recorded
2. identify the last valid completed step
3. verify package identity / hash
4. verify target BODY identity
5. verify protected tested-artifact identity where applicable
6. record OPERATOR_RESTART / RESUME event
7. resume from the first incomplete step
8. preserve all earlier evidence
```

The author may instruct Kilo to resume the frozen procedure, but that instruction must not contain the solution to the tested problem or alter the declared experiment logic.

## 6. Append-oriented evidence and audit chain

Experiment evidence should be append-oriented where practical.

Important events include:

```text
PRE_RUN
STEP_START
STEP_COMPLETE
STEP_FAIL
CHECKPOINT
INFRASTRUCTURE_INTERRUPTION
OPERATOR_RESTART
DECLARED_TEST_RESTART
MANUAL_INTERVENTION
RECOVERY
FINAL_CLASSIFICATION
```

Where implemented, sequential audit records should retain integrity references or a hash-chain so silent modification of earlier records becomes detectable.

External or reviewer-held hash anchors may be used during important experiments so the evidence history does not rely only on a mutable local machine.

Cryptographic integrity demonstrates artifact identity/integrity against a recorded digest. It does not independently prove that a scientific claim is correct or that no human action was physically possible.

## 7. Kilo role

Kilo is the procedural executor of the frozen package.

Kilo may:

```text
VERIFY
LAUNCH
EXECUTE DECLARED STEPS
RECORD
CHECKPOINT
RESUME
COLLECT EVIDENCE
CLASSIFY ACCORDING TO THE FROZEN CONTRACT
PREPARE SANITIZED EXPORT
```

Kilo must not silently:

```text
CHANGE THE RESEARCH QUESTION
CHANGE ACCEPTANCE CRITERIA
CHANGE THE TESTED SSI LOGIC TO OBTAIN PASS
DELETE FAILURES
SUPPLY THE TESTED BODY WITH THE EXPECTED ANSWER
REWRITE HISTORY AFTER THE RESULT
PUBLISH PRIVATE SSI SOURCE CODE
```

Kilo is not described as an independent scientific auditor merely because it executes the procedure.

## 8. Publication firewall — zero private source code

The public SSI V5 repository is an evidence mirror, not a source distribution.

For official experiment publication, private source code and implementation internals have:

```text
PUBLICATION_PERMISSION = NEVER
```

This includes, unless the author explicitly changes the project publication policy in a separately recorded decision:

```text
SSI PRIVATE SOURCE CODE
V10 IMPLEMENTATION SOURCE
MICRONETWORK IMPLEMENTATION SOURCE
ISKRA / MORAL AI IMPLEMENTATION SOURCE
ROBERT PRIVATE SOURCE
PRIVATE FILE TREE
PRIVATE PROMPTS / INSTRUCTIONS
RAW PRIVATE MEMORY
RUNTIME CONFIGURATION
LOCAL PRIVATE PATHS
SECRETS / TOKENS / CREDENTIALS
RAW LOGS THAT LEAK SOURCE OR INTERNAL IMPLEMENTATION
STACK TRACES THAT DISCLOSE PRIVATE SOURCE CONTENT OR PRIVATE PATHS
```

The publication model is:

```text
PRIVATE SSI / BODY
-> reviewer-safe data extraction
-> SANITIZED PUBLIC EXPORT
-> PUBLICATION_STAGING
-> PUBLICATION FIREWALL
-> APPROVED FILE ALLOWLIST
-> PRE-PUSH SCAN
-> PUBLIC GITHUB
```

Public evidence should be generated from reviewer-safe fields rather than copied blindly from private runtime directories.

## 9. Allowlist, not denylist

The publication firewall should use a positive allowlist.

A file is publishable only when its type, destination and content class are explicitly allowed by the current experiment publication contract.

Examples of potentially allowed artifacts include:

```text
sanitized Markdown reports
sanitized machine-readable JSON
sanitized CSV measurement tables
SHA256 / manifest references
reviewer-safe event summaries
claim-boundary documents
```

The absence of a filename extension from a denylist is not permission to publish it.

## 10. Pre-push publication verification

Kilo must not use broad staging commands such as:

```text
git add .
git add -A
```

for the public SSI evidence repository during the experimental publication flow.

Only explicitly approved files from the sanitized publication staging area may be staged.

Before push, the publication gate should check, where technically practical:

- file allowlist;
- destination path allowlist;
- source-code signatures;
- private paths;
- secrets/credentials;
- raw prompts/configuration;
- stack traces/source excerpts;
- accidental private-memory content;
- unexpected binary/archive files;
- unexpected file extensions;
- files not declared in the public export manifest.

Expected gate semantics:

```text
PUBLICATION_SCAN = PASS
PRIVATE_CODE_FOUND = 0
SECRET_FOUND = 0
PRIVATE_PATH_LEAK = 0
UNDECLARED_FILES = 0

ONLY THEN
-> PUBLIC COMMIT / PUSH
```

Any uncertain or unexpected item results in:

```text
PUBLICATION_BLOCKED
```

A CI check after push is not an adequate substitute for the pre-push firewall because once sensitive code has been pushed to public Git history, deleting it in a later commit does not erase the original disclosure.

## 11. Public/private evidence split

An official experiment may maintain richer private evidence than the public mirror.

Conceptually:

```text
PRIVATE EVIDENCE
= full evidence needed by the author for engineering and later controlled inspection

PUBLIC EVIDENCE
= sanitized reviewer-safe subset
+ measured outcomes
+ hashes
+ lineage
+ failure/recovery summaries
+ claim boundaries
```

A public hash may refer to a retained private artifact without publishing that artifact.

## 12. External reviewer / challenge-provider requirement

An external researcher, grant reviewer, partner or challenge provider may propose the research question, cases or falsification challenge.

However, an experiment represented as an official SSI controlled external challenge must preserve this execution/evidence standard.

The external party may propose:

```text
CHALLENGE
TEST CASES
FAILURE CONDITIONS
ACCEPTANCE CRITERIA
MEASUREMENTS
```

After those elements are agreed and frozen, execution follows the canonical package format.

The external challenge provider is not given a hidden route to alter SSI during execution, and the author is not permitted to silently steer SSI toward the preferred result.

If a proposed collaboration requires abandoning the core requirements for frozen inputs, evidence preservation, explicit intervention logging, crash-safe resume or private-source protection, that run will not be represented as an official SSI experiment under this methodology.

This is a methodological compatibility requirement, not a requirement that an external reviewer agree with SSI's scientific hypothesis.

External reviewers are explicitly encouraged to disagree, falsify, break the mechanism or propose stronger tests.

## 13. Reviewer live interface

Where the live reviewer interface is used, the same authority boundary remains:

```text
REVIEWER
= observe + ask informational questions

KILO
= execute frozen procedure

PROGRAMMER_ROOT
= infrastructure authority / declared recovery only during the run

SSI BODY
= tested system
```

The reviewer interface does not become an execution or mission-control channel.

## 14. Final experiment classification

Every closed run ends as:

```text
PASS
FAIL
INCONCLUSIVE
```

Infrastructure interruption, recovery, failed attempts and manual intervention status remain part of the lineage.

A later PASS cannot erase an earlier FAIL.

A repaired experiment receives a new version/run identity when required by the frozen-input rule.

## 15. Why this standard exists

The purpose of this standard is not to make every SSI claim automatically true.

Its purpose is to make the experiment process more auditable by preserving:

```text
WHAT WAS AGREED BEFORE THE RESULT?
WHAT EXACT ARTIFACT / BODY WAS TESTED?
WHAT DID KILO EXECUTE?
WHAT HAPPENED AT EACH STEP?
DID THE MACHINE OR TOOL CRASH?
WHAT DID PROGRAMMER_ROOT DO TO RESTORE IT?
DID THAT RECOVERY CHANGE THE EXPERIMENT?
WHAT FAILED?
WHAT RECOVERED?
WHAT WAS PUBLISHED?
WAS PRIVATE IMPLEMENTATION KEPT PRIVATE?
```

The intended evidence claim is narrow:

> SSI V5 official experiments use a predeclared, versioned and integrity-identified execution package with Kilo as procedural executor, stepwise checkpoint/evidence recording, explicit interruption/intervention lineage, and a sanitized allowlist-based publication path designed to prevent private SSI source code from entering the public research mirror.

The scientific value of each individual experiment must still be evaluated from its actual design, evidence, controls, outcomes and limitations.
