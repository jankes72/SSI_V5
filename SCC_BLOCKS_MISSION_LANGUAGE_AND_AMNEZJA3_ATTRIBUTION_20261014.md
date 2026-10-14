# SCC — język misji dla Blocks / BLOCKS Mission Language

**Published:** 2026-10-14  
**SSI integration:** Universal Lab, A27 declarative goal module  
**Deployment:** reported by the author/operator on 2026-10-14  
**Reproduced checks:** 22 Python tests and 10 JavaScript contract assertions passed, with zero provider calls.

## Polski — nowy moduł i podziękowanie

**SCC to rozwijany język programowania misji dla klocków Blocks w SSI V5.** Pierwszy działający moduł A27 pozwala zapisać cel misji w uporządkowanej notacji, sprawdzić jej składnię i deterministycznie przełożyć ją na istniejący kontrakt planowania. Paweł Jankiewicz deklaruje, że ten etap został wdrożony i działa w jego środowisku SSI. Zapis określa projekt, zadanie, strategię i wersję, domenę, stan wejściowy, cel, kontekst, kryterium oraz ograniczenia.

**Inspiracją i źródłem adaptowanych mechanizmów jest Awareness autorstwa mojego brata, [amnezja3](https://github.com/amnezja3).** Jego [projekt przetwarzania języka polskiego](https://github.com/amnezja3/awareness) podsunął mi sposób myślenia o elementach, konstrukcjach, ich powiązaniach i statystykach. Przeniosłem wybrane mechanizmy konstrukcji z obszaru języka na misje mikrosieci i Blocks. Tak powstaje SCC: język opisujący cel i powiązania działań SSI. Adaptacja, implementacja języka misji i integracja z SSI są pracą Pawła Jankiewicza; autorstwo źródłowego Awareness pozostaje przypisane amnezja3.

To kolejny wkład mojego brata w idee rozwijane w SSI. Przypisuję mu również **źródłowe idee Moralnej SI/Iskier, pomysł rekursji wykorzystany w świecie piłki nożnej oraz początkowy pomysł i pierwszy krok połączenia Czary**. Późniejsze rozwinięcia i implementacje tych elementów w SSI mają swoją odrębną historię. Ta wzmianka uzupełnia istniejące zapisy pochodzenia i podkreśla ciągłość jego inspiracji.

Chcę szczególnie wyróżnić pracę mojego brata i zachęcić do poznania jego biblioteki. **W mojej ocenie jego umiejętności są większe od moich; wiele zawdzięczam jego pomysłom. Dziękuję za Awareness i inspiracje, które pomogły mi rozwinąć język SCC do Blocks.**

Obecny etap jest **deklaracją celu i planowaniem liniowych konstrukcji**. Pełne polecenia operacyjne, warunki i równoległe programy stanowią dalszy zakres języka. Publikacja rozróżnia poniżej działającą notację od dostępności wykonania championów i od przyszłych rozszerzeń.

## Awareness — poznaj oryginalną bibliotekę do języka polskiego

[**Awareness autorstwa amnezja3**](https://github.com/amnezja3/awareness) to biblioteka Pythona poświęcona analizie i budowaniu konstrukcji w języku polskim. Warto poznać ją jako samodzielny projekt autora.

Według dokumentacji projektu oferuje między innymi:

- **analizę budowy zdania** przez moduł Action: rozpoznawanie podmiotu, orzeczenia i innych elementów oraz zapis analizowanych konstrukcji w bazie;
- **tworzenie bardziej złożonych konstrukcji** przez Advanced Action, z powiązaniem elementów i kategoriami;
- **obsługę odmiany rzeczowników i przymiotników** przez przypadki oraz pracę z formami czasowników w `verb_flex`;
- **narzędzia do analizy tekstu, generowania konstrukcji i badań lingwistycznych** nad językiem polskim.

Dokumentacja źródłowa zawiera opis instalacji i przykłady użycia po polsku i angielsku. **[Zobacz Awareness i przykłady autora](https://github.com/amnezja3/awareness/blob/main/README.md).** Biblioteka jest udostępniona na licencji MIT.

### Dokładne pochodzenie mechanizmów wykorzystanych w SSI

Historia adaptacji i manifest przypiętych zasobów wskazują repozytorium `amnezja3/awareness`, commit `2767692de842fb1184f17d3249fc17b72c7527d1`. Z niego wykorzystano wybrane funkcje trzech modułów:

| Moduł autora | Funkcje wykorzystane w adaptacji | Rola w konstrukcjach misji |
|---|---|---|
| [baseTools.py](https://github.com/amnezja3/awareness/blob/2767692de842fb1184f17d3249fc17b72c7527d1/baseTools.py) | `take_word`, `take_LID`, `take_se`, `take_links`, `take_sentens` | Odczyt kanonicznych elementów, identyfikatorów, konstrukcji i połączeń |
| [checkerBaseOperators.py](https://github.com/amnezja3/awareness/blob/2767692de842fb1184f17d3249fc17b72c7527d1/checkerBaseOperators.py) | `fix_cat_list`, `neuralSentensPrepare`, `part_split_IN_OUT`, `part_most_popular` | Porządkowanie struktur, przygotowanie trajektorii oraz analiza wejść, wyjść i częstości |
| [addionalisAwe.py](https://github.com/amnezja3/awareness/blob/2767692de842fb1184f17d3249fc17b72c7527d1/addionalisAwe.py) | `stats_part`, `generator_AI_most_popular` | Statystyki elementów i generator konstrukcji |

W SSI identyfikatory elementów reprezentują bloki i mikrosieci, konstrukcje opisują trajektorie misji, a powiązania opisują przejścia. Adaptacja zawiera również poprawkę statystyki `stats_part`, odnotowaną w manifeście zasobów. Oryginalny projekt Awareness zachowuje autorstwo amnezja3 i własny zakres językowy; dostosowanie wybranych mechanizmów do misji oraz parser i integracja SCC należą do prac Pawła Jankiewicza nad SSI.

## What the implemented module does

SCC is the public name used in this announcement for SSI's developing BLOCKS mission language. The first implementation is A27's versioned, deterministic goal notation. Existing `SSI_MISJA 1` syntax and `ssi.mission.goal.r1` / `ssi.mission.intent.r1` identifiers remain unchanged for compatibility.

The module provides:

- parsing, canonical rendering and deterministic conversion to the existing mission intent;
- explicit strategy/version, input/goal, context SHA-256, acceptance reference and bounded step count;
- project/task selection through existing Operations and project access controls;
- a view of the linear proposals returned by the existing backend, including assigned Champions, versions, feature contracts and validation requirements;
- saved-context reads through the existing Research Memory, with integrity checks and pagination;
- explicit gap reporting and the existing Shadow proposal path.

Parsing, rendering, validation and history reads require no external language-model call. Existing Router V10, Research Memory and Operations remain the host mechanisms. Optional decision assistance and tasks that themselves require a language model retain their existing provider and budget rules.

## Supported declaration

This is a syntax example with illustrative IDs and a placeholder context hash, rather than an executable reference to a real project or Champion:

```text
SSI_MISJA 1
PROJEKT "example_project"
ZADANIE "example_task"
STRATEGIA "example_strategy"
WERSJA_STRATEGII "v1"
DOMENA "example_domain"
WEJSCIE "example_input"
CEL "example_goal"
KONTEKST_SHA256 "0000000000000000000000000000000000000000000000000000000000000000"
KRYTERIUM "example_criterion_v1"
MAKS_KROKOW 16
PELNA_WALIDACJA false
KONIEC
```

Values are JSON literals; IDs are quoted strings. The current parser rejects unknown symbols, duplicate/missing fields, unsupported versions, invalid types and requirements it cannot preserve. It also rejects imperative operations, branching and parallelism instead of silently converting them into a simple goal query.

## From Polish-language constructions to BLOCKS missions

The adapted idea is compositional: canonical elements form constructions, constructions have links, and repeated verified constructions can inform later planning. In SCC, those elements represent blocks, networks, transitions and mission trajectories.

Selected Awareness construction, graph and statistics primitives underpin the Transition Champions layer. Their input in this adaptation is network identity and mission history. The language-facing work of an existing LLM remains separate from deterministic mission validation.

The mission layer preserves one strategy and acceptance criterion across decisions. Champion assignments remain explicit and versioned. Reuse of a known complete trajectory, validation of a partially known composition and full-flow preparation retain distinct meanings. Frequency alone does not establish successful execution.

Reducing repeated planning and unnecessary model calls is an engineering objective. This publication makes no measured production speedup claim; comparable mission latency, call count and verified outcomes are required to quantify the gain.

## Deployment and validation boundaries

| Item | Status recorded for this publication |
|---|---|
| A27 deployment and use | Author/operator reports it deployed and working on 2026-10-14; a new production receipt was not independently checked for this publication |
| Declarative parser and integration tests | 22 Python tests reproduced successfully against the supplied A27 code and temporary native RM/Operations fixtures |
| Frontend notation contract | 10 JavaScript assertions reproduced successfully, including Python/JavaScript notation agreement |
| Paid provider calls during these checks | 0 |
| Browser DOM, phone acceptance and live MSI/NODE01 tests | Not performed in this publication's validation |
| Champion execution in the reviewed A26/A27 implementation | Disabled; semantic execution Evidence remains unbound |
| General imperative operations, branches and parallel programs | Future implementation; explicitly rejected by the current parser |

An accepted goal declaration is a planning input. Native feature contracts, actual capability bindings, approvals and semantic Evidence determine execution readiness. The reviewed module preserves separate states for proposal, qualification, execution and verified result. The author's deployment statement concerns the implemented declarative module, not completion of every planned SCC feature.

## Planned Robert integration — 2026-10-15

**PLANNED / NOT IMPLEMENTED / NOT DEPLOYED.** The next extension connects the common SSI mission language to Robert's own desktop-control loop and GUI cockpit, an additional Luna instance with visual Navigator and Technology Radar profiles, and source qualification before active Decomposer/BLOCKS adaptation. The additional Luna is separate from Flow/Full Flow assistance. A27's deployed declarative scope and reproduced checks above do not establish this future runtime.

See the [dated Robert upgrade plan](ROBERT/PLANNED_SCC_LUNA_NAVIGATOR_RADAR_UPGRADE_20261015.md) and [Robert's preserved mission history](ROBERT/README.md). No new imperative syntax, live visual-model capability or desktop acceptance result is announced here.

## Attribution and continuing contribution

**Author-supplied attribution, 2026-10-14:** Paweł Jankiewicz identifies [amnezja3](https://github.com/amnezja3) as his brother and credits him for several formative contributions:

| Contribution | Credit and scope |
|---|---|
| Awareness and SCC | Awareness is amnezja3's Polish-language project and the source/inspiration for selected construction mechanisms adapted into the SCC mission layer |
| Moralna SI / early ISKRA ideas | Earlier source ideas informed later moral/value and ISKRA work; SSI's later implementations and integration have their own authorship history |
| Football World recursion | The source recursion idea/mechanisms influenced later Football World work; the Football World project and its SSI implementation remain Paweł's project line |
| CZARA origin | Initial direction and first connection step, as already recorded in the early-CZARA attribution |
| Appreciation | Paweł expresses his personal view that his brother has greater technical skills and acknowledges the influence of his ideas |

Existing chronology is preserved:

- [Early CZARA contribution and attribution](EXTERNAL_REVIEW_FEEDBACK_AND_ATTRIBUTION_20260929.md)
- [Moralna SI / ISKRA source attribution](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)
- [Earlier source archives and later SSI adaptation](MICHAL_JANKIEWICZ_SOURCE_PROJECTS_AND_SSI_ADAPTATION_20260916.md)
- [Football World mechanism-level influences](FOOTBALL_WORLD_CURRENT_STATUS_20260916.md)

### Awareness as a standalone Polish-language project

Awareness deserves recognition for its own documented Polish-language sentence analysis, construction generation and inflection tools. The Polish introduction above links to the author's original project and names the exact three source modules and eleven functions used in the SSI construction adaptation. The recognition of amnezja3's work is independent of the later SCC implementation.

### Upstream provenance

- Repository: [amnezja3/awareness](https://github.com/amnezja3/awareness).
- Source revision used by the adapted construction resources: [`2767692de842fb1184f17d3249fc17b72c7527d1`](https://github.com/amnezja3/awareness/commit/2767692de842fb1184f17d3249fc17b72c7527d1).
- Upstream licence: MIT. Source credit and licence are retained with the adapted resources.
- SCC mission-language adaptation and SSI integration: Paweł Jankiewicz.

This is the public module description, validation summary and attribution record for the proprietary SSI implementation.
