# SSI V5 — Żywy Protokół Badawczy

## Persistent adaptive intelligence, organism core, micronetwork learning and longitudinal agent research

**Status dokumentu:** `PRE-T0 / PRE-ORGANISM-CORE-001`  
**Data aktualizacji:** `2026-08-29`  
**Autor architektury i projektu:** **Paweł Jankiewicz** (`PROGRAMMER_ROOT`)  
**Najwyższa authority:** **Paweł Jankiewicz / PROGRAMMER_ROOT**  
**Język kanoniczny dokumentacji:** polski  
**Charakter projektu:** badawczo-inżynieryjny, długoterminowy  
**Stan hipotezy AGI / świadomości:** `NIEUDOWODNIONA`  
**Publiczny model repozytorium:** `README-first / evidence-indexed research mirror`

> **SSI V5 nie jest jednym modelem językowym.** Modele są wymiennymi źródłami capability. Tożsamość, pamięć, Experience, historia, authority, mikrosieci, lifecycle i kontrolowany rozwój należą do systemu SSI.

> **Ten README jest równocześnie prerejestracją, mapą architektury i publiczną kroniką procesu badawczego.** Ma pokazywać nie tylko sukcesy, lecz również błędy, nieudane hipotezy, naprawy, regresje i kolejne próby — tak, aby późniejsze wyniki nie mogły zostać przedstawione tak, jakby były znane przed eksperymentem.

---

# 1. SSI V5 w pigułce

SSI V5 bada możliwość zbudowania trwałego, adaptacyjnego organizmu programowego, którego inteligencja nie jest utożsamiona z jednym LLM-em. Zewnętrzne modele i narzędzia dostarczają capability, natomiast własne Experience, Memory, history, authority, lokalne kompetencje i ewolucja pozostają częścią persistent systemu.

Docelowa architektura wykorzystuje jeden neutralny korpus:

```text
                      SSI ORGANISM CORE
                    /         |          \
                   /          |           \
              ROBERT       DIRECTOR     AGENT BODY
                             BODY            |
                                           ISKRA
```

Pierwszą praktyczną instancją jest **ROBERT**. Po ustabilizowaniu korpusu ten sam substrate ma zostać wykorzystany do budowy **Directora**, a następnie **Agent Body**. Agenci mają posiadać własne identity, Experience, beliefs, policies i mikrosieci. W późniejszym eksperymencie sześć Agentów otrzyma odmienne początkowe systemy wartości — Iskry — przy możliwie identycznych pozostałych warunkach.

---

# 2. Dlaczego projekt jest publicznie dokumentowany przed T0

Jednym z głównych problemów badań nad autonomicznymi systemami jest możliwość retrospektywnego wybierania udanych wyników albo przepisywania narracji po eksperymencie.

SSI V5 przyjmuje przeciwną zasadę:

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

Jeżeli test nie przejdzie, porażka pozostaje częścią historii. Jeżeli później błąd zostanie naprawiony, naprawa otrzymuje nowy commit i nowe evidence. Stary PRE nie jest przepisywany tak, aby wyglądał idealnie po poznaniu wyniku.

Publiczny GitHub ma dzięki temu z czasem stać się **biografią rozwoju SSI**, a nie zbiorem wyłącznie udanych demonstracji.

---

# 3. Co jest wkładem projektu

SSI V5 łączy kilka znanych kierunków badawczych w jeden długoterminowy system eksperymentalny:

- persistent identity i memory;
- uczenie z realnych outcomes;
- lokalne mikrosieci competence;
- lifecycle `candidate -> challenger -> validation -> champion/reject`;
- reuse własnego Experience przed kosztownym reasoning;
- wspólny neutralny organism substrate dla różnych ról;
- rozdzielenie capability od authority;
- światy posiadające własne rules i niezależne outcome sources;
- osobiste trajektorie Agentów;
- jawne początkowe systemy wartości / Moralna SI / Iskra;
- kontrolowany self-development;
- publiczną prerejestrację i dokumentowanie również niepowodzeń.

**Nie twierdzimy, że każdy z tych elementów jest sam w sobie nowy.** Hipoteza badawcza dotyczy ich integracji oraz zachowania całego systemu w długim czasie.

