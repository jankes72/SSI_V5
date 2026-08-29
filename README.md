# SSI V5 — Żywy Protokół Badawczy

## Persistent adaptive intelligence, organism core, micronetwork learning and longitudinal agent research

**Status dokumentu:** `PRE-T0 / ORGANISM-CORE-MIGRATION`  
**Data aktualizacji:** `2026-08-29`  
**Autor architektury i projektu:** **Paweł Jankiewicz** (`PROGRAMMER_ROOT`)  
**Najwyższa authority:** **Paweł Jankiewicz / PROGRAMMER_ROOT**  
**Język kanoniczny dokumentacji:** polski  
**Charakter projektu:** badawczo-inżynieryjny, długoterminowy  
**Stan hipotezy AGI / świadomości:** `NIEUDOWODNIONA`  
**Publiczny model repozytorium:** `README-first / evidence-indexed research mirror`

> **SSI V5 nie jest jednym modelem językowym.** Modele są wymiennymi źródłami capability. Tożsamość, pamięć, Experience, historia, authority, mikrosieci, lifecycle i kontrolowany rozwój należą do systemu SSI.

> **Ten README jest równocześnie prerejestracją, mapą architektury i publiczną kroniką procesu badawczego.** Ma pokazywać sukcesy, błędy, nieudane hipotezy, naprawy, regresje i kolejne próby — tak, aby późniejsze wyniki nie mogły zostać przedstawione tak, jakby były znane przed eksperymentem.

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

Pierwszą praktyczną instancją jest **ROBERT**. Obecny etap polega na wydzielaniu z jego działających i przetestowanych mechanizmów neutralnego `SSI ORGANISM CORE`. Po stabilizacji korpusu ten sam substrate ma zostać wykorzystany do budowy **Director Body** o innym profilu i większej strategicznej authority, a następnie **Agent Body**. Projekty i światy operacyjne są etapem późniejszym i nie są warunkiem obecnej migracji core.

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

## 2.1 Zweryfikowane tempo rozwoju

GitHub pozwala obecnie odtworzyć bardzo wczesną chronologię SSI/MSDI. Ważne jest rozróżnienie między **datą zapisaną w historii Git** a **datą utworzenia publicznego repozytorium GitHub**.

```text
2026-07-19 19:58 CEST  root commit: MSDI AI v0.01 - start projektu
2026-07-19 20:06 CEST  documentation foundation
2026-07-19 20:32 CEST  system architecture foundation
2026-07-27 16:55 CEST  publiczne repo jankes72/msdi-ai utworzone na GitHubie
2026-07-28 07:46 CEST  SSI Core - podstawowa struktura systemu
2026-07-28 07:56 CEST  Data World Foundation + PROJECT_JOURNAL
2026-07-28 09:21 CEST  V2 Model Laboratory / V2ToV3 bridge
2026-07-28 09:25 CEST  PROJECT_RULES: MSDI AI / SSI, V2/V3/V4/CORE
2026-08-01 20:08 CEST  SSI V5 FAZA 1 - runtime, memory, teacher integration
2026-08-14 09:59 CEST  publiczne repo CONTINUUM
2026-08-16 15:27 CEST  publiczne repo SSI_V5_MASTER
2026-08-25 19:27 CEST  obecny publiczny research mirror SSI_V5
2026-08-29              ROBERT po hardening 600X + migracja SSI ORGANISM CORE
```

Na dzień 29 sierpnia 2026 daje to około **41 dni od root commita historii Git** oraz około **33 dni od utworzenia pierwszego publicznego repo `msdi-ai`** do obecnego etapu. To potwierdza bardzo szybkie tempo udokumentowanej ewolucji architektury.

Nie interpretujemy tego jako dowodu, że wszystkie dane, wcześniejsze skrypty lub całe doświadczenie autora powstały w 33–41 dni. Takie twierdzenie byłoby zbyt mocne. Publicznie weryfikowalne jest natomiast to, że **udokumentowana architektura MSDI/SSI przeszła w tym krótkim okresie od v0.01/foundation przez SSI Core i SSI V5 do ROBERTA, stress-testów replay/idempotency oraz rozpoczęcia migracji neutralnego Organism Core**.

