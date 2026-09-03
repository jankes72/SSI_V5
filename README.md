# SSI V5 — Research Front Door

**Experimental persistent competence architecture for adaptive AI systems.**  
SSI V5 investigates whether a long-running system can build, validate, preserve, reuse and revise competence across tasks using **Experience, micronetworks, Candidate -> Challenger -> Champion lifecycle, V10 stateful routing, LEGO composition and CONTINUUM persistence**.

## What this repository publishes — and what it does not

This repository is a **public, evidence-indexed research mirror** of SSI V5. It publishes the architecture's research history, contracts, measured effects, machine-readable summaries, failures, repairs, test boundaries and reviewer-facing documentation. It is **not** the source-code distribution of the private SSI V5 runtime, V10 implementation or full micronetwork engine.

SSI V5 is an independently developed system architecture authored by **Paweł Jankiewicz**. Language models and other third-party components used by the system remain replaceable capability providers and retain their respective authorship, licences and ownership; they are not presented as models created or owned by SSI. The private SSI implementation, its original integration logic and its non-public source code are reserved by the author. Publication of results or architectural descriptions in this repository does not by itself grant a licence to the unpublished implementation.

```text
PUBLIC HERE
= research history + architecture + evidence + measured outcomes + claim boundaries

NOT PUBLISHED HERE
= private SSI runtime + proprietary V10 implementation + full micronetwork engine
```

## Start here