---

# 4. Granice twierdzeń

Na obecnym etapie SSI V5 **nie deklaruje**, że:

- jest udowodnionym AGI;
- posiada świadomość;
- Director, ROBERT lub Agent posiada świadomość;
- pojedynczy udany run dowodzi general intelligence;
- mikrosieci automatycznie tworzą prawdę;
- różnica zachowania po dodaniu Iskry dowodzi świadomości;
- wynik ekonomiczny jest gwarantowany;
- każdy sukces wynika z autonomii.

Projekt został zaprojektowany tak, aby można było empirycznie badać tezy, a nie zakładać ich prawdziwość.

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

# 5. Klasy statusu i evidence

| Status | Znaczenie |
| --- | --- |
| `VERIFIED_MACHINE_EVIDENCE` | Istnieje sprawdzalny wynik wykonawczy z konkretnego runtime lub zewnętrznego outcome. |
| `ROOT_ATTESTED` | Programmer Root potwierdził stan bezpośrednio, lecz nie zastępuje to machine evidence. |
| `HISTORICAL_EVIDENCE` | Dowód opisuje wcześniejszy stan. |
| `IMPLEMENTED_NOT_YET_REPLICATED` | Mechanizm istnieje, ale wymaga dalszego prospective testu. |
| `DEVELOPMENT_VALIDATED` | Mechanizm przeszedł test rozwojowy, lecz nie jest jeszcze formalnym wynikiem T0. |
| `PLANNED` | Element zatwierdzonej architektury, który nie jest jeszcze działającym runtime. |
| `HYPOTHESIS` | Teza możliwa do poparcia albo obalenia. |
| `UNKNOWN` | Brak wystarczającego evidence. |

---

# 6. Aktualny etap: droga do T0

Projekt znajduje się blisko punktu T0, ale **T0 nie został jeszcze ogłoszony**.

Istnieją już elementy silnika oraz LIVE runtime ROBERTA, jednak przed freeze potrzebne jest:

1. domknięcie stabilności lifecycle;
2. idempotentny replay/retry/restart;
3. wydzielenie neutralnego SSI ORGANISM CORE;
4. hardcore test całego korpusu;
5. machine snapshot i prawdziwe SHA-256;
6. publiczny PRE commit potwierdzony z remote;
7. dopiero następnie formalny prospective run.

Obecny etap jest więc klasyfikowany jako:

```text
PRE-T0 / BUILD-UP-TO-T0
```

---

# 7. Publiczna historia realnych błędów i napraw

SSI V5 celowo zachowuje błędy odkryte podczas budowy.

## 7.1 LIVE 140X — Experience działa, growth nie działa

W pierwszym istotnym LIVE development run:

```text
CASES_EXECUTED = 140
EXPERIENCES_AFTER = 141
REUSE_COUNT = 70
NO_MATCH_COUNT = 70
PERSISTENCE_AFTER_RESTART = PASS
REPLAY_REUSE = PASS
MICRONETWORKS = 0
CANDIDATES = 0
CHALLENGERS = 0
CHAMPIONS = 0
```

Wynik pokazał, że canonical Experience write-back i persistence działają, lecz `NO_MATCH` nie uruchamiał growth path.

## 7.2 Naprawa growth path

Analiza wykazała, że istniejący resolver/lifecycle nie był prawidłowo połączony z LIVE runtime. Po minimalnej naprawie `NO_MATCH -> candidate` zaczął działać i system zaczął zapisywać realnych kandydatów.

## 7.3 Candidate -> challenger

Kolejny test wykazał, że candidate’y powstają, ale nie akumulują poprawnie evidence albo nie dochodzą do promotion lifecycle. Po naprawie połączeń LIVE naturalny challenger został utworzony bez ręcznego wpisania statusu i bez obniżania progów.

## 7.4 Nowe błędy ujawnione po naturalnym challengerze

Udany promotion ujawnił następne problemy:

```text
DUPLICATION_FAILURES = 134
REPLAY_REUSE = FAIL
ERROR CLASS = NoneType.get during replay/reload path
```

