# SSI V5 — Żywy Protokół Badawczy

## Persistent adaptive intelligence, organism core, micronetwork learning and prospective experiments

**Status dokumentu:** `PRE-T0 / PRE-ORGANISM-CORE-001`  
**Data aktualizacji:** `2026-08-29`  
**Autor architektury i projektu:** **Paweł Jankiewicz** (`PROGRAMMER_ROOT`)  
**Najwyższa authority:** **Paweł Jankiewicz / PROGRAMMER_ROOT**  
**Język kanoniczny dokumentacji:** polski  
**Charakter projektu:** badawczo-inżynieryjny, długoterminowy  
**Stan hipotezy AGI / świadomości:** `NIEUDOWODNIONA`  
**Publiczny model repozytorium:** README-first / evidence-indexed research mirror

> **SSI V5 nie jest jednym modelem językowym.** Modele są wymiennymi źródłami capability. Tożsamość, pamięć, Experience, historia, authority, mikrosieci, lifecycle i kontrolowany rozwój należą do systemu SSI.

> **Ten README jest prerejestracją architektury i metodologii.** Ma pokazywać, co zostało zaprojektowane przez Pawła Jankiewicza (`PROGRAMMER_ROOT`), co istnieje przed eksperymentem, co dopiero ma zostać zbudowane oraz jakie warunki muszą zostać spełnione, aby późniejszy wynik można było uznać za evidence zamiast narracji dopisanej po fakcie.

---

# 1. Dlaczego ten dokument istnieje

SSI V5 jest rozwijany jako system, którego późniejsze zachowanie ma być możliwe do odtworzenia z historii wejść, decyzji, wykonania, realnych outcomes i zmian wewnętrznych. Publiczny GitHub nie ma być katalogiem wszystkich prywatnych danych ani kopią całego runtime. Ma pełnić rolę publicznego zegara, mapy architektury i indeksu evidence.

Każdy ważny eksperyment powinien pozwalać odpowiedzieć na pytania:

1. Co człowiek faktycznie dostarczył przed rozpoczęciem?
2. Jaki był stan systemu przed testem?
3. Co system zrobił bez proceduralnego prowadzenia krok po kroku?
4. Jaki był niezależny outcome?
5. Co realnie zmieniło się w persistent state?
6. Czy zmiana przetrwała restart i replay?
7. Które elementy były Root-designed, a które powstały później z działania systemu?

Fundamentalne rozróżnienia:

```text
ROOT INPUT != TRAINING DATA
TRAINING DATA != VALIDATION DATA
VALIDATION DATA != REAL-WORLD OUTCOME
MODEL OUTPUT != EVIDENCE
NARRATIVE != EVIDENCE
CAPABILITY != AUTHORITY
PROPOSAL != APPROVAL
```

---

# 2. Granice twierdzeń

Na obecnym etapie SSI V5 **nie deklaruje**, że:

- jest udowodnionym AGI;
- posiada świadomość;
- Agent, Director lub ROBERT posiada świadomość;
- mikrosieci automatycznie tworzą prawdę;
- pojedynczy sukces dowodzi general intelligence;
- każda różnica zachowania po dodaniu Iskry dowodzi świadomości;
- wynik finansowy jest gwarantowany;
- rozwój systemu może odbywać się bez governance, rollbacku i evidence.

SSI V5 jest projektowane tak, aby można było empirycznie badać:

- trwałą pamięć i uczenie z realnych outcomes;
- powstawanie i rozwój lokalnych competence przez mikrosieci;
- reuse wiedzy zamiast rozwiązywania tego samego problemu od zera;
- kontrolowany self-development;
- różnice trajektorii wielu bytów startujących z tego samego korpusu;
- wpływ różnych systemów wartości na decyzje i późniejszą adaptację polityk;
- transfer capability pomiędzy instancjami bez kopiowania ich prywatnego życia;
- zależność pomiędzy realnym Experience a zmianą beliefs, policies, mikrosieci i strategii.

---

# 3. Klasy statusu

