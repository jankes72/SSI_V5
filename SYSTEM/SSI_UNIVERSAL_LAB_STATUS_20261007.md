# SSI Universal Lab — installed state and next integration boundary — 2026-10-07

**Role:** dated public installation/status record for the Universal Lab workstream  
**Repository boundary:** architecture, installation state, measured preparation counts and conservative integration claims only  
**Implementation boundary:** proprietary source code, credentials, private prompts and reconstructive runtime internals are intentionally excluded  
**Evidence boundary:** this document does not convert planned integration into completed evidence

> Canonical architecture: [SSI V5 — C4 Architecture](../SSI_V5_C4_ARCHITECTURE.md)

## 1. Current operator-verified installation

The current operator machine retains **Universal Lab Live Gate R3** as the installed baseline.

| Item | Current state |
|---|---|
| Package lineage | `SSI_UNIVERSAL_LAB_LIVE_GATE_V1_1_R3` |
| Reported installed version | `1.1.1` |
| Compatibility module name | `UNIVERSAL_LAB_LIVE_GATE_V1` |
| Local bind | `127.0.0.1:8090` |
| Persistent database | SQLite `live_gate.sqlite3` |
| Password storage | scrypt-derived password hashes |
| Sessions | server-side authenticated sessions |
| Installed accounts | `pawel`, `sara`, `leire` |
| Current account roles | `pawel=ADMIN`; `sara/leire=RESEARCH_GUEST` |
| Database preservation across R3 install | reported preserved |
| Tailscale availability at install | reported available |
| Native SSI runtime socket at preflight | **not bound / false** |
| Bridge policy | **fail-closed; disabled until explicitly configured and tested** |

The installed R3 baseline therefore establishes the external-facing web/auth/session foundation, but it does **not** establish that Director, CZARA, Router V10, BODY_FROZEN or ZeroLab are already live-bound through the Universal Lab UI.

Synthetic UI/telemetry fixtures used for interface testing remain explicitly synthetic and are not promoted to research evidence.

### Network exposure boundary

R3 includes a Tailscale-assisted exposure path while the application itself stays bound to localhost. The next Universal Lab integration revision is intended to use a public HTTPS Tailscale Funnel meeting entry point so invited partners can open the supplied `*.ts.net` address in a standard browser.

**Current claim boundary:** public Funnel meeting access is part of the R5 integration plan and is **not claimed as the installed R3 state**.

### Account model decision for R5

The planned meeting-access model uses **persistent named accounts**, not expiring accounts. Availability is controlled operationally by the host starting/stopping the Universal Lab service and the public meeting ingress. Accounts can be disabled, reset or deleted by the administrator when required.

Passwords are not intended to be stored in retrievable plaintext; the administration flow should support password reset rather than password recovery.

---

## 2. SSI knowledge preparation installed for CZARA / Universal Lab

The separate SSI knowledge-preparation workstream is installed and indexed, but not yet claimed trained or qualified.

### Preparation / scan results

| Measurement | Recorded value |
|---|---:|
| Candidate text/data files scanned | **348,579** |
| Route candidates | **64,842** |
| Selected source artifacts | **98** |
| Maximum copied artifact size | **67,108,864 bytes** |
| Knowledge documents indexed | **345,961** |
| Large documents skipped | **266** |
| Curriculum cases prepared | **1,432** |

### Route-source counts

| Route | Selected artifacts |
|---|---:|
| `MEXICO_CZARA_TO_CZARA` | **2** |
| `MEXICO_DIRECTOR_CZARA_TO_DIRECTOR_CZARA` | **0** |
| `BODY_FROZEN_SSI_V5_TO_BODY_FROZEN_CZARA` | **48** |
| `DIRECTOR_SSI_V5_TO_DIRECTOR_CZARA` | **48** |

Because one declared Mexico Director_Czary route has no selected source artifact, the preparation snapshot remains conservatively marked **PARTIAL_SOURCE**.

### Knowledge/curriculum state

- knowledge index: **INDEX_READY**
- prepared curriculum: **1,432 cases**
- qualification: **NOT_RUN**
- training qualification: **false / not claimed**
- native runner / ZeroLab binding for the prepared curriculum: **pending**
- completion of the 1,432-case curriculum: **not claimed**

The prepared phases are:

1. P0 — preflight, learning disabled;
2. P1 — single-domain learning;
3. P2 — cross-domain learning;
4. P3 — know-how guard learning;
5. P4 — meeting simulation learning;
6. P5 — frozen validation, learning disabled;
7. P6 — Champion benchmark, learning disabled.

This preparation is intended to let Director/CZARA retrieve bounded SSI knowledge without injecting the entire private SSI corpus into one prompt.

---

## 3. R4 package boundary

An R4 development package was prepared after R3 with broader interface coverage, including Conference, CZARA, Director_Czary, ZeroLab, Router/Micronetwork views, Shadow, Explorer, Notebook and Operator surfaces.

It was **intentionally not installed as the operator baseline**. R3 remains the installed baseline while the newer requirements are consolidated into R5. R4 therefore must not be described as the current live operator deployment.

---

## 4. Universal Lab R5 — current PRE-BUILD integration specification

R5 is the next integration target. The following items are specified but are not yet claimed complete.

### 4.1 Conference remains the primary human meeting surface

The central meeting view keeps three participant video tiles visible:

- Paweł;
- Sara;
- Leire.

Camera state may degrade independently; the participant tile remains present when video is unavailable.

Audio/video are **not intended to be archived** by Universal Lab. The evidence path stores text/events/timestamps and bounded system receipts instead.

### 4.2 One session, one main timeline

All human and SSI interaction is normalized into one chronological session event stream.

Sources include:

- participant voice converted to text;
- participant typed chat;
- DIRECTOR responses;
- safe CZARA/Shadow status events;
- Router decisions;
- BODY_FROZEN task lifecycle events;
- ZeroLab validation;
- evidence creation.

Targeted chat views are convenience filters over the same session. A participant can select a destination such as:

`ALL | DIRECTOR | PAWEL | SARA | LEIRE`

without manually typing an addressee. The selected destination becomes structured message metadata.

A message sent in a targeted view is still represented on the main timeline with actor, target, channel, language and timestamp so the meeting remains auditable as one coherent session.

### 4.3 DIRECTOR is the primary SSI conversational interface

The R5 meeting UI is intended to expose the Director as the main SSI conversation endpoint alongside the Conference view.

The Director should answer from bounded SSI knowledge/retrieval and preserve status distinctions such as validated, experimental, installed, ready and planned. If the live backend cannot verify a state, the UI must not invent it.

Specialized views may pass a safe `context_object` to the Director so a researcher can ask why a route, micronetwork, task or evidence record was selected.

### 4.4 CZARA is contextual/Shadow support, not the main chatbot

CZARA operates in the background over the same session event stream.

The intended high-level flow is:

```text
transcript.partial
-> early context / intent update
-> knowledge prefetch
-> SHADOW_SPECULATIVE

transcript.final
-> final intent check
-> SHADOW_FINAL
```

The main timeline may show safe operational states such as context detected, Shadow started, Shadow updated and Shadow ready. Private chain-of-thought, hidden prompts and reconstructive internals are excluded.

CZARA does not independently authorize execution.

### 4.5 Router V10 / Micronetwork laboratory view

A separate technical view is intended to expose bounded, real backend telemetry for:

```text
INPUT
-> CZARA CONTEXT
-> ROUTER V10
-> CANDIDATE MICRONETWORKS
-> SELECTED MICRONETWORKS
-> SKILLS / CHAMPIONS
-> ROUTE DECISION
```

No confidence, score or micronetwork identifier should be fabricated by the frontend.

### 4.6 Timings are first-class evidence

The event model is intended to preserve timestamps such as:

- `transcript_first_partial_at`
- `context_detected_at`
- `context_lock_at`
- `question_final_at`
- `router_started_at`
- `router_decision_at`
- `director_started_at`
- `answer_ready_at`
- optional Shadow/BODY/ZeroLab timestamps where real events exist.

A particularly important visible metric is:

```text
CONTEXT DETECTED -> ROUTER DECISION
```

The frontend must compute these timings from real event timestamps rather than visual animation or synthetic delay.

### 4.7 BODY_FROZEN is an execution layer, never a chatbot

The public meeting view should preserve this chain:

```text
DIRECTOR
-> TASK / COMMAND
-> BODY_FROZEN
-> ACTION
-> RECEIPT
-> VALIDATION / EVIDENCE
```

