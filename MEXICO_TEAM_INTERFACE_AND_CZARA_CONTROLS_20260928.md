# SSI V5 — Mexico Team Interface and CZARA Controls

**Evidence update — 2026-10-02:** This remains the preserved interface proposal. Current ZeroLab roles use Director_Czary and BODY_FROZEN_1_0 for CZARA; Final has its own Director and executors. The local pilot does not establish a deployed external Mexico interface or complete professor/shadow workflow.

[Current CZARA status](CZARA_CURRENT_STATUS.md) · [ZeroLab results](ZERO_LAB_V2_FIRST_RESULTS_20261002.md) · [Evidence and provenance](evidence/ZERO_LAB_V2_20261002/README.md)

Recorded: `2026-09-28`  
Status: `PLANNED INTERFACE / ACTIVE DESIGN / NOT YET CLAIMED AS DEPLOYED`

This document records the currently intended Mexico research-team interface before implementation and external benchmark execution. It is a design declaration, not evidence that the interface has already been deployed.

## Purpose

The interface should allow a professor, authorized technical staff, students and observers to participate in one research session without giving every participant the same authority or mixing every utterance into an anonymous conversation stream.

The system remains role-scoped:

```text
PROFESSOR -> DIRECTOR
TECHNICAL STAFF -> bounded BODY_FROZEN diagnostics
STUDENT / TEAM -> read-only observer view + optional CZARA microphone
ROOT / OWNER -> private local control
```

## Professor view

The verified professor may:

- communicate with DIRECTOR as the R&D session guide;
- inspect the experiment, LAB state and sanitized evidence;
- request explanations, reruns and versioned benchmark changes;
- issue an authorized immediate STOP, PAUSE or SAFE_STATE request.

A safety action must not wait for model reasoning. DIRECTOR receives the resulting event and explains what stopped, why it stopped and what evidence was retained. Professor access is not ROOT access.

## Authorized technical view

Authorized technical staff may inspect and diagnose a selected BODY_FROZEN execution channel and may use declared safety controls. A technical channel cannot silently change the frozen benchmark objective or acceptance criteria.

## Student and team observer view

Students and research-team observers may inspect:

- the current benchmark and status;
- the professor/DIRECTOR conversation;
- sanitized BODY_FROZEN state;
- LAB outcomes;
- shared evidence and experiment chronology.

They cannot write into the professor chat, command BODY_FROZEN, change acceptance criteria or control ROOT.

## CZARA ON/OFF control

Each authenticated participant may explicitly enable or disable microphone/context capture using Mexican-Spanish controls:

```text
ACTIVAR CZARA
DESACTIVAR CZARA
```

Planned interface explanation:

> CZARA escucha y transcribe el audio de este dispositivo para identificar tus observaciones y añadirlas al contexto de la sesión de investigación. CZARA no te permite controlar el experimento ni enviar órdenes a BODY_FROZEN. Puedes desactivarla en cualquier momento.

Planned visible states:

```text
CZARA: ACTIVA — el micrófono está encendido
CZARA: INACTIVA — el micrófono está apagado
```

Disabling CZARA stops microphone/context capture without removing read-only access to the experiment view. Microphone use requires explicit participant permission.

## Source identity and context separation

An enabled browser/device becomes a separately labelled CZARA context source. The intended metadata includes account, declared role, session, device/source identifier, timestamp, language and confidence.

Authentication identifies the account/session/device source. It does not by itself prove the biological identity of every person heard near that device. Speaker uncertainty must remain visible.

Multiple devices may capture the same utterance. The future implementation must avoid counting duplicate audio as multiple independent opinions.

CZARA should classify information into at least:

```text
VERIFIED_PROFESSOR_REQUEST
TECHNICAL_WARNING
TEAM_OBSERVATION
STUDENT_SUGGESTION
BACKGROUND_SPEECH
DUPLICATE_AUDIO
UNCERTAIN_SPEAKER
```

Team observations may influence research context, but they do not become executable commands. A frozen benchmark may change only through the declared professor/research-control path.

## Claim boundary

This document records what is being built. It does not establish:

- completed Mexico deployment;
- validated multi-device speaker identification;
- validated audio deduplication;
- production load capacity;
- physical robot control;
- safety certification;
- independent external validation.

The implementation must preserve the SSI rule: observation, context and suggestion do not equal execution authority.