| Status | Znaczenie |
| --- | --- |
| `VERIFIED_MACHINE_EVIDENCE` | Istnieje sprawdzalny wynik wykonawczy z konkretnego runtime lub zewnętrznego outcome. |
| `ROOT_ATTESTED` | Programmer Root potwierdził stan bezpośrednio, lecz nie zastępuje to machine evidence. |
| `HISTORICAL_EVIDENCE` | Dowód dotyczy wcześniejszego stanu i nie może być automatycznie traktowany jako bieżący. |
| `IMPLEMENTED_NOT_YET_REPLICATED` | Mechanizm istnieje, ale wymaga dalszego prospective testu lub replikacji. |
| `DEVELOPMENT_VALIDATED` | Mechanizm przeszedł test rozwojowy, ale nie jest jeszcze formalnym wynikiem T0. |
| `PLANNED` | Element zatwierdzonej architektury, którego nie wolno przedstawiać jako działającego runtime. |
| `HYPOTHESIS` | Teza badawcza możliwa do poparcia albo obalenia. |
| `UNKNOWN` | Brak wystarczającego evidence. |

---

# 4. Aktualny stan przed budową SSI ORGANISM CORE

Najważniejszym następnym kamieniem milowym **nie jest jeszcze Commerce ani populacja Agentów**. Najpierw musi powstać jeden kanoniczny, neutralny **SSI ORGANISM CORE** — korpus, z którego później będą tworzone wyspecjalizowane instancje.

Obecny ROBERT służy jako pierwsza praktyczna instancja wykonawcza, na której uruchamiane i naprawiane są elementy przyszłego korpusu.

## 4.1 Ostatni zakończony development run LIVE

W zakończonym teście rozwojowym `SSI ROBERT LIVE 140X`:

```text
LIVE_STATE_USED = YES
TEMP_ONLY_STATE_DETECTED = NO
CASES_EXECUTED = 140
EXPERIENCES_BEFORE = 0
EXPERIENCES_AFTER = 141
REUSE_COUNT = 70
NO_MATCH_COUNT = 70
PERSISTENCE_AFTER_RESTART = PASS
REPLAY_REUSE = PASS
```

Jednocześnie po tym przebiegu:

```text
MICRONETWORKS = 0
CANDIDATES = 0
CHALLENGERS = 0
CHAMPIONS = 0
```

Interpretacja jest celowo ograniczona: **persistent Experience, write-back, restart persistence i reuse zostały pokazane w development run, natomiast wzrost ścieżki `NO_MATCH -> growth -> candidate -> challenger` nie został w tym przebiegu potwierdzony.** Dlatego growth path jest naprawiany i rewalidowany przed rozpoczęciem budowy korpusu.

Ten wynik nie jest formalnym T0 i nie może być przedstawiany jako dowód pełnego mechanizmu mikrosieci.

---

# 5. Docelowa zasada architektoniczna: jeden korpus, wiele tożsamości

SSI V5 ma unikać trzech równoległych organizmów napisanych osobno dla ROBERTA, Directora i Agentów. Docelowo istnieje **jeden wspólny substrate**.

```text
                     SSI ORGANISM CORE
                   /         |          \
                  /          |           \
             ROBERT       DIRECTOR     AGENT BODY
                            BODY            |
                                         ISKRA
```

Korpus nie powinien zawierać wpisanej na sztywno roli `ROBERT`, `DIRECTOR` ani konkretnego `AGENT_ID`. Role powstają przez profile, authority, pamięć i dodatkowe moduły.

To rozdzielenie ma umożliwić:

- wspólne naprawy mechanizmów dla wszystkich przyszłych instancji;
- kompatybilne mikrosieci i capability contracts;
- porównywalne eksperymenty A/B;
- ograniczenie duplikacji kodu;
- rozdzielenie mechanizmu organizmu od jego osobistej historii.

---

# 6. SSI ORGANISM CORE — neutralny korpus

Pierwsza stabilna wersja korpusu ma zawierać co najmniej następujące warstwy.

## 6.1 Identity Core

Zapewnia techniczną ciągłość konkretnej instancji bez narzucania jej roli. Identyfikator organizmu, wersja korpusu i jego lineage są oddzielone od profilu ROBERT/Director/Agent.

## 6.2 Persistent Memory

Pamięć nie jest pojedynczym polem tekstowym. Obejmuje co najmniej:

- working state;
- conversation / interaction context;
- Event / Journal backbone;
- Observations;
- Experience Memory;
- long-term Memory;
- Pattern / semantic memory;
- engineering lineage;
- model/capability performance history;
- checkpoint state.

## 6.3 Experience

