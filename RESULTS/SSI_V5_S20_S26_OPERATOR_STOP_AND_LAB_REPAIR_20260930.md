# SSI V5 — S20-S26 operator stop, LAB reliability diagnosis and repair boundary — 2026-09-30

**Status:** TRAINING STOPPED BY OPERATOR / DIAGNOSIS COMPLETED / REPAIR PACKAGE PREPARED / LIVE RESTART NOT AUTHORIZED  
**Repository role:** public evidence/review mirror for a private SSI implementation.  
**Evidence boundary:** software/runtime evidence only. Physical validation and independent external replication are not claimed.

## Executive summary

After the pre-S20 hardening gate passed and S19 consolidation was reported committed, the core training run continued through S20-S25 and into S26.

The operator then **manually stopped the run with Ctrl-C** because the growing number of INCONCLUSIVE outcomes and pending work no longer looked acceptable as a trustworthy training signal.

The stop was intentional. The project did not continue toward S40 merely to increase the stage counter.

The latest preserved diagnostic snapshot supplied for this incident contains:

~~~text
TOTAL VERDICTS = 1,326
PASS           =   848
INCONCLUSIVE   =   470
FAIL           =     8
~~~

These values are a preserved run snapshot. They must not be interpreted as a universal SSI capability score.

## Why the run was stopped

The operator observed that unresolved cases were accumulating while the stage traversal continued.

That created a methodological problem:

~~~text
stage progression
!=
reliable completion of every case
~~~

Continuing unchanged to S40 would have allowed the backlog to grow while mixing capability failures with execution, transport, parsing and reviewer-delivery failures.

The correct action was therefore:

~~~text
observe abnormal INCONCLUSIVE accumulation
-> stop the run
-> preserve existing verdicts
-> diagnose the execution/review path
-> repair the infrastructure
-> validate the repair offline
-> restart only under a new explicit continuation boundary
~~~

## Consolidation boundary

The broader run record reports completed stage consolidations for **S20 through S25**.

For those completed stages, consolidation of the verified subset was reported as PASS for both BODY_FROZEN and the independent DIRECTOR view.

This does **not** convert unresolved cases into PASS.

~~~text
stage may remain INCONCLUSIVE
+ verified PASS subset may be consolidated
+ unresolved/failed cases remain preserved outside that verified subset
~~~

S26 was still in progress when the operator stopped the run. No S26 completion or S26 consolidation is claimed by this record.

## Diagnostic finding 1 — sampled JSON failures were empty responses after INFLIGHT_LIMIT

A targeted inspection checked **18 cases** previously surfaced as JSON/parse failures.

In all 18 inspected cases, the apparent JSON problem was associated with an **empty response after INFLIGHT_LIMIT**.

~~~text
visible symptom:
unparseable_json

observed sampled cause:
empty response after INFLIGHT_LIMIT
~~~

### Claim boundary

This finding applies to the **18 inspected cases**.

It does **not** prove that every unparseable_json or every INCONCLUSIVE result in S20-S26 has the same cause. A replay after repair is required before reclassifying any broader population.

## Diagnostic finding 2 — training continued while the blockage persisted

The training traversal continued to request later cases even while the inflight condition was producing unresolved work. As a result, the pending backlog grew instead of acting as a hard reliability gate.

The repair therefore treats backlog growth as an execution-control problem, not as evidence that later cases were independently evaluated under clean conditions.

## Diagnostic finding 3 — required task outputs were not reaching the reviewer correctly

The diagnosis also found that required outputs produced for a task were not always propagated correctly into the reviewer path.

This means that some outcomes can reflect an incomplete executor-to-reviewer contract rather than a clean evaluation of the underlying solution.

~~~text
TASK
-> CANDIDATE / EXECUTION OUTPUT
-> CONTRACT BINDING
-> REVIEWER INPUT
-> VERDICT
~~~

The affected path must preserve the task-required outputs before a capability conclusion is made.

## Diagnostic finding 4 — missing dedicated R&D execution scenarios for S20-S26

