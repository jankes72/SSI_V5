# SSI V5 — Aktualna naprawa / Active repair record

**Status: OPEN — NAPRAWA W TOKU**  
**Record opened:** 2026-10-03  
**Last evidence assessment:** 2026-10-03, Europe/Warsaw  
**Scope:** SSI Final recovery, Evidence V3 / Dynamic Resolution Labs, local graph measurements and the candidate-to-reviewer path.  
**Owner:** Paweł Jankiewicz.  
**Closure:** not established by the evidence available for this update.

> **Po polsku:** To jeden aktualizowany rejestr trwającej naprawy. Zawiera błędy, odrzucone próby, wyniki lokalnych testów i brakujące potwierdzenia. Lokalny wariant naprawy S23-01-01 przeszedł 24/24 testy, ale późniejsza recenzja zakończyła się FAIL. Ponowna recenzja i wykonanie w docelowym systemie pozostają niepotwierdzone. Historyczne oceny szkolenia pozostają bez zmian; naprawę zamkniemy dopiero po udokumentowaniu wymaganych kontroli.

This file is the continuing repair record for this incident. New observations belong here, including unsuccessful attempts. Earlier dated reports remain snapshots of what was known at their publication dates. This record supplements them with subsequent repair evidence; it does not overwrite their verdicts or declare the training complete.

## 1. Current state

| Item | Last confirmed observation | Meaning for closure |
|---|---|---|
| Original Final continuation | Seven closed cases: 4 PASS / 3 INCONCLUSIVE / 0 FAIL; `STOPPED_INFRASTRUCTURE` | Original outcomes remain preserved |
| Evidence V3 installation | Offline installation/tests completed; `CODE_READY`; zero model calls in those checks | Code readiness established within the checked scope |
| R3 investigation update | Installed; a subsequent live investigation produced `RESOLUTION_FAILED` | Installation did not establish a successful repair |
| R4 graph-rule update | Installed after 5 updater tests and 15 graph tests passed | Local update and regression checks completed |
| R4 field-only variant | 4/24 tests passed; 20 failed; `RESOLUTION_FAILED` | Unsuccessful variant retained |
| R4 selected graph variant | 24/24 local tests passed; initially `AWAITING_INDEPENDENT_REVIEW` | Local comparison succeeded |
| Negative control for that comparison | 2/24 tests passed; 22 failed; comparison `FAIL` | The intentionally incorrect control differs from the local reference |
| Subsequent model review | Reported signed verdict `FAIL` / `RESOLUTION_FAILED` | Review gate remains unsatisfied |
| Review-context audit | Candidate identity reported consistent; graph presentation and measurement labels examined | Reassessment needed; the earlier FAIL remains in the record |
| R5 / review reassessment | Proposed in the repair discussion; no subsequent installation/reassessment result located in the assessed evidence | Execution and outcome remain unconfirmed |
| Native BODY execution / training verdict | R4 output: `native_body_execution_verified=false`, `training_verdict=null`; native retest `NOT_RUN` | No completed native qualification established |

The negative-control counts describe test-vector comparisons. They are not an agent failure rate or a general safety-detection rate. These measurements are not added to training PASS totals.

## 2. Related training, status and evidence

The following links collect the relevant entry points in this single file. The existing documents retain their own dated observations.

