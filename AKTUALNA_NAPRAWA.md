# SSI V5 — Aktualna naprawa / Active repair record

**Status: OPEN — NAPRAWA W TOKU**  
**Record opened:** 2026-10-03  
**Last evidence assessment:** 2026-10-04, Europe/Warsaw  
**Scope:** SSI Final recovery, Evidence V3 / Dynamic Resolution Labs, ZeroLab repair rules, model review, native retests and bounded knowledge qualification.  
**Owner:** Paweł Jankiewicz.  
**Closure:** not established by the evidence available for this update.

> **Po polsku — aktualizacja 2026-10-04:** Potwierdzono nowe natywne wyniki PASS dla naprawianych przypadków ISKRA3 / S23-01-01 i ISKRA2 / S20-01-02, z różnym zakresem odtworzenia recenzowanej poprawki opisanym w sekcji 9. Najnowsza poprawka operatorów dla ISKRA5 / S21-01-03 przeszła 24/24 lokalne testy, uzupełniającą recenzję Qwen R16 i nowy natywny retest PASS. Retest odtworzył dokładnie recenzowaną poprawkę i ustawił `knowledge_eligible=true`; automatycznej konsolidacji nie wykonano. Naprawa pozostaje otwarta; nie ogłaszamy zakończenia szkolenia ani rozwiązania wszystkich problemów ZeroLab. Aktualne ustalenia są w sekcjach 9–10; wcześniejszy zapis pozostaje historią.

This file is the continuing repair record for this incident. New observations belong here, including unsuccessful attempts. Earlier dated reports remain snapshots of what was known at their publication dates. This record supplements them with subsequent repair evidence; it does not overwrite their verdicts or declare the training complete.

## 1. State recorded on 2026-10-03 — preserved snapshot

