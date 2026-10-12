# Universal Lab — Director A16 installation and knowledge update

**Published:** 2026-10-12  
**State:** `A16_INSTALLED` + `A16_HTTP_READY`, reported by the MSI operator.  
**Evidence:** the operator's installation/activation transcript and the preserved A16 offline build reports. This publication does not represent independent access to either runtime host.

## Co zostało wdrożone / what was installed

Operator potwierdził instalację A16 w Universal Lab na MSI i ponowne uruchomienie samego serwera HTTP. Wiedza Dyrektora wzrosła z 24 do **48 tematów**, z odpowiedziami **PL/EN** w trzech wariantach: krótko, rozszerzenie i technicznie. Łącznie daje to **288 przygotowanych wariantów odpowiedzi**. Zakres obejmuje m.in. sześć Iskier, drony, systemy Mother, humanoidy, ratownictwo, Research Memory, Router V10, Blocks, Hermes, Świat Piłki, WEB i dalsze plany badawcze.

Log potwierdza instalację oraz gotowość HTTP. Test prowadzenia rozmowy na żywo ma nadal status `NOT_RUN`. Dostęp publiczny do nowej strony z Dyrektorem pozostaje planem; deklaracja z 12 października 2026 jest opublikowana w kanonicznym dokumencie architektury.

The operator verified the package checksum, applied A16 and obtained HTTP readiness after reloading the Universal Lab HTTP process. This expands prepared explanations while preserving the existing A15 conversation path. It does not establish live model-gateway availability, native micronetwork execution or a public web service.