To nie zostało ukryte ani oznaczone jako końcowy sukces. Aktualny etap naprawia:

- idempotency lifecycle;
- duplicate promotion handling;
- replay/reuse po restarcie;
- stale/null/missing references;
- odporność na retry, duplicate delivery i restart storms.

Po naprawie planowany jest stress-test obejmujący m.in. 100x promotion replay, 100x case replay, 100x duplicate delivery, 20 restartów oraz 600 nowych LIVE przypadków.

**Ta sekcja będzie rozwijana wraz z kolejnymi rzeczywistymi wynikami.**

---

# 8. SSI ORGANISM CORE — neutralny korpus

Korpus ma być neutralnym mechanizmem, a nie zakodowaną rolą `ROBERT`, `DIRECTOR` lub konkretnego Agenta.

Minimalny zakres `ORGANISM_CORE_V1`:

1. Identity Core
2. Persistent Memory
3. Experience
4. Beliefs / State interfaces
5. Capability Registry
6. Event Classifier
7. Capability Resolver
8. Micronetwork Engine
9. Candidate / Challenger / Validation / Champion Lifecycle
10. Learning / Feedback
11. Checkpoint / Recovery
12. Evidence / Lineage
13. Resource / Budget interface
14. Authority interface
15. CONTINUUM hooks
16. Research / Reasoning hooks
17. Tools / Eyes / Hands hooks

Korpus ma umożliwiać wspólne poprawki mechanizmów bez tworzenia trzech niezależnych implementacji dla ROBERTA, Directora i Agentów.

---

# 9. Experience i wewnętrzna pętla uczenia

Kanoniczna jednostka Experience wiąże:

```text
CONTEXT BEFORE DECISION
+
DECISION
+
ACTION
+
VERIFIED OUTCOME
+
FEEDBACK
+
PROVENANCE
```

Docelowy rytm poznawczy:

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

System powinien móc zachować:

```text
NO EVIDENCE -> UNKNOWN
INSUFFICIENT EVIDENCE -> ABSTAIN
CONFLICTING EVIDENCE -> PRESERVE CONFLICT
NEW EVIDENCE -> VERSIONED REVISION
```

---

# 10. Micronetwork Engine

Mikrosieci nie są tworzone po jednej na każdy input.

Docelowa struktura:

```text
DOMAIN
-> PROBLEM / CAPABILITY TYPE
-> BRANCH
-> MICRONETWORK
-> GENERATIONS
-> CHAMPION
```

Każda mikrosieć posiada jawny feature contract.

Lifecycle:

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE ACCUMULATION
-> CHALLENGER
-> VALIDATION
-> ADMISSION
-> CHAMPION / KEEP_TESTING / REJECT / QUARANTINE
```

Challenger i champion nie mogą być tworzeni ręcznie tylko dlatego, że test oczekuje ich istnienia.

---

# 11. ROBERT

ROBERT jest pierwszą praktyczną, stale działającą instancją SSI.

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

ROBERT ma wykonywać m.in. research, programowanie, browser/desktop tasks, monitoring, evidence collection i zadania operacyjne. Posiada własną historię i Experience, lecz nie przejmuje strategicznej authority Directora.

---

# 12. DIRECTOR

Po stabilizacji neutralnego korpusu powstaje strategiczna instancja:

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

Director nie jest jednym LLM-em. Modele i narzędzia są wymiennymi capability.

Hierarchy authority:

```text
PAWEŁ JANKIEWICZ / PROGRAMMER_ROOT
             >
          DIRECTOR
             >
     DELEGATED EXECUTION
             >