| Purpose | Related record |
|---|---|
| Main repository entry | [README](README.md) |
| Current claims and historical snapshots | [Current Truth Index](CURRENT_TRUTH_INDEX.md) |
| Reviewer orientation | [Start here for reviewers](START_HERE_FOR_REVIEWERS.md), [Reviewer Index](REVIEWER_INDEX.md) |
| Programme and training tracks | [Current Research Roadmap — 2026-10-02](CURRENT_RESEARCH_ROADMAP_20261002.md) |
| Original S20-S26 stop and reliability repair | [Operator stop / LAB repair — 2026-09-30](RESULTS/SSI_V5_S20_S26_OPERATOR_STOP_AND_LAB_REPAIR_20260930.md) |
| Latest Final continuation and unresolved cases | [Final recovery stop — 2026-10-02](RESULTS/SSI_FINAL_RECOVERY_STOP_20261002.md) |
| Preserved source-run public evidence | [Final recovery transcript, case events, CSV and hashes](evidence/SSI_FINAL_RECOVERY_20261002T181736Z/README.md) |
| Earlier recovery batch and local pilot | [ZeroLab V2 first results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) |
| ZeroLab public evidence | [ZeroLab V2 evidence pack](evidence/ZERO_LAB_V2_20261002/README.md) |
| Separate CZARA / BODY 1.0 scope | [CZARA current status](CZARA_CURRENT_STATUS.md) |
| Completed first CZARA curriculum | [CZARA first training-cycle results](CZARA_FIRST_TRAINING_CYCLE_RESULTS_20261001.md), [run-level evidence](evidence/CZARA_FIRST_TRAINING_20261001/README.md) |
| ZeroLab scope and authority boundaries | [ZeroLab V2 architecture and authority](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md) |
| Earlier laboratory-design proposal | [CZARA ZeroLab / LAB_ARCHITECT](CZARA_ZERO_LAB_LAB_ARCHITECT_MODULE_20261001.md) |
| Separate future mission curriculum | [Dynamic Mission V6 installation and gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md) |
| Evidence and publication policy | [Contributing / evidence policy](CONTRIBUTING.md) |

The discussion used the title “Podsumowanie etapu S22”; the selected repair below concerns **ISKRA3 / S23-01-01**. A discussion title is not a case identifier.

The Final recovery cases are separate from the completed CZARA curriculum and from the 8/8 ZeroLab local-data pilot. ZeroLab readiness alone does not establish that the Final cases executed through ZeroLab. This repair record does not regrade those separate evidence families.

## 3. Incident identity and preserved baseline

```text
source_run = RUN_DOMAIN_20261002T181736Z_f600e74c
source_plan = DUP_01fe5854e782f647a46351d1
source_run_status = STOPPED_INFRASTRUCTURE
source_outcomes = 4 PASS / 3 INCONCLUSIVE / 0 FAIL

selected_actor = ISKRA3
selected_case = S23-01-01
ticket_id = DLAB_826115a59e72fe2dec7295786c72a4a3
R3_parent_fix_id = FIX_882d7d8c1aa444269ea67011
R3_followup_fix_id = FIX_e915b8ce24d8ce5a9df9589b
R4_field_only_fix_id = FIX_de76fb03b81689a7771b82e8
R4_selected_fix_id = FIX_b6acaa6f1656b0891f7d88c3
R4_selected_candidate_sha256 = 2397712b2b29978b5669be2c58b94bd8d635d5f2fc715b2fb8c3e0ccdf9205f3
R4_measurements_sha256 = 6f28dbcb46f2c8e17bb23a1e4b7841ab5ab78720803c3db39f9e316301585f1a
```

The run identity and counts are grounded in the linked public Final stop record. Repair identifiers and measurement hashes above are transcribed from operator-supplied logs. The original private signed artifacts have not been independently authenticated by this publication.

The older 2026-09-30 snapshot remains **848 PASS / 470 INCONCLUSIVE / 8 FAIL across 1,326 verdicts**. The two separately published 2026-10-02 recovery batches remain **14 distinct closed outcomes: 9 PASS / 5 INCONCLUSIVE / 0 FAIL**. Neither denominator includes the local R3/R4 repair comparisons.

## 4. Errors and open items

| ID | Affected path | Evidence and diagnosis boundary | Current status / required follow-up |
|---|---|---|---|
| AR-01 | ISKRA3 / S23-01-01 contract | Original candidate rejected with `LAB_OPERATION_FIELDS:merge:missing=[]:extra=["input_blocks"]`. Diagnosis reproduced a local contract failure; `input_blocks` was placed inside the operation rather than at the block level. | A locally passing variant exists; review and native execution remain open |
| AR-02 | S23 graph semantics | Moving a field alone was insufficient: R4 `DECLARE_CONCAT_INPUT_BLOCKS` compiled but passed only 4/24 comparisons. `SERIALIZE_IDENTICAL_ROOT_IDENTITIES` passed 24/24. | Local result established for the declared reference; broader semantic acceptance remains to be reviewed |
| AR-03 | Candidate-to-reviewer context | Subsequent review returned FAIL. The discussion's packet audit reported `candidate_matches_fix=true`, a merge with `inputs=["b_ingest"]` and `lab_op={"op":"identity"}`, and omitted proposal/control labels in the reviewer message. | Check the complete submitted graph and explicitly labelled measurements; rerun the review. A merge snippet alone does not establish that the complete graph was wrong or that the reviewer verdict was invalid |
| AR-04 | ISKRA2 / S21-01-02 | Original recovery outcome remained INCONCLUSIVE with `LAB_EXPRESSION_SHAPE`; tier limit reached. | No successful post-repair native result established in this assessment; retain as an open follow-up |
| AR-05 | ISKRA6 / S20-01-01 | Original candidate 1: `LAB_OUTPUT_MISMATCH`; candidate 2: `NO_CANDIDATE_GENERATED` / `INVALID_WORKER_JSON`; runner stopped. | A successful targeted repair/retest is not established here. Keep output, parsing and transport causes distinct until measured |
| AR-06 | Historical response / evidence completeness | Selected S23 diagnostic probes recorded an empty worker response on a historical backend call. The diagnostic did not probe current provider/socket health; scientific ambiguity stayed explicit. | Do not infer a current provider outage or attribute every INCONCLUSIVE result to one transport cause |