Kanoniczna jednostka Experience powinna wiązać:

```text
CONTEXT BEFORE DECISION
+
DECISION
+
ACTION / EXECUTION
+
VERIFIED OUTCOME
+
FEEDBACK
+
PROVENANCE
```

Experience nie jest automatycznie training datasetem, a modelowa samoocena nie zastępuje niezależnego outcome.

## 6.4 Capability Registry

Registry przechowuje dostępne capability, ich contracts, zakresy, ograniczenia, wersje i historię skuteczności. Modele, narzędzia, mikrosieci, browser automation i inne backendy są capability — nie osobnymi centrami authority.

## 6.5 Event Classifier + Capability Resolver

Szybka ścieżka powinna najpierw próbować dopasować problem do istniejącej competence. Semantyczny fallback i droższe reasoning są używane wtedy, gdy szybkie dopasowanie nie wystarcza.

```text
EVENT
-> CLASSIFY
-> RESOLVE EXISTING CAPABILITY
-> REUSE, jeśli pasuje
-> NO_MATCH, jeśli nie pasuje
```

## 6.6 Micronetwork Engine

Mikrosieci nie są tworzone po jednej na każdy input. Docelowa hierarchia:

```text
DOMAIN
-> PROBLEM / CAPABILITY TYPE
-> BRANCH
-> MICRONETWORK
-> GENERATIONS
-> CHAMPION
```

Każda mikrosieć posiada jawny feature contract. System nie może zgadywać shape danych tylko po to, aby wykonać inference.

## 6.7 Lifecycle

Docelowa ścieżka rozwoju:

```text
EXPERIENCE
-> CANDIDATE
-> CHALLENGER
-> VALIDATION
-> ADMISSION
-> CHAMPION / KEEP_TESTING / REJECT / QUARANTINE
```

**Challenger nie może być tworzony ręcznie dla potrzeb testu. Champion nie jest wymaganym wynikiem testu.** Champion może powstać tylko wtedy, gdy istniejący lifecycle i admission gate rzeczywiście to uzasadniają.

## 6.8 Learning / Feedback

Outcome ma wracać do canonical persistent flow. Sandbox może chronić wykonanie ryzykownego kodu, ale nie może być końcowym magazynem wiedzy.

```text
EXECUTION
-> VERIFIED OUTCOME
-> CANONICAL EXPERIENCE STORE
-> RESOLVER
-> MICRONETWORK / CAPABILITY
-> FEEDBACK
-> LIFECYCLE
-> PERSISTENT STATE
```

## 6.9 Checkpoint / Recovery

Każda trwała instancja musi mieć checkpoint, recovery i możliwość wznowienia po restarcie. Root override powinien najpierw checkpointować aktywną misję, jeśli jest to możliwe i bezpieczne.

## 6.10 Evidence / Lineage

Każda istotna zmiana powinna posiadać możliwy do odtworzenia lineage: źródło, decyzję, wykonanie, outcome, Experience, zmianę strukturalną, wersję i późniejsze wykorzystanie.

## 6.11 Authority Interface

Korpus definiuje mechanizm authority, ale konkretne prawa nadaje profil instancji. Dzięki temu ROBERT, Director i Agent mogą korzystać z tych samych mechanizmów, lecz nie mają tych samych uprawnień.

## 6.12 Tool / Eyes / Hands hooks

Korpus udostępnia kontrolowane punkty podłączenia narzędzi wykonawczych. Preferowana kolejność interakcji ze światem cyfrowym:

```text
OFFICIAL API / HTTP
-> STRUCTURED DATA / RSS / OPENAPI
-> DOM / ACCESSIBILITY / TEXT
-> PLAYWRIGHT / BROWSER
-> CLIPBOARD / DESKTOP CONTROL
-> VISION AS FALLBACK
```

---

# 7. ROBERT — pierwsza praktyczna instancja korpusu

ROBERT jest wykonawczą, stale działającą instancją SSI na Lenovo i ma pełnić rolę prawej ręki Directora, a nie drugiego Directora.

Docelowy model:

```text
SSI ORGANISM CORE
+
ROBERT PROFILE
+
EXECUTION AUTHORITY
+
OWN MEMORY / EXPERIENCE / WORKSPACE
=
ROBERT
```