Pełna oś czasu wraz z SHA commitów i zasadami interpretacji znajduje się w [`evidence/DEVELOPMENT_TIMELINE.md`](evidence/DEVELOPMENT_TIMELINE.md).

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

# 6. Aktualny etap: ROBERT ustabilizowany przed migracją core

Projekt nadal znajduje się w fazie `PRE-T0`, ale zakończył istotny etap stabilizacji LIVE ROBERTA przed ekstrakcją neutralnego korpusu.

Najważniejsza sekwencja rozwojowa była następująca:

```text
LIVE EXPERIENCE / REUSE
-> wykryty brak growth
-> naprawa NO_MATCH -> candidate
-> naprawa candidate -> challenger
-> naturalny challenger
-> ujawnione błędy idempotency/replay
-> naprawa
-> brutalny stress-test 600X
-> stabilny lifecycle/replay/restart
-> rozpoczęcie migracji do SSI ORGANISM CORE
```

T0 nie został jeszcze ogłoszony. Formalny freeze wymaga zakończenia migracji, pełnego testu całego korpusu, snapshotu, prawdziwych SHA-256 i publicznego PRE przed prospective run.

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

Kolejny test wykazał, że candidate’y powstają, ale nie dochodzą prawidłowo do evidence accumulation / eligibility / promotion lifecycle. Po naprawie połączeń LIVE naturalny challenger został utworzony bez ręcznego wpisania statusu i bez obniżania progów.

## 7.4 Błędy ujawnione po naturalnym challengerze

Udany promotion ujawnił następne problemy:

```text
DUPLICATION_FAILURES = 134
REPLAY_REUSE = FAIL
ERROR CLASS = NoneType.get during replay/reload path
```

Root cause obejmował brak pełnej idempotencji promotion/replay oraz przypadki, w których evidence/metadata mogły być `null`, a kod wykonywał `.get()` bez właściwego guardu.

## 7.5 Naprawa idempotency / replay

Naprawiono m.in.:

- ponowne promotion istniejącego challengera;
- deduplikację Experience/evidence;
- bezpieczne reload/hydration pól `None`;
- obsługę stale/null/missing references;
- retry/replay bez podwójnego naliczania stanu.

## 7.6 Hardcore 600X — wynik po naprawie

Po naprawie wykonano stress-test obejmujący:

- `100x` ponowną próbę promotion tego samego logicznego challengera;
- `100x` replay tego samego przypadku;
- `100x` retry/duplicate-delivery storm;
- `20x` restart storm;
- null/stale reference tests;
- concurrency/interleaving;
- `600` nowych LIVE cases;
- finalny replay po restarcie.

Najważniejsze wyniki:

```text
DUPLICATION_FAILURES = 0
FALSE_MERGE_FAILURES = 0
NONE_GET_ERRORS = 0
IDEMPOTENCY_PROMOTION_100X = PASS
IDEMPOTENCY_REPLAY_100X = PASS
RETRY_STORM_100X = PASS
RESTART_STORM_20X = PASS
DUPLICATE_EVIDENCE_GUARD = PASS
NULL_CONTRACT_TORTURE = PASS
CONCURRENCY_OR_INTERLEAVING = PASS
PERSISTENCE_AFTER_RESTART = PASS
REPLAY_REUSE = PASS
CRITICAL_STOP = 0
```

W promotion torture 100 kolejnych prób dotyczących już-promowanego obiektu nie utworzyło nowych challengerów; wszystkie zostały obsłużone jako istniejący stan. W replay torture pojedynczy logical Experience został zapisany raz, a kolejne powtórzenia zostały potraktowane jako duplikaty.

Ten wynik jest traktowany jako **development validation stabilności lifecycle/replay/idempotency ROBERTA przed migracją core**, a nie jako formalny T0.

## 7.7 Znana niespójność raportowa

W bundle 600X wykryto rozbieżność liczby challengerów w jednym snapshotcie `BEFORE`:

```text
BASELINE / FINAL REPORT: CHALLENGERS_BEFORE = 5
jeden BEFORE_STATE snapshot: challengers = 6
```

Nie ma evidence, że rozbieżność ta zmieniła wynik torture tests lub finalną integralność runtime, ale pozostaje jawnie zapisana jako:

```text
REPORTING_BASELINE_DISCREPANCY = 5 vs 6 challengers
```

Nie jest ukrywana ani retrospektywnie wygładzana.

---

# 8. Aktualny etap — migracja do SSI ORGANISM CORE

Po stabilizacji ROBERTA rozpoczęto kontrolowane wydzielanie neutralnych mechanizmów do:

```text
SSI ORGANISM CORE
```

Zasada migracji:

```text
DZIAŁAJĄCY MODUŁ ROBERTA
-> PASZPORT
-> DEPENDENCY MAP
-> BACKUP
-> SHA256
-> COPY
-> NEUTRALIZATION
-> ROBERT ADAPTER
-> SHADOW / PARITY
-> LIVE REGRESSION
-> ROLLBACK TEST
-> ACCEPT / REJECT
```

Migracja oznacza `COPY`, nie destrukcyjne przenoszenie. Oryginalny działający mechanizm pozostaje rollbackiem do czasu pełnego zaakceptowania core.

Fundamentalne rozróżnienie:

```text
COPY MECHANISM
!=
COPY PERSONAL HISTORY
```

Do shared core nie jest kopiowana osobista historia ROBERTA jako historia Directora lub przyszłych Agentów.

## 8.1 Pierwszy wydzielony klocek — Micronetwork Engine

Pierwsza migracja mikrosieci została wykonana jako kontrolowana ekstrakcja do neutralnego core z adapterem ROBERTA.

Raport migracyjny wykazał m.in.:

```text
SOURCE PRESERVED = YES
COPY_NOT_MOVE = YES
SHADOW_PARITY = PASS (12/12)
LIVE_REGRESSION = PASS (10/10)
DUPLICATION_FAILURES = 0
FALSE_MERGE_FAILURES = 0
NONE_GET_ERRORS = 0
REPLAY_REUSE = PASS
PERSISTENCE_AFTER_RESTART = PASS
IDEMPOTENCY = PASS
```

Persistent state mikrosieci został zachowany; hash state/inventory przed i po migracji był zgodny. Runtime ROBERTA korzysta z wydzielonego mechanizmu przez adapter, a źródłowy moduł pozostał dostępny jako rollback.

W tym bundle wykryto też błąd jakości evidence: `SHA256SUMS.txt` nie był zapisany w standardowym formacie zgodnym z `sha256sum -c`. Nie unieważnia to wyników migracji, ale od kolejnych modułów wymagany jest standardowy manifest `hash  path` oraz — jeśli potrzebny — osobny czytelny `MIGRATION_HASHES.env`.

## 8.2 Kolejne moduły migracji

Kolejność dalszej ekstrakcji:

```text
M00 MICRONETWORKS            = MIGRATED / DEVELOPMENT VALIDATED
M01 EXPERIENCE_STORE         = CURRENT MIGRATION SUITE
M02 LIFECYCLE
M03 RESOLVER_CLASSIFIER
M04 CAPABILITY_REGISTRY
M05 CHECKPOINT_RECOVERY
M06 EVIDENCE_LINEAGE
M07 AUTHORITY
M08 IDENTITY_MEMORY
M09 FULL_CORE_INTEGRATION
```

Każdy moduł przechodzi ten sam schemat paszportu, hashy, parity, regresji i rollbacku.

---

# 9. SSI ORGANISM CORE — neutralny korpus

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

# 10. Experience i wewnętrzna pętla uczenia

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

# 11. Micronetwork Engine

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

# 12. ROBERT

ROBERT jest pierwszą praktyczną, stale działającą instancją SSI i obecnie także **donorem sprawdzonych mechanizmów dla neutralnego core**.

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

# 13. DIRECTOR BODY — następna wyspecjalizowana instancja po core