The diagnosed contract defect, local output mismatch, incomplete review context and unavailable model response are different failure classes. Fixing one does not establish that all remaining cases are resolved.

## 5. Repair chronology

| Observation date | Action / evidence | Observed outcome |
|---|---|---|
| 2026-09-30 | Operator stopped the broader S20-S26 run; targeted reliability diagnosis and repair package prepared | Historical snapshot retained; 17/17 offline repair tests reported in the original incident record |
| 2026-10-02 | IPC R2 checks and ZeroLab pilot; separate selected Final batch | 19/19 synthetic IPC tests; 8/8 local pilot; 5 PASS / 2 INCONCLUSIVE in the first Final batch — separate measurements |
| 2026-10-02 | Later Final continuation under the same recovery plan | 4 PASS / 3 INCONCLUSIVE; `STOPPED_INFRASTRUCTURE` |
| 2026-10-03 | Evidence V3 installer and check | 8 installer tests, 38 core tests and 17 scope tests passed; `CODE_READY`; checks called no models and did not perform live end-to-end validation |
| 2026-10-03 | Local S23 diagnosis | Contract rejection reproduced; diagnostic controls PASS; original result unchanged; no training verdict assigned |
| 2026-10-03 | R3 update and live follow-up investigation | 5 updater and 11 feedback tests passed; ISKRA4 / together-deepseek investigation produced `FIX_e915b8ce24d8ce5a9df9589b`, `RESOLUTION_FAILED` |
| 2026-10-03 | R4 update and bounded graph variants | 5 updater and 15 graph tests passed; field-only variant failed; selected graph variant passed 24/24 local comparisons; models called by local rule generation: 0 |
| 2026-10-03 | Subsequent review of the selected fix | Reported signed model verdict FAIL; previous observations retained |
| 2026-10-03 | Audit of review context; R5 / reassessment proposed | Review-message representation and labels identified for correction; successful execution of the proposed next step remains unconfirmed |

Counts from different test suites, pilot executors, case outcomes and comparison vectors stay separate. A live model-assisted investigation occurred in this sequence; the zero-call property applies only to the explicitly identified offline/local checks.

### Selected R4 result excerpt

The following is an abbreviated transcription of the operator's R4 result, not a replacement for its original signed files:

```json
{
  "ticket_id": "DLAB_826115a59e72fe2dec7295786c72a4a3",
  "selected_fix_id": "FIX_b6acaa6f1656b0891f7d88c3",
  "status_at_local_generation": "AWAITING_INDEPENDENT_REVIEW",
  "author_identity": "CODEX_ENGINEERED_LOCAL_GRAPH_RULES_V1",
  "proposal": {
    "comparison_status": "PASS",
    "tests": 24,
    "passed_tests": 24,
    "failed_tests": 0
  },
  "negative_control": {
    "comparison_status": "FAIL",
    "tests": 24,
    "passed_tests": 2,
    "failed_tests": 22
  },
  "models_called": 0,
  "training_verdict": null,
  "native_body_execution_verified": false,
  "original_grades_changed": false,
  "independent_review_at_local_generation": "NOT_RUN",
  "native_retest": "NOT_RUN",
  "automatic_replay": false
}
```

