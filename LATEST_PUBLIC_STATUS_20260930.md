# SSI V5 — Latest Public Status

**Snapshot date:** 2026-09-30 (Europe/Warsaw)  
**Source repository commit:** `9562bcd3e61031a2621ef303b24e17cbba26cbcd`  
**Scope:** public evidence mirror of the private runtime; internal software training and installation records.

This snapshot reconciles the published S20 runtime excerpt, the parallel core/CZARA integration note, the V6 installation/gate note and the operator update that both core and CZARA training continue. It is not a live connection to the private machine.

## Current training snapshot — 2026-09-30

The operator reports that core SSI training continues alongside CZARA. The public S20 log is a partial capture of `RUN_20260929T212837Z_92e516e1`, not a final stage report.

| Track | Latest published state | Evidence scope |
|---|---|---|
| Core S20-S40 | S20 started; core training reported ongoing | S20 excerpt: 116 unique completed cases, 79 PASS, 37 INCONCLUSIVE, 0 FAIL; full-stage completion not established |
| S19 recovery / pre-S20 hardening | Startup banner reports hardening PASS and S19 COMMITTED | Operator-supplied log; transaction journal and detailed gate reports are not included in this excerpt |
| CZARA Live Training | Running alongside core training | Internal integration snapshot; 160-item curriculum = 120 training + 24 frozen validation + 16 frozen Champion benchmark; final completion not published |
| Dynamic Mission V6 | Installed; scheduler active; waiting for CZARA completion | 0/72 live missions at the recorded snapshot; 48 training + 12 frozen validation + 12 frozen blind Champion |
| WEB01-WEB24 | Installed / READY; gated after S40 | Requires S40 execution completion and COMMITTED consolidation; live completion not published |
| Mexico external benchmark | Planned | Internal simulations do not establish Mexico-side execution or independent validation |

The S20 excerpt covers BODY_FROZEN, ISKRA1, ISKRA2 and part of ISKRA3. It declares seven actors and 210 assignments, but does not include results for the entire stage. All captured verdicts remain visible, including the 37 INCONCLUSIVE rows. The excerpt contains no FAIL rows; the final stage outcome is not established.

V6 adds complete evolving experiments with a simulated professor and four experts, DIRECTOR-managed MAIN/SHADOW branches and explicit formal promotion. Installer self-tests are recorded separately from live mission results. The planned 48-stage Mexico robotics curriculum, the 160-item CZARA curriculum and the 72-mission V6 curriculum are distinct programmes.

Current sources:
- [Machine-readable current snapshot](RESULTS/SSI_V5_CURRENT_PUBLIC_STATUS_20260930.json)
- [Supplied S20 runtime log](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log)
- [Parallel core/CZARA integration simulation](MEXICO_PARALLEL_INTEGRATION_SIMULATION_20260929.md)
- [V6 installation, self-tests and post-CZARA gate](DYNAMIC_MISSION_ORCHESTRATOR_V6_INSTALL_AND_GATE_20260930.md)

The earlier S19 incident and pre-S20 preregistration remain historical evidence. S20 startup is now recorded; the excerpt does not independently audit all prerequisite gates or the S19 commit.

## S20 excerpt accounting

The supplied log contains 116 `[CASE_DONE]` rows with distinct actor/case pairs:

| Actor | Completed rows in excerpt | PASS | INCONCLUSIVE | FAIL |
|---|---:|---:|---:|---:|
| BODY_FROZEN | 30 | 21 | 9 | 0 |
| ISKRA1 | 30 | 19 | 11 | 0 |
| ISKRA2 | 30 | 20 | 10 | 0 |
| ISKRA3 | 26 | 19 | 7 | 0 |
| **Excerpt total** | **116** | **79** | **37** | **0** |

The excerpt ends at request `ssi-s20-iskra3-s20-05-03-a1`, before that case's completion. These counts describe the captured text only. They are not a current progress percentage, a 210-case final score, or a seven-actor completion claim.

