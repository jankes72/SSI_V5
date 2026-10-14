# Robert — planned SCC, Luna Navigator and Technology Radar upgrade

**Decision recorded:** 15 October 2026, Europe/Warsaw.  
**Status:** `PLANNED / NOT IMPLEMENTED / NOT DEPLOYED`.  
**Runtime acceptance of this upgrade:** `NOT RUN`.  
**Scope:** future extension of Robert's existing desktop missions and Technology Radar within the SSI research project.

## Polski — co dopiero zostanie dodane

**To jest zapowiedź kolejnego upgrade'u Roberta. Opisane tutaj rozszerzenie nie jest jeszcze zaimplementowane ani wdrożone.** Plan obejmuje własny kokpit GUI Roberta, zintegrowane sterowanie rzeczywistym kursorem i klawiaturą, dodatkową instancję Luny do obrazu i nawigacji oraz analizę materiałów Radaru Technologii przed ich adaptacją przez Decomposer do wspólnego języka SSI.

Dodatkowa Luna ma być odrębna od instancji używanej przy mikrosieciach, Flow i Full Flow. Otrzyma dwa stałe profile: **Navigator** do sytuacji wizualnej i **Radar** do źródeł oraz kodu. Robert zachowa wykonanie i sprawdzanie efektów. Ocena Luny nie będzie samodzielnym dowodem kompletności ani poprawności kodu. Do aktywnego wykorzystania przejdzie wyłącznie zakres potwierdzony odpowiednimi sprawdzeniami.

Ten plan rozwija [ostatnio opisane misje Roberta](README.md#2-the-initial-drone-to-desktop-mission-transfer) oraz [publikację modułu SCC](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md). Nie zmienia wyników wcześniejszych misji.

## Existing baseline and future scope

The [Robert record](README.md) preserves the V9 local research result: 10/10 waypoints and 24 signed events, with zero GUI actions, network access or model calls. The latest GUI diagnostic in that record stopped before acting. Those observations do not test the upgrade proposed here.

A27's declarative goal notation remains the separately published, operator-reported deployment. Its reproduced parser/integration checks are not runtime acceptance of Robert navigation, visual Luna assistance, Technology Radar qualification or a general imperative SCC executor.

This publication adds a dated development plan only. It provides no installation package, new runtime result or activation receipt.

## 1. Robert owns the desktop-control loop

Robert is planned to own perception, navigation, native mouse/keyboard execution and outcome verification as one integrated module. His own GUI is the cockpit: current view, selected target, mission step, proposed action, observed result and control ownership.

The local controller performs cursor movement and immediate checks. Model consultation occurs at navigation decision points rather than for each cursor increment. The target session uses the operating system's native access mechanism, explicit human/Robert/paused states and a tested return-control action.

The current desktop mission retains its Dell-only constraint and discovers geometry at runtime. Old coordinates are not a substitute for current targeting. A changed screen or target invalidates the associated action until it is checked again.

## 2. Additional Luna: two fixed profiles

The proposed additional Luna instance is separate from the model context used for micronetwork construction, Flow and Full Flow.

| Profile | Proposed responsibility | Output |
|---|---|---|
| Navigator | Interpret the current image or crop together with the mission goal and recent actions | A bounded next-step proposal, an identified target, an expected effect or a request for another observation |
| Radar | Analyse retrieved source material, implementation scope, dependencies and gaps | A source-linked assessment and a proposal for the checks needed to qualify the relevant capability |

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

## Acceptance before a deployment claim

The following results are required for this upgrade; all are pending:

- Verify real image input through the selected model/gateway if direct visual analysis is used.
- Complete a bounded desktop task with observed outcome, including changed-target handling, pause and return of control.
- Show that navigation requests and Radar tasks keep their assigned contexts, priority and mission-wide budget limits.
- Exercise complete, partial, unfinished and unknown Radar-source cases; prevent unqualified material from becoming an active block.
- Validate a qualified source adaptation through the existing SSI contracts and evidence path.
- Compare equivalent tasks with and without Luna assistance: completion, errors, retries, elapsed time and cost.

A later dated report must identify the implemented version and actual test scope before this upgrade is marked implemented, deployed or accepted. No performance gain or successful desktop mission is claimed by this plan.

## References and continuity

- [Robert: existing missions, Technology Radar and repair research](README.md).
- [Canonical C4 architecture and this planned extension](../SSI_V5_C4_ARCHITECTURE.md#planned-robert-scc-luna-navigator-and-radar-upgrade--2026-10-15).
- [Implemented SCC declaration, validation and Awareness attribution](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md).
- [Current truth index](../CURRENT_TRUTH_INDEX.md).

The attribution to amnezja3 for Awareness remains in the SCC source record. This future Robert integration adds no new upstream authorship or historical test claim.