The later reviewer FAIL supersedes the waiting status as the latest observed review outcome for this attempt. It does not erase the local measurement or establish a final training FAIL. “Independent review” in the internal status denotes a separate review role/model; it is not external academic replication.

## 6. Evidence provenance for the new repair entries

| Source assessed | Content used | Publication boundary |
|---|---|---|
| `Wklejony tekst(20261002-234835).txt` | Evidence V3 installation, test counts and `CODE_READY` check | Operator-provided terminal transcript; local readiness checks |
| `Wklejony tekst(20261002-235133).txt` | S23 diagnosis, contract controls, historical response probes | Diagnosis preserved original result; no current provider probe |
| `Wklejony tekst(20261003-000654).txt` | R3 installation and unsuccessful live investigation | Actual installation/investigation outcome, not a planned run |
| `Wklejony tekst(20261003-061615).txt` | R4 installation, two variants, labelled proposal/control measurements and hashes | Actual local results; native execution and review not run at that output boundary |
| “Podsumowanie etapu S22”, 2026-10-03 review and packet-audit entries | Subsequent reported signed FAIL, candidate/context audit and proposed reassessment | Retrieved conversation evidence; successful reassessment not established |

Transcript filenames contain UTC-style timestamps; the record uses calendar dates in Europe/Warsaw. These filenames are provenance labels, not public download links. The selected results are reproduced above so this one-file record remains readable without access to private conversation history. Original runtime signatures and a complete replay bundle are not included in this publication.

## 7. Conditions for closing this repair record

All gates below remain open until their evidence references are added here. A prepared package, successful installer, local PASS or proposed command does not close the incident.

- [ ] **Review input verified:** bind the complete candidate graph, candidate hash, frozen protocol/criteria and separately labelled `proposal` / `negative_control` measurements to the actual reviewer request.
- [ ] **Review reassessment completed:** record the new review ID, reviewer identity, authorization, outcome and reasons. Preserve the earlier FAIL and its original request unchanged.
- [ ] **Native retest completed:** execute the repaired path in the intended Final BODY/agent runtime under the bound protocol; record execution receipts, measurements, final verdict and run identity. Local generation alone is insufficient.
- [ ] **Other incident items accounted for:** complete targeted checks for the S21 expression and S20 output/worker failures. Distinguish repaired infrastructure from any remaining task-capability limitation; retain valid FAIL/INCONCLUSIVE outcomes.
- [ ] **Regression and history checks completed:** verify that the repair preserves historical grades, evidence, frozen criteria and relevant runtime boundaries; record the checked version and results.
- [ ] **Closure entry completed:** record closure date, exact repair scope/version, supporting evidence, residual limitations and operator acceptance.

A completed infrastructure repair need not make every task PASS. It must establish a functioning execution/review path and preserve any measured capability failures. Closing this record also does not establish completion of S20-S40, Dynamic Mission V6, WEB training, external replication or physical validation.

## 8. How this single record is maintained

Append one dated entry per actual event with: affected issue/case, version or fix ID, action, observed result, evidence reference and remaining work. Mark ideas as **PROPOSED**, execution without a final result as **STARTED**, measured outcomes as **CONFIRMED**, and unresolved interpretation as **UNCONFIRMED**. These labels describe documentation evidence, not new runtime states.

Preserve unsuccessful attempts, controls, INCONCLUSIVE outcomes and prior reviewer verdicts. If an interpretation changes, add a dated correction rather than silently replacing the earlier observation. Do not retroactively count a repair comparison as a training success.

When every closure gate is supported, change the top status to **CLOSED — NAPRAWA ZAKOŃCZONA**, complete the closure entry below and retain this file at the same path. A later, separate incident gets its own identity; it does not erase this history.

### Update log

| Date | Entry | Evidence state |
|---|---|---|
| 2026-10-03 | Record opened; prior stop, Evidence V3 / R3 / R4 results, subsequent reviewer FAIL, pending reassessment and native retest collected | OPEN; no completed repair or new training qualification claimed |

### Closure entry

```text
closure_status = OPEN
closed_at = NOT_ESTABLISHED
accepted_repair_version = NOT_ESTABLISHED
new_review_id = NOT_ESTABLISHED
native_retest_run_id = NOT_ESTABLISHED
closure_evidence = NOT_ESTABLISHED
residual_limitations = review reassessment, native execution and related incident follow-ups remain open
```
