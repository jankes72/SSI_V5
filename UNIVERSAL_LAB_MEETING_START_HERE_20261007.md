# SSI Universal Lab — Partner Meeting Start Here — 2026-10-07

**Purpose:** concise entry point for external researchers and meeting participants  
**Current boundary:** installed Universal Lab baseline + verified preparation + clearly separated R5 integration work  
**Private boundary:** proprietary SSI source code, credentials, private prompts and reconstructive runtime internals are not published

## This is not intended to be a conventional video call

Universal Lab is being developed as a research-meeting environment in which invited participants can talk with the SSI Director, observe bounded SSI processing and inspect evidence from the same session.

The current meeting model is built around **Paweł, Sara and Leire** and is intended to combine:

- Conference video/audio presence;
- one shared chronological meeting timeline;
- directed participant chat;
- Director interaction;
- safe CZARA / Shadow status events;
- Router V10 / Micronetwork telemetry;
- BODY_FROZEN execution visibility;
- ZeroLab validation;
- evidence/provenance generated from the session.

The target result is that a research meeting can be inspected afterwards as a bounded evidence package rather than remembered only as a presentation.

## What already exists

### Universal Lab baseline

The operator baseline is **Universal Lab Live Gate R3 / 1.1.1**.

The installed baseline includes authenticated web access, persistent SQLite-backed accounts and a localhost-first deployment path. The current named accounts include Paweł, Sara and Leire.

### ZeroLab

**ZeroLab V2 already exists as a separate bounded laboratory/runtime layer.** Its earlier local pilot evidence is published elsewhere in this repository. Universal Lab R5 is intended to expose bounded ZeroLab session/validation information during research meetings without merging ZeroLab into the chat UI.

### SSI knowledge preparation for CZARA / Director_Czary

The prepared knowledge path currently records:

- **345,961 indexed documents**;
- **1,432 prepared curriculum cases**;
- **48 selected `DIRECTOR_SSI_V5_TO_DIRECTOR_CZARA` source artifacts**;
- **48 selected `BODY_FROZEN_SSI_V5_TO_BODY_FROZEN_CZARA` source artifacts**;
- knowledge state **INDEX_READY**;
- qualification **NOT_RUN**.

This means the Director_Czary/CZARA knowledge path has been prepared from existing SSI material, but this repository does **not** claim that every private skill has already been live-qualified through Universal Lab.

## Translation bridge and measured host behavior

The current R3 configuration contains a local translation command bridge using:

```text
translation
-> command_json
-> python module
-> translation_ollama
```

The development host uses local Ollama with **qwen3:4b**.

A recent operator-side test reported roughly **2 seconds for the local translation step on this host**. This is recorded as a host-specific observed value, not a universal latency guarantee or an external benchmark.

The intended meeting pipeline keeps translation parallel to SSI processing so the Director/CZARA path does not have to wait for a human-facing Polish translation before it can start context work.

## Designed around the actual modest development computer

Universal Lab is deliberately being adapted to the real local machine instead of assuming a datacenter GPU:

- **MSI GV62-8RE**;
- Intel i7;
- **16 GB RAM**;
- **GTX 1060 6 GB VRAM**;
- Ubuntu;
- Ollama;
- local **qwen3:4b**.

The integration strategy is therefore resource-bounded:

1. local-first execution;
2. avoid loading several large models simultaneously;
3. reuse one local LLM through role-specific calls where practical;
4. keep event handling, session state, retrieval/prefetch and other light work away from scarce GPU memory where practical;
5. use text as the common fallback when voice/video components degrade;
6. reserve cloud inference for fallback/escalation rather than making the meeting dependent on a large remote model.

This hardware constraint is part of the research/engineering context: the goal is to demonstrate that the meeting workflow can be made usable on a relatively modest local computer.

## Current bridge boundary — important

The Universal Lab architecture includes Director, CZARA, Router, Micronetwork, BODY_FROZEN, ZeroLab and evidence integration points.

However the latest R3 bridge configuration must be described conservatively. The **translation bridge is configured**, while the current configuration still shows other native meeting bridges such as Director/CZARA context/STT as disabled or awaiting the next binding step.

Therefore this repository does **not** claim that every native SSI bridge is already live-bound through R3.

R5 is the integration step intended to bind and verify the remaining live paths before they are presented as complete.

## R5 meeting flow

The current R5 target is:

```text
PAWEŁ / SARA / LEIRE
        |
        v
CONFERENCE + ONE MAIN TIMELINE
        |
        +--> DIRECTOR
        |
        +--> CZARA / SHADOW
        |
        +--> ROUTER V10 / MICRONETWORKS
        |
        +--> BODY_FROZEN
        |
        +--> ZERO LAB
        |
        v
EVIDENCE / PARTNER-SAFE SESSION PACKAGE
```

The technical views remain separate so researchers can inspect different parts of the process without turning the main meeting view into a debugging console.

## Evidence from the meeting

The target partner-safe meeting export is intended to contain:

- participant transcript;
- translation;
- Director interactions;
- bounded CZARA/Shadow events;
- Router decisions and timings;
- BODY task receipts;
- ZeroLab validation;
- evidence references;
- timestamps/provenance.

Raw audio/video are not required as part of the evidence package.

## Current research status

| Area | Status |
|---|---|
| Universal Lab R3 | **INSTALLED** |
| Persistent web authentication/session layer | **INSTALLED** |
| ZeroLab V2 | **EXISTS / bounded evidence published** |
| SSI knowledge index | **INDEX_READY** |
| 1,432-case curriculum | **PREPARED / NOT RUN** |
| Translation bridge | **CONFIGURED** |
| Recent local translation observation | **~2 s on the development host, operator-reported** |
| Director/CZARA/Router/BODY/ZeroLab native live binding through R3 | **NOT ALL LIVE-BOUND** |
| R5 unified meeting integration | **PRE-BUILD / current next step** |

## Detailed status

See:

- [Universal Lab installed state and next integration boundary](SYSTEM/SSI_UNIVERSAL_LAB_STATUS_20261007.md)
- [Universal Lab architecture addendum](SSI_V5_C4_ARCHITECTURE_20261007_UNIVERSAL_LAB_ADDENDUM.md)
- [Current Universal Lab truth update](CURRENT_TRUTH_UPDATE_UNIVERSAL_LAB_20261007.md)
- [Canonical SSI V5 C4 Architecture](SSI_V5_C4_ARCHITECTURE.md)
