# SSI V5 — LAB release and S11 continuation — 2026-09-22

**Status:** `THREE NEW BODY_FROZEN CASE PASSES / STAGE SUMMARY NOT YET SUPPLIED`  
**Scope:** private implementation update, offline software tests and an operator-supplied runtime excerpt.  
**Public boundary:** sanitized evidence and descriptions; proprietary source and private access remain private.

## Latest observed continuation

```text
SSI V5 Final = IMPLEMENTED / CONTINUATION RUN OBSERVED
BODY_FROZEN + ISKRA1..ISKRA6 = 7/7 runtime/profile readiness reported
DIRECTOR = INDEPENDENT CORE
POCKET readiness = 1 qualified package checked for 7 actors

BODY_FROZEN S11 continuation
inherited prefix = 27 cases verified by the local continuation checker
S11-05-04 = native PASS / CI PASS / CASE_DONE PASS
S11-05-05 = native PASS / CI PASS / CASE_DONE PASS
S11-05-06 = native PASS / CI PASS / CASE_DONE PASS
pending at the last shown CASE_DONE = 0

S11 stage summary = NOT INCLUDED IN THE SUPPLIED EXCERPT
S11 completion for all 7 BODY = NOT ESTABLISHED BY THIS EXCERPT
S12-S40 completion = NOT CLAIMED
PRIVATE LAB FIX = 165/165 offline tests across 14 suites
```

Run identifier: `RUN_20260922T182234Z_5ffa1394`.

| BODY_FROZEN case | Native evaluation | Collective verification | Recorded outcome |
| --- | --- | --- | --- |
| S11-05-04 | PASS | PASS | PASS |
| S11-05-05 | PASS | PASS | PASS |
| S11-05-06 | PASS | PASS | PASS |

The continuation checker reported a verified 27-case inherited prefix before
resuming at S11-05-04. That prefix was checked, not rerun through models in this
continuation check. The three tail cases shown above were executed anew.
The excerpt ends after the last case and does not contain a `STAGE_DONE` or
final run result. No full-stage, seven-BODY or S12–S40 completion is inferred.

The preflight also reports seven available BODY/LUNA runtimes and one qualified
Pocket package checked for seven actors. Runtime availability and resource
readiness are separate from training acceptance. Doctor's `acceptance=NOT_RUN`
means doctor did not perform training; it does not negate the later case results.

## Evidence origin and limits

The runtime record was supplied by the operator from the local installation.
The public [excerpt](../evidence/SSI_V5_S11_CONTINUATION_20260922_OPERATOR_EXCERPT.md)
retains selected lines and removes private paths and configuration details.
It is a transcription, not a replacement for the complete native case files,
reviewer receipts, stage report or provider usage ledger. Those full artifacts
were not supplied with this update. Independent external replication is not
claimed. No elapsed-time, cost, token-count or comparative-speed figure is
inferred from these lines.

## What changed

The release aligns the established plan-field alias across author and reviewer
requirements. A prior reviewer could demand `modular_plan` while receiving the
same plan under canonical `lego_plan`. Requirements and grades are preserved;
this update records later passing executions rather than rewriting the failure.

A separate flow policy retains unresolved case-local INCONCLUSIVE outcomes,
records reasons and continues independent work. It preserves stop behavior for
true FAIL/BLOCKED, cost and call limits, service/deadline issues and unknown
transport outcomes. Dependent stages await their prerequisites. New summary
states therefore distinguish a completed traversal with gaps from a passed
curriculum.

The release also adds permanent controlled-experiment registration, bounded
comparison execution, expert reviews, software stop/presence controls and
Director/BODY integration. [Component roles and boundaries](../SYSTEM/LEGO_POCKET_META_LEGO_AND_DIRECTOR_LABS_20260922.md)
explain LEGO Pocket, META-LEGO, laboratories and the Football World together.

## Offline release verification

The private `SSI_V5_LAB_FIX_20260922` release passed **165 tests in 14 suites**.
These counts are software regression tests, not 165 training cases or flights.
The machine-readable [public summary](SSI_V5_LAB_FIX_OFFLINE_TEST_SUMMARY_20260922.json)
records the source report identity, total counts and execution boundaries.

Executed locally during testing:

- bounded R&D CPU comparisons, including native evaluation of recorded cases;
- the existing stage runner across seven explicit actor fixtures;
- strict continuation and integrity/rollback checks;
- plan-field consistency across author, reviewer and final result;
- unresolved-case recording and preservation of prerequisite and budget gates;
- deterministic 2-D UAV comparisons;
- HTTP access roles, credential revocation, review and software-stop paths;
- expert presence expiry and native-entry integration through an explicit runtime fixture.

Model/reviewer responses and the new live BODY path were represented by
explicit offline fixtures. The suite made zero paid model calls. The later
operator runtime excerpt is a separate source; its model usage is not quantified
here. JavaScript syntax and HTTP behavior were checked. Browser visual testing
was not completed because the test environment lacked the browser executable.
No physical flight, Tailscale deployment, autopilot SIL/HIL validation or real
external expert session was performed by the offline suite.

## Remaining validation

- Complete S11 stage report and results for the remaining BODY lines.
- S12–S40 execution and applicable acceptance gates.
- New end-to-end evidence of Director-delegated experimental execution.
- Football World source identity, ingress, frozen prediction and independent outcome flow.
- External partner-defined experiments and target-specific replication.
- Physical domain integration where separately commissioned and tested.

The [2026-09-20 stopped run](SSI_V5_CONTROLLED_EVOLUTION_LIVE_S11_20260920.md)
remains unchanged historical evidence. The preserved V4 and Dual Mother results
retain their own version, scope and provenance.