- **Technical reviewers / grant evaluators:** [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
- **General project entry:** [START_HERE.md](START_HERE.md)
- **Current project truth:** [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
- **Grant / methodology FAQ:** [GRANT_REVIEWER_FAQ.md](GRANT_REVIEWER_FAQ.md)
- **V10 architecture:** [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- **Public machine evidence:** [evidence/README.md](evidence/README.md)
- **Independent reproduction / critique:** [CONTRIBUTING.md](CONTRIBUTING.md)

## Research focus

```text
EXPERIENCE
-> MICRONETWORK
-> CANDIDATE / CHALLENGER / CHAMPION
-> V10 STATEFUL ROUTING
-> LEGO COMPOSITION
-> CONTINUUM
-> OUTCOME
-> FAILURE / SUCCESS HISTORY
-> NEXT DECISION
```

The project is intentionally evidence-driven. Public claims are separated from hypotheses, failed or insufficient tests remain part of the record, and current claim boundaries are documented explicitly.

> **Important:** SSI V5 does not claim proven AGI or consciousness. Current results are scoped development evidence for specific mechanisms and test conditions.

---

# SSI V5 — Żywy Protokół Badawczy

## Persistent adaptive intelligence, micronetwork learning, stateful predictive competence routing, dynamic worlds and longitudinal agent research

**Status:** `PRE-T0 / ORGANISM-CORE-MIGRATION / SSI BODY INTEGRATION HARDENING`  
**Data aktualizacji:** `2026-09-03`  
**Najnowszy zamknięty milestone:** `TEST 5 / SSI BODY FINAL CONVERGENCE / DEVELOPMENT_VALIDATED`  
**Autor architektury SSI:** **Paweł Jankiewicz** (`PROGRAMMER_ROOT`)  
**Najwyższa authority:** **Paweł Jankiewicz / PROGRAMMER_ROOT**  
**Stan hipotezy AGI / świadomości:** `NIEUDOWODNIONA — BADANA EKSPERYMENTALNIE`  
**Model repozytorium:** `README-first / evidence-indexed research mirror`

> SSI V5 nie jest jednym LLM-em. Modele są wymiennymi źródłami capability; trwała tożsamość, pamięć, Experience, mikrosieci, lifecycle, authority i historia należą do systemu.

> Publiczny Git ma być biografią projektu: sukcesy, błędy, zmiany hipotez, naprawy, superseded results i wyniki mają pozostać widoczne.

---

# Aktualny zweryfikowany milestone — TEST 5

TEST 5 jest obecnie najnowszą publiczną podstawą claimu dotyczącego **testowanego lokalnego SSI BODY control/integration path**.

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROOT_CONTROL = 111/111 PASS
ROOT_RUNTIME_BRIDGE = 338/338 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
FINAL_CONVERGENCE_PASS = TRUE
```

Najważniejsza rzecz metodologiczna: wcześniejszy Stage 12 miał `27/27 PASS`, ale niezależny audyt wykazał, że nie był wystarczającą podstawą closure. Wykryto m.in. zbyt słabe real integration gates, słaby restart assertion, niepełne authentication checks na granicy IPC oraz możliwość zaakceptowania spoofed ROOT identity. Wynik Stage 12 nie został usunięty — pozostaje jako `SUPERSEDED`. Dopiero po naprawach Stage 13 stał się aktualną podstawą TEST 5.

Finalny TEST 5 rozdziela coverage na:

```text
UNIT / CONTROLLED
REAL INTEGRATION
REAL PROCESS E2E
REGRESSION
```

W badanym lokalnym zakresie obejmuje m.in. realne V10/micronetwork integration, lokalne CONTINUUM, provider registry/gateway, restart/recovery procesu, ROOT authentication boundary, receipt/audit E2E, CLI/IPC parity oraz HTTP -> IPC -> runtime flow.

Publiczne evidence:

- [evidence/TEST5_FINAL_CONVERGENCE_20260903.md](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [evidence/TEST5_FINAL_RESULT_20260903.json](evidence/TEST5_FINAL_RESULT_20260903.json)
- [evidence/TEST5_FINAL_MATRIX_20260903.json](evidence/TEST5_FINAL_MATRIX_20260903.json)
- [evidence/TEST5_STAGE12_SUPERSEDED_20260903.json](evidence/TEST5_STAGE12_SUPERSEDED_20260903.json)

**Current claim boundary:** TEST 5 wspiera claim, że testowany lokalny SSI BODY control/integration path przeszedł zdefiniowane acceptance, security-boundary, restart/recovery, receipt/audit, interface i regression checks po cyklu independent audit -> repair -> retest. Nie jest to dowód production readiness całego SSI, uniwersalnej niezawodności, jakości zewnętrznych providerów/modeli, AGI ani świadomości.

---

# Najważniejsza rzecz do zrozumienia o V10

**V10 nie jest przede wszystkim szybszym routerem.**

Kanoniczna rola V10 w SSI to:

> **Stateful Predictive Competence & Recovery Router** — warstwa, która wykorzystuje bieżący stan zadania, istniejące zwalidowane kompetencje, historię prób, wcześniejsze outcomes, failure signatures i confidence do wyboru następnej ścieżki działania.

```text
CURRENT TASK / WORLD STATE
+ VERIFIED MICRONETWORK COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
        |
        v
V10 STATEFUL PREDICTIVE ROUTING
        |
        +-> REUSE_TOP1
        +-> VERIFY_TOPK
        +-> ALTERNATIVE COMPETENCE / LEGO COMPOSITION
        +-> BLOCK BLIND RETRY
        +-> FULL_FLOW
```

Podstawowa zasada anti-loop:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE

=> DO NOT BLINDLY REPEAT
```

Jeżeli system już zna negatywny outcome danej ścieżki w porównywalnym stanie, V10 ma nie tylko „znaleźć coś podobnego”, ale również wykorzystać historię wykonania, aby zdecydować czy:

- ponownie użyć sprawdzonej części rozwiązania;
- zmienić parametry;
- zmienić kompozycję klocków LEGO;
- wybrać innego Championa / kompetencję;
- przejść przez `VERIFY_TOPK`;
- eskalować do canonical `FULL_FLOW`.

**Przyspieszenie jest ważnym skutkiem poprawnego reuse, ale nie pełnym znaczeniem V10.**

TEST 5 wzmacnia evidence, że w badanym lokalnym SSI BODY path V10/micronetwork integration jest testowana przez real integration gate zamiast placeholder acceptance. Nie oznacza to jeszcze uniwersalnego dowodu anti-loop/recovery.

Pełny opis:

- [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- [V10_PREDICTIVE_ROUTING_FAQ.md](V10_PREDICTIVE_ROUTING_FAQ.md)

---

# Dla grantodawców, sponsorów i recenzentów technicznych

Jeżeli oceniasz SSI V5 po raz pierwszy, zacznij tutaj:

- **[START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)** — aktualna ścieżka wejścia dla recenzenta;
- **[CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)** — aktualny indeks stanu projektu;
- **[TEST 5 — Final Convergence](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)** — najnowszy zamknięty milestone;
- **[TEST 5 final result](evidence/TEST5_FINAL_RESULT_20260903.json)** — machine-readable verdict;
- **[TEST 4 — ROOT Terminal](evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md)** — poprzedni zamknięty etap;
- **[Micronetwork Migration Final Lineage](evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md)** — wcześniejszy zamknięty etap;
- **[GRANT_REVIEWER_FAQ.md](GRANT_REVIEWER_FAQ.md)** — odpowiedzi na pytania techniczne i metodologiczne;
- **[evidence/README.md](evidence/README.md)** — pełny indeks publicznego machine evidence.

SSI V5 nie prosi recenzenta o przyjęcie głównych tez na wiarę. Projekt jest rozwijany jako łańcuch:

```text
CLAIM
-> IMPLEMENTATION
-> TEST
-> MACHINE EVIDENCE
-> AUDIT WHAT THE TEST REALLY PROVES
-> FAILURE / ROOT CAUSE / WEAK CONTRACT IF FOUND
-> PRESERVE HISTORY
-> REPAIR
-> RETEST
-> CURRENT CLAIM BOUNDARY
```

## Najkrótsza aktualna sekwencja evidence

```text
TEST 2 / fuller lifecycle + persistence
-> 600/600 PASS
-> 126.65 s

TEST 3 / V10 selective routing
-> 600/600 PASS in historical run
-> 57.61 s
-> 534 REUSE_TOP1 / 66 VERIFY_TOPK

TEST3 100x v2 / migration closure hardening
-> 60 000/60 000 accounted
-> 0 unresolved failures
-> 0 incorrect routing
-> restart 20/20

TEST 4 / ROOT Terminal
-> final regression 461/461
-> E2E 1000/1000
-> concurrency 1000 commands / 20 workers
-> restart 20/20
-> receipt accounting clean

TEST 5 / SSI BODY Final Convergence
-> Stage 12 27/27 SUPERSEDED after audit
-> Stage 13 audit retest PASS
-> 29/29 acceptance
-> 524/524 total regression
-> 0 open blockers
```

To pokazuje zmianę charakteru projektu: od testów mechanizmów mikrosieci i V10, przez kanoniczny ROOT control/terminal, do coraz szerszego lokalnego SSI BODY integration path.

---

# 0. Czym jest SSI V5

SSI V5 jest eksperymentalną architekturą persistent-agent, w której kompetencja nie ma istnieć wyłącznie wewnątrz jednego modelu albo jednego kontekstu rozmowy.

Główna hipoteza:

```text
MODEL OUTPUT != SYSTEM KNOWLEDGE

MODEL / TOOL / EXECUTION
+ EXPERIENCE
+ REAL OUTCOME
+ EVIDENCE
+ VALIDATION
+ HISTORY
-> PERSISTENT COMPETENCE
```

Architektura łączy m.in.:

- persistent state;
- Experience;
- mikrosieci kompetencji;
- lifecycle `Candidate -> Challenger -> Champion`;
- zbiorową inteligencję;
- V10 stateful predictive competence & recovery routing;
- CONTINUUM;
- LEGO development methodology;
- checkpoint/recovery;
- replay/persistence/regression testing;
- ROOT authority/control boundaries;
- dynamiczne światy i przyszłe Agent Bodies.

Nie twierdzimy, że każdy z tych mechanizmów jest nowy samodzielnie. Badana jest wartość **konkretnego połączenia tych mechanizmów w jeden persistent competence-development system**.

---

# 1. Linia rozwoju i obecna migracja

`SSI_V5_MASTER` oznacza początek obecnej linii SSI V5, ale nie początek całej historii eksperymentów autora.

```text
EARLIER DATA / PREDICTION EXPERIMENTS
-> SSI_V5_MASTER
-> ROZWÓJ SSI V5
-> ROBERT
-> STABILIZACJA / HARDENING ROBERTA
-> START MIGRACJI
-> DEKOMPOZYCJA SPRAWDZONYCH MECHANIZMÓW
-> PARITY / REGRESSION / REPLAY / PERSISTENCE
-> MICRONETWORK MIGRATION CLOSURE
-> ROOT TERMINAL / AUTHORITY CLOSURE
-> SSI BODY CONTROL / INTEGRATION CONVERGENCE
-> SSI ORGANISM CORE
-> ROBERT BODY / DIRECTOR BODY / AGENT BODY
```

Obecny etap jest **kontrolowaną rekonstrukcją i migracją istniejącej linii systemu**, nie budowaniem całego SSI od zera.

Metodologia migracji:

```text
WORKING SYSTEM
-> DECOMPOSITION
-> CANONICAL MODULE
-> CONTRACT TEST
-> EVIDENCE
-> INTEGRATION
-> REGRESSION
-> AUDIT
-> REPLAY / PERSISTENCE
-> NEXT MODULE
```

Celem jest uzyskanie audytowalnego systemu, w którym można wskazać, co działało, co zawiodło, który wcześniejszy PASS był za słaby, dlaczego dokonano zmiany i czy późniejszy test rzeczywiście naprawił problem.

---

# 2. Geneza: od predykcji do pamięci kompetencji

SSI wyrosło z wieloletnich eksperymentów autora z danymi sportowymi, predykcjami, własnymi modelami i obserwacją **dlaczego model działa albo nie działa**.

```text
FOOTBALL WORLD / REAL OUTCOMES
-> OWN MODELS / FEATURE ENGINEERING
-> 60% TRAINING / 40% UNSEEN OBSERVATION
-> TEACHER GENERATIONS
-> OBSERVATION MEMORY
-> KNOWLEDGE COLLECTORS
-> DIRECTOR
-> CONTINUUM / TOOLS
-> MICRONETWORKS
-> ROBERT
-> ORGANISM CORE
```

Kluczowa obserwacja była prosta: błąd modelu może być informacją, jeśli powtarza się w sposób systematyczny.

Ta zasada wraca w V10 w bardziej ogólnej postaci:

```text
FAILURE
!= ONLY ERROR TO RETRY

FAILURE
= INFORMATION FOR THE NEXT ROUTING DECISION
```

Szczegóły genezy:

- [evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md](evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md)
- [evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)

---

# 3. Mikrosieci — pamięć i rozwój kompetencji

Mikrosieć SSI nie jest definiowana jako zwykły wpis pamięci ani odpowiedź z cache.

Jej rolą jest reprezentowanie rozwijanej kompetencji:

```text
DOMAIN
-> CAPABILITY / PROBLEM TYPE
-> BRANCH
-> MICRONETWORK
-> GENERATIONS
-> CHAMPION
```

Canonical lifecycle:

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION / REJECT / KEEP TESTING
```

Champion nie jest niezmiennym rekordem. Może być:

- wzbogacony nowymi zweryfikowanymi przypadkami;
- rewalidowany;
- challenged;
- zastąpiony lepszym rozwiązaniem;
- cofnięty przy regresji.

```text
CHAMPION vN
+ NOVEL VERIFIED CASES
-> DEDUPLICATION
-> REGRESSION
-> REVALIDATION
-> CHAMPION vN+1
```

## Wielozadaniowość i wieloprzestrzeniowość

Mikrosieci nie są projektowane jako prywatny skill jednego agenta do jednego zadania.

Zweryfikowana kompetencja może być ponownie wykorzystywana w różnych zadaniach, domenach i przestrzeniach działania, jeśli jej kontrakt i evidence na to pozwalają.

```text
SHARED VERIFIED COMPETENCE
!=
SHARED PERSONAL HISTORY / IDENTITY
```

To umożliwia docelowo korzystanie z praktycznych Championów przez ROBERTA, Directora lub Agent Bodies bez automatycznego kopiowania prywatnej historii konkretnego Agenta.

## Dynamiczny wzrost

Przestrzeń mikrosieci nie ma być zamkniętą listą ręcznie wpisanych skilli.

Docelowy flow dla nowej klasy problemu:

```text
NEW EXPERIENCE
-> NO SUITABLE VERIFIED COMPETENCE
-> FULL FLOW
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION
-> NEW / EXTENDED MICRONETWORK
-> V10 ROUTE BINDING
```

Nowa mikrosieć nie powinna powstawać automatycznie po jednym sukcesie. Warunkiem jest normalny lifecycle i wymagane evidence.

---

# 4. V10 — stateful predictive competence & recovery routing

V10 nie zastępuje mikrosieci. Mikrosieć przechowuje rozwijaną kompetencję; V10 decyduje **czy, kiedy i jak jej użyć w aktualnym stanie działania**.

```text
MICRONETWORK
= PERSISTENT VALIDATED COMPETENCE

V10
= STATEFUL PREDICTIVE ACCESS
+ CONFIDENCE GATE
+ HISTORY / OUTCOME AWARENESS
+ FAILURE-AWARE ROUTING
+ ANTI-LOOP
+ RECOVERY DECISION
```

Podstawowy confidence flow:

```text
INPUT / STATE
-> V10
-> HIGH CONFIDENCE      -> REUSE_TOP1
-> MEDIUM CONFIDENCE    -> VERIFY_TOPK
-> LOW / UNKNOWN        -> FULL_FLOW
```

Ale V10 ma również szerszą funkcję:

```text
STATE
+ ROUTE X
-> FAILURE F
-> RECORD OUTCOME
-> EQUIVALENT STATE
-> V10 SEES X + F
-> DO NOT BLINDLY REPEAT X WITHOUT NEW EVIDENCE
-> CHANGE / VERIFY / ALTERNATIVE / FULL_FLOW
```

Architektura V10 obejmuje więc nie tylko szybki lookup, similarity, confidence gate, feedback i route compilation, ale również **history-aware recovery**.

Najważniejsze pytania badawcze nie brzmią tylko:

> Czy reuse jest szybkie?

ale również:

> Czy router potrafi rozpoznać sytuację, w której wcześniejszej kompetencji nie wolno bezpiecznie użyć?

oraz:

> Czy po znanym niepowodzeniu potrafi nie wrócić bezmyślnie do tej samej strategii, lecz wybrać sensowną alternatywę?

---

# 5. Dlaczego SSI nie jest po prostu cache'em

V10 może używać mechanizmów przypominających cache lub routing. Nie jest to ukrywane ani przedstawiane jako samodzielna innowacja.

Różnica dotyczy zarówno obiektu, do którego router prowadzi, jak i informacji wykorzystywanej do decyzji.

```text
CACHE
= zachowaj wcześniejszy wynik

SIMPLE ROUTER
= wybierz trasę na podstawie wejścia

SSI / V10
= zbieraj Experience
+ utrzymuj historię prób i outcomes
+ porównuj rozwiązania
+ gromadź evidence
+ waliduj
+ buduj / aktualizuj Championa
+ umożliwiaj challengerom konkurencję
+ rewaliduj / rollback
+ routuj do zweryfikowanej kompetencji
+ nie powtarzaj ślepo znanej nieskutecznej ścieżki
+ wybierz recovery / alternatywę / full flow
```

Najważniejszym obiektem nie jest więc zapamiętana odpowiedź, lecz **ewoluujący Champion wraz z historią evidence, konkurującymi rozwiązaniami i historią ich użycia**.

---

# 6. Collective Intelligence

Zbiorowa inteligencja SSI nie oznacza tylko "zapytaj kilka modeli i zagłosuj".

Różne modele, narzędzia, wykonania i późniejsze realne outcomes mogą wnosić evidence do tej samej kompetencji.

System wykorzystuje stopniowanie pracy dla trudniejszych przypadków:

```text
BRAINSTORM
-> TORNADO
-> TYPHOON
```

Najbardziej wartościowe wyniki mogą później przejść lifecycle i zasilić trwałą kompetencję systemu.

Docelowa zasada:

```text
DIRECTOR -> nowe validated competence
ROBERT   -> nowe validated competence
AGENTS   -> niezależnie odkryte skille

BEST VERIFIED PRACTICAL COMPETENCE
-> SHARED CHAMPION POOL
-> STRONGER SSI
```

---

# 7. CONTINUUM

CONTINUUM jest persistent mission-execution layer.

```text
MISSION
-> EXECUTION
-> CHECKPOINT
-> EVIDENCE
-> PAUSE / FAILURE / RESTART
-> RECONCILE
-> CONTINUE
```

CONTINUUM i mikrosieci rozwiązują różne problemy:

- CONTINUUM przechowuje ciągłość pracy;
- mikrosieci przechowują i rozwijają kompetencję;
- V10 wykorzystuje bieżący stan i historię outcomes do wyboru następnej ścieżki.

TEST 5 potwierdza lokalną integrację CONTINUUM w badanym SSI BODY path; niedostępna funkcjonalność remote pozostaje jawnie poza zakresem zamiast być symulowana jako dostępna.

---

# 8. LEGO development methodology i V10

LEGO to metodologia rozbijania dużych zmian na małe kontraktowe jednostki.

```text
LARGE GOAL
-> DECOMPOSITION
-> SMALL BLOCK
-> CLEAR INPUT / OUTPUT
-> EXECUTOR
-> TEST
-> EVIDENCE
-> CHECKPOINT
-> INTEGRATION
-> REGRESSION
-> NEXT BLOCK
```

V10 nadaje temu dodatkowe znaczenie wykonawcze: historia tego, które klocki i kompozycje działały albo zawodziły, może wpływać na kolejną decyzję.

```text
GOAL
-> LEGO BLOCK A + B + C
-> TEST
-> FAILURE F
-> V10 CONSULTS HISTORY
-> KEEP VERIFIED GOOD BLOCKS
-> REPLACE / RECONFIGURE FAILED PATH
-> RETEST
```

Celem nie jest wykonywanie całej budowy od początku ani powtarzanie dokładnie tej samej nieskutecznej konfiguracji.

---

# 9. ROBERT i Director

```text
PROGRAMMER_ROOT
      >
   DIRECTOR
      >
    ROBERT
      >
HERMES / CONTINUUM / WORKERS / TOOLS
```

Director jest nadrzędnym obserwatorem, decydentem i meta-learnerem.

ROBERT jest wykonawczym ciałem systemu posiadającym narzędzia, runtime, Eyes/Hands/Browser/Tools i mechanizmy persistent execution.

Director i ROBERT mogą korzystać z tych samych przenośnych Championów, ale nie oznacza to automatycznie wspólnej prywatnej pamięci ani tożsamości.

TEST 5 wzmacnia publiczne evidence dla ROOT/control boundaries w badanym przepływie: missing/invalid auth ma zostać odrzucone przed side effects, a spoofed ROOT identity nie może być zaakceptowane jako valid ROOT.

---

# 10. ROBERT: BUILD -> USE -> DISCOVER LIMITATION -> MODIFY -> RETEST

Jednym z ważnych eksperymentów jest sytuacja, w której ROBERT nie tylko tworzy artefakt, ale później sam go używa.

```text
ROBERT BUILDS TOOL / GAME
-> TEST / FREEZE
-> EYES OBSERVE
-> HANDS INTERACT
-> REAL FEEDBACK
-> LIMITATION DISCOVERED
-> DIAGNOSIS
-> V10 CONSULTS STATE + HISTORY
-> REUSE VALID SKILL OR SELECT NEW PATH
-> MODIFY ARTIFACT OR STRATEGY
-> RETEST
-> NEW EXPERIENCE
-> MICRONETWORK UPDATE
```

## Dlaczego Tetris jest ważnym przykładem

Tetris pozwala oddzielić dwie klasy problemów.

### ROBERT buduje / naprawia grę

```text
BUILD
-> TEST
-> FAILURE
-> FAILURE SIGNATURE
-> V10
-> DO NOT REPEAT BAD LEGO COMPOSITION BLINDLY
-> CHANGE ROUTE / BLOCK / STRATEGY
-> RETEST
```

### ROBERT później sam gra

```text
BOARD STATE
-> PERCEPTION
-> V10 / COMPETENCE SELECTION
-> ACTION
-> OUTCOME
-> EXPERIENCE
-> NEXT STATE
```

Jeżeli określona strategia w porównywalnym stanie wielokrotnie prowadzi do tego samego złego rezultatu, historia outcome ma wpływać na następną decyzję.

Wartością nie jest konkretny skill grania w jedną grę. Wartością mogą być kompetencje bardziej ogólne:

```text
PERCEIVE INTERFACE
CONTROL TOOL
MEASURE FEEDBACK
DISTINGUISH TOOL FAILURE FROM STRATEGY FAILURE
REMEMBER FAILED ROUTE
SELECT RECOVERY
MODIFY OWN ARTIFACT
RETEST
ROLL BACK REGRESSION
REUSE VERIFIED SOLUTION
```

---

# 11. Agent Bodies, dynamiczne światy i Iskra / Moral AI

Docelowy eksperyment zakłada wiele technologicznie podobnych Agent Bodies z możliwie wspólnym substrate, ale odmiennym initial value prior oraz późniejszą indywidualną historią Experience.

```text
SAME ORGANISM CORE
SAME BASE CAPABILITY CLASS
SAME INITIAL ACCESS RULES

BUT

DIFFERENT EXPERIENCE
DIFFERENT RELATIONSHIPS
DIFFERENT VALUE TRAJECTORY
```

Iskra / Moral AI ma działać jako jedna z warstw wpływających na decyzję Agenta w świecie, nie jako deklaracja świadomości.

```text
WORLD STATE
-> MEMORY
-> EXPERIENCE
-> MICRONETWORKS
-> RELATIONSHIPS
-> POSSIBLE ACTIONS
-> ISKRA EVALUATION
-> DECISION
-> CONSEQUENCE
-> NEW EXPERIENCE
```

`ISKRA != ŚWIADOMOŚĆ`.

---

# 12. Dynamiczne światy i pamięć biograficzna

Światy nie są projektowane jako jedna zamrożona plansza.

Agent może wracać do świata z wcześniejszą pamięcią, ale sam świat może być już inny.

```text
PERSISTENT MEMORY OF WORLD
!=
FROZEN WORLD STATE
```

Docelowo możliwe jest badanie transferu między kolejnymi środowiskami:

```text
WORLD 1
-> WORLD 2
-> WORLD 3
-> RETURN TO WORLD 1
```

Agent zachowuje historię sukcesów, porażek, relacji, zdobytych kompetencji i wcześniejszych wyborów.

---

# 13. Director jako meta-obserwator genezy strategii

Director ma analizować nie tylko wynik końcowy, ale genezę kompetencji:

- jakie źródła zostały wybrane;
- które zostały odrzucone;
- jakie Experience były kluczowe;
- jakie mikrosieci powstały;
- jakie relacje zmieniły decyzję;
- kiedy pojawiła się nowa strategia;
- jakie trasy/strategie zawiodły;
- czy skill jest przenośny;
- czy powinien zostać Challengerem/Championem.

Publiczny Git ma być również potencjalnym źródłem przyszłej **pamięci genealogicznej systemu**:

```text
EARLIER STATE
-> FAILURE / LIMITATION / WEAK TEST CONTRACT
-> DIAGNOSIS
-> MODIFICATION
-> TEST
-> EVIDENCE
-> CURRENT CAPABILITY
```

TEST 5 jest dobrym przykładem takiego lineage: earlier PASS -> independent audit contradiction -> Stage 12 superseded -> repair -> Stage 13 retest -> current claim.

---

# 14. Organism Core

Celem obecnej migracji jest wydzielenie sprawdzonych mechanizmów ROBERTA do neutralnego substrate:

```text
ROBERT HARDENED MECHANISMS
-> SSI ORGANISM CORE
-> ROBERT BODY
-> DIRECTOR BODY
-> AGENT BODY
```

Core ma obejmować m.in.:

- Identity;
- Memory;
- Experience;
- Capability Registry;
- Resolver;
- Micronetwork Engine;
- lifecycle;
- checkpoint/recovery;
- evidence/lineage;
- authority;
- hooks do CONTINUUM/research/tools.

---

# 15. Publiczne evidence i zasada zachowywania FAIL / SUPERSEDED

Repo nie ma prezentować wyłącznie sukcesów.

```text
EARLIER FAIL OR WEAK PASS
-> ROOT CAUSE / AUDIT FINDING
-> PRESERVE ORIGINAL RESULT
-> REPAIR
-> LATER STRONGER RETEST
!=
EARLIER PROBLEM NEVER HAPPENED
```

Wcześniejszy failure albo niewystarczający PASS powinien być zachowany nie tylko jako historia dla człowieka. W architekturze V10 failure ma również potencjalnie stać się informacją wpływającą na przyszły routing i recovery.

`SUPERSEDED` oznacza: wynik historyczny pozostaje w repo, ale nie jest już aktualną podstawą danego claimu.

---

# 16. Test 2 — pełniejszy flow i persistence hardening

**Status:** `DEVELOPMENT_VALIDATED — scoped idempotency/replay/persistence hardening`  
**Data:** `2026-08-31`

```text
600 cases / 40 rounds / 15 cases per round

start candidates:       125
end candidates:         125
start challengers:       31
end challengers:         31
start experiences:     5195
end experiences:       5195

duplication_failures:     0
none_get_errors:          0
half_promoted_objects:    0

RESULT: PASS
DURATION: 126.65 s
```

Dodatkowo persistence replay zakończył się `50/50 PASS`.

Test 2 był istotny nie dlatego, że był szybki, ale dlatego, że miał pokazać **szerszy/full-flow stan lifecycle, replay i persistence** przed wprowadzeniem szybkiego routingu.

Pełne evidence:

- [evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md)

---

# 17. Test 3 — V10 Hybrid Router

**Data:** `2026-09-01`

```text
cases:               600
rounds:               40
cases per round:      15
duration:          57.61 s

REUSE_TOP1:          534
VERIFY_TOPK:          66
fallback_count:        0
known correctness: 100/100
```

W tym konkretnym historycznym eksperymencie Test 3 był około `2.20x` szybszy od Testu 2 i około `54.5%` krótszy czasowo.

**To nie jest najważniejsza definicja V10.** Test 3 pokazuje część mechanizmu — selektywny routing i reuse. Pełna hipoteza obejmuje również state/history awareness, false-reuse control, failure-aware routing, anti-loop i recovery.

Pełne evidence:

- [evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md](evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md)
- [evidence/router_v10_test3/H_TEST3_RESULTS.json](evidence/router_v10_test3/H_TEST3_RESULTS.json)
- [evidence/router_v10_test3/A_BASELINE.json](evidence/router_v10_test3/A_BASELINE.json)

Późniejszy TEST3 100x v2 / migration closure jest mocniejszą podstawą dla aktualnych claimów o canonical micronetwork/V10 state niż ten historyczny single run.

---

# 18. TEST 4 — ROOT Terminal / Authority / Recovery

**Status:** `DEVELOPMENT_VALIDATED / ROOT_TERMINAL_MIGRATION_CLOSED`  
**Data:** `2026-09-02`

```text
FINAL REGRESSION = 461/461 PASS
AUTHORITY BOUNDARY = PASS
FULL PIPELINE E2E = 1000/1000 PASS
CONCURRENCY = 1000 commands / 20 workers PASS
REAL PROCESS RESTART = 20/20 PASS
PHYSICAL_RECEIPTS = 2000 for 1000 commands
DUPLICATES = 0
ORPHANS = 0
MISSING = 0
OPEN_BLOCKERS = []
```

TEST 4 zamknął kanoniczną migrację ROOT terminal/control path po osobnym evidence audit i hardeningu pierwszego closure candidate.

Pełne evidence:

- [evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md](evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md)
- [evidence/TEST4_ROOT_TERMINAL_FINAL_CLOSURE_20260902.json](evidence/TEST4_ROOT_TERMINAL_FINAL_CLOSURE_20260902.json)

---

# 19. TEST 5 — SSI BODY Final Convergence / Independent Audit Retest

**Status:** `DEVELOPMENT_VALIDATED / PASS`  
**Data:** `2026-09-03`

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5 = 29/29 PASS
TOTAL_REGRESSION = 524/524 PASS
OPEN_BLOCKERS = 0
FINAL_CONVERGENCE_PASS = TRUE
```

TEST 5 nie zastępuje historii TEST 4 ani migration closure. Łączy i weryfikuje szerszy lokalny control/integration path SSI BODY po audycie, który odrzucił wcześniejszy Stage 12 jako niewystarczająco silny.

Pełne publiczne evidence:

- [evidence/TEST5_FINAL_CONVERGENCE_20260903.md](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [evidence/TEST5_FINAL_RESULT_20260903.json](evidence/TEST5_FINAL_RESULT_20260903.json)
- [evidence/TEST5_FINAL_MATRIX_20260903.json](evidence/TEST5_FINAL_MATRIX_20260903.json)
- [evidence/TEST5_STAGE12_SUPERSEDED_20260903.json](evidence/TEST5_STAGE12_SUPERSEDED_20260903.json)

---

# 20. Publiczny demonstrator dla recenzentów

Planowany jest mały, reprodukowalny demonstrator, który nie wymaga dostępu do prywatnego runtime ani sekretów.

Przykład programistyczny może pokazać:

```text
CLEAN EXAMPLE
-> CONTINUUM / LEGO
-> FIRST SOLUTION
-> EXPERIENCE
-> LIFECYCLE
-> MICRONETWORK
-> V10 BINDING
-> CONTROLLED FAILURE
-> V10 RECOVERY / ROUTE CHANGE
```

Tetris jest dobrym kandydatem, ponieważ może pokazać zarówno budowę/naprawę, jak i późniejsze autonomiczne używanie artefaktu przez ROBERTA.

---

# 21. Co może obalić lub osłabić hipotezę SSI

Projekt traktuje falsyfikowalność jako ważną część metodologii.

Hipotezę osłabiłoby m.in.:

- V10 przyspiesza, ale powoduje niedopuszczalny false reuse;
- V10 nadal powtarza tę samą znaną nieskuteczną strategię mimo zachowanego failure history;
- recovery wybiera alternatywy losowo lub bez poprawy outcome;
- kompetencja działa tylko na niemal identycznych przypadkach;
- Champion accumulation prowadzi do degradacji;
- dynamiczny wzrost mikrosieci generuje niekontrolowaną redundancję;
- pełny flow jest uruchamiany tak często, że routing traci sens;
- persistent competence staje się nieaktualna i nie daje się poprawić;
- przewaga benchmarkowa znika przy niezależnej reprodukcji;
- shared competence powoduje konflikty, których system nie potrafi rozwiązać;
- późniejsze audyty pokażą, że current acceptance gates nadal nie mierzą deklarowanej granicy.

---

# 22. Granice twierdzeń

SSI V5 **nie deklaruje**, że:

- jest udowodnionym AGI;
- posiada świadomość;
- niespodziewane zachowanie dowodzi świadomości;
- wynik 600×, 60 000× lub 524/524 dowodzi general intelligence;
- V10 zawsze będzie szybszy od innych architektur;
- pełny anti-loop został już uniwersalnie udowodniony;
- każdy Agent-discovered skill nadaje się do transferu;
- każda mikrosieć reprezentuje prawdę;
- cały system jest production-ready;
- wynik ekonomiczny jest gwarantowany.

Używane statusy obejmują:

```text
VERIFIED_MACHINE_EVIDENCE
ROOT_ATTESTED
HISTORICAL_EVIDENCE
SUPERSEDED
DEVELOPMENT_VALIDATED
IMPLEMENTED_NOT_YET_REPLICATED
PLANNED
HYPOTHESIS
UNKNOWN
```

---

# 23. Oryginalność i state of the art

SSI jest autorską architekturą rozwijaną niezależnie przez Pawła Jankiewicza.

Jednocześnie repo **nie twierdzi bez przeglądu literatury, że żaden podobny mechanizm nie istnieje**.

Obszary wymagające formalnego porównania obejmują m.in.:

- hierarchical agent memory;
- episodic / semantic / procedural memory;
- RAG;
- semantic cache;
- semantic/model routing;
- knowledge graphs;
- long-term agent memory;
- dynamic routing;
- planning/recovery architectures;
- self-improving agents;
- agent foundations;
- multi-agent competence aggregation.

Najsilniejsza obecnie hipoteza oryginalności dotyczy dokładnej kombinacji:

```text
MULTI-TASK / MULTI-SPACE MICRONETWORKS
+ CANDIDATE / CHALLENGER / CHAMPION LIFECYCLE
+ COLLECTIVE COMPETENCE EVOLUTION
+ V10 STATEFUL PREDICTIVE COMPETENCE ROUTING
+ HISTORY / OUTCOME-AWARE ANTI-LOOP
+ RECOVERY / ALTERNATIVE ROUTE SELECTION
+ CANONICAL FULL-FLOW FALLBACK
+ DYNAMIC LEGO COMPOSITION
+ DYNAMIC NEW-COMPETENCE FORMATION
+ PERSISTENT DEVELOPMENTAL LINEAGE
+ ROOT AUTHORITY / AUDITABLE CONTROL BOUNDARIES
```

Formalny state-of-the-art review pozostaje osobnym zadaniem badawczym.

---

# 24. Uczciwa atrybucja

Paweł Jankiewicz jest autorem nadrzędnej architektury SSI V5 i najwyższą authority projektu.

```text
SSI MICRONETWORK / CHAMPION ARCHITECTURE
= PAWEŁ JANKIEWICZ

SOURCE IDEA / WORLD PARADIGM OF MORAL AI
= EARLIER PROJECT BY AUTHOR'S BROTHER (ROOT_ATTESTED)

SSI ADAPTATION OF MORAL AI / ISKRA
= PAWEŁ JANKIEWICZ
```

---

# 25. Publiczna chronologia

```text
2026-07-19  root Git commit: MSDI AI v0.01
2026-07-27  publiczne repo msdi-ai
2026-07-28  SSI Core / Data World / Model Laboratory
2026-08-01  pierwsze jawne SSI V5
2026-08-14  CONTINUUM repo
2026-08-16  SSI_V5_MASTER — początek obecnej linii SSI V5
2026-08-25  SSI_V5 public research mirror
2026-08-29  ROBERT stabilization/hardening -> start Organism Core migration
2026-08-31  final scoped 600× idempotency/replay/persistence PASS
2026-09-01  V10 Hybrid Router Test 3 — 600 cases / 57.61 s / PASS
2026-09-01  V10 stateful predictive competence & recovery definition formalized in public reviewer docs
2026-09-02  micronetwork migration closure — TEST3 100× v2 / 60 000 accounted / 0 unresolved failures
2026-09-02  TEST 4 ROOT Terminal final closure — authority / E2E / concurrency / restart / receipt accounting
2026-09-03  TEST 5 Stage 12 27/27 marked SUPERSEDED after independent audit
2026-09-03  TEST 5 Stage 13 audit retest — 29/29 acceptance / 524/524 total / 0 blockers
```

---

# 26. Długoterminowe pytania badawcze

1. Czy persistent competence może być skutecznie oddzielona od konkretnego LLM?
2. Czy V10 potrafi bezpiecznie odróżnić reuse od sytuacji wymagającej pełnego flow?
3. Czy V10 potrafi wykorzystać historię failure/outcome do uniknięcia ślepego powtarzania nieskutecznej strategii?
4. Czy recovery wybiera lepszą alternatywę niż blind retry?
5. Czy system potrafi dynamicznie przeorganizować kompozycję LEGO na podstawie outcome?
6. Czy system potrafi tworzyć nowe kompetencje bez ręcznie zdefiniowanej kompletnej listy skilli?
7. Czy Champion może być wzbogacany przez wiele niezależnych źródeł evidence bez degradacji jakości?
8. Czy przenośna kompetencja może być współdzielona między różnymi bodies bez kopiowania ich prywatnej tożsamości?
9. Czy Agent Bodies z tym samym substrate, ale inną historią i value prior rozwiną różne trwałe strategie?
10. Czy Director potrafi odtworzyć genezę sukcesu lub porażki zamiast tylko obserwować finalny outcome?
11. Czy system potrafi uczyć się własnej metodologii budowania i naprawiania narzędzi?
12. Czy kilka równoległych CONTINUUM zachowa spójność checkpointów, evidence i state?
13. Czy niezależny recenzent odtworzy przewagę i recovery V10 na publicznym demonstratorze?
14. Czy coraz szersze integracyjne testy SSI BODY zachowają te same authority, persistence i audit invariants po dołączeniu kolejnych warstw?

---

# 27. Pętla ekonomiczna — cel długoterminowy

SSI ma w przyszłości badać również realne decyzje ekonomiczne jako źródło mierzalnych outcomes.

```text
OPPORTUNITY
-> STRATEGY
-> EXECUTION
-> REAL OUTCOME
-> PROFIT / LOSS / FAILURE
-> EXPERIENCE
-> V10 / MICRONETWORK UPDATE
-> NEXT DECISION
```

To jest **planowany kierunek eksperymentalny**, nie gwarancja zysku ani aktualne twierdzenie o autonomicznej rentowności systemu.

Docelowa polityka podziału dodatniego wyniku ekonomicznego ma rozdzielać dwa niezależne zasoby SSI:

```text
50% -> AUTHOR / OWNER
40% -> SSI INVESTMENT CAPITAL
10% -> SSI INFRASTRUCTURE DEVELOPMENT
```

Kapitał inwestycyjny ma umożliwiać Dyrektorowi prowadzenie kontrolowanych eksperymentów w światach ekonomicznych. Oddzielny budżet rozwojowy SSI ma finansować sprzęt, serwery, modele, API, narzędzia i inne uzasadnione rozszerzenia infrastruktury. Badaniu ma podlegać nie tylko końcowy wynik finansowy, lecz również provenance decyzji, ryzyko, wykorzystane kompetencje, rzeczywisty outcome oraz wpływ reinwestycji na późniejsze możliwości systemu.

Grant lub inne finansowanie zewnętrzne może przyspieszyć skalowanie infrastruktury i eksperymenty wymagające większej mocy obliczeniowej, ale nie jest podstawowym celem ani warunkiem kontynuowania projektu. Bez finansowania zewnętrznego rozwój ma postępować etapami na dostępnej infrastrukturze i — jeżeli eksperymenty ekonomiczne zaczną przynosić dodatnie wyniki — również z wydzielonego budżetu rozwojowego SSI. Nie jest to deklaracja gwarantowanej rentowności.

---

# 28. Główne dokumenty publiczne

## Dla recenzenta / grantu

- [START_HERE_FOR_REVIEWERS.md](START_HERE_FOR_REVIEWERS.md)
- [START_HERE.md](START_HERE.md)
- [CURRENT_TRUTH_INDEX.md](CURRENT_TRUTH_INDEX.md)
- [GRANT_REVIEWER_FAQ.md](GRANT_REVIEWER_FAQ.md)
- [V10_PREDICTIVE_ROUTING.md](V10_PREDICTIVE_ROUTING.md)
- [V10_PREDICTIVE_ROUTING_FAQ.md](V10_PREDICTIVE_ROUTING_FAQ.md)
- [evidence/README.md](evidence/README.md)

## Latest validated evidence

- [evidence/TEST5_FINAL_CONVERGENCE_20260903.md](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [evidence/TEST5_FINAL_RESULT_20260903.json](evidence/TEST5_FINAL_RESULT_20260903.json)
- [evidence/TEST5_FINAL_MATRIX_20260903.json](evidence/TEST5_FINAL_MATRIX_20260903.json)
- [evidence/TEST5_STAGE12_SUPERSEDED_20260903.json](evidence/TEST5_STAGE12_SUPERSEDED_20260903.json)
- [evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md](evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md)
- [evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md](evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md)

## Geneza i architektura

- [evidence/PROJECT_GENESIS_AND_EVOLUTION.md](evidence/PROJECT_GENESIS_AND_EVOLUTION.md)
- [evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md](evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md)
- [evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)
- [evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md](evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md)
- [evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md](evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md)
- [evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)

---

# 29. Najkrótsza definicja projektu

**SSI V5 bada, czy trwały system może gromadzić Experience, rozwijać wielozadaniowe i wieloprzestrzeniowe mikrosieci kompetencji, walidować je poprzez lifecycle Candidate -> Challenger -> Champion, agregować kompetencję pochodzącą z wielu źródeł, a następnie używać V10 do stanowego i predykcyjnego wyboru następnej strategii — uwzględniając confidence, historię prób, wcześniejsze outcomes i failure signatures — tak aby ponownie używać sprawdzonych kompetencji, weryfikować sytuacje niepewne, unikać ślepego powtarzania znanych nieskutecznych ścieżek oraz eskalować do pełnego flow, kiedy wcześniejsza wiedza jest niewystarczająca.**

```text
NEW PROBLEM
-> FULL FLOW
-> EXPERIENCE
-> VERIFIED COMPETENCE
-> CHAMPION
-> MICRONETWORK
-> V10
-> REUSE / VERIFY / ALTERNATIVE / FULL_FLOW
-> OUTCOME
-> FAILURE OR SUCCESS HISTORY
-> NEXT ROUTING DECISION
-> FURTHER EVOLUTION
```

Historia Git ma pokazywać, czy ten mechanizm naprawdę działa — również wtedy, gdy odpowiedź brzmi: **nie**, albo gdy wcześniejszy zielony test okazuje się zbyt słaby i musi zostać oznaczony `SUPERSEDED`.

---

# 30. Reviewer invitation

Niezależna krytyka jest mile widziana.

Najbardziej wartościowe są:

- reprodukcje;
- wykryte błędy metodologiczne;
- przypadki false reuse;
- przypadki blind retry / failure loop;
- testy recovery i alternative-route selection;
- adversarial / distribution-shift tests;
- próby obejścia authority/authentication boundaries;
- wskazanie zbyt słabych acceptance gates;
- porównania z istniejącym state of the art;
- wskazanie, gdzie hipoteza SSI jest za szeroka względem evidence.

Projekt nie potrzebuje niezasłużonego endorsementu. Potrzebuje **sprawdzalnych testów, krytyki, audytów i coraz mocniejszego evidence**.