The table below records the earlier assessment. Subsequent results and the current open boundary are in [section 9](#9-update-2026-10-04--native-retests-qualification-and-r16-review).

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

## 4. Errors and open items recorded on 2026-10-03

These entries preserve the original diagnosis and then-required follow-up. Section 9 records subsequent progress; a newer case or fix is not silently substituted for an older one.

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

At the 2026-10-03 assessment, the later reviewer FAIL superseded the waiting status as the latest observed review outcome for this attempt. Subsequent reassessment is recorded in section 9. It does not erase the local measurement or establish a final training FAIL. “Independent review” in the internal status denotes a separate review role/model; it is not external academic replication.

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

These are incident-wide closure gates. Section 9 records completed steps for specific cases, but the full set of incident items has not been closed. A prepared package, successful installer, local PASS or proposed command does not close the incident.

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
| 2026-10-04 | Added subsequent native retests, bounded Challenger qualification, preserved batch failures and R16 supplemental review in section 9 | OPEN; latest ISKRA5 fix READY_FOR_RETEST; no latest native retest result supplied at that update |
| 2026-10-04, follow-up | Added ISKRA5 / S21-01-03 native PASS with exact reviewed-fix reproduction in section 10 | Case retest PASS; knowledge eligible; no automatic consolidation or general OR/NE activation |

### Closure entry

```text
closure_status = OPEN
closed_at = NOT_ESTABLISHED
accepted_repair_version = NOT_ESTABLISHED
new_review_id = NOT_ESTABLISHED
native_retest_run_id = NOT_ESTABLISHED
closure_evidence = NOT_ESTABLISHED
residual_limitations = remaining incident follow-ups, general OR/NE rule qualification and activation, and sustained training stability remain open; see sections 9–10
```

## 9. Update 2026-10-04 — native retests, qualification and R16 review

**Evidence status: CONFIRMED IN OPERATOR-SUPPLIED RESULTS; incident remains OPEN.** This section preserves the update at the R16 review boundary; the later native retest result is in section 10. This update records results supplied after the 2026-10-03 assessment. The public entry is a transcription and assessment of those results, not an independent authentication of the private evidence store or an external replication.

### Completed steps and their exact scope

| Track | Confirmed result | Remaining boundary |
|---|---|---|
| Earlier S23 review reassessment | `RREV_fce64abe1e661aaf1791dede` returned PASS / READY_FOR_RETEST for `FIX_b6acaa6f1656b0891f7d88c3`; earlier FAIL preserved | Subsequent attempts included an unresolved run and new INCONCLUSIVE outcomes; this review alone did not resolve the case |
| ISKRA3 / S23-01-01 expression repair | `FIX_82c3bc8078dd6df873d90216`, independently reviewed under `QREV_395218ff7276bc2a94396da2`; native retest `RUN_DLAB_RETEST_20261004T083807Z_371f3dac` returned PASS; `exact_reviewed_fix_reproduced=true`, `knowledge_eligible=true` | Original INCONCLUSIVE preserved; automatic consolidation remained false |
| R12 expression-rule qualification | 96 engineered paired cases: 32 improvements, 0 regressions; skill `SKILL_a381f1a3bb3ccddd4077aaa0591f8f96` registered as CHALLENGER | Qualification was engineered contract validation, not an unseen external holdout; qualification itself did not promote a Champion |
| R13 training batch and report repair | `RUN_DOMAIN_20261004T112724Z_7b282c51`: 5 PASS / 1 INCONCLUSIVE, 6 measured of 7 selected; signed-run diagnostic reported integrity PASS and sealed=true. Report R2 handled the nullable evidence field without the earlier AttributeError | Batch retained STOPPED_INFRASTRUCTURE. All five final PASS candidates were UNCHANGED_VALID: this batch does not demonstrate five automatic repairs |
| ISKRA2 / S20-01-02 conditional repair | `FIX_8d4a655dc4222dd3e79db0b4` passed model review; `RUN_DLAB_RETEST_20261004T123928Z_8b9088ac` returned PASS with an identical graph and compiled program | Full response changed. Original retest flags remained `exact_reviewed_fix_reproduced=false` and `knowledge_eligible=false` |
| R14 conditional-rule qualification | Separate graph-scoped qualification: 96 engineered paired cases, 32 improvements, 0 regressions; `SKILL_46084d49ba2e8d9029a1c5d5f2c60c72` registered as CHALLENGER | Preserved the stricter full-response gate and its earlier flags. General-rule independent review and consolidation were NOT_RUN at qualification |
| Latest ISKRA5 / S21-01-03 operator repair | 24/24 local comparisons PASS; intentionally incorrect control failed 22/24. R16 supplemental Qwen review returned PASS / READY_FOR_RETEST | New native retest outcome has not been supplied; no new training verdict or knowledge eligibility established |

These are distinct measurements and runs, not a combined success rate. In particular, ISKRA2 / **S20-01-02** is not the older ISKRA6 / **S20-01-01** or ISKRA2 / **S21-01-02** follow-up. Their similar identifiers do not establish closure of AR-04 or AR-05.

### Latest open case: ISKRA5 / S21-01-03

The source run `RUN_DOMAIN_20261004T153618Z_0ee16590` recorded INCONCLUSIVE. Its current expression failed the bound contract with `LAB_EXPRESSION_SHAPE`. The recorded R15 conditional-rule application declined the candidate rather than granting a result.

A separate engineered operator-shape repair produced three AST corrections under `OR_NE_KEYS_TO_OP_ARGS_V1`. Local measurements accepted the corrected candidate and passed all 24 frozen comparisons. This generated a proposal for review; it did not activate a general runtime repair rule.

The first Qwen request returned HTTP 200 but the validator rejected its evidence-binding representation. The recorded JSON values matched diagnostically; whitespace followed the binding prefix. Crucially, the raw model verdict was also **PARTIAL**, with substantive evidence-completeness concerns. Correcting whitespace alone could not turn that response into PASS.

R16 supplied a fuller, explicitly scoped evidence packet and a binding parser that accepts equivalent JSON formatting while enforcing the expected values. It obtained a **new** review and preserved the earlier rejected response and its PARTIAL verdict. The candidate and frozen protocol, criteria and vectors remained bound to the same hashes.

| R16 operator result | Observation |
|---|---|
| Revision | `SSI_QWEN_EVIDENCE_SUPPLEMENT_R16` |
| Offline installer suite | 19/19 tests PASS in 171.880 s; synthetic provider transport, zero model calls |
| Installed-system check | `doctor_after=READY_FOR_BOOT` |
| Runtime restart | BODY_FROZEN and ISKRA1..6: 7/7 READY; no training started by restart |
| New model calls in supplemental review | 1 |
| Reviewer identity | `Qwen/Qwen3.5-9B` via `together-qwen35-review` |
| Accepted review result | PASS; `blocking_scope=NONE`; `state=READY_FOR_RETEST` |
| New training verdict | null |
| Native retest | `NOT_RUN_BY_THIS_OPERATION`; no later result supplied for this update |
| Knowledge / consolidation | `knowledge_eligible=false`; `automatic_consolidation=false` |
| Runtime activation | `NO_NEW_RULE_ACTIVATED` by R16 |
| History and limits | Historical records preserved; grades, campaign plan and budget unchanged |

The installer reported no change to existing runtime implementation code, but did report a changed runtime dependency identity; the required restart was subsequently completed. The zero-model-call property applies to installation and restart, not to the live supplemental review.

#### Binding references

```text
ticket_id = DLAB_b0ab5cec6f3ec31fd9d8d882a7775863
actor = ISKRA5
case_id = S21-01-03
fix_id = FIX_8098d99dbf00edf8209874fc
fix_sha256 = 55297938eb7ad2101f3a65a7239a10d4842098731a593d271a43b1d7e945ad8c
review_id = QSUP_5b7e4627e74c131adacdbd27
parent_review_sha256 = 6008040c4682c5032d1a5186c96c5266fc07140436ef0cf7292093859e2407ff
protocol_sha256 = a612fab830c1430dbdf89c4e349957a58108e3340a7ae3d90550d220c0c4b31b
criteria_sha256 = e01b4b9015099b2c743be624a73a499eebbd0d976ae9ef8bfebabcb08d827a9d
test_vectors_sha256 = b2cd0451e939b602601fc93d414cd9d7bbe0689633f6bdbcf74872b51d918a97
review_authorization_sha256 = 10e7747ad2cea41b70d63d99cebdb69fb08ee99e82b478779130b5824ce0c975
latest_native_retest_result = NOT_SUPPLIED
```

The latest installation, restart and live-review observations come from operator transcript `Wklejony tekst(20261004-163336).txt`. The preceding repair, review and retest entries are transcribed from the corresponding operator outputs, identified above by their run, fix and review IDs. Hashes are traceability references; listing them does not itself verify a signature.

“Independent” here means a reviewer with a distinct model identity from the contributing author identities, not an independent institution. Local data tests and frozen simulated observations do not establish physical-device validation.

### Research maturity and immediate next gate

**Ocena etapu R&D:** Jak na projekt prowadzony przez jedną osobę, udokumentowany zakres obejmuje znaczną pracę integracyjną: wykonawców, laboratorium, recenzentów, kontrolę kosztów i historię dowodów. W wybranych przypadkach pokazano cały ciąg od zachowanego INCONCLUSIVE przez diagnozę, poprawkę, kontrolę negatywną i recenzję do nowego natywnego PASS. To uzasadnia opis zaawansowanego prototypu badawczego. Powtarzające się ręczne poprawki integracji pokazują jednak, że stabilność i automatyzacja nadal wymagają pracy. Dłuższe przebiegi bez interwencji, testy poza przygotowanymi zestawami i niezależne odtworzenie wyników są kolejnymi potrzebnymi dowodami; obecny zapis nie ustanawia przewagi nad innymi projektami ani przełomu naukowego.

The next gate is the native retest bound to `QSUP_5b7e4627e74c131adacdbd27`, followed by verification of its actual verdict, evidence and candidate-reproduction scope. A supplied command is not a completed run. Any knowledge qualification or general-rule activation requires its own recorded checks.

Current work remains focused on training reliability and ZeroLab repairs. Universal Lab interface work and a repository-wide status refresh are deferred. This publication updates **only this continuing repair record**.

## 10. Follow-up 2026-10-04 — ISKRA5 native retest PASS

**CONFIRMED IN OPERATOR-SUPPLIED RESULTS.** The operator subsequently executed the native retest bound to the R16 supplemental review. This supplies the outcome that was still pending when section 9 was published.

| Field | Recorded value |
|---|---|
| Actor / case | ISKRA5 / S21-01-03 |
| Ticket | `DLAB_b0ab5cec6f3ec31fd9d8d882a7775863` |
| Fix | `FIX_8098d99dbf00edf8209874fc` |
| Review selected in the command | `QSUP_5b7e4627e74c131adacdbd27` |
| New run | `RUN_DLAB_RETEST_20261004T163448Z_15836c5a` |
| Preserved parent run | `RUN_DOMAIN_20261004T153618Z_0ee16590` |
| Original / new verdict | INCONCLUSIVE / PASS |
| Native candidate evaluation / CI | PASS / PASS |
| Training event | VERIFIED / CASE_VERIFIED; no reported reasons |
| Exact reviewed fix reproduced | true |
| Knowledge eligible | true |
| Historical grade changed | false |
| Automatic consolidation | false |

The protocol and criteria hashes match the reviewed case recorded in section 9:

```text
protocol_sha256 = a612fab830c1430dbdf89c4e349957a58108e3340a7ae3d90550d220c0c4b31b
criteria_sha256 = e01b4b9015099b2c743be624a73a499eebbd0d976ae9ef8bfebabcb08d827a9d
new_evidence_head_sha256 = 3d3a08b1034ab33884d9c6480185e877a259e913d519120b852cbb493a2e6a97
new_case_sha256 = 4c34f0167eb6cb7f1dc6c99fe244fe23f7676e67534d55a1297d1ebfd1b21634
```

This establishes a new native PASS for the exact reviewed correction within this case's declared scope. The earlier INCONCLUSIVE and rejected review remain part of the history. Knowledge eligibility permits the next qualification step; it does not itself register, promote or activate a general repair skill.

**Training continuation boundary:** the installed R15 launcher and campaign enforce a cumulative maximum of seven measured trial cases. Remaining trial slots may be used through the existing checks; publishing this result does not expand that policy. Full-queue continuation requires an explicit subsequent campaign transition. The general OR/NE repair has not been activated by this retest.

Source: the operator's 2026-10-04 terminal output for the run identified above. This one-file publication does not independently authenticate the private signed artifacts, establish completion of the remaining training queue or close every ZeroLab issue.