Source: [raw S20 excerpt](evidence/S20_20260929/S20_LIVE_EXCERPT_RUN_20260929T212837Z_92e516e1.log). SHA-256 of the exact published UTF-8 source:

```text
33777eaab647fb52af17164b57d78af545561e1053c15d74015bb16614b8ecf8
```

The header states `PRE-S20 HARDENING PASS + S19 COMMITTED`. This supersedes the older navigation statement that S20 had not started. It records a runtime-reported recovery, not an independent journal-level verification. The same log declares `EVIDENCE_CHAIN LOCAL_DEVELOPMENT external_pilot_ready=False`; external notary readiness is not established.

## What changed since the S19 incident

The [earlier S19 report](RESULTS/SSI_V5_S19_OBSERVABILITY_INCIDENT_AND_PRE_S20_STATUS_20260929.md) recorded 210/210 executed cases (182 PASS, 24 INCONCLUSIVE, 4 FAIL) and a blocked post-stage consolidation. Those verdicts are preserved. The later S20 startup reports recovery without rerunning S19 cases.

The [pre-S20 preregistration](SYSTEM/SSI_V5_PRE_S20_OBSERVABILITY_AND_EVIDENCE_HARDENING_PREREGISTRATION_20260929.md) and [Hamid Ahmadian attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md) remain the requirement/provenance records. The startup banner is not a substitute for publishing individual gate results.

## Distinct training paths and gates

| Programme | Declared size | Relationship |
|---|---|---|
| Core SSI | S11-S40 | S11-S19 results retained; latest captured stage S20 |
| WEB engineering | 24 stages / 192 cases / 7 actors | Configured after S40 completion and committed consolidation |
| CZARA Live Training | 160 items: 120 + 24 + 16 | Active internal multilingual research-session training |
| Dynamic Mission V6 | 72 missions: 48 + 12 + 12 | Scheduler waits for CZARA completion; no completed live mission in published snapshot |
| Mexico robotics plan | 48 stages: 38 training + 4 validation + 6 capstones | Planned research programme leading to later partner-defined benchmarks |

The core-to-WEB gate and the CZARA-to-V6 gate are separate. No requirement that V6 wait for S40 is established by these sources.

## Research roles and benchmark integrity

CZARA preserves original language, translation, roles and research context. DIRECTOR manages experiment contracts, revisions and routing decisions. BODY_FROZEN executes technical work; LAB and evidence records support verification.

In V6, MAIN is the official experiment. SHADOW is an exploratory variant authorized by DIRECTOR. A SHADOW may become official only through an explicit matching professor-level revision and recorded promotion. The self-test reports controls for both matching and incorrect anticipation; live effectiveness is not yet measured.

The [Mexico pre-benchmark protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md) separates collaborative R&D from official scoring. Its first intended baseline uses DIRECTOR, BODY_FROZEN, OFFLINE_DIRECTOR and CZARA, with ISKRA comparisons later. Internal simulated participants do not count as independent external researchers.

## Preserved results and open evidence

Preserved results include the [V4 S1-S10 baseline](RESULTS/V4_S1_S10_AND_POST_S10_RESULTS_20260917.md), [Dual Mother software laboratory](RESULTS/DUAL_MOTHER_CROSS_LAB_V1_20260918.md), [S11/S12 results](RESULTS/SSI_V5_S12_LIVE_TRAINING_AND_CONSOLIDATION_20260926.md) and [S13-S18 routing/recovery results](RESULTS/SSI_V5_S13_S18_ROUTING_AND_RECOVERY_UPDATE_20260929.md). Their original dates and scopes remain authoritative.

Still required for stronger claims: final S20 and later-stage reports, transaction-bound S19 recovery evidence, detailed hardening gate results, final CZARA results, actual V6 mission/validation/blind results, controlled routing/cost comparisons, remote two-endpoint rehearsal and independent partner-defined benchmark evidence.

Full S20-S40 completion, WEB completion, completed CZARA/V6 qualification, successful live MAIN/SHADOW promotion, Mexico-side execution, physical validation, safety certification and independent external replication are not established by this snapshot.
