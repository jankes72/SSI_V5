# SSI UNIVERSAL APP — Commercial Smart Home / Robotics Platform R1

**Date:** 2026-10-17  
**Status:** **PROPOSED PRODUCT ARCHITECTURE, NOT IMPLEMENTED OR DEPLOYED**  
**Architecture source of truth:** [SSI V5 canonical C4](../SSI_V5_C4_ARCHITECTURE.md). This document defines the product contract and delivery stages, but **does not introduce an alternative SSI architecture diagram**.

## The user's required experience

A customer opens **SSI Universal App**, signs in once, and says or types:

> I have two robot vacuum cleaners, a robotic mower, an entrance gate, cameras, several radiators and air conditioners, and microphones/speakers. Connect them into one system so I can see them, talk to the house, create routines and control supported devices.

The application should:
1. Ask for **device vendors, exact models, connection types, location/room and the customer's permission**.
2. Discover available devices locally where the standards allow it; show matches and potential duplicates; verify exact capabilities, firmware and APIs rather than assuming every brand supports automation.
3. Pair each device using its native method (Matter commissioning/QR, official OAuth, LAN pairing, Zigbee/Z-Wave radio, etc.) with user confirmation. Do not solicit or copy unrelated passwords.
4. Install/enable only approved **signed, version-pinned integration adapters** in an isolated local home gateway. Never self-install arbitrary unreviewed code from a device's advertising text.
5. Test connectivity, access permissions, supported actions and state read-back; clearly distinguish **READY**, **PARTIAL**, **CLOUD_DEPENDENT**, **INCOMPATIBLE**, **OFFLINE** and **NEEDS_USER_ACTION**.
6. Generate device tiles, rooms, scenes, permitted automations and voice phrases from the actual supported capabilities.
7. Offer **voice and text** control with confirmation of real state, accessible through permitted microphone/speaker endpoints or phone app.
8. Preserve offline-capable basic control where vendor protocols permit it. Remote web/mobile operation is optional, explicit and access-controlled.
9. Record redacted operational evidence, errors, versions and recovery actions without exposing household camera/video/audio streams or device secrets.

**Honesty boundary:** Merely naming devices cannot grant access or make incompatible proprietary hardware work. A device must support a suitable LAN protocol, integration, bridge or permitted cloud API; some hardware is cloud-only and fails when offline.

## Commercial system layers

- **SSI Universal App (frontend):** mobile-friendly web and future native clients; per-home setup wizard, device registry, room dashboards, chat, voice, access control, maintenance status, support and billing.
- **Tenant / household API & identity:** exactly one customer login, per-home boundaries, OAuth/OIDC tokens to local hub, owner/resident/guest/installer roles, revocable access; no reuse of internal SSI operator sessions across customers.
- **SSI Home Edge Hub (customer premises):** always-on low-power controller on mini-PC, Raspberry Pi-class device or supported gateway; local rules, secure credential vault, integrations, wake word/STT/TTS (resources permitting), schedules, state caching and device health.
- **Adapter registry:** plugin contracts for Matter-over-Wi-Fi/Thread, Zigbee, Z-Wave, MQTT, HTTP/LAN, KNX/Modbus when applicable, RTSP/ONVIF camera reads, vendor-sanctioned APIs, and optional **Home Assistant bridge**. Some transports require USB radios or other bridge hardware.
- **Capability model (semantic device twin):** device -> entities -> attributes/telemetry -> authorized actions -> constraints -> acknowledgment and observed state. Gate, lock, mower and alarm controls are privileged actions.
- **SSI Director / Router V10:** planning, explanation, model/provider selection, supervised automation proposal, failure recovery and evidence. Existing SSI private research identity and memory must remain isolated from customer data.
- **SSI MultiQuant:** **model preparation and deployment service**, not an on-device automatic quantizer for every arbitrary model. Model profiles `HOME-EDGE-2GB`, `HOME-EDGE-4GB`, `HOME-EDGE-8GB`, `CORE24-CPU16GB`, and robotics/drone variants; choose known compatible quantizer/runtime or require smaller architecture / distillation when fitting is impossible. Preserve original hashes, licenses and version, measure actual resident RAM/CPU/thermal/power envelope.
- **Local real-time action layer:** deterministic authorized routines, safety checks, device state confirmation, retries with idempotency and fail-closed behavior. An LLM supplies interpretation/planning, **not direct unlimited control of actuators**.
- **Optional cloud SSI services:** remote access via outbound authenticated tunnel, account management, fleet software updates, optional expensive model escalation (opt-in), aggregated privacy-safe support diagnostics. Basic LAN-compatible home control should not depend on external LLM APIs.

## Minimum connector interface (design contract)

An approved adapter registers:
- `adapter_id`, `vendor`, `supported_model_ids`, `protocol`, `version`, `license`, `supported_capabilities`, `required_permissions`;
- `discover()` (only within customer-approved network scope);
- `pair(request, user_approval)` (per protocol; secret to encrypted vault);
- `read_state(device)`, `subscribe_state(device)`;
- `list_actions(device)` (only actual supported actions);
- `validate_action(device, action, caller_roles, policy)`;
- `execute_action(device, action, idempotency_key)` (request receipt, no false success);
- `confirm_observed_state(device, expected, timeout)`;
- `health()`, `remove_credentials(device)`, `update()/rollback()`.

No raw arbitrary shell commands or unrestricted LLM-to-device API access. Adapters execute in a separately authenticated, least-privilege environment.

## First-class device classes

| Class | Discovery / integration candidate | Typical capability | Requirements |
|---|---|---|---|
| Lights / switches / plugs | Matter, Zigbee, Z-Wave, MQTT, vendor LAN | On/off, level, energy | Supports local profile; normalize rooms |
| Heating / thermostats | Matter, heating controller, Modbus/KNX or vendor API | Temperature, setpoint, modes | Bounds, schedules, anti-freeze protection |
| Air conditioning / HVAC | Matter, local vendor API, IR bridge (with feedback caveats) | Mode, fan, setpoint | Prevent conflicting HVAC control |
| Robot vacuum | Supported vendor integration / Home Assistant / approved API | Clean, return to dock, status | Verify each model supports commands and maps |
| Robot mower | Supported vendor integration / approved LAN/cloud API | Start, pause, dock, state | Human/pet safety checks; no safety bypass |
| Gate / garage door | Matter closure where *device* supports it, approved controller / dry-contact bridge | Open, close, state | Owner-approved actions; state sensor and obstacle safety; confirmation |
| Cameras / video doorbell | ONVIF/RTSP for supported cameras; Matter 1.5 where implemented | View events, permitted stream | Private video by default; consent, access roles and retention controls |
| Microphones / speakers | Voice satellite or user phone, local audio IO | Wake word, commands, TTS | Separate mic consent, permission indicators, compatible multiroom endpoints |
| Security sensors / alarms | Matter, Zigbee, Z-Wave, vendor APIs | Motion, opening, leak/smoke state | Local notifications; do not bypass certified alarm/safety systems |

**Matter is not the same as Thread**; Matter pairing needs an actual Matter-capable device and in some cases a Thread border router. A vendor may require a cloud account; mark such devices as **CLOUD_DEPENDENT**, not offline compatible.

## Spoken-command pipeline (example)

```text
"SSI, when I'm back home, turn on hallway lights,
set living-room temperature to 21 and tell me if the mower is docked."

1. Wake word / UI microphone enabled with user consent
2. Local STT -> text
3. SSI parses intent and resolves device IDs against homeowner's actual registry
4. Policy & schema validator checks allowed actions, owners, conflicting automations
5. For low-risk routine: confirmed local deterministic actions/events
6. Device adapter obtains acknowledgments and reads back observed state
7. SSI replies via local TTS only with *observed or appropriately qualified* results
8. Events / redacted evidence stored locally; no automatic microphone/video recording
```

For higher-risk actions such as opening a gate, disarming an alarm, unlocking a door or activating machinery, require explicit owner authorization and an appropriate second factor or physical control when warranted. **Voice alone is not reliable identity verification**.

## MultiQuant — how this helps commercial products

Universal App supports both:
- **Configurable commercial software skills/adapters** that work even without a full LLM (deterministic rules);
- **Replaceable local/offline LLMs** selected per hardware and task class, using model-specific quantization, CPU/NPU/GPU support, memory budget and outcome measurements.

A big model that cannot be practically represented at an edge device's memory/compute budget is **not** compressed by magic; SSI MultiQuant declares `DISTILL_SMALLER_MODEL_REQUIRED`, `UNSUPPORTED_ARCHITECTURE`, or `CPU_LATENCY_TOO_HIGH` and proposes a compatible alternative.

The customer's smart home should not need expensive cloud inference for ordinary `turn_off(light)` actions. More demanding conversational planning can use a cloud provider **only when chosen/authorized**, with per-customer costs and privacy policy.

## Separation of Universal App from SSI Universal Lab

**SSI Universal Lab** remains the existing research/meetings/training interface. **SSI Universal App** is a proposed commercial customer product which may reuse **verified** gateways, approved skill interfaces and the mission/evidence model, but must provide:
- separate tenant boundaries, authentication keys, device secrets, support staff privileges and per-home memory;
- no exposure of internal MSI/NODE-01/Robert operations or private research datasets;
- separate deployment channels and release/evidence labels;
- customer-installed local edge component if real physical devices need local network access.

The commercial smart-home twin is only one of multiple possible sector packages; the same adapter/MultiQuant foundation may later support offices, energy/industrial controls and robotics with domain-specific constraints.

## Delivery stages and acceptance evidence

**R0 — architecture & compatibility registry (NOW):** map devices, protocols, vendor permissions, support policy, offline vs cloud distinctions; provide a conservative device intake wizard contract. No device access or automated installations.

**R1 — customer onboarding MVP (FUTURE):** one homeowner account, local edge hub installation with user consent, integration catalog, manual pairing, read-only discovery and a simple dashboard for **lights + heating + one tested robotic device**. Acceptance: explicit paired device state and reproducible removal.

**R2 — local voice & reliable automation (FUTURE):** local STT/TTS (e.g. Speech-to-Phrase/Whisper + Piper when appropriate), permissions, actual device acknowledgment, schedules, receipts, fail-closed error handling. Acceptance: complete useful homeowner scenes and speech replies without cloud on **verified offline-capable devices**.

**R3 — expanded commercial integrations (FUTURE):** mower, gate, HVAC, multiple cameras and audio zones, approved adapters and safety/security reviews. Acceptance per make/model, not a blanket claim that all devices work.

**R4 — SSI MultiQuant edge models (FUTURE):** quantized local model chosen under user hardware limits and licensing; no extra synthetic benchmarks; real authorized device/voice flows generate anonymized, opt-in calibration data. Acceptance: memory and end-to-end command latency under representative load, non-intrusive temperatures and safe controller fallback.

**R5 — commercial rollout (FUTURE):** installer workflow, ongoing support, paid subscription/licensing if chosen, secure updates/rollback, audit/privacy controls, data portability and service lifecycle. Customer environments remain isolated. No deployment or revenue claims are made in this document.

## Source references (public external standards/integrations)

- [Connectivity Standards Alliance — Matter 1.5: cameras & closures (2025-11-20)](https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/)
- [Home Assistant — Matter requirements and Thread distinctions](https://www.home-assistant.io/integrations/matter/)
- [Home Assistant — local voice assistant](https://www.home-assistant.io/voice_control/voice_remote_local_assistant/)
- [Home Assistant — lawn mower integration](https://www.home-assistant.io/integrations/lawn_mower/)
- [Home Assistant — wake words](https://www.home-assistant.io/voice_control/about_wake_word/)

**Important:** These external open technologies are potential integration foundations. Availability of a standard or Home Assistant integration does not imply any particular customer's model is compatible, or that SSI currently implements that adapter. Review plugin licenses, cloud API terms and customer consent before commercial delivery.
