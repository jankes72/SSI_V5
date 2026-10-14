# Robert — planned SCC, Luna Navigator and Technology Radar upgrade

**Decision recorded:** 15 October 2026, Europe/Warsaw.  
**Plan revision:** 2 — guided engineering missions, Director roles, Work and evidence/response integration.  
**Status:** `PLANNED / NOT IMPLEMENTED / NOT DEPLOYED`.  
**Runtime acceptance of this upgrade:** `NOT RUN`.  
**Scope:** future extension of Robert's existing desktop missions and Technology Radar within the SSI research project.

## Polski — co dopiero zostanie dodane

**To jest zapowiedź kolejnego upgrade'u Roberta. Opisane tutaj rozszerzenie nie jest jeszcze zaimplementowane ani wdrożone.** Plan obejmuje własny kokpit GUI Roberta, zintegrowane sterowanie rzeczywistym kursorem i klawiaturą, dodatkową instancję Luny do obrazu i nawigacji oraz analizę materiałów Radaru Technologii przed ich adaptacją przez Decomposer do wspólnego języka SSI.

Dodatkowa Luna ma być odrębna od instancji używanej przy mikrosieciach, Flow i Full Flow. Otrzyma trzy stałe profile: **Navigator** do sytuacji wizualnej, **Radar** do źródeł oraz kodu i **prompty misji** przygotowywane z wytycznych Dyrektora Charlie. Robert zachowa wykonanie i sprawdzanie efektów. Ocena Luny nie będzie samodzielnym dowodem kompletności ani poprawności kodu. Do aktywnego wykorzystania przejdzie wyłącznie zakres potwierdzony odpowiednimi sprawdzeniami.

Szkolenie obejmie długą rozmowę, oczekiwanie, kopiowanie odpowiedzi, pobieranie paczek, instalację w terminalu oraz przekazanie sprawdzonego wyniku. Robert ma też zakładać projekty, wiązać je z istniejącą organizacją i budować własne narzędzia pod naszym prowadzeniem. Hierarchia Champion–Challenger oraz zasady kwalifikacji i awansu pozostają takie, jakie obowiązują w istniejącym SSI; plan nie wprowadza nowego progu liczby wywołań. Każda misja uwzględni testy, Evidence, Notariusza, Research Memory, checkpointy CONTINUUM oraz odpowiedź opartą na dowodach. Podpis zapisu nie zastępuje potwierdzenia poprawności zadania.

