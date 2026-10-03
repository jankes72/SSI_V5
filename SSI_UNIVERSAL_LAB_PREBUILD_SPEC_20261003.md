# SSI V5 — Universal Meeting and Benchmark Laboratory

**Author:** Paweł Jankiewicz  
**Recorded:** 2026-10-03  
**Specification version:** 1.0  
**Status:** PRE-BUILD INTEGRATION PLAN / RESULTS NOT PRECLAIMED  
**Base:** existing Lab Mexyk / Mexico research module  
**Target roles:** CZARA, Director_Czary, BODY_FROZEN_1_0 and ZeroLab in the CZARA scope

This document records the intended integration before construction of the complete module. It describes requirements and acceptance conditions. Existing SSI components and their published results remain separate from the proposed meeting, translation, laboratory and consolidation integration.

## 1. Purpose and architectural base

The existing Lab Mexyk is to be extended into a common environment for multilingual research meetings, ordinary conversations, grant presentations and partner-defined benchmarks. The Mexico research profile remains one application of the same platform.

Participants should be able to speak in their own languages, define an experiment together, observe its execution and trace its results to recorded measurements. The module combines communication with a bounded research workflow.

Integration should reuse the existing engines, routing, supported adapters, BLOCKS, micronetworks, Champion mechanisms and evidence infrastructure. Before implementation and before each benchmark, the actual installed versions, checkpoints, contracts and readiness must be recorded. "Latest" means the latest verified compatible state available to the installation.

| Component | Target responsibility |
|---|---|
| CZARA | Preserve original and translated conversation context from both sides; identify roles, questions, hypotheses and revisions; initiate permitted shadow work. |
| Director_Czary | Interpret the benchmark request, prepare the protocol, coordinate resources and execution, and explain the evidence. |
| BODY_FROZEN_1_0 | Check input completeness and execution resources, run supported methods through adapters, and return execution evidence. |
| ZeroLab — CZARA scope | Retain versioned protocols and methods, measurements, comparisons, execution records and separate main/shadow results. |

Director_Czary and BODY_FROZEN_1_0 retain their distinct runtime identities. Director_Final, Final BODY_FROZEN and ISKRA1–ISKRA6 remain the separate SSI Final scope. Sharing infrastructure or transferring compatible competence does not merge these identities.

The universal interface is extensible through adapters. Each benchmark domain requires declared inputs, executable methods, measurement definitions and appropriate resources. A new adapter expands the supported research scope.

## 2. Meeting room and bidirectional translation

Participants join a browser session through a meeting link. The room contains video, audio, translated chat and a shared laboratory panel. Each session has a topic, participants, roles, language settings and a declared scope of permitted actions.

Polish is the author's working language. A partner may use another supported language, initially including English or Spanish as target examples. Translation works in both directions: Polish to the partner's selected language and the partner's language to Polish.

Each participant independently selects:

- **Translated voice:** synthesized speech in the selected language, with control of translated and original audio levels.
- **Translated captions:** original audio with translated text.
- **Voice and captions:** both forms together.

The participant can change this selection during the meeting. Chat retains both the original message and its translation for the recipient. Speaker language and recipient language are separate settings.

Each conversation segment records its author, language, timestamp and session context. Corrections to recognized speech or translation remain linked to the original version. Numbers, units, formulas, technical identifiers and component names must be preserved. Uncertain recognition must be visible, with a way to repeat or confirm a segment before it is used in a research protocol.

Translation alone does not start laboratory jobs. Conversation retention, material sharing and session access settings are visible to participants. Reconnection should restore the same session and its retained history.

Speech recognition, translation and synthesis services will be selected after quality, latency and cost measurements. This specification does not preclaim a particular latency or error-free technical translation.

## 3. Benchmark initiation from either side

Both sides have a **Start benchmark** control. An authorized participant opens the shared task form and writes the request in a supported language. The request retains its original text, translation and author. Director_Czary receives these alongside the structured experiment fields.

| Form field | Required content |
|---|---|
| Research question and objective | What is being tested and which hypothesis is being assessed. |
| Inputs and resources | Data, files or input vectors; adapter; environment; required equipment. |
| Methods | SSI configuration under test and the reference method for comparative studies. |
| Evaluation criteria | Metrics, units, PASS / FAIL / INCONCLUSIVE conditions and evaluation rules. |
| Trials and initial state | Repetitions, starting conditions, checkpoint, learning/adaptation policy. |
| Limits and shadow scope | Time, resource and cost bounds; permitted shadow work and participant actions. |

The target execution sequence is:

1. Director_Czary structures the request, identifies missing information and prepares the protocol. BODY_FROZEN_1_0 checks whether the inputs, resources and adapter support execution.
2. An authorized participant approves the complete protocol. The system records its version, criteria, execution configuration and benchmark identity.
3. Director_Czary delegates the supported method to BODY_FROZEN_1_0. ZeroLab records the measurements and result against the specific protocol and method versions.
4. Both sides observe the same trial. Repeated submission, double-clicks and reconnects must not create an unintended second execution. A deliberate repeat has its own trial identity.
5. The shared panel presents the result and its limitations. Changing criteria or the selected method creates a new research revision.

Start, pause and stop rights follow session roles. Meeting participation grants only the declared research permissions; administrative runtime access remains a separate authority.

## 4. CZARA and shadow experiments

The **Enable CZARA** control activates analysis of eligible statements from both sides. CZARA preserves sources, identifies questions, hypotheses, corrections and contradictions, and connects them to the meeting topic or focused experiment.

Shadow execution has an explicit session setting. In **CZARA + shadow** mode, CZARA may initiate experiments within the previously authorized topics, adapters and resource limits, using Director_Czary, BODY_FROZEN_1_0 and ZeroLab. Individual jobs inside that scope can proceed automatically. Work outside the declared scope requires a corresponding authority or protocol revision.

A shadow hypothesis may arise from the author's statement, the research partner's proposal or the combination of both. Its record must show which conversation segments prompted the hypothesis, what changed in the method and what was actually executed.

During an ordinary conversation, a focused standalone shadow experiment may be created from the session topic if the required inputs and permissions are available. Otherwise the proposal remains a draft with explicit missing information.

### Main and shadow result separation

The main benchmark and each shadow retain separate identities, methods, measurements and results. The panel shows their relationship while preserving their evidence paths.

A frozen main benchmark continues with its declared configuration. Later conversation and shadow findings do not silently change that configuration or replace its result. If adaptive feedback is itself the research subject, its permitted behavior must be defined in the protocol before execution.

Selecting a shadow direction for further research creates a new main revision and a new execution. Earlier PASS, FAIL and INCONCLUSIVE records remain retained. Qualification and consolidation of a competence discovered through shadow work are subsequent verified steps.

The shared panel shows the shadow queue, initiation reason, progress and resource use. Additional work respects the main experiment's declared priority, installed slot capacity and session cost limits.

## 5. Online laboratory and inspectable measurements

The laboratory panel should display live execution and allow replay of a completed trial from retained data. Participants should be able to move from a result to the observations and materials that support it.

| View | Inspectable content |
|---|---|
| Execution timeline | Start/end events, decisions, state changes, errors, pauses and interventions. |
| Measurement detail | Metric name, value, unit, source, timestamp, calculation method and trial identity. |
| Comparison | Reference method, main SSI execution and separate shadow results under declared conditions. |
| Repeated trials | Individual outcomes, repetition count, dispersion and statistical calculation method. |
| Visualization | Charts, states and adapter-supported trajectories or replay derived from recorded events. |
| Evidence | Inputs, protocol, method and runtime versions, logs, execution receipts and integrity information. |
| Export | Report and available measurement data, such as CSV or JSON, with a stated reproducibility scope. |

Each reported value must identify whether it is **measured, simulated, estimated or unavailable**. Software execution time is a software measurement; physical robot response requires an appropriate physical measurement path.

Uncertainty estimates, intervals and statistics are shown where the repetitions and calculation method justify them. Missing data remain visible. Negative and inconclusive outcomes remain available alongside positive outcomes.

Both sides see the same numerical data and identifiers. CZARA translates descriptions. Any optional unit conversion retains the original value and an explicit conversion rule.

Partner-visible reports expose selected sanitized evidence and state which checks can be reproduced from the export. Proprietary source, agent memory, credentials and administrative configuration remain private. Evidence-integrity claims must match the controls actually performed; a local hash chain alone is not an independent audit.

## 6. Consolidation across the three roles

The module is intended to use accumulated SSI V5 competence and verified CZARA training. Transfer must retain contracts, versions, qualification evidence and recipient-specific compatibility. Each recipient keeps its own identity, history, memory and role.

| Source | Intended recipient and use |
|---|---|
| Verified SSI V5 Director competence | Director_Czary: compatible planning, coordination and research interpretation competence. |
| Verified SSI V5 BODY_FROZEN competence | BODY_FROZEN_1_0: compatible execution methods, BLOCKS, micronetworks and Champion packages. |
| Verified CZARA checkpoint | CZARA in the meeting module: its qualified context, translation, role and revision capabilities. |
| Newly verified laboratory findings | Role-appropriate competence packages for CZARA, Director_Czary and BODY_FROZEN_1_0. |

The target consolidation process is:

1. Select confirmed source checkpoints and create a manifest of competence, dependencies, versions, restrictions and qualification evidence.
2. Check contract compatibility and validate the competence in the recipient environment. Source-system success requires recipient-side confirmation of compatible use.
3. Activate an accepted package as a new checkpoint, retaining the previous state, transfer record and rollback path.
4. Bind the exact active checkpoint to each benchmark. Later consolidations have their own records and do not rewrite a completed experiment's history.