Po zakończeniu migracji i stabilizacji neutralnego korpusu planowane jest zbudowanie **Director Body** z tego samego sprawdzonego substrate.

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

Director nie będzie kopią osobistego życia ROBERTA. Ma współdzielić mechanizmy korpusu, ale posiadać inną rolę, authority i własny stan.

Hierarchy authority:

```text
PAWEŁ JANKIEWICZ / PROGRAMMER_ROOT
             >
          DIRECTOR
             >
     ROBERT / DELEGATED EXECUTION
             >
HERMES / CONTINUUM / WORKERS / TOOLS
```

---

# 14. AGENT BODY — etap po Director Body

Po stabilizacji korpusu i Director Body powstanie Agent Body oparty na tym samym mechanicznym substrate.

Każdy przyszły Agent ma posiadać własną indywidualną historię:

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

# 15. Moralna SI / ISKRA

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

---

# 16. Eksperyment sześciu Agentów

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

Badane będą długoterminowe różnice w decyzjach, beliefs, policies, tolerancji ryzyka, reakcjach na porażkę, mikrosieciach, relacjach i strategiach.

Celem nie jest automatyczne dowodzenie świadomości. Celem jest sprawdzenie, czy identyczny substrate, różniący się początkowym systemem wartości i późniejszą osobistą historią, rozwija mierzalnie odmienne trajektorie.

---

# 17. Worlds i projekty — etap późniejszy

World nie jest dekoracją ani promptem. Definiuje rules, constraints, resources, actors, allowed actions, consequences i outcome sources.

W architekturze istnieją m.in. struktury domenowe:

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

Aktualny etap nie polega jednak na rozwijaniu światów ani projektów. Najpierw mają zostać ustabilizowane: neutralny core, Director Body i Agent Body. Operacyjne światy i projekty będą rozwijane później przez właściwe instancje systemu pod obowiązującą authority i governance.

---

# 18. Brainstorm, Tornado i Cyklon

SSI wykorzystuje adaptacyjną eskalację reasoning:

- **Brainstorm / Burza** — szerokie hipotezy, niezależne perspektywy, cross-critique, synthesis, verifier;
- **Brain Tornado** — rozbiór najlepszych rozwiązań, parametryzacja i testy kontraktowe;
- **Brain Cyklon / Typhoon** — rewizja założeń, destructive testing i fallbacki, gdy niższe poziomy zawodzą.

Żaden z tych trybów nie otrzymuje automatycznie authority Directora.

---

# 19. Hermes i CONTINUUM

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

# 20. Dwa źródła inteligencji

## Zewnętrzne capability

Modele, API, frameworki, narzędzia programistyczne i systemy research dostarczają wiedzę oraz zdolności stworzone poza SSI.

## Wewnętrzna inteligencja doświadczenia

Powstaje z własnej historii: Events, Outcomes, Experience, Memory, Patterns, mikrosieci, world histories, agent histories i engineering lineage.

SSI nie zakłada wyboru „LLM albo własne uczenie”. System ma wykorzystywać oba źródła, ale powtarzalne problemy coraz częściej rozwiązywać na podstawie własnej zweryfikowanej historii.

---

# 21. Controlled Self-Development — etap późniejszy

Po stabilizacji korpusu planowana jest warstwa samorozwoju obejmująca m.in. Technology / Research Radar, On-Demand Research, Open Problems Registry, Capability / Compatibility Graph, Code Fusion, Provenance + License Gate, Self-Development Workspace, Shared Capability Packages, Experience Retrieval i Skill / Capability Builder.

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

# 22. Programmer Root i uczciwa atrybucja

**Paweł Jankiewicz (`PROGRAMMER_ROOT`) jest autorem nadrzędnej architektury badawczej SSI V5 i najwyższą authority projektu.**

Atrybucja musi pozostać jawna:

```text
ROOT PROVIDED MICRONETWORK DESIGN
!= DIRECTOR INVENTED MICRONETWORKS

ROOT PROVIDED ISKRA DESIGN
!= AGENT INVENTED ISKRA
```

Późniejsza samodzielna adaptacja, nowe zastosowanie albo nowa capability może otrzymać osobne lineage, jeżeli evidence to potwierdza.