- [Full 48-topic PL/EN catalog, all three answer levels](../KNOWLEDGE/SSI_DIRECTOR_A16_PL_EN_20261012.md)
- [Machine-readable installation, activation and build-test summary](UNIVERSAL_LAB_DIRECTOR_A16_PUBLIC_SUMMARY_20261012.json)
- [Canonical architecture and long-term programme](../SSI_V5_C4_ARCHITECTURE.md)
- [Dated declaration of the future web Director](../SSI_V5_C4_ARCHITECTURE.md#web-director-declaration-20261012)

## Installation and activation evidence

Package: `SSI_DYREKTOR_A16_WIEDZA_I_PLANY_20261012.zip`  
SHA-256: `82dce7eda4d2a4dd89bf924cffdb1a5dbfd229e091c19e1fc03fb31a47495ead`

| Observation | Reported result | What it supports |
|---|---|---|
| Package checksum | OK | Operator verified this package identity before installation |
| Installer | `A16_INSTALLED`, `apply=true` | A16 files applied on MSI |
| Prepared topics | 48 | Available authored knowledge topics; no qualification implied |
| New trained micronetworks | 0 | This update creates no trained native skills |
| Installation model calls | 0 | Installation did not invoke models |
| Installer host tests | `hosts_tested=false` | No host integration test was performed by the installer |
| HTTP reload | `A16_HTTP_READY` after replacing the HTTP process | Universal Lab HTTP readiness reported after activation |
| Live narration | `NOT_RUN` | End-to-end conversation is still unverified by this evidence |
| NODE-01 files / restart | Both false | This installation did not deploy or restart NODE-01 |
| Session restart | false | The activation script did not restart the meeting/session service |
| Gateway policy / call-state rewriting | Both false | A16 did not change the gateway policy or rewrite call states |

The installation step's `reload_required=true` is followed by the successful HTTP activation step; it is not presented as an outstanding reload failure. Exact host paths, process identifiers, private routes and backup locations are omitted from this public record. The publication date is not an inferred timestamp for every line in the original transcript.

## Knowledge and conversation behaviour

A16 retains the 24 original topic identifiers and adds 24 domain/research topics. Each topic has short, extended and technical Polish/English text with source references. The catalog contains prepared narration. A spoken description of Router V10, Research Memory or a micronetwork does not prove that component executed for that answer.

The reviewed A15/A16 package provides the following conversation behaviour; offline tests cover it within the stated test-double scope:

| Function | Implemented behaviour and boundary |
|---|---|
| Topic selection | Paired prepared PL/EN explanations at the selected depth, without a new model call for that prepared path |
| Meeting mode | Explicitly enabled by an authorized session owner; uses shared final captions/messages from the current room/session |
| Partial captions | Can identify a likely topic; a response follows the finalized segment rather than treating changing partial text as final |
| Participant context | Bounded per-user history and shared session context in process memory; automatic durable Research Memory binding is not established |
| Questions combining subjects | Use the existing gateway when generation is required; current availability must be checked separately |
| Translation recovery | Existing translation path with a visible Director takeover for supported definite failure cases; uncertain calls are not automatically repeated |
| Voice reading | Optional local browser speech synthesis with a chosen language; no claim that it transmits audio as a conference participant |
| Pacing | Existing duplicate suppression and conversation pacing are preserved; measured live latency is not claimed |

A16 updates the knowledge data, loader/pin, topic UI and related server/page version hooks. The complete operator-reported changed-file list, relative to the existing Universal Lab module, is:

```text
director_live_a15.json
director_live_a15.py
director_live_a15_pin.py
director_narration_a14.py
server.py
static/director_live_a15.js
static/index.html
```

The retained A14/A15 filenames are compatibility identifiers. No new public endpoint or replacement SSI actor is declared by this documentation update. The proprietary implementation and private installer remain outside this public repository.

## Recorded offline verification

These are the A16 build's recorded checks, performed before the operator's installation. They are not live-host acceptance results or new tests executed during this documentation publication.

| Check | Recorded result | Scope |
|---|---|---|
| Python tests | 41 passed; 0 failures/errors | Knowledge, bounded conversation paths, authorization/isolation checks and installer/rollback cases |
| Bilingual answer matrix | 288 combinations passed with paired translations; 0 model calls | 48 topics × 2 languages × 3 levels in the prepared-answer path |
| UI checks | 18 declared assertions passed | DOM and SpeechSynthesis doubles; no real browser/audio acceptance |
| Syntax | 16 Python files; JavaScript and shell passed | Syntax checks |
| GitHub source integrity | 199 checked files; 0 hash mismatches | Pinned public source snapshot; 27 selected documents included in the private archive |
| Roadmap references at build time | 18 document links checked; readback exact match | PR #2's original roadmap revision |

The offline integration fixture used the provided Operations R1 hooks plus unrelated-edit markers. It was not the actual R11 runtime. Model gateway, translation bridge, Notary callback, DOM and speech synthesis were test doubles where specified. MSI installation, NODE-01, live gateway, real browser and audio were not exercised by those build tests.

The subsequent operator transcript advances **MSI installation and HTTP activation** only. It leaves live narration, actual audio/translation, gateway availability, NODE-01 interoperability and independent evidence verification as separate checks. The operator's terminal working-directory name is not evidence of successful Operations Center integration.

## Sources, plans and remaining acceptance

The knowledge build used public GitHub source commit `3fb422e4988ecb753af96d3bc5394b6a545ca709`. Its long-term roadmap reference was PR #2 at `9c3a760f3d59a58a5723f465de9d3b310d8b1464`, then a draft. The installed archive remains an immutable snapshot of that state; later GitHub publication does not silently rewrite its checksum, text or source pins.

Local project records are labeled separately from public GitHub sources in the catalog. Project information stored in OpenAI products is not an OpenAI endorsement or independent verification. This publication does not release private conversations, credentials, signing keys or reconstructive implementation details.

The next live checks are the actual SSI/CZARA/Router questions in PL and EN, translation-failure recovery, room/user context separation, voice reading and gateway error handling, followed by any separately authorized two-host test. Their outputs should be published as new dated evidence rather than inferred from HTTP readiness.

The future externally reachable Director website is specified in the [12 October declaration](../SSI_V5_C4_ARCHITECTURE.md#web-director-declaration-20261012). No launch date, live URL or public deployment is claimed. Earlier Research Memory, qualification, rehearsal and independent-attestation boundaries remain as recorded in the [9 October progress report](UNIVERSAL_LAB_RESEARCH_MEMORY_PROGRESS_20261009.md).