Ten plan rozwija [ostatnio opisane misje Roberta](README.md#2-the-initial-drone-to-desktop-mission-transfer) oraz [publikację modułu SCC](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md). Nie zmienia wyników wcześniejszych misji.

## Existing baseline and future scope

The [Robert record](README.md) preserves the V9 local research result: 10/10 waypoints and 24 signed events, with zero GUI actions, network access or model calls. The latest GUI diagnostic in that record stopped before acting. Those observations do not test the upgrade proposed here.

A27's declarative goal notation remains the separately published, operator-reported deployment. Its reproduced parser/integration checks are not runtime acceptance of Robert navigation, visual Luna assistance, Technology Radar qualification or a general imperative SCC executor.

This publication adds a dated development plan only. It provides no installation package, new runtime result or activation receipt.

## 1. Robert owns the desktop-control loop

Robert is planned to own perception, navigation, native mouse/keyboard execution and outcome verification as one integrated module. His own GUI is the cockpit: current view, selected target, mission step, proposed action, observed result and control ownership.

The local controller performs cursor movement and immediate checks. Model consultation occurs at navigation decision points rather than for each cursor increment. The target session uses the operating system's native access mechanism, explicit human/Robert/paused states and a tested return-control action.

The current desktop mission retains its Dell-only constraint and discovers geometry at runtime. Old coordinates are not a substitute for current targeting. A changed screen or target invalidates the associated action until it is checked again.

## 2. Additional Luna: three fixed profiles

The proposed additional Luna instance is separate from the model context used for micronetwork construction, Flow and Full Flow.

| Profile | Proposed responsibility | Output |
|---|---|---|
| Navigator | Interpret the current image or crop together with the mission goal and recent actions | A bounded next-step proposal, an identified target, an expected effect or a request for another observation |
| Radar | Analyse retrieved source material, implementation scope, dependencies and gaps | A source-linked assessment and a proposal for the checks needed to qualify the relevant capability |
| Mission prompts | Turn Director Charlie's assigned objective, context and acceptance criteria into task-specific communication | A versioned prompt linked to the mission and step; no independent change of the assigned objective |

Direct image input requires verified support in the selected model and gateway. This plan does not assert that the currently bound provider already accepts images. Radar searching requires connected retrieval tools; the model is not presumed to have independent browsing access.

The profiles keep separate task contexts. Radar analysis has lower scheduling priority than active navigation. Existing gateway, queue and budget accounting are reused, with a bounded consultation allowance across the whole mission. The allowance must not reset after each action. No new provider, model identity or public runtime endpoint is announced.

## 3. Qualify Radar material before active BLOCKS adaptation

A retrieved source is a candidate. Luna can identify missing files, stubs, mismatches between documentation and implementation, or absent tests. The native qualification process must check the actual version and the capability needed by SSI.

Completeness of the retrieved material and correctness of a named capability are separate questions. A small library can implement a complete capability; a complete repository can contain an unfinished feature.

| Assessment | Planned handling |
|---|---|
| Capability verified in its declared scope | Eligible for adapter preparation, followed by validation of that adaptation |
| Partial implementation | Record supported scope and concrete gaps; do not activate the whole proposed block |
| Unfinished implementation | Keep as research material and create an explicit completion/retest task |
| Insufficient evidence | Retain as an unqualified candidate; do not infer either completeness or failure |

Source version, hash, dependencies and qualification results remain associated with the candidate. Luna's judgment, a download, a signed record or one passing test alone does not establish correctness of the whole project.

## 4. One SSI mission language across the modules

**SCC is the public name of the developing SSI BLOCKS mission language.** The planned common contracts cover BLOCKS Space, BLOCKS Navigator, Robert, Hermes and other participating micronetwork modules.

Source implementations may retain their programming languages. Decomposer prepares a common capability description and an execution adapter: inputs, outputs, dependencies, supported operations, completion criteria and verification requirements. It must preserve missing capability as a gap rather than inventing an implementation.

Qualified source material is not automatically an active Champion. The adapted block requires its own checks and the existing qualification/activation path. Champion assignment stays explicit and versioned; Luna does not replace that hierarchy.

History, qualification and results use existing Research Memory, Operations and evidence mechanisms. This plan does not create a parallel competence database.

### Skill and Champion scope in Research Memory

Research Memory organizes and separates skills under the existing native contracts and supplies the relevant qualified candidates through the existing selection/Router integration. The additional Luna consumes that result; it does not create a competing Champion hierarchy, ranking database or promotion policy.

A Champion is scoped to a named task or transition, domain, input conditions, environment/version and acceptance criterion. Competence in finding a chat editor does not imply competence in selecting a download, operating a terminal or validating an installation. One block can participate in multiple mission constructions, but its qualified scope must match each use.

The Polish-construction analogy concerns canonical elements and their combinations: a reused element can occur in many constructions. It does not imply that a frequently used block is the best performer for every role. A composed mission retains one overall strategy and its own end-to-end verification.

The existing Research Memory/Router binding and qualification authority remain integration gates. Missing eligibility or a missing native connection stays an explicit gap; this future plan does not silently enable routing that earlier evidence recorded as unbound.


## 5. Director roles and task delegation

The proposed fixed hierarchy keeps Director SSI as the strategic authority and Director Charlie as the R&D mission coordinator consulting that authority. Director Charlie specifies the objective, permitted changes, target environment, resources and acceptance criteria, and assigns work to Robert or BODY_FROZEN.

Robert owns desktop execution, conversation handling, artifact receipt and installation. BODY_FROZEN remains a distinct runtime and competence identity for tasks assigned to it. R&D Director Charlie, assistant Charlie and Director_Czary are not merged by this plan.

The additional Luna prepares mission prompts and supplies navigation/Radar assistance in its three fixed contexts. Work or ChatGPT can act as the coding/research collaborator. Prompt production does not replace the Director's mission authority. Each returned artifact and correction stays associated with its originating project, mission and version.

## 6. Guided engineering curriculum: conversation to installation

The first training is a long engineering mission under human guidance:

| Stage | Planned action and observable completion |
|---|---|
| Open the conversation | Identify the intended chat and the text editor between the plus and microphone landmarks |
| Write and send | Focus the editor, check the draft and send once |
| Wait | Preserve mission state until generation has finished and the conversation is ready; an icon or fixed delay alone is insufficient |
| Receive the answer | Copy the intended text accurately, retain its revision and identify instructions/artifacts |
| Retrieve the artifact | Confirm the correct completed download, package identity and target version |
| Prepare installation | Bind the instruction to the module, host and mission scope, retaining exact text rather than guessing shell punctuation from an image |
| Install | Open the terminal with the configured Ctrl+Alt+T shortcut, paste the checked instruction and execute the assigned installation |
| Verify and report | Check the expected version/service/function, retain the result and return a factual report to the conversation |

A failed check can lead to a diagnosis, corrected artifact and retest within the same mission. Reopening a mission first reconciles prior effects: an uncertain send or installation must not be blindly repeated. Existing CONTINUUM/checkpoint mechanisms are the intended integration point. Waiting does not require a fresh Luna consultation on every observation.

The proposed first useful project is Robert's own laboratory/control panel connected to a real, bounded mouse-control adapter. Robert should create the project, associate it with the existing organization/Operations record, obtain and run the implementation, assess the interface and its actual functions, and submit corrections. This records work in the company/project context; it does not create a legal entity.

The laboratory supplies observable targeting, clicking, text-entry and changed-state tasks. Initial guidance is reduced as qualified competence becomes available. New tools begin as candidate versions with a retained recovery path; the plan does not authorize rewriting canonical frozen actor state.

## 7. Challenger, Champion and the model-free demonstration

The existing SSI Champion/Challenger hierarchy, qualification criteria and promotion rules remain unchanged. This upgrade adds no new call-count threshold or automatic promotion rule. Training trials and their outcomes must use the native lifecycle and evidence contracts.

Training continues until the actual qualification/promotion mechanism admits a Champion for the named task and environment. Subskills and the complete long mission require their own scoped evaluation. Shared SSI constructions and reuse of qualified transitions may shorten time to qualification; no acceleration is measured by this publication.

A frozen version is then evaluated on held-out task variants without teacher assistance to its navigation/controller. Reports distinguish:

- models acting as the conversation partner or code-generation teacher;
- Luna or other models advising Robert's own navigation/decisions;
- any language-vision model still used for perception.

Zero navigation-model calls does not mean that the conversation partner or perception used no LLM. A claim of entirely LLM-free execution requires zero relevant local and remote model calls, including perception, within the declared execution scope.

## 8. Work, project files and domain adapters

Robert is planned to choose the available Work mode/environment for client projects and more complex laboratory tasks. A task must identify accessible project files, toolchains, dependencies, required CPU/GPU/memory and its resource allowance. Selecting Work alone does not establish available compute or device access.

Local Work and cloud execution have distinct access boundaries. Cloud tasks do not automatically inherit the host's disk, applications or sessions; authorized file/project transfer or a configured local connection is required. Environment capabilities must be checked for the actual task. See the official [Work overview](https://learn.chatgpt.com/docs/enterprise/chatgpt-work-overview) and [cloud-environment documentation](https://learn.chatgpt.com/docs/environments/cloud-environments).

The common SSI language is intended to describe missions across application languages such as C/C++, Java, C#, Python, JavaScript/TypeScript, Rust and Go, and across smart-home configuration/firmware, PLC automation, CNC, drones, robotics and automotive/embedded projects. These are extensible adapter targets, not a claim that every language, compiler or device is already supported.

Each adapter records supported language/dialect, toolchain/version, environment, build/check/package operations and target-specific acceptance. Generating source, compiling it, passing software tests and validating a physical device remain separate capability levels. Existing organization/project access controls and the resource ledger remain authoritative.

## 9. Verification, Notary, memory and evidence-backed replies

The upgrade must integrate the existing confirmation/signing and conversation modules, with each binding retaining its own status:

| Role or existing mechanism | Planned responsibility in the mission |
|---|---|
| Robert / BODY_FROZEN / laboratory executor | Produce the actual artifact, action receipt and observed outcome in its own runtime scope |
| Native tests, laboratory protocol, verifier/reviewer | Evaluate the declared acceptance criteria and preserve PASS, FAIL or INCONCLUSIVE with reasons |
| Evidence | Bind mission/version, actor, source/package hashes, relevant prompt revision, action/result references and verdict in the event chronology |
| Local Notary / signing | Sign the committed record or manifest and allow integrity/chain verification; never manufacture a missing execution result |
| CONTINUUM | Preserve checkpoints, pending results and effect reconciliation across interruption |
| Research Memory / CEPA and qualification path | Retain observations, failures and verified trials with their scope; apply the existing Challenger/Champion gates |
| Director Charlie and the applicable existing conversation/Navigator or Hermes channel | Prepare and deliver a response from verified outcomes and evidence references, with the appropriate project/private/public projection |
| CZARA/Shadow, when used | Supply labeled proposals or analysis; generated advice is distinct from a native execution verdict |

The response should identify what was performed, what was checked, the outcome, unresolved gaps and the next step. A prompt draft or installation message must not become a factual claim that execution succeeded. The outgoing response and any later correction are subsequent versioned events; prior failures and evidence remain preserved. Existing response delivery must reconcile an uncertain send before retrying.

Local provenance, semantic task validation and independent external attestation remain distinct. The current published local-signing observations do not establish an independent external notary for this new mission path. No external signature or attestation state may be fabricated.

Where external attestation is required, reuse the existing bounded pending-attestation/outage policy and its recovery behavior. Parameters and gates must come from the native contract rather than a new parallel mechanism. See the [Evidence, Digital Signature and Independent Notary/Attestation Contract](../UNIVERSAL_LAB_EVIDENCE_NOTARY_AND_ATTESTATION_CONTRACT_20261008.md).

The integrated sequence is an assigned mission, execution, declared checks, recorded verdict, signed evidence, scoped memory/qualification update and an evidence-backed response. A signature proves the declared record's provenance and integrity; it does not prove the installed module works.

## Acceptance before a deployment claim

The following results are required for this upgrade; all are pending:

- Verify real image input through the selected model/gateway if direct visual analysis is used.
- Complete a bounded desktop task with observed outcome, including changed-target handling, pause and return of control.
- Show that navigation requests and Radar tasks keep their assigned contexts, priority and mission-wide budget limits.
- Exercise complete, partial, unfinished and unknown Radar-source cases; prevent unqualified material from becoming an active block.
- Validate a qualified source adaptation through the existing SSI contracts and evidence path.
- Compare equivalent tasks with and without Luna assistance: completion, errors, retries, elapsed time and cost.
- Complete the guided conversation/download/install/report mission, including interruption and effect reconciliation.
- Demonstrate project registration, the laboratory/control panel and a real bounded input adapter in their declared scopes.
- Verify Director task delegation, prompt-to-mission binding and separate actor identities.
- Confirm Challenger/Champion qualification and the precise model-call scope of any model-free demonstration.
- Verify executor/verifier separation, evidence-chain/signature checks, preserved failure/correction history and accurate response delivery.
- Verify missing-signature, unavailable-notary, altered-record and duplicate-response behavior against the existing contract, without fabricating external attestation.

A later dated report must identify the implemented version and actual test scope before this upgrade is marked implemented, deployed or accepted. No performance gain or successful desktop mission is claimed by this plan.

## References and continuity

- [Robert: existing missions, Technology Radar and repair research](README.md).
- [Canonical C4 architecture and this planned extension](../SSI_V5_C4_ARCHITECTURE.md#planned-robert-scc-luna-navigator-and-radar-upgrade--2026-10-15).
- [Implemented SCC declaration, validation and Awareness attribution](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md).
- [Current truth index](../CURRENT_TRUTH_INDEX.md).

The attribution to amnezja3 for Awareness remains in the SCC source record. This future Robert integration adds no new upstream authorship or historical test claim.