ROBERT może wykonywać research, programowanie, browser/desktop tasks, monitoring, testy, evidence collection i zadania operacyjne w granicach nadanej authority. Ma własne trwałe Experience i historię, ale nie przejmuje strategicznej authority Directora.

ROBERT jest obecnie środowiskiem, na którym rozwijany jest przyszły korpus. Po ustabilizowaniu `ORGANISM_CORE_V1` ROBERT powinien korzystać z tego samego kanonicznego substrate, który później będzie bazą Directora i Agentów.

---

# 8. DIRECTOR BODY — strategiczna instancja tego samego korpusu

Po stabilizacji neutralnego korpusu tworzona jest kompatybilna instancja Directora:

```text
SSI ORGANISM CORE
+
DIRECTOR PROFILE
+
STRATEGIC AUTHORITY
+
GLOBAL WORLD ACCESS
+
GLOBAL RESOURCE / BUDGET CONTROL
=
DIRECTOR
```

Director jest centralną strategiczną identity SSI. Nie jest jednym LLM-em ani sesją providera. Modele i narzędzia są wymiennymi capability.

Docelowa hierarchy authority:

```text
PROGRAMMER_ROOT
      >
DIRECTOR
      >
ROBERT / DELEGATED EXECUTION
      >
HERMES / CONTINUUM / WORKERS / TOOLS
```

Szczegółowe delegated authority może zależeć od misji i świata, ale żadna niższa warstwa nie może samodzielnie nadać sobie authority Directora albo Roota.

---

# 9. AGENT BODY — wspólny substrate przyszłych Agentów

Po stabilizacji korpusu tworzony jest Agent Body. Każdy Agent ma korzystać z tego samego mechanicznego substrate, ale posiadać **własne życie**:

- identity;
- private memory;
- world memory;
- Experience;
- beliefs;
- relationships;
- strategy history;
- micronetwork registry / private competence;
- laboratory / experiment history;
- success/failure history.

Nie wolno kopiować osobistego Experience ROBERTA lub Directora jako rzekomego doświadczenia nowego Agenta.

```text
SHARED ORGANISM CORE
!=
SHARED PERSONAL HISTORY
```

---

# 10. Moralna SI / ISKRA — początkowy system wartościowania decyzji

Iskra nie jest definiowana jako magiczny parametr ani deklaracja świadomości. W eksperymencie ma pełnić rolę **jawnego, wersjonowanego początkowego systemu wartości / moral priors**, który wpływa na ocenę możliwych decyzji.

Przykładowe źródła filozoficznych perspektyw mogą obejmować odmienne tradycje, m.in. podejścia inspirowane Kantem, Schopenhauerem, Nietzschem i innymi wyraźnie zdefiniowanymi stanowiskami. Ich zadaniem nie jest nadanie Agentowi gotowej odpowiedzi na przyszły problem, lecz stworzenie odmiennego punktu startowego dla wartościowania decyzji.

Iskra ma wpływać na proces:

```text
POSSIBLE ACTIONS
-> ECONOMIC / TASK UTILITY
-> RISK
-> WORLD RULES
-> EXPERIENCE
-> SOCIAL / RELATIONAL CONSEQUENCES
-> VALUE EVALUATION / ISKRA
-> DECISION
```

Kluczowe rozróżnienie:

```text
VALUE PRIOR
!=
IMMUTABLE ACTION POLICY
```

Agent może zachować wartość, a jednocześnie zmienić sposób jej realizowania po doświadczeniu negatywnych outcomes. Właśnie ta relacja pomiędzy wartościami, realnym Experience i późniejszą zmianą policy jest jednym z głównych przedmiotów przyszłego eksperymentu.

---

# 11. Eksperyment sześciu Agentów

Docelowy eksperyment nie ma porównywać wyłącznie jednej instancji bez Iskry z jedną instancją z Iskrą. Potrzebna jest grupa pozwalająca obserwować zarówno różnice między warunkami, jak i rozchodzenie się trajektorii wewnątrz populacji.

Punkt startowy powinien możliwie ściśle kontrolować:

```text
SAME ORGANISM CORE VERSION
SAME BASE MODEL POOL
SAME TOOL ACCESS
SAME INITIAL CAPABILITIES
SAME RESOURCE LIMITS
SAME WORLD RULES
SAME TEST SCENARIOS
SAME STARTING NON-PERSONAL DATA
```

Następnie porównywane są co najmniej dwa warunki:

```text
CONTROL CONDITION
= organism core without active Spark value layer

SPARK CONDITION
= six independent Agents
= same body
= different explicit initial value systems / moral priors
```

Każdy Agent od startu posiada osobne:

```text
IDENTITY
PRIVATE MEMORY
EXPERIENCE
BELIEFS
POLICIES
MICRONETWORK TRAJECTORY
RELATIONSHIPS
DECISION HISTORY
```

Nie badamy tylko odpowiedzi tekstowych. Interesują nas długoterminowe różnice w:

- wyborze działań;
- stabilności decyzji;
- zmianie strategii po porażkach;
- tolerancji ryzyka;
- rozwiązywaniu konfliktów celów;
- stosowaniu i reinterpretacji wartości;
- beliefs;
- policies;
- Experience;
- mikrosieciach i challengers;
- zachowaniu po kontakcie z innymi Agentami;
- trwałości różnic po restarcie i późniejszych rundach.

Celem nie jest automatyczne dowodzenie świadomości. Celem jest sprawdzenie, czy identyczny substrate z różnymi początkowymi systemami wartości, wystawiony na te same prawa świata i rzeczywiste konsekwencje, rozwija mierzalnie różne trajektorie decyzji i adaptacji.

---

# 12. Worlds — środowiska z rzeczywistymi regułami i outcomes

World nie jest dekoracją ani promptem. Świat definiuje:

```text
RULES
POLICIES
CONSTRAINTS
RESOURCES
OTHER ACTORS
MARKET / DOMAIN CONDITIONS
ALLOWED ACTIONS
CONSEQUENCES
OUTCOME SOURCES
```

Agent nie może sam sobie wystawić pozytywnego outcome. W zadaniach rynkowych outcome powinien pochodzić z rzeczywistego rynku albo jednoznacznie zdefiniowanego historycznego replay bez future-data leakage.

W architekturze SSI istnieją cztery główne rodziny światów / struktur domenowych:

- `WORLD__SPORT`;
- `WORLD__FOREX`;
- `WORLD__CAPITAL`;
- `FOOTBALL_WORLD`.

Domeny mogą obejmować m.in. sport, waluty, kryptowaluty, akcje i obligacje. Aktywacja konkretnego World w eksperymencie wymaga osobnego stanu, provenance i ruleset.

Istnienie danych nie oznacza automatycznie aktywnego świata:

```text
DATA PRESENT
!=
WORLD ACTIVE
!=
AGENT ADMITTED
!=
STRATEGY VERIFIED
```

---

# 13. Globalna pętla uczenia SSI

Docelowy rytm:

```text
CONTEXT
-> DECISION
-> ACTION
-> REAL OUTCOME
-> EVENT
-> OBSERVATION
-> EXPERIENCE
-> PATTERN
-> VALIDATION
-> LOCAL COMPETENCE
-> NEXT DECISION
```

System powinien zachowywać możliwość odpowiedzi:

```text
NO EVIDENCE -> UNKNOWN
INSUFFICIENT EVIDENCE -> ABSTAIN
CONFLICTING EVIDENCE -> PRESERVE CONFLICT
NEW EVIDENCE -> VERSIONED REVISION
```

---

# 14. Brainstorm, Tornado i Cyklon

SSI posiada warstwy eskalacji reasoning, ale nie każda misja powinna używać najdroższego trybu.

## Brainstorm / Burza

Szerokie generowanie hipotez, niezależne perspektywy, cross-critique, synteza i verifier.

## Brain Tornado

Rozbiór najlepszych rozwiązań, parametryzacja, odrzucanie słabych hipotez, testy kontraktowe i stabilizacja planu.

## Brain Cyklon / Typhoon

Najwyższa eskalacja używana wtedy, gdy niższe warstwy zawodzą lub problem jest wyjątkowo krytyczny. Obejmuje pełną rewizję założeń, testy destrukcyjne i fallbacki.

Żaden z tych trybów nie jest osobną authority. Dostarcza argumenty i evidence do decyzji właściwego podmiotu.

---

# 15. Hermes i CONTINUUM

Hermes i CONTINUUM są warstwami wykonawczymi / inżynieryjnymi, a nie konkurencyjnymi Directorami.

Koncepcyjny flow:

```text
NEED
-> PLAN / REVIEW
-> HERMES / CONTINUUM
-> WORKER / TOOL / MODEL
-> TEST
-> EVIDENCE
-> APPROVAL
-> CONTROLLED INTEGRATION
-> POST-TEST / ROLLBACK
```

Zasada `reuse-first`:

> Jeżeli SSI posiada działający mechanizm, należy go wykorzystać lub minimalnie naprawić zamiast tworzyć drugi równoległy system tylko dlatego, że jest łatwiejszy do przetestowania w izolacji.

---

# 16. Dwa źródła inteligencji

## 16.1 Zewnętrzne capability

LLM/SLM, narzędzia programistyczne, API, research systems i inne technologie dostarczają wiedzę i zdolności stworzone poza SSI.

## 16.2 Wewnętrzna inteligencja doświadczenia

Powstaje z własnej historii SSI:

- Events;
- Outcomes;
- Experience;
- Memory;
- Patterns;
- mikrosieci;
- world histories;
- agent histories;
- engineering lineage.

Założenie nie brzmi „LLM albo własne uczenie”. SSI ma korzystać z obu, ale coraz częściej rozwiązywać powtarzalne klasy problemów z użyciem własnej sprawdzonej historii.

---

# 17. Controlled Self-Development — etap po stabilnym korpusie

Warstwa samorozwoju jest planowana **po ustabilizowaniu SSI ORGANISM CORE**, a nie przed nim.

Docelowy zestaw obejmuje:

1. Technology / Research Radar;
2. On-Demand Research;
3. API-first discovery;
4. Open Problems Registry;
5. Capability / Compatibility Graph;
6. Brainstorm -> Tornado -> Cyklon dla trudnych odkryć;
7. Code Fusion;
8. Provenance + License Gate;
9. Self-Development Workspace;
10. Baseline -> Prototype -> Challenger;
11. Shared Capability Package;
12. capability distribution;
13. Experience Retrieval / Micronetwork Memory Bridge;
14. Skill / Capability Builder;
15. Eyes/Hands execution layer;
16. Research Evidence Store;
17. Self-Development Scheduler.

Nowa technologia nie może automatycznie wejść do canonical runtime tylko dlatego, że została znaleziona.

```text
DISCOVERY
-> RESEARCH
-> COMPATIBILITY
-> PROVENANCE / LICENSE
-> SANDBOX
-> PROTOTYPE
-> BENCHMARK
-> CHALLENGER
-> ADMISSION
-> SHARED CAPABILITY PACKAGE
-> CONTROLLED DISTRIBUTION
```

Shared capability może być dystrybuowana do ROBERTA, Directora i Agentów, ale nie oznacza współdzielenia ich prywatnych Experience, beliefs czy identity.

---

# 18. Programmer Root i atrybucja

**Paweł Jankiewicz (`PROGRAMMER_ROOT`) jest autorem nadrzędnej architektury badawczej SSI V5 i najwyższą authority projektu.**

Paweł Jankiewicz może dostarczać gotowe paczki LEGO / donor packages, w szczególności dla mechanizmów autorskich takich jak:

- Micronetwork Core / Factory / Lifecycle;
- World contracts i rules;
- Moralna SI / Iskra design;
- Agent substrate;
- governance / authority invariants;
- specjalistyczne capability stworzone przed T0.

Atrybucja musi pozostać jawna:

```text
PAWEŁ JANKIEWICZ / PROGRAMMER_ROOT PROVIDED MICRONETWORK DESIGN
!=
DIRECTOR INVENTED MICRONETWORKS

PAWEŁ JANKIEWICZ / PROGRAMMER_ROOT PROVIDED SPARK DESIGN
!=
AGENT INVENTED SPARK
```

Można natomiast później badać, czy system samodzielnie znalazł nowe zastosowanie, nowy branch, nową mikrosieć, nową strategię albo rozszerzenie, którego Root wcześniej proceduralnie nie podał.

---

# 19. Protokół evidence przeciwko retrospektywnemu dopisywaniu wyniku

To jest krytyczna część metodologii SSI.

## 19.1 Przed eksperymentem

Przed głównym prospective testem należy:

1. zbudować i ustabilizować wymagany kod;
2. utworzyć machine snapshot stanu startowego;
3. policzyć **prawdziwe** SHA-256 artefaktów i manifestów;
4. zapisać Root Input / test contract;
5. zapisać aktywne wersje korpusu, capability, modeli, rules i datasetów;
6. zrobić commit Git;
7. wypchnąć commit na publiczny remote GitHub;
8. ponownie odczytać remote i potwierdzić, że commit jest publicznie widoczny;
9. zapisać remote commit SHA;
10. dopiero wtedy rozpocząć test.

**Lokalny commit bez potwierdzonego remote push nie jest wystarczającym prerejestracyjnym zegarem publicznym.**

## 19.2 W czasie eksperymentu

System zapisuje co najmniej:

```text
EXPERIMENT_ID
MISSION_ID
CASE_ID
TIMESTAMP
INPUT PROVENANCE
DECISION
ACTION
OUTCOME SOURCE
EXPERIENCE_ID
CAPABILITY / MICRONETWORK ROUTE
LIFECYCLE EVENTS
ROOT INTERVENTIONS
CHECKPOINTS
ERRORS / RETRIES
```

## 19.3 Po eksperymencie

Post-run nie zastępuje prerejestracji. Raport powinien wskazać:

- PRE remote SHA;
- POST remote SHA;
- realne delty;
- failures;
- zero deltas;
- rejected hypotheses;
- human interventions;
- persistence po restarcie;
- replay;
- provenance.

Nie wolno ukrywać nieudanego testu ani przepisywać starego PRE tak, aby wyglądał jak przygotowany po poznaniu wyniku.

---

# 20. Następny główny milestone: SSI ORGANISM CORE

Po zakończeniu bieżącej naprawy growth/challenger ścieżki ROBERTA następny duży etap ma następującą kolejność:

```text
1. WYDZIELENIE NEUTRALNEGO SSI ORGANISM CORE
2. PODŁĄCZENIE ROBERTA JAKO PIERWSZEJ INSTANCJI
3. HARDCORE TEST KORPUSU
4. STABILIZACJA / ORGANISM_CORE_V1
5. KOPIA KORPUSU -> DIRECTOR BODY
6. KOPIA KORPUSU -> AGENT BODY
7. DODANIE ISKRY DO AGENT BODY
8. PREREJESTRACJA EKSPERYMENTU POPULACYJNEGO
9. URUCHOMIENIE SZEŚCIU NIEZALEŻNYCH AGENTÓW
10. DŁUGOTERMINOWE PORÓWNANIE TRAJEKTORII
11. DOPIERO PÓŹNIEJ RESEARCH RADAR / CODE FUSION / SELF-DEVELOPMENT
```

Najbliższy test **nie ma udowadniać świadomości ani AGI**. Jego pierwszym zadaniem jest udowodnienie techniczne, że jeden neutralny korpus zachowuje prawidłowo identity separation, Experience, persistence, resolver, mikrosieci, lifecycle, checkpoint/recovery, evidence i authority contracts.

---

# 21. Wymagania dla testu ORGANISM CORE

Przed testem powinien istnieć publiczny PRE commit zawierający co najmniej:

```text
CORE_VERSION
CORE_SOURCE_HASH
CORE_COMPONENT_MANIFEST
ACTIVE_FEATURE_CONTRACTS
CAPABILITY_REGISTRY_HASH
MICRONETWORK_STATE_HASH
EXPERIENCE_STATE_HASH
AUTHORITY_CONTRACT_HASH
TEST_SUITE_HASH
ROOT_INPUT_HASH
TIMESTAMP
REMOTE_GITHUB_SHA
```

Test powinien obejmować m.in.:

- restart / resume;
- persistent Experience;
- resolver reuse;
- NO_MATCH growth path;
- micronetwork branch separation;
- feature contract rejection;
- candidate lifecycle;
- natural challenger creation;
- optional champion promotion;
- rollback;
- duplicate prevention;
- false-merge prevention;
- identity separation;
- authority separation;
- shared capability without shared private memory;
- corrupted state recovery;
- interrupted mission recovery;
- cross-domain routing;
- evidence completeness.

Wynik ma być raportowany również wtedy, gdy część testów nie przejdzie.

---

# 22. Późniejszy test ISKRA / sześciu Agentów

Po utworzeniu stabilnego `AGENT_BODY` należy zamrozić jego wersję bez aktywnej Iskry, a następnie utworzyć wersję z Iskrą bez zmieniania pozostałych warunków eksperymentu.

