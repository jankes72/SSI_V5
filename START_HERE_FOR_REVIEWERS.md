# SSI V5 — Start Here for Grant and Technical Reviewers

**Updated:** 2026-09-05  
**Current experimental baseline:** `T0 / BODY_FROZEN / PRE-ISKRA`  
**Latest closed validation test:** `TEST 5 / DEVELOPMENT_VALIDATED`

If you evaluate SSI V5 as a grant reviewer, sponsor, researcher or independent technical reviewer, the key distinction is now:

```text
TEST 5
= latest closed validation of a scoped local SSI BODY control/integration path

T0
= newest frozen experimental baseline from which the next comparative experiments start
```

## 1. Current experimental baseline — T0

Primary entry:

[`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)

Sanitized evidence:

[`evidence/BODY_FROZEN_T0_20260905/`](evidence/BODY_FROZEN_T0_20260905/)

Recorded public baseline:

```text
CONTINUUM_FINAL_STATUS = CLOSED
CONTINUUM_TESTS = 23/23 PASS
MAIN_SCENARIOS = 22/22 PASS
E2E_CLOSURE = 19/19 PASS
FINAL_GUARD = 26/26 PASS
ACTIVE_FAILURES = 0
INVARIANT_VIOLATIONS = 0
OPEN_BLOCKERS = 0
EXISTING_SUITE = 580 PASS + 12 SUPERSEDED = 592

BODY_FROZEN = 1781 files / 587 Python files retained privately
MICRONETWORKS = 8
MODULES = 8
LAYERS = 3
V10 = ACTIVE
```

The code is not distributed by this evidence mirror. The public package contains sanitized counts, test results, lifecycle counters, claim boundaries and SHA256 evidence only.

The formal skill lifecycle registry counters in the supplied T0 sanitized snapshot are `0`; the repository deliberately does not relabel micronetwork candidate records as formal skills.

## 2. Why T0 matters scientifically

T0 establishes one frozen pre-ISKRA origin for future comparison. It should remain immutable.

Planned comparison:

```text
T0
-> T1 NO-ISKRA
-> T1 ISKRA variants starting from the same T0
-> T2 separately tested competence consolidation / promotion
```

The immediate first T1 experiment is intentionally controlled. A clean Micronetworks + V10 LEGO package is to be transferred into a safe civilian drone simulation using a supplied recipe, prepared blocks/adapters and explicit PASS/FAIL gates. This tests whether the technology can be transferred under known instructions.

The second transfer experiment reduces scaffolding and requires more autonomous mapping/engineering. A later open-ended experiment can test discovery of a new application domain without revealing the expected answer in advance.

T2 is planned to test whether independently produced competences can be compared, deduplicated, ranked and promoted. Equivalent competence should increase evidence/data coverage rather than silently create duplicate skills. Ambiguous comparisons should request more cases instead of forcing a Champion.

These are plans; no T1/T2 performance result is claimed in T0.

## 3. Latest closed validation — TEST 5

Primary evidence:

[`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

TEST 5 is methodologically important because the earlier Stage 12 `27/27 PASS` was rejected as insufficient after audit. It remained in history as `SUPERSEDED`; the test/system boundary was repaired and Stage 13 was rerun.

**Claim boundary:** this is development validation of the tested local SSI BODY control/integration path. It is not evidence of universal system reliability, production readiness, AGI or consciousness.

## 4. Prior closed evidence

### TEST 4 — ROOT Terminal / Authority / Recovery

- [`evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md`](evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md)

```text
461/461 final regression PASS
1000/1000 controlled E2E PASS
1000 commands / 20 workers concurrency PASS
20/20 real process restart PASS
receipt accounting clean
```

### Micronetwork Migration / Test3 100x v2

- [`evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md`](evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md)

```text
60 000 / 60 000 accounted
failed = 0
unresolved failures = 0
incorrect routing = 0
restart = 20/20 PASS
```

An earlier PASS formula was found too weak and was repaired before final closure.

## 5. V10 — reviewer-safe definition

V10 is designed as a **stateful predictive competence & recovery router**:

```text
CURRENT STATE
+ VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
-> NEXT ROUTE / STRATEGY
```

Anti-loop principle:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE
+ SAME STRATEGY
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

The historical Test 3 speed result is evidence for selective routing under one measured setup, not the full definition of V10 and not universal proof of anti-loop/recovery.

## 6. Role boundaries

```text
BODY_FROZEN T0
= immutable experimental baseline

AGENTS
= operate inside worlds and their own laboratory/CONTINUUM trajectories

DIRECTOR
= observes, audits, compares, ranks and evaluates results

ROBERT
= separate execution/runtime/tooling body
```

This distinction matters when interpreting future skill transfer and consolidation evidence.

## 7. What should not be inferred

Current public evidence does not prove:

- AGI or consciousness;
- production readiness of the whole system;
- universal correctness or universal V10 superiority;
- successful T1/T2 results before those experiments are run;
- that every candidate record is a formal skill;
- that private source implementation is publicly reproducible.

## 8. Recommended reading order

1. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)
2. [`evidence/BODY_FROZEN_T0_20260905/README.md`](evidence/BODY_FROZEN_T0_20260905/README.md)
3. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
4. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
5. [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)
6. [`GRANT_REVIEWER_FAQ.md`](GRANT_REVIEWER_FAQ.md)
7. [`evidence/README.md`](evidence/README.md)

SSI V5 is intended to be evaluated as an evidence chain, including failed/weak tests, repairs, superseded results and future falsifiable comparisons — not as a claim that every planned capability is already proven.