CZARA remains responsible for research context and permitted shadow initiation. Director_Czary remains the coordinator. BODY_FROZEN_1_0 remains the executor. Consolidation transfers compatible verified competence; it does not transfer core identity or imply model-weight retraining.

A raw statement, successful installation, local repair test or shadow result does not automatically qualify a new skill. Appropriate measurements, evaluation, recipient validation and a recorded promotion are required. Learning and consolidation during a benchmark must follow the policy declared in its protocol.

## 7. Existing evidence and proposed integration

The following summarizes the public documentation reviewed on 2026-10-03. Implementation must still inventory the actual current private code and installed state before changing it.

| Element | Documented evidence boundary |
|---|---|
| Lab Mexyk | Mexico panel, Director/BODY communication and laboratory/evidence foundations are described as implemented or prepared. The complete proposed meeting module remains an integration target. |
| First CZARA curriculum | Final checkpoint: 160/160 PASS and 520/520 qualified skills for the specified internal curriculum. These totals do not qualify the new complete integration. |
| Frozen CZARA evaluation | 24 validation and 16 Champion evaluations PASS / REUSE, with learning disabled. |
| ZeroLab V2 pilot | BODY_FROZEN_1_0 participated in the reported 8/8 local record-transformation pilot; training_pass=false and models_called=0. This is narrower than conversational or physical validation. |
| Conversation, shadow and main revision | Implemented workflow is described in the V2 documentation. The pilot does not establish the complete conversational sequence end to end. |
| Cross-scope consolidation | Read-only Final hints are available to Director_Czary in the reviewed integration. Full transfer and common consolidation for all three proposed roles are not established by those results. |

The new integration scope comprises the shared audio/video room, independent translation preferences, benchmark initiation on both sides, CZARA analysis of both sides, bounded shadow execution, the online measurement interface and validated role-specific consolidation.

Integration should preserve existing resource controls, accounting, histories and checkpoints. Repairs in progress retain their confirmed status. Installation or a local repair PASS must not be presented as completion of this module.

Use for another grant or domain requires the appropriate protocol, metrics and adapters. The extensible interface does not establish eligibility for every funding call or support for arbitrary equipment.

### Source documents

- [CZARA current status and role boundaries](CZARA_CURRENT_STATUS.md)
- [ZeroLab V2 architecture, authority and consolidation boundaries](SYSTEM/ZERO_LAB_V2_ARCHITECTURE_AND_AUTHORITY_20261002.md)
- [Mexico pre-benchmark R&D protocol](MEXICO_PREBENCHMARK_RND_PROTOCOL_20260928.md)
- [ZeroLab V2 first results and provenance](ZERO_LAB_V2_FIRST_RESULTS_20261002.md)
- [Current repair record](AKTUALNA_NAPRAWA.md)

## 8. Acceptance conditions and implementation sequence

Acceptance requires a recorded full session using real compatible components. Transport tests, interface mockups and local adapter checks remain separately identified verification levels.

| Acceptance check | Required evidence |
|---|---|
| Bidirectional communication | Polish and the selected partner language work in voice and chat; voice/caption choices are independent; quality and latency are measured. |
| Meaning preservation | Technical terms, numbers and units are preserved; uncertainty and corrections remain visible in history. |
| Benchmark controls on both sides | Either authorized participant can request a trial; repeated clicks and reconnects do not duplicate execution. |
| Protocol and authority | Missing inputs block execution with an explanation; criteria changes create revisions; session permissions are respected. |
| CZARA and shadow | Statements from both sides retain sources; shadow stays within its authorized scope and preserves the main result. |
| Online laboratory | Charts and values match retained measurements; exports support the declared verification checks. |
| Consolidation and rollback | Source packages, recipient tests, new checkpoints and rollback are documented for all three roles. |
| Complete research execution | A partner request passes through Director_Czary to BODY_FROZEN_1_0 and ZeroLab; main, shadow and reported outcomes retain complete supporting evidence. |

Implementation should proceed in this order:

1. Inventory the current Lab Mexyk code, integration points, versions, contracts and verified checkpoints.
2. Connect the shared text benchmark form to the existing execution and evidence path; verify the basic request-to-result sequence.
3. Add translated chat, followed by audio/video and independent voice/caption controls.
4. Integrate CZARA context from both sides, bounded shadow execution and the shared measurement panel.
5. Validate source-competence imports and subsequent consolidation using retained checkpoints and a rollback test.
6. Run an internal rehearsal of the full meeting and freeze the verified version for the first external session.

Schedule and cost estimates require the code inventory and service measurements. This publication records the intended scope before construction; completed deployment, external benchmark success, physical validation and independent replication require their own subsequent evidence.