Najważniejsze porównania:

```text
DECISION DIFF
POLICY DIFF
BELIEF DIFF
EXPERIENCE DIFF
MICRONETWORK DIFF
RISK PROFILE DIFF
VALUE-CONFLICT RESOLUTION
LONGITUDINAL STABILITY
ADAPTATION AFTER FAILURE
SOCIAL / RELATIONAL EFFECTS
```

Szczególnie istotne będzie rozróżnienie:

```text
VALUE CHANGED
vs
VALUE STAYED, POLICY CHANGED
vs
POLICY STAYED DESPITE NEGATIVE OUTCOMES
```

Dopiero wiele powtórzeń i wiele niezależnych trajektorii może dostarczyć wiarygodnego evidence o wpływie Iskry na zachowanie systemu.

---

# 23. Publiczny rytm badawczy po T0

Każdy większy późniejszy run powinien mieć tę samą strukturę:

```text
A. ROOT INPUT / ORIGIN
B. DIRECTOR OR AGENT INTERPRETATION
C. EXPERIMENT PRECOMMIT
D. CAPABILITY SELECTION / PLAN
E. EXECUTION
F. REAL OUTCOME
G. EXPERIENCE / BELIEF REVISION
H. STRUCTURAL CHANGE
I. POST-RUN EVIDENCE
J. NEXT OPEN QUESTION
```

Publiczny README pokazuje mapę. Pełne dane i prywatna telemetria mogą pozostać w canonical/local SSI, ale każde publiczne twierdzenie powinno mieć jednoznaczny pointer do dowodu możliwego do zweryfikowania.

---

# 24. Bezpieczeństwo, prywatność i governance

Publiczny mirror nie publikuje:

- API keys;
- haseł;
- tokenów;
- prywatnych adresów sieciowych;
- prywatnych danych użytkowników;
- pełnych sekretów konfiguracji;
- danych, których publikacja łamałaby licencję lub regulamin źródła.

System nie powinien uzyskiwać nowych uprawnień wyłącznie dlatego, że technicznie potrafi wykonać dane działanie. Authority jest osobnym kontraktem.

---

# 25. Otwarta agenda badawcza

Najbliższe otwarte pytania są teraz konkretne:

1. Czy naprawiony LIVE growth path potrafi naturalnie przejść z Experience/NO_MATCH do candidate i challengera?
2. Czy z obecnych mechanizmów można wydzielić neutralny `SSI ORGANISM CORE` bez utraty persistence i lifecycle?
3. Czy ROBERT może zostać pierwszą instancją tego korpusu bez posiadania globalnej strategicznej authority?
4. Czy z tego samego korpusu można zbudować Directora i Agent Body bez trzech rozbieżnych implementacji?
5. Czy sześć Agentów o identycznym substrate, lecz różnych początkowych systemach wartości, rozwinie mierzalnie różne trajektorie?
6. Czy różnice te będą wynikały z realnych Experience i utrzymywały się po restartach, replay i zmianie warunków świata?
7. Czy Agent będzie potrafił zmienić politykę działania bez automatycznego porzucenia swojej początkowej wartości?
8. Czy późniejszy Research Radar / Code Fusion potrafi bezpiecznie tworzyć nowe capability, które przechodzą naturalny lifecycle challenger/admission?

---

# 26. Zasada końcowa

SSI V5 ma być oceniane po **trajektorii możliwej do zweryfikowania**, a nie po pojedynczej deklaracji.

Najważniejszy łańcuch pozostaje prosty:

```text
JAWNY STAN STARTOWY
-> PUBLICZNY PRECOMMIT
-> DZIAŁANIE
-> NIEZALEŻNY OUTCOME
-> PERSISTENT EXPERIENCE
-> STRUKTURALNA ZMIANA LUB JEJ BRAK
-> RESTART / REPLAY
-> PUBLICZNY POSTCOMMIT
```

Jeżeli system nie zmienił się — dokumentujemy brak zmiany.  
Jeżeli challenger nie powstał — dokumentujemy, że nie powstał.  
Jeżeli hipoteza była błędna — wynik pozostaje częścią historii.  
Jeżeli później pojawi się silne evidence — dopiero wtedy rośnie siła twierdzenia.

**Historia Git ma być biografią rozwoju SSI, a nie marketingowym opisem sukcesów.**