The technical view can expose bounded fields such as task ID, requested-by, issued/start/completion timestamps, current state, receipt reference and evidence/validation status.

Arbitrary participant text must never be converted directly into unrestricted shell execution.

### 4.8 ZeroLab remains a separate live experiment/validation view

ZeroLab is not the same panel as the Router/Micronetwork visualization.

A bounded ZeroLab session view is intended to show real experiment/session/task identifiers, modules involved, start/end events, validation, evidence ID and final PASS / FAIL / INCONCLUSIVE state when those backend events actually exist.

### 4.9 Shadow/benchmark approval boundary

The intended controlled flow is:

```text
CZARA
-> SHADOW
-> DIRECTOR REVIEW
-> HOST APPROVAL
-> BENCHMARK
-> BODY_FROZEN
-> ZERO LAB
-> EVIDENCE
```

The guest may ask questions and generate Shadow proposals, but BODY execution remains behind host approval in demonstration-safe mode.

### 4.10 Meeting evidence is generated from the live session

The target evidence path is:

```text
LIVE SESSION
-> continuous event/evidence capture
-> session close
-> final manifest / hashes
-> partner-safe export
```

The partner-safe package is intended to preserve:

- participant transcript and translation;
- Director interactions;
- bounded CZARA/Shadow events;
- Router decisions and timings;
- BODY task receipts;
- ZeroLab validation;
- evidence references;
- session timestamps and provenance.

Private prompts, credentials, provider secrets and reconstructive private SSI internals are excluded.

No raw audio or video archive is required for this evidence package.

### 4.11 Multilingual meeting path

The current meeting/rehearsal requirement includes both:

- Spanish <-> Polish;
- English <-> Polish;

plus mixed-language scenarios.

Original-language text is intended to reach Director/CZARA immediately while human-facing translation runs in parallel so translation does not block SSI context detection.

### 4.12 Training and rehearsal before partner use

The current curriculum plan separates generalized simulated meetings from final host-in-the-loop rehearsal:

1. **Foundation meetings** — Paweł, Sara and Leire simulated;
2. **Technical/partner meetings** — all three simulated;
3. **Adaptive meetings** — interruptions, incomplete questions, topic changes and multilingual switching;
4. **Execution meetings** — Shadow -> review -> approval -> BODY -> ZeroLab -> Evidence;
5. **Final live rehearsal** — real Paweł with simulated Sara and Leire, limited to a small number of complete meeting runs.

Readiness is intended to consider factual accuracy, disclosure safety, CZARA context accuracy, Shadow lead time, Router timing/correctness, BODY task correctness, ZeroLab evidence completeness, host intervention count, continuity and fallback readiness.

---

## 5. Current status matrix

| Area | Status on 2026-10-07 |
|---|---|
| Universal Lab Live Gate R3 | **INSTALLED / operator baseline** |
| Authentication / persistent SQLite accounts | **INSTALLED** |
| Tailscale availability | **AVAILABLE at install** |
| Native Director/CZARA/Router/BODY bridge through Universal Lab | **NOT BOUND / not claimed live** |
| SSI knowledge preparation | **INDEX_READY / NOT QUALIFIED** |
| 1,432-case knowledge curriculum | **PREPARED / NOT RUN** |
| R4 package | **PREPARED / NOT INSTALLED** |
| R5 unified Conference + Director + main timeline | **PRE-BUILD** |
| R5 CZARA speculative/final Shadow integration | **PRE-BUILD** |
| R5 Router/Micronetwork live telemetry and timing | **PRE-BUILD** |
| R5 BODY_FROZEN execution view | **PRE-BUILD** |
| R5 ZeroLab live meeting view | **PRE-BUILD** |
| R5 continuous meeting evidence + partner-safe export | **PRE-BUILD** |
| R5 public HTTPS Funnel meeting ingress | **PRE-BUILD** |
| R5 multilingual meeting rehearsal | **PRE-BUILD** |

## Claim boundary

This document records the current transition from an installed web/authentication Live Gate and prepared SSI knowledge index toward a fully live-bound R5 research meeting environment.

It does **not** claim that the R5 bridge, partner meeting, complete multilingual voice path, 1,432-case curriculum, external benchmark or partner validation has already completed.