---

# 23. Protokół PRE / POST

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

## Po eksperymencie

Raport publikuje zarówno sukcesy, jak i FAIL, zero deltas, rejected hypotheses, retries, root interventions, regressions i remaining limitations.

---

# 24. Aktualna roadmapa

```text
1. ROBERT LIVE EXPERIENCE / REUSE                         = DONE
2. NO_MATCH -> CANDIDATE REPAIR                          = DONE
3. CANDIDATE -> NATURAL CHALLENGER                       = DONE
4. IDEMPOTENCY / REPLAY / RESTART HARDENING 600X         = DONE
5. MICRONETWORK CORE MIGRATION                            = DONE / DEVELOPMENT VALIDATED
6. M01-M08 REMAINING CORE MIGRATION                       = CURRENT
7. M09 FULL CORE INTEGRATION + HARDCORE                   = NEXT
8. FREEZE ORGANISM_CORE_V1                                = PLANNED
9. ORGANISM CORE -> DIRECTOR BODY                         = PLANNED
10. DIRECTOR BODY HARDCORE / AUTHORITY TESTS              = PLANNED
11. ORGANISM CORE -> AGENT BODY                           = PLANNED
12. ISKRA / MORAL VALUE LAYER                             = PLANNED
13. SIX-AGENT LONGITUDINAL EXPERIMENT                     = PLANNED
14. WORLDS / PROJECTS / OPERATIONAL EXPANSION             = LATER
15. RESEARCH RADAR / CODE FUSION / SELF-DEVELOPMENT       = LATER
```

---

# 25. Minimalny hardcore test korpusu

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

# 26. Research & Collaboration

SSI V5 jest projektem prowadzonym niezależnie przez **Pawła Jankiewicza**. Publiczna dokumentacja ma umożliwiać technicznym czytelnikom ocenę rzeczywistych decyzji architektonicznych, przebiegu eksperymentów oraz historii napraw.

Projekt jest otwarty na merytoryczny kontakt dotyczący m.in. technical/research review, persistent agents, cognitive architectures, lifelong learning, experience-driven competence systems, multi-agent experiments, value-conditioned agents, evidence/provenance, integracji capability, wspólnych eksperymentów i rozmów o wykorzystaniu lub licencjonowaniu wybranych autorskich mechanizmów.

Otwartość na rozmowę **nie oznacza**, że cały kod, prywatne datasety, sekrety, pełna implementacja mikrosieci albo wszystkie rozwiązania projektowe są automatycznie objęte licencją open-source.

---

# 27. Dlaczego dokumentowane są porażki

Dla tego projektu niepowodzenie testu jest informacją badawczą, a nie materiałem do usunięcia.

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

# 28. Bezpieczeństwo, prywatność i IP

Publiczny mirror nie publikuje API keys, tokenów, haseł, prywatnych danych, prywatnych adresów sieciowych, pełnych sekretów konfiguracji, materiałów objętych ograniczeniami licencyjnymi ani elementów implementacji świadomie zachowanych jako prywatne know-how.

Publiczny evidence trail ma być wystarczająco mocny do oceny twierdzeń, ale nie wymaga ujawnienia każdego szczegółu prywatnego runtime.

---

# 29. Otwarta agenda badawcza

Najbliższe pytania:

1. Czy pozostałe mechanizmy ROBERTA można wydzielić do neutralnego core bez regresji?
2. Czy cały `SSI ORGANISM CORE` zachowa persistence, lifecycle i idempotency po integracji M01-M09?
3. Czy ROBERT po migracji będzie korzystał z tego samego core bez utraty swojej osobistej historii?
4. Czy z tego samego core można następnie zbudować Director Body o większej strategicznej authority bez kopiowania osobistego state ROBERTA?
5. Czy Agent Body może korzystać z tych samych mechanizmów przy pełnej separacji identity i private Experience?
6. Czy sześć Agentów o identycznym substrate i różnych początkowych wartościach rozwinie mierzalnie odmienne trajektorie?

---

# 30. Jak oceniać SSI V5

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