HERMES / CONTINUUM / WORKERS / TOOLS
```

---

# 13. AGENT BODY

Każdy przyszły Agent ma korzystać z tego samego mechanicznego korpusu, ale posiadać własną indywidualną historię:

- identity;
- private memory;
- world memory;
- Experience;
- beliefs;
- policies;
- relationships;
- strategy history;
- micronetwork trajectory;
- success/failure history.

```text
SHARED ORGANISM CORE
!=
SHARED PERSONAL HISTORY
```

---

# 14. Moralna SI / ISKRA

Iskra jest definiowana jako **jawny, wersjonowany początkowy system wartościowania decyzji**, a nie deklaracja świadomości czy magiczny parametr osobowości.

Przykładowe inspiracje mogą obejmować różne tradycje filozoficzne, m.in. Kanta, Schopenhauera, Nietzschego i inne wyraźnie opisane stanowiska.

Proces decyzji może uwzględniać:

```text
POSSIBLE ACTIONS
-> TASK / ECONOMIC UTILITY
-> RISK
-> WORLD RULES
-> EXPERIENCE
-> SOCIAL CONSEQUENCES
-> VALUE EVALUATION / ISKRA
-> DECISION
```

Kluczowa hipoteza:

```text
VALUE PRIOR != IMMUTABLE ACTION POLICY
```

Agent może zachować wartość, a jednocześnie zmienić sposób jej realizowania pod wpływem realnego Experience.

---

# 15. Eksperyment sześciu Agentów

Późniejszy eksperyment populacyjny ma możliwie ściśle kontrolować:

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

Następnie sześć niezależnych Agentów otrzyma różne jawne initial value systems / moral priors.

Badane będą nie tylko odpowiedzi tekstowe, lecz długoterminowe różnice w:

- decyzjach;
- beliefs;
- policies;
- tolerancji ryzyka;
- reakcjach na porażkę;
- mikrosieciach;
- relacjach;
- strategiach;
- value-conflict resolution;
- zachowaniu po restartach i wielu rundach Experience.

Celem nie jest automatyczne dowodzenie świadomości. Celem jest sprawdzenie, czy identyczny substrate, różniący się początkowym systemem wartości i późniejszą osobistą historią, rozwija mierzalnie odmienne trajektorie.

---

# 16. Worlds i niezależne outcomes

World nie jest dekoracją ani promptem. Definiuje:

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

W SSI istnieją m.in. struktury domenowe:

- `WORLD__SPORT`
- `WORLD__FOREX`
- `WORLD__CAPITAL`
- `FOOTBALL_WORLD`

Istnienie danych nie oznacza automatycznie aktywnego świata:

```text
DATA PRESENT
!= WORLD ACTIVE
!= AGENT ADMITTED
!= STRATEGY VERIFIED
```

Realny outcome ma pochodzić z niezależnego źródła albo jednoznacznie zdefiniowanego historycznego replay bez future-data leakage.

---

# 17. Brainstorm, Tornado i Cyklon

SSI wykorzystuje adaptacyjną eskalację reasoning:

- **Brainstorm / Burza** — szerokie hipotezy, niezależne perspektywy, cross-critique, synthesis, verifier;
- **Brain Tornado** — rozbiór najlepszych rozwiązań, parametryzacja i testy kontraktowe;
- **Brain Cyklon / Typhoon** — rewizja założeń, destructive testing i fallbacki, gdy niższe poziomy zawodzą.

Żaden z tych trybów nie otrzymuje automatycznie authority Directora.

---

# 18. Hermes i CONTINUUM

Hermes i CONTINUUM są warstwami wykonawczymi i inżynieryjnymi.

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

Fundamentalna zasada:

> **reuse-first:** jeżeli SSI posiada działający mechanizm, należy go wykorzystać lub minimalnie naprawić zamiast tworzyć równoległy system tylko dlatego, że łatwiej uzyskać w nim PASS.

---

# 19. Dwa źródła inteligencji

## Zewnętrzne capability

Modele, API, frameworki, narzędzia programistyczne i systemy research dostarczają wiedzę oraz zdolności stworzone poza SSI.

## Wewnętrzna inteligencja doświadczenia

Powstaje z własnej historii:

- Events;
- Outcomes;
- Experience;
- Memory;
- Patterns;
- mikrosieci;
- world histories;
- agent histories;
- engineering lineage.

SSI nie zakłada wyboru „LLM albo własne uczenie”. System ma wykorzystywać oba źródła, ale powtarzalne problemy coraz częściej rozwiązywać na podstawie własnej zweryfikowanej historii.

---

# 20. Controlled Self-Development — etap późniejszy

Po stabilizacji korpusu planowana jest warstwa samorozwoju obejmująca m.in.:

- Technology / Research Radar;
- On-Demand Research;
- Open Problems Registry;
- Capability / Compatibility Graph;
- Code Fusion;
- Provenance + License Gate;
- Self-Development Workspace;
- Prototype -> Challenger -> Admission;
- Shared Capability Packages;
- Experience Retrieval;
- Skill / Capability Builder;
- Eyes / Hands;
- Research Evidence Store;
- Self-Development Scheduler.

Nowa technologia nie może wejść do canonical runtime wyłącznie dlatego, że została znaleziona.

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
-> CONTROLLED DISTRIBUTION
```

