# SSI V5 — Micronetwork Migration & Repair Lineage

**Public status:** `PRE-CLOSURE / FINAL CONTRACT TEST PENDING`  
**Date:** `2026-09-02`  
**Scope:** `ROBERT micronetworks + V10 routing + M00–M09 integration`  
**Character:** public research/engineering record; full raw evidence remains in local/private SSI Evidence Storage.

> This document intentionally does not yet declare `MICRONETWORK_MIGRATION_CLOSED = TRUE`. The final test clarifying the Test3 metric contract was executed separately and the later closure documents preserve its final result.

---

## 1. Why this record exists

The goal is not to show only a final PASS. The goal is to preserve engineering lineage:

```text
INITIAL STATE
-> EXPERIMENT
-> DETECTED INCONSISTENCY
-> MACHINE EVIDENCE
-> DIAGNOSIS
-> REPAIR
-> RETEST
-> REGRESSION
-> FINAL CONTRACT TEST
-> ONLY THEN CLOSURE
```

This record serves two purposes:

1. **for reviewers / grant evaluators** — to show whether the project preserves errors, root causes, repairs and retests rather than publishing only favorable outcomes;
2. **for future Director / SSI Self-Model** — engineering memory explaining why a mechanism exists and what conditions must be preserved during later controlled self-development.

---

## 2. Evidence-source separation

The local ROBERT environment intentionally separated two evidence layers:

```text
EVIDENCE/
= HISTORICAL / BEFORE
= not overwritten after repair


evidence/
= REPAIR / AFTER / CLOSURE CANDIDATE
= current repair and regression tests
```

This separation is methodologically important. A later PASS does not erase an earlier failure or a weak test contract.

The public GitHub repository is an evidence mirror, so it primarily stores descriptions, indexes and claim boundaries; full local JSON/JSONL/log artifacts may remain outside the public repository.

---

## 3. BEFORE — what historical evidence showed

Historical Test3A/Test3B evidence exposed an important methodological problem: **execution status `PASS` did not guarantee that `expected_route` matched `actual_route`**.

The earlier test could therefore confirm completion while still being too weak to establish correctness of V10 routing decisions.

The earlier result was not deleted or rewritten. It was preserved as:

```text
HISTORICAL_EVIDENCE
-> exposes a weaker test contract
-> justifies repair
-> becomes part of lineage
```

This is a falsifiability principle: a test later found to be too weak is not retrospectively presented as sufficient.

---

## 4. DIAGNOSIS — main problem classes

The repair audit identified several connected issues:

- Router V10 did not fully apply required `min_confidence_for_reuse` and `min_success_ratio_for_reuse` thresholds;
- `REUSE_TOP1` needed a stronger capability gate and proof of real micronetwork execution;
- runtime did not fully initialize/call `V10LearningFlow`;
- M00–M09 flow required explicit bridge/callsite evidence;
- `robert/micronetworks.py` should not maintain a parallel engine beside the canonical core;
- technical domain `test` should not enter production selection;
- a `CHAMPION` without executable weights should not remain an active Champion;
- interface authentication required fail-closed rather than fail-open behavior;
- IdentityManager required safer concurrent write / atomic update behavior;
- systemd and tests still contained stale ROBERT paths;
- Test3 had to verify routing correctness, background failures and real execution rather than only final status.

---

## 5. REPAIR — what changed

### V10 Router

- real use of sample / confidence / success-ratio thresholds;
- capability lookup before `REUSE_TOP1`;
- escalation to full flow when the gate is not satisfied;
- target-capability seeding and warmup only for executable capabilities.

### ROBERT Runtime

- pass thresholds and capability lookup into V10;
- initialize `V10LearningFlow`;
- register outcomes in the learning flow;
- connect feedback to V10 flow;
- execute the micronetwork for reuse rather than only returning a control shortcut.

### Canonical Micronetwork Engine

- reduce `robert/micronetworks.py` to a thin adapter/re-export of canonical core;
- downgrade a `CHAMPION` without executable weights to a non-executable state;
- filter technical domain `test` from production `advise`.

### Security / persistence / concurrency

- interface authentication changed to fail-closed;
- IdentityManager uses unique tempfile, locking and atomic replace;
- systemd points to the canonical ROBERT directory.

### Test contract

Test3 was rebuilt to account for:

- expected route vs actual route;
- capability gate;
- threshold boundary;
- real execution;
- background failures;
- complete 600/600 accounting.

---

## 6. AFTER — repaired Test3 result

The final repair report for a single canonical Test3 run recorded:

```text
total:                    600
accounted:                600
reuse_valid:              227
escalated_and_resolved:   260
full_flow_resolved:       113
failed:                     0
incorrect_routing:          0
background_failures:        0
exceptions:                 0
global_success_ratio:     1.0
PASS:                    True
```

Router thresholds:

```text
min_samples_for_reuse       = 3
min_confidence_for_reuse    = 0.7
min_success_ratio_for_reuse = 0.8
```

Boundary tests supported:

```text
THRESHOLDS PASS + EXECUTABLE CAPABILITY
-> REUSE_TOP1

ANY REQUIRED GATE FAILS
-> ESCALATE_FULL_FLOW
```

---

## 7. M00–M09 layer flow

The repair report marked M00–M09 as connected in the tested flow:

```text
M00 Store
M01 Experience Store
M02 Experience Graph
M03 Lifecycle
M04 Factory
M05 Pattern
M06 Semantic
M07 Safe Routing
M08 Self-Improvement
M09 Persistence
```

A further audit goal was to reduce the risk of creating a second side-channel learning state. Final closure required the compatibility bridge not to become a separate second organism with a competing state truth.

---

## 8. Additional repair tests

The evidence set also recorded:

- fail-closed auth: missing / empty / invalid token -> deny;
- IdentityManager concurrency: `400/400` writes without exception and valid final JSON;
- SQLite integrity for primary databases;
- lifecycle transitions;
- corrected systemd paths;
- restart/recovery testing;
- A01–A20 regression;
- repeated Test3 stability testing.

These results were part of local `evidence/`. At this pre-closure point the public mirror intentionally did not elevate the status to final closure before the final Test3 contract audit completed.

---

## 9. Final inconsistency discovered before closure

During audit of repeated Test3 runs, a field named `failed` appeared in a small number of runs even while the overall run reported PASS.

This could not be resolved by merely renaming the field or weakening PASS criteria.

The final audit had to determine from raw evidence and code whether `failed` meant:

1. **a real unresolved failure** — requiring repair and full retest; or
2. **an intermediate failure later correctly resolved by escalation** — requiring metric-contract clarification, for example separating `initial_path_failed` from `unresolved_failures`.

The public pre-closure status at that point was:

```text
REPAIR IMPLEMENTED
MAJOR RETESTS PASS
FINAL TEST3 METRIC-CONTRACT CLARIFICATION = PENDING
MICRONETWORK_MIGRATION_CLOSED = NOT YET CLAIMED PUBLICLY
```

Later evidence established that `failed` represented a real unresolved failure, the PASS formula was repaired with `failed == 0`, and a new 100x run was executed from the beginning. The separate final-lineage and closure documents record the resulting closure.

---

## 10. Why this case matters to a grant reviewer

This case shows more than router behavior. It shows the project method:

```text
PASS DOES NOT END THE AUDIT
-> CHECK WHAT PASS ACTUALLY MEASURES
-> PRESERVE OLD EVIDENCE
-> FIND INCONSISTENCY
-> REPAIR ROOT CAUSE
-> STRENGTHEN TEST CONTRACT
-> RERUN THE TEST
-> CHECK PERSISTENCE / RESTART / CONCURRENCY
-> ONLY THEN CLOSE THE STAGE
```

For grant evaluation, the value is the traceable path from a weaker test to a stronger contract, not only an impressive final number.

---

## 11. Why this case matters to Director

The same record should form part of future SSI engineering memory.

Director should be able to reconstruct:

```text
WHY A COMPONENT EXISTS
-> WHAT PROBLEM IT WAS MEANT TO SOLVE
-> HOW AN EARLIER TEST WAS TOO WEAK
-> WHAT EVIDENCE EXPOSED THE ERROR
-> HOW ARCHITECTURE CHANGED
-> HOW THE TEST WAS STRENGTHENED
-> WHICH INVARIANTS MUST REMAIN
-> WHICH CONDITIONS MUST HOLD BEFORE THE NEXT MODIFICATION
```

This supports future **supervised self-build / controlled self-development**, not unrestricted self-modification.

Authority invariants remain:

```text
ROOT = HIGHEST AUTHORITY
KNOWLEDGE != AUTHORITY
CAPABILITY != AUTHORITY
MODEL OUTPUT != AUTHORITY
```

Knowledge of construction history may improve Director engineering hypotheses but does not grant automatic permission to deploy a change into canonical runtime without required authority, tests and evidence.

---

## 12. Engineering lesson schema for future SSI

```text
OBSERVED SUCCESS
-> CHECK WHETHER SUCCESS METRIC IS STRONG ENOUGH

CONFLICTING EVIDENCE
-> PRESERVE CONFLICT
-> DO NOT RETROACTIVELY ERASE OLD RESULT

ROOT CAUSE FOUND
-> CHANGE CANONICAL PATH, NOT CREATE PARALLEL ARCHITECTURE

REPAIR
-> TEST BOUNDARIES
-> TEST REAL EXECUTION
-> TEST PERSISTENCE
-> TEST RESTART
-> TEST CONCURRENCY

METRIC AMBIGUITY
-> RESOLVE SEMANTICS FROM RAW EVIDENCE
-> DO NOT LOWER PASS CRITERIA

ONLY THEN
-> CLOSURE
```

This is the type of knowledge CEPA / Engineering Memory / Director Self-Model may later use to generate better repair/development proposals.

---

## 13. Evidence lineage — private/local pointers

Important local artifacts included:

```text
EVIDENCE/
  R03_REPORT.md
  R03_POST_IMPORT_MATRIX_20260901.txt
  R09_FEASIBILITY.json
  R09_FREEZE_MANIFEST.json
  TEST3A_EVIDENCE_20260901/
  TEST3B_EVIDENCE_20260901/


evidence/
  micronetwork_full_stack_experiment/
  FINAL_REPAIR_REPORT.md
  TEST3_REPEAT_100X.*
  RUNTIME_RESTART_20X.*
  REGRESSION_A01_A20.*
  V10_CANONICAL_STATE_TEST.*
  TEST3_FAILED_FIELD_AUDIT.*
```

These names are provenance pointers. Not every raw local artifact must be published in the public mirror.

---

## 14. Final closure condition

The pre-closure case required machine evidence to establish:

```text
TEST3_REPEAT = 100/100 PASS
accounted = 600/600 per run
unresolved_failures_total = 0
incorrect_routing_total = 0
background_failures_total = 0
exceptions_total = 0
RESTART = 20/20 PASS
A01-A20 = PASS
parallel_runtime_state = FALSE
parallel_micronetwork_engine = FALSE
parallel_v10_learning_state = FALSE
open_blockers = []
```

The later closure evidence records that these conditions were satisfied and then supports:

```text
MICRONETWORK_MIGRATION_CLOSED = TRUE
MICRONETWORK_CANONICAL = TRUE
FINAL_PASS = TRUE
```

This document remains intentionally marked as the historical **pre-closure** stage rather than being rewritten into the later final state.