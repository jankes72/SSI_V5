# SSI V5 — S19 observability incident and pre-S20 status — 29 September 2026

**Status:** `PUBLIC INCIDENT / RECOVERY RECORD`  
**Scope:** software/runtime evidence only.  
**Repository role:** sanitized public evidence mirror; proprietary implementation remains private.

## Executive summary

S19 exposed two different events that must not be conflated:

1. an earlier host interruption after BODY_FROZEN had produced 30 S19 case results; and
2. a later **post-stage consolidation regression introduced during the integration of new routing observability** intended to answer whether Champion execution and Full Flow escalation were actually occurring.

The second event is classified here as an **observability-induced integration regression**, not as evidence that the S19 case workload itself failed to execute.

## Chronology

### A. First S19 interruption

Run `RUN_20260926T064644Z_793783ad` reached S19/BODY_FROZEN and was interrupted after 30 BODY_FROZEN cases:

```text
PASS = 14
INCONCLUSIVE = 16
FAIL = 0
```

Fifteen already-existing S19/BODY_FROZEN case files had not yet received their CASE attestations when the host interruption occurred. Recovery was restricted to that explicit boundary. Original case contents and outcomes were preserved, evidence coverage was rechecked, and the source run was sealed as interrupted.

### B. Why observability was expanded

The S13-S18 unique-case audit showed:

```text
unique cases = 1,260
micronetwork_used = 1,260 / 1,260
v10_used = 1,260 / 1,260
collective_used = 1,260 / 1,260

automatic_champion = false for 1,260 / 1,260
explicit champion route observed = 0
```

This proved participation of the Micronetwork/V10 layer but did **not** prove the final per-case routing path. In particular, the older receipts could not reliably separate:

- exact reuse;
- micronetwork-only completion;
- Champion selected vs merely present in the catalog;
- Champion actually executed;
- Full Flow escalation;
- provider/model fallback.

A new routing-observability layer was therefore introduced specifically to make those questions falsifiable in later cases.

### C. S19 was then fully executed

A later continuation run, `RUN_20260929T005550Z_a356e86c`, completed S19 across BODY_FROZEN and ISKRA1..ISKRA6:

```text
execution_complete = true
PASS = 182
INCONCLUSIVE = 24
FAIL = 4
BLOCKED = 0
verified subset = 182
excluded from consolidation = 28
stage status = INCONCLUSIVE
training status = TRAINING_COMPLETE_WITH_FAILURES
```

The presence of FAIL/INCONCLUSIVE outcomes is preserved. They were not rewritten as PASS.

### D. The failure occurred after S19 execution, during consolidation

Cross-consolidation transaction:

```text
CC_09eae1705906e8acaa653eb28123fc84
```

did not commit. The post-stage path stopped on:

```text
CONSOLIDATION_SNAPSHOT_RESPONSE
```

Subsequent diagnosis showed that the runtime path used after the observability/continuation changes was missing the consolidation hook in the canonical bootstrap. After that hook was restored and runtimes restarted, six ISKRA runtimes returned valid SNAPSHOT responses while BODY_FROZEN still reported a pending-mission condition requiring separate recovery handling.

## Current root-cause classification

The current engineering classification is:

```text
PRIMARY CLASS:
OBSERVABILITY_INDUCED_INTEGRATION_REGRESSION

TRIGGER:
routing / Champion / Full-Flow observability integration

AFFECTED LAYER:
post-stage runtime lifecycle / cross-consolidation path

NOT CLASSIFIED AS:
S19 case-execution failure
proof of SSI capability weakness
Champion execution failure
Full-Flow execution failure
```

The immediate regression was introduced while adding instrumentation needed to verify routing behavior. Recovery then exposed stale mission-state handling that also has to be resolved before consolidation can be considered healthy.

This distinction matters: **the S19 case workload completed; the post-stage consolidation path did not.**

## What has already been verified during recovery

Observed readiness checks include:

```text
Pocket Micro = READY
Doctor = READY_FOR_BOOT
BODY_FROZEN + ISKRA1..ISKRA6 runtimes = 7/7
WEB LEGO preflight = READY
WEB stages = 24
WEB cases = 192
WEB LEGO items = 126
WEB templates = 15
WEB data policy = SYNTHETIC_ONLY
```

The consolidation hook is now present in the restarted runtime path. A later probe demonstrated valid transaction-bound SNAPSHOT responses for ISKRA1..ISKRA6; BODY_FROZEN remained correctly blocked by its pending-mission guard.

## Why the incident is useful

The incident revealed a methodological requirement that is now being made explicit:

> **An observability layer must not alter the behavior of the system it is intended to measure.**

The next routing telemetry revision will therefore be gated by a non-interference test before S20 is allowed to start.

The target relationship is:

```text
NORMAL EXECUTION
        |
        +--> execution result
        |
        +--> read-only / append-only observer event
```

The observer may record routing facts but must not:

- change mission status;
- change PASS/FAIL/INCONCLUSIVE;
- modify the pending mission queue;
- control SNAPSHOT;
- modify consolidation semantics;
- modify Champion qualification or promotion;
- modify model weights;
- alter routing merely because it is observing routing.

## Current public boundary

At the time of this record:

- S19 full execution is evidenced;
- S19 cross-consolidation is **not claimed COMMITTED**;
- S20 start is **not claimed**;
- WEB01-WEB24 live execution is **not claimed**.

The intended continuation is:

```text
pre-S20 hardening gates
-> recover / commit S19 consolidation
-> S20 ... S40
-> require S40 execution_complete
-> require S40 consolidation COMMITTED
-> WEB01 ... WEB24
-> final cross-actor / routing / model diagnostic report
```

## Related records

- [S13-S18 routing and recovery evidence](SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md)
- [Pre-S20 observability and evidence hardening preregistration](../SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)
- [External review feedback and attribution](../EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