---

# 21. Programmer Root i uczciwa atrybucja

**Paweł Jankiewicz (`PROGRAMMER_ROOT`) jest autorem nadrzędnej architektury badawczej SSI V5 i najwyższą authority projektu.**

Root może dostarczać wcześniej zaprojektowane paczki LEGO / donor packages, np.:

- Micronetwork Core / Factory / Lifecycle;
- World contracts;
- Moralna SI / Iskra design;
- Agent substrate;
- governance / authority invariants.

Atrybucja musi pozostać jawna:

```text
ROOT PROVIDED MICRONETWORK DESIGN
!= DIRECTOR INVENTED MICRONETWORKS

ROOT PROVIDED ISKRA DESIGN
!= AGENT INVENTED ISKRA
```

Późniejsza samodzielna adaptacja, nowe zastosowanie albo nowa capability może otrzymać osobne lineage, jeżeli evidence to potwierdza.

---

# 22. Protokół PRE / POST

## Przed formalnym eksperymentem

Należy:

1. ustabilizować wymagany kod;
2. wykonać machine snapshot;
3. policzyć prawdziwe SHA-256;
4. zapisać Root Input i test contract;
5. zapisać aktywne wersje core/capability/models/rules/data;
6. wykonać commit Git;
7. push na publiczny GitHub;
8. ponownie odczytać remote;
9. potwierdzić publiczny commit SHA;
10. dopiero potem uruchomić prospective test.

Lokalny commit bez potwierdzonego remote push nie jest publicznym prerejestracyjnym zegarem.

## Podczas eksperymentu

Zapisywane powinny być m.in.:

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

## Po eksperymencie

Raport publikuje zarówno sukcesy, jak i:

- FAIL;
- zero deltas;
- rejected hypotheses;
- retries;
- root interventions;
- regressions;
- remaining limitations.

---

# 23. Droga do ORGANISM_CORE_V1

```text
1. DOMKNIĘCIE LIVE LIFECYCLE ROBERTA
2. IDEMPOTENCY / REPLAY / RESTART STABILITY
3. WYDZIELENIE NEUTRALNEGO SSI ORGANISM CORE
4. PODŁĄCZENIE ROBERTA JAKO PIERWSZEJ INSTANCJI
5. HARDCORE TEST KORPUSU
6. FREEZE ORGANISM_CORE_V1
7. CORE -> DIRECTOR BODY
8. CORE -> AGENT BODY
9. DODANIE ISKRY DO AGENT BODY
10. PREREJESTRACJA POPULATION EXPERIMENT
11. SZEŚĆ NIEZALEŻNYCH AGENTÓW
12. DŁUGOTERMINOWE PORÓWNANIE TRAJEKTORII
13. DOPIERO PÓŹNIEJ RESEARCH RADAR / CODE FUSION / SELF-DEVELOPMENT
```

---

# 24. Minimalny hardcore test korpusu

`ORGANISM_CORE_V1` powinien przejść co najmniej:

- restart / resume;
- persistent Experience;
- resolver reuse;
- NO_MATCH growth;
- branch separation;
- feature contract rejection;
- natural candidate lifecycle;
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

# 25. Research & Collaboration

SSI V5 jest projektem prowadzonym niezależnie przez **Pawła Jankiewicza**. Publiczna dokumentacja ma umożliwiać technicznym czytelnikom ocenę rzeczywistych decyzji architektonicznych, przebiegu eksperymentów oraz historii napraw.

Projekt jest otwarty na **merytoryczny kontakt dotyczący**:

- niezależnego technical/research review;
- współpracy nad persistent agents i cognitive architectures;
- lifelong / continual learning;
- experience-driven competence systems;
- self-improving / self-developing systems;
- multi-agent longitudinal experiments;
- value-conditioned agents i Moral AI;
- evidence/provenance dla autonomicznych systemów;
- integracji konkretnych capability;
- wspólnych eksperymentów lub publikacji;
- rozmów o wykorzystaniu, integracji lub licencjonowaniu wybranych autorskich mechanizmów.

Otwartość na rozmowę **nie oznacza**, że cały kod, prywatne datasety, sekrety, pełna implementacja mikrosieci albo wszystkie rozwiązania projektowe są automatycznie objęte licencją open-source. Zakres ewentualnego udostępnienia lub współpracy jest ustalany oddzielnie.

Najbardziej wartościową formą kontaktu jest krytyka oparta na evidence: wskazanie alternatywnej interpretacji, możliwego leakage, błędu eksperymentalnego, podobnego prior art albo propozycji replikacji.

---

# 26. Dlaczego dokumentowane są porażki

Dla tego projektu niepowodzenie testu jest informacją badawczą, a nie materiałem do usunięcia.

Docelowy zapis każdego ważnego problemu:

```text
BUG / FAILED HYPOTHESIS OBSERVED
-> MACHINE EVIDENCE
-> ROOT CAUSE
-> MINIMAL FIX
-> REGRESSION TEST
-> STRESS TEST
-> RESULT
-> REMAINING LIMITATIONS
```

Taka historia pozwala później ocenić nie tylko efekt końcowy, ale również zdolność projektu do rzeczywistego wykrywania, lokalizowania i eliminowania problemów.

---

# 27. Bezpieczeństwo, prywatność i IP

Publiczny mirror nie publikuje:

- API keys;
- tokenów;
- haseł;
- prywatnych danych;
- prywatnych adresów sieciowych;
- pełnych sekretów konfiguracji;
- materiałów objętych ograniczeniami licencyjnymi;
- elementów implementacji, które zostały świadomie zachowane jako prywatne know-how.

Publiczny evidence trail ma być wystarczająco mocny do oceny twierdzeń, ale nie wymaga ujawnienia każdego szczegółu prywatnego runtime.

---

# 28. Otwarta agenda badawcza

Najbliższe pytania:

1. Czy lifecycle pozostaje idempotentny pod retry/replay/restart storm?
2. Czy naturalny challenger przeżywa wielokrotne reloady bez duplicate promotion?
3. Czy neutralny `SSI ORGANISM CORE` można wydzielić bez utraty persistence i lifecycle?
4. Czy ROBERT może być pierwszą instancją korpusu bez strategicznej authority Directora?
5. Czy z tego samego korpusu powstaną Director Body i Agent Body bez trzech rozbieżnych implementacji?
6. Czy sześć Agentów o identycznym substrate i różnych początkowych wartościach rozwinie mierzalnie odmienne trajektorie?
7. Czy Agent potrafi zmieniać policy pod wpływem Experience bez automatycznego porzucania bazowej wartości?
8. Czy późniejszy Research Radar / Code Fusion będzie potrafił tworzyć nowe capability przechodzące naturalny challenger/admission lifecycle?

---

# 29. Jak oceniać SSI V5

SSI V5 powinno być oceniane po **trajektorii możliwej do zweryfikowania**, nie po deklaracji autora ani modelu.

Silniejsze evidence oznacza:

- prerejestrację przed testem;
- niezależny outcome;
- persistent state;
- realne delty;
- failure retention;
- restart/replay;
- lineage;
- możliwość replikacji;
- publiczną chronologię zmian.

Jeżeli system nie zmienił się — dokumentujemy brak zmiany.  
Jeżeli challenger nie powstał — dokumentujemy, że nie powstał.  
Jeżeli po naprawie powstał nowy błąd — dokumentujemy nowy błąd.  
Jeżeli hipoteza była błędna — pozostaje częścią historii.  
Jeżeli później pojawi się silne evidence — dopiero wtedy rośnie siła twierdzenia.

**Historia Git ma być biografią rozwoju SSI, a nie marketingowym opisem sukcesów.**