The diagnostic package also identified that the current S20-S26 training material still lacks dedicated execution scenarios for some R&D behaviors.

This is recorded as a curriculum/evaluation coverage gap. It must not be hidden by a high-level stage PASS percentage or by successful verified-subset consolidation.

## Repair package

A local repair package was prepared as **SSI_LAB_REPAIR_20260930.zip** with installer entry point **SSI_LAB_REPAIR_20260930/NAPRAW.py**.

The prepared repair was reported to pass **17 / 17 offline tests**.

The installer is designed to:

- create a backup before modification;
- preserve historical verdicts and configured limits;
- repair the LAB/reviewer flow rather than rewrite old results;
- inspect evidence before attempting to close a CANCELLED report;
- leave training stopped after the repair step.

## Live-application boundary

At the time of this public incident record, the repository does **not** use the offline test result as proof that the private live runtime has been safely resumed.

~~~text
REPAIR PACKAGE PREPARED = YES
OFFLINE TESTS = 17/17 PASS
HISTORICAL VERDICTS REWRITTEN = NO

LIVE REPAIR APPLICATION = not claimed by this record
CANCELLED REPORT CLEANLY CLOSED = not claimed by this record
S20-S40 RESTART = not authorized by this record
S26 COMPLETION = not claimed
S40 COMPLETION = not claimed
~~~

A later terminal/evidence record may advance these claims after the installer result is inspected.

## Restart policy

The previous S20-S40 launcher must not simply be restarted unchanged. Continuation must explicitly account for the code/infrastructure change.

The next run should preserve at minimum:

- pre-repair run identity;
- repair version/hash;
- post-repair run identity;
- unchanged historical verdicts;
- replay identity for selected pending cases;
- raw provider/model response metadata for parse failures;
- INFLIGHT_LIMIT / concurrency state;
- candidate-to-reviewer output mapping;
- PASS / FAIL / INCONCLUSIVE without silent relabeling.

Recommended comparison:

~~~text
PRE_REPAIR ORIGINAL CASE
vs
POST_REPAIR REPLAY OF THE SAME FROZEN CASE
~~~

This allows the project to measure how many unresolved outcomes were caused by infrastructure and how many remain genuine capability or verification failures.

## Research interpretation

The incident does not justify either extreme conclusion that SSI capability is simply 848/1326 or that all 470 INCONCLUSIVE cases were infrastructure failures.

What the current record supports is narrower:

1. the training process progressed into S26;
2. verified subsets were consolidated through completed S20-S25 stages;
3. unresolved outcomes accumulated;
4. the operator stopped the run rather than treating stage progression as sufficient;
5. a targeted 18-case sample linked the apparent JSON failure to empty responses after INFLIGHT_LIMIT;
6. reviewer-input propagation problems were identified;
7. missing dedicated R&D execution scenarios were identified;
8. a repair package passed 17 offline tests;
9. a clean live restart remains a separate evidence event.

## Why this incident is public

SSI V5 is described as evidence-first. That claim is only meaningful if the public mirror preserves failures, unresolved results, operator stops, instrumentation defects, repair boundaries, retests and differences between prepared fixes and live-validated fixes.

This record is therefore intentionally published as part of the project history rather than being replaced by a cleaner-looking stage summary.

## Related records

- [README](../README.md)
- [Current Truth Index](../CURRENT_TRUTH_INDEX.md)
- [Reviewer Index](../REVIEWER_INDEX.md)
- [S20 supplied live excerpt](../evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)
- [Historical S19 incident / pre-S20 state](SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md)
- [Pre-S20 hardening preregistration](../SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md)

## Claim boundary

This record does not establish:

- that all 470 INCONCLUSIVE outcomes share one root cause;
- that all pending cases would become PASS after repair;
- that the repair has already been applied successfully to the private live runtime;
- that the CANCELLED report has already been closed;
- that S26 completed;
- that S20-S40 training completed;
- that WEB01-WEB24 completed;
- physical robot/drone validation;
- safety certification;
- independent external replication;
- production readiness.
