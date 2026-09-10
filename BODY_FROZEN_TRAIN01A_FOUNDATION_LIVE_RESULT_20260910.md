# SSI V5 — BODY_FROZEN TRAIN01A Foundation live result

**Recorded:** `2026-09-10`  
**Target:** `BODY_FROZEN`  
**Package:** `SSI_TRAIN01A_BODY_FROZEN_FOUNDATION_FROM_DIRECTOR_GOLDEN_MASTER_V1_20260910`  
**Executor:** `CODEX` with a durable local user-systemd supervisor  
**Run scope:** 48 Foundation steps / 16 blind validations  
**Status:** `RUN COMPLETE / RECOVERY RETEST COMPLETE / FINAL GATE NOT PASSED`

## 1. Original completed run

The first completed live supervisor run recorded:

```text
TOTAL STEPS ATTEMPTED = 48 / 48
PASS                  = 43
FAIL                  = 0
INCONCLUSIVE          = 5

BLIND VALIDATIONS     = 16 / 16 attempted
BLIND PASS            = 14
BLIND FAIL            = 0
BLIND INCONCLUSIVE    = 2

FINAL_GATE            = FAIL
FOUNDATION_S1         = NOT CREATED
```

The five original `INCONCLUSIVE` steps were:

```text
06 — BLIND_VALIDATION — Ambiguity and missing-information discipline
16 — INSTRUCTION      — Simple programming correctness
17 — GUIDED_PRACTICE  — Simple programming correctness
23 — GUIDED_PRACTICE  — Root-cause vs symptom patching
24 — BLIND_VALIDATION — Root-cause vs symptom patching
```

No completed step in the original run was recorded as a substantive `FAIL`.

## 2. Recovery retest

A separate recovery run retested exactly the five unresolved historical cases while preserving the original evidence.

Observed recovery result:

```text
06 = INCONCLUSIVE
16 = INCONCLUSIVE
17 = INCONCLUSIVE
23 = PASS
24 = INCONCLUSIVE

RECOVERY PASS         = 1 / 5
RECOVERY FAIL         = 0 / 5
RECOVERY INCONCLUSIVE = 4 / 5
FINAL_GATE            = FAIL
FOUNDATION_S1         = NOT CREATED
```

Step `23` produced a substantive `CHAT` response and passed its recovery evaluation. Its successful path selected `openrouter` after earlier backend attempts; this demonstrates that this individual unresolved case was recoverable in a later attempt, but does not by itself prove the root cause of the original timeout.

Steps `06`, `16`, and `17` again returned live runtime records with:

```text
classification = CODE
status = RUNNING_LOCAL
micronetwork_used = true
v10_used = true
continuum_used = true
provider_gateway_used = false
selected_backend = null
```

The executor again received no substantive BODY answer to grade, so these cases remain `INCONCLUSIVE`. Their repeatability strengthens the evidence that they are associated with the live routing/execution path rather than a one-off missing response, but this publication does not claim that Router V10 source code, the model, hardware, classifier state or any single subsystem has been proven causal.

Step `24` again did not produce a substantive answer and ended after approximately 420 seconds with:

```text
TimeoutError('timed out')
```

It therefore remains `INCONCLUSIVE`.

## 3. Completion-gate consequence

The original history remains unchanged: `43 PASS / 5 INCONCLUSIVE / 0 FAIL`. The recovery history is appended separately: one of the five unresolved cases (`23`) later passed, while `06`, `16`, `17`, and `24` remain unresolved.

Because blind validations `06` and `24` still lack determinate acceptance outcomes, the current Foundation completion gate remains:

```text
FINAL_GATE = FAIL
BODY_FROZEN_FOUNDATION_S1 = NOT CREATED
```

No result has been rewritten from the original run. A future diagnosis/repair and new controlled retest may be performed, but historical `INCONCLUSIVE` evidence must remain preserved.

## 4. Provenance

Original completed-run archive SHA-256 previously published:

```text
d3dc90ecac6fe11abd8150ec373bbbeb51ab612ba6dd4e4f366fd50b78e6a7a6
```

Updated archive containing the recovery evidence SHA-256:

```text
101a2589a1f7c5f1e84a2aead7914773c15e6f854990c25d9efc6d505142441b
```

Recovery evidence includes:

```text
evidence_runtime/recovery_retest_20260910/RECOVERY_RETEST_SUMMARY.json
evidence_runtime/recovery_retest_20260910/RECOVERY_RETEST_EVENTS.jsonl
evidence_runtime/recovery_retest_20260910/RECOVERY_RETEST_REPORT.md
evidence_runtime/recovery_retest_20260910/step_006/result.json
evidence_runtime/recovery_retest_20260910/step_016/result.json
evidence_runtime/recovery_retest_20260910/step_017/result.json
evidence_runtime/recovery_retest_20260910/step_023/result.json
evidence_runtime/recovery_retest_20260910/step_024/result.json
```

## 5. Claim boundary

This publication records one completed Foundation execution plus its first controlled recovery retest. It does **not** claim:

- that BODY_FROZEN has reached Foundation S1;
- that the four remaining unresolved cases are substantive BODY reasoning failures;
- that hardware, Router V10, the model or infrastructure has been proven to be the sole cause;
- that later S2-S5 training or cross-domain experiments will pass;
- AGI, consciousness, universal transfer, production readiness or external-system superiority.

The next valid state transition requires a completion-gate result supported by preserved evidence.