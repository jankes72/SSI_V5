# SSI V5 — Universal Lab architecture addendum — 2026-10-07

This dated addendum records the Universal Lab architecture delta after the canonical C4 snapshot.

## Status transition

Universal Lab is no longer only a PRE-BUILD concept.

- **Installed baseline:** Universal Lab Live Gate R3 / 1.1.1.
- **Knowledge preparation:** INDEX_READY / NOT QUALIFIED.
- **Prepared curriculum:** 1,432 cases / NOT RUN.
- **Native SSI bridges:** not claimed live-bound through the Universal Lab UI.
- **R5:** PRE-BUILD integration layer over the installed R3 baseline.

## R5 target architecture

Conference remains the central human meeting surface for Paweł, Sara and Leire. The meeting uses one session timeline that aggregates participant text/voice-derived transcript, Director responses, bounded CZARA/Shadow events, Router decisions, BODY_FROZEN task lifecycle events, ZeroLab validation and evidence creation.

DIRECTOR is the main SSI conversational interface. CZARA provides contextual/Shadow support rather than acting as the main chatbot.

The technical views remain separate:
- Router V10 / Micronetwork laboratory;
- BODY_FROZEN execution view;
- ZeroLab live experiment/validation view;
- benchmark/evidence view.

Timing is a first-class observable, especially context detection to Router decision.

## Meeting evidence boundary

Meeting evidence is generated from the live event stream and finalized after session close. The target partner-safe export includes transcript/translation, Director interactions, bounded CZARA/Shadow events, Router decisions/timings, BODY receipts, ZeroLab validation, evidence references and provenance. Raw audio/video archives are not required.

## Multilingual rehearsal boundary

The current rehearsal plan includes Spanish <-> Polish, English <-> Polish and mixed-language scenarios. Generalized simulated meetings precede the final host-in-the-loop rehearsal with real Paweł and simulated Sara/Leire.

For full dated detail, see [SYSTEM/SSI_UNIVERSAL_LAB_STATUS_20261007.md](SYSTEM/SSI_UNIVERSAL_LAB_STATUS_20261007.md).
