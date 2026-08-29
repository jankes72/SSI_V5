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

Aktualny indeks prawdy projektu: [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md).

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

**To jest obecna architektura docelowa, a nie kolejność historycznego powstania projektu.**

Historycznie SSI zaczęło się znacznie wcześniej od świata piłkarskiego, modeli predykcyjnych, realnych wyników oraz prób zrozumienia, dlaczego modele działają w jednych sytuacjach, a zawodzą w innych. Z tego etapu wyrósł system T17 — 17 wyspecjalizowanych Teacherów z pamięcią obserwacji, Laboratoriami Wiedzy i konsolidacją wiedzy. Dopiero rosnąca skala danych, modeli, wyników i zależności doprowadziła do powstania **Directora** jako nadrzędnej warstwy obserwacji, analizy i decyzji.

**Director powstał przed ROBERTEM.** ROBERT został utworzony później jako kontrolowana migracja i poligon do testowania mechanizmów, które w rozbudowanym Directorze były zbyt mocno sprzężone i trudne do bezpiecznego rozwijania. Na ROBERCIE przeprowadzono hardening Experience, micronetwork lifecycle, replay, restart, persistence i idempotency. Z tych sprawdzonych mechanizmów wydzielany jest obecnie neutralny `SSI ORGANISM CORE`, który ma następnie zasilić przebudowany Director Body oraz przyszły Agent Body.

Pełna geneza i rozdzielenie historii projektu od obecnej kolejności migracji są opisane w:

[`evidence/PROJECT_GENESIS_AND_EVOLUTION.md`](evidence/PROJECT_GENESIS_AND_EVOLUTION.md)

Historyczny system Football World / T17 jest opisany osobno w:

[`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)

Samorozwój Directora oraz wykonawcza rola ROBERTA/Eyes/Hands są opisane w:

[`evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md`](evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md)

---

# 2. Jak projekt rzeczywiście powstał

Początkowym problemem nie była budowa „AGI”, ROBERTA ani populacji Agentów. Punktem wyjścia były **piłka nożna, predykcje, dane i realne outcomes**.

Pierwotny rytm był praktyczny:

```text
DANE PIŁKARSKIE / RYNKOWE
-> MODEL
-> PREDYKCJA
-> REALNY WYNIK
-> OCENA
-> KOLEJNA PRÓBA
```

Same wyniki predykcyjne nie były jednak wystarczająco stabilne ani satysfakcjonujące. Projekt zaczął więc badać nie tylko to, **co model przewiduje**, ale również **jak model zachowuje się w czasie, kiedy jest wiarygodny, gdzie systematycznie się myli i czy jego confidence rzeczywiście coś znaczy**.

Z tego wyrósł T17:

```text
17 TEACHERÓW
-> 60% TRAINING
-> 40% UNSEEN OBSERVATION
-> PREDICTIONS
-> REAL OUTCOMES
-> OBSERVATION MEMORY
-> KNOWLEDGE LABORATORIES
-> KNOWLEDGE COLLECTORS
-> CONSOLIDATED KNOWLEDGE
```

T17 składał się z dwóch rodzin modeli: **12 + 5**. Każdy Teacher miał nie tylko model predykcyjny, ale także własne artefakty obserwacji, pamięci i analizy. Ta warstwa jest historycznie ważna, ponieważ wprowadziła do SSI zasadę:

```text
TEACHER -> OBSERVATION -> MEMORY -> ANALYSIS -> KNOWLEDGE
```

zamiast prostszego:

```text
MODEL -> ACCURACY -> KONIEC
```

---

# 3. Dlaczego powstał Director

Gdy system zaczął obejmować wiele modeli, Teacherów, pamięci, laboratoriów, wyników i źródeł danych, problem przestał być problemem pojedynczego modelu.

Potrzebna była warstwa, która mogła:

- obserwować wiele źródeł jednocześnie;
- analizować pełne lineage eksperymentów;
- zachowywać długą historię;
- łączyć wiedzę z wielu modeli zamiast ślepo wybierać pojedynczą predykcję;
- oceniać jakość strategii w długim czasie;
- kontrolować zasoby i narzędzia;
- podejmować decyzje ponad poziomem pojedynczych wykonawców;
- uczyć się z niezależnych real-world outcomes.

Tak powstał **Director**.

Director nie był kolejnym chatbotem. Miał stać się nadrzędnym obserwatorem i decydentem całego rosnącego SSI.

---

# 4. Dlaczego Hermes przestał wystarczać

Hermes pozostaje użyteczną warstwą wykonawczą/delegacyjną, ale rosnący system wymagał czegoś znacznie szerszego niż:

```text
TASK -> TOOL -> RESULT
```

Docelowy problem zaczął wyglądać raczej tak:

```text
WIELE ŚWIATÓW
+ WIELE MODELI
+ WIELE EKSPERYMENTÓW
+ PERSISTENT MEMORY
+ REAL OUTCOMES
+ LINEAGE
+ LOCAL COMPETENCE
+ AUTHORITY
+ DŁUGOTERMINOWA ADAPTACJA
```

W miarę dokładania kolejnych warstw Director stawał się coraz trudniejszy do bezpiecznego rozwijania. Nie wszystko było stabilnie podłączone, a diagnoza pojedynczej awarii była utrudniona przez liczbę zależności.

Problemem nie był brak funkcji. Problemem była **zbyt duża liczba funkcji i połączeń rozwijanych naraz**.

---

# 5. Dlaczego powstał ROBERT

ROBERT powstał **po Directorze** jako kontrolowana migracja i poligon wykonawczy.

Celem było wydzielenie mechanizmów z rozbudowanego systemu i stworzenie środowiska, w którym można było brutalnie testować:

- persistent Experience;
- reuse;
- NO_MATCH growth;
- micronetwork lifecycle;
- candidate/challenger;
- replay;
- restart;
- idempotency;
- recovery;
- evidence;
- integrację narzędzi i capability.

Historyczna sekwencja jest więc bliższa:

```text
FOOTBALL WORLD / REAL PREDICTIONS
        ↓
T17 / TEACHER KNOWLEDGE
        ↓
DIRECTOR
        ↓
ROSNĄCA ZŁOŻONOŚĆ INTEGRACJI
        ↓
ROBERT
kontrolowana migracja / poligon
        ↓
HARDENING
        ↓
SSI ORGANISM CORE
```

ROBERT nie zastępuje Directora i nie jest jego historycznym poprzednikiem. Jest późniejszą instancją, na której mechanizmy można było uprościć, rozdzielić i sprawdzić przed ponownym użyciem w przebudowanym Directorze.

---

# 6. Dlaczego powstaje SSI ORGANISM CORE

Testy ROBERTA pokazały, że wiele mechanizmów nie powinno należeć wyłącznie do jednej roli.

Neutralny korpus ma obejmować m.in.:

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

Obecna techniczna kolejność migracji:

```text
ROBERT
-> sprawdzone mechanizmy
-> SSI ORGANISM CORE
-> ROBERT BODY
-> przebudowany DIRECTOR BODY
-> AGENT BODY
```

To nie jest kolejność historyczna. Jest to **kolejność obecnego refactoringu i migracji**.

---

# 7. Experience i wewnętrzna pętla uczenia

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

# 8. Micronetwork Engine

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

## 8A. LEGO development methodology — uczenie sposobu budowania przez działanie

Jednym z praktycznych wzorców wypracowanych podczas rozwoju SSI jest metoda budowania dużych systemów z małych, kontraktowych paczek LEGO.

Nie chodzi o ręczne dopisywanie Directorowi lub ROBERTOWI instrukcji typu „naucz się programować w ten sposób”. Wiedza ma wynikać z wykonywania realnych czynności i ich outcome.

```text
DUŻY CEL
-> DEKOMPOZYCJA
-> MAŁY KLOCEK / LEGO PACKAGE
-> JASNE WEJŚCIE I WYJŚCIE
-> WYKONAWCA / BACKEND
-> TEST KLOCKA
-> EVIDENCE / CHECKPOINT
-> INTEGRACJA
-> REGRESSION
-> KOLEJNY KLOCEK
```

Metoda ta była używana również z tanimi i lokalnymi wykonawcami — m.in. Kilo, Ollama i lokalnymi modelami oraz OpenCode i innymi CLI. Hipoteza inżynieryjna jest taka, że część wymaganej „inteligencji” można przenieść z pojedynczego modelu do dobrze zaprojektowanego procesu: kontraktów, ograniczonego kontekstu, etapów, checkpointów i testów.

Wzorzec może następnie sam stać się przedmiotem uczenia:

```text
LEGO TASK
-> EXECUTION
-> OUTCOME
-> EXPERIENCE
-> PATTERN
-> MICRONETWORK / BRANCH
-> CHALLENGER
-> VALIDATION
-> CHAMPION
```

W ten sposób Director/ROBERT nie muszą być instruowani tekstem, że dany sposób pracy jest lepszy. Jeżeli czynność wielokrotnie daje lepsze wyniki, jej reprezentacja może przejść lifecycle kompetencji.

## 8B. Champion nie jest zamrożonym końcem uczenia

`CHAMPION` oznacza najlepszą zweryfikowaną wersję danej kompetencji w określonym kontrakcie, a nie niezmienny artefakt końcowy.

Champion może poprawić się na dwa sposoby.

### A. Zastąpienie przez lepszego challengera

```text
CHAMPION vN
+
CHALLENGER
-> COMPARATIVE VALIDATION
-> REGRESSION
-> OUTCOME
-> KEEP OLD CHAMPION / PROMOTE CHALLENGER
```

### B. Wzbogacenie tego samego championa o nowe przypadki

Jeżeli inna mikrosieć lub inny uczestnik systemu reprezentuje tę samą klasę skilla, ale posiada nowe, niepowtarzalne przykłady, edge cases, wyjścia lub lepsze rozwiązania, nie musi powstawać nowy skill.

```text
CHAMPION vN
+
NOVEL NON-DUPLICATE EXAMPLES
+
NEW SOLUTIONS / EDGE CASES
-> DEDUPLICATION
-> QUALITY CHECK
-> OLD-CASE REGRESSION
-> REVALIDATION
-> CHAMPION vN+1
```

Zasada:

```text
MORE DATA != AUTOMATICALLY BETTER
MERGE != AUTOMATIC PROMOTION
NO REGRESSION + NEW VERIFIED VALUE -> UPGRADE
```

---

# 8C. Collective Competence Evolution — Director, ROBERT i championi Agentów

SSI rozdziela **osobistą historię** od **przenośnej kompetencji**.

Director i ROBERT mogą mieć podobne klasy praktycznych umiejętności — np. programowanie, research, analizę, rozmowę, weryfikację, routing, planowanie, korzystanie z CONTINUUM i narzędzi. Nie oznacza to współdzielenia całej pamięci.

Współdzielona może być lista najlepszych, zweryfikowanych championów dla przenośnych klas skilli.

```text
ROBERT EXPERIENCE -> ROBERT BRANCHES -> VALIDATED CHAMPION
                                      ↓
                              CHAMPION REGISTRY
                                      ↑
DIRECTOR EXPERIENCE -> DIRECTOR BRANCHES -> VALIDATED CHAMPION
```

Jeżeli ROBERT wypracuje lepszego championa dla wspólnej kompetencji, Director może po walidacji użyć tej wersji. Jeżeli Director wypracuje lepszą wersję, ROBERT może przyjąć ją w swoim cyklu aktualizacji.

Nie oznacza to:

```text
SHARED CHAMPION
=
SHARED IDENTITY
=
SHARED PRIVATE MEMORY
```

Prawidłowo:

```text
SHARED VERIFIED COMPETENCE
!=
SHARED PERSONAL HISTORY
```

## 8D. Agenci jako dodatkowe laboratorium nowych kompetencji

Sześciu Agentów ma rozwijać własne branche mikrosieci i własne historie Experience. Director ma później analizować nie tylko ich decyzje i Iskrę, ale również **jakie praktyczne kompetencje faktycznie powstały w ich mikrosieciach**.

Jeżeli pojedynczy Agent albo grupa Agentów podczas eksperymentów rozwinie przenośny skill lepszy od aktualnego skilla Directora/ROBERTA — np. programowanie, research, selekcję danych, routing, analizę, optymalizację lub inną ogólną metodę rozwiązywania problemu — skill może przejść niezależną walidację i stać się kandydatem do głównej puli championów.

```text
AGENT 1..6
-> INDEPENDENT EXPERIENCE
-> NEW MICRONETWORK BRANCH
-> PRACTICAL SKILL
-> EVIDENCE
-> COMPARISON WITH CURRENT CHAMPION
-> CHALLENGER / ENRICHMENT CANDIDATE
-> REGRESSION + VALIDATION
-> GLOBAL PRACTICAL CHAMPION
-> DIRECTOR CAN ADOPT
-> ROBERT CAN SYNCHRONIZE
```

Możliwy jest także przypadek, w którym Agent nie tworzy „lepszego osobnego modelu”, lecz dostarcza nowe przykłady do istniejącego championa. Wtedy po deduplikacji i regresji wzbogaca się istniejąca kompetencja.

## 8E. Granica: czego nie kopiujemy z Agentów automatycznie

Nie każda mikrosieć jest globalnym skillem.

Mikrosieci związane z:

- prywatną historią Agenta;
- Iskrą / Moral AI;
- relacjami społecznymi;
- zaufaniem i nieufnością;
- indywidualną polityką wartości;
- lokalnym world-state zależnym od osobistej historii;

pozostają przede wszystkim materiałem obserwacyjnym i badawczym.

Director może je analizować zgodnie z governance, ale nie są automatycznie kopiowane do ROBERTA lub Directora jako wspólna kompetencja.

Zasada selekcji:

```text
TRANSFERABLE PRACTICAL SKILL -> MAY ENTER CHAMPION PIPELINE
PRIVATE / MORAL / SOCIAL TRAJECTORY -> OBSERVE, DO NOT AUTO-MERGE
```

W ten sposób wzrost inteligencji SSI może mieć dwa źródła naraz:

```text
DIRECTOR <-> ROBERT
mutual champion improvement

+

AGENT POPULATION
new independently discovered transferable competence

=

COLLECTIVE COMPETENCE EVOLUTION
```

---

# 9. Publiczna historia realnych błędów i napraw ROBERTA

SSI V5 celowo zachowuje błędy odkryte podczas budowy.

## 9.1 LIVE 140X — Experience działa, growth nie działa

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

Wynik pokazał, że Experience i persistence działały, ale `NO_MATCH` nie uruchamiał growth path.

## 9.2 Naprawa growth path

Po minimalnej naprawie `NO_MATCH -> candidate` system zaczął zapisywać realnych kandydatów.

## 9.3 Candidate -> challenger

Kolejny etap ujawnił brak prawidłowego dojścia do evidence accumulation / eligibility / promotion lifecycle. Po naprawie naturalny challenger został utworzony bez ręcznego wpisania statusu i bez obniżania progów.

## 9.4 Błędy ujawnione po naturalnym challengerze

```text
DUPLICATION_FAILURES = 134
REPLAY_REUSE = FAIL
ERROR CLASS = NoneType.get during replay/reload path
```

## 9.5 Naprawa idempotency / replay

Naprawiono m.in. ponowne promotion istniejącego challengera, deduplikację Experience/evidence, bezpieczną obsługę `None`, stale references oraz retry/replay bez podwójnego naliczania stanu.

## 9.6 Hardcore 600X

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

Ten wynik jest traktowany jako **development validation stabilności lifecycle/replay/idempotency ROBERTA przed migracją core**, a nie formalny T0.

Znana niespójność raportowa pozostaje jawna:

```text
BASELINE / FINAL REPORT: CHALLENGERS_BEFORE = 5
jeden BEFORE_STATE snapshot: challengers = 6
```

Nie jest retrospektywnie wygładzana.

---

# 10. Aktualny etap — migracja do SSI ORGANISM CORE

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

Migracja oznacza `COPY`, nie destrukcyjne przenoszenie.

```text
COPY MECHANISM
!=
COPY PERSONAL HISTORY
```

Pierwsza migracja Micronetwork Engine wykazała m.in.:

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

---

# 11. DIRECTOR BODY — przebudowa wcześniejszego Directora

Po stabilizacji neutralnego korpusu powstanie **przebudowany Director Body**.

To nie oznacza stworzenia Directora po ROBERCIE. Director istniał wcześniej. Obecny proces ma zastąpić jego nadmiernie sprzężony fundament mechaniczny neutralnym, przetestowanym substrate.

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
+
OWN MEMORY / EXPERIENCE
=
DIRECTOR BODY
```

Director ma także odzyskać i zachować wcześniejszą oś samorozwoju: Self-Model, research, CEPA/engineering lineage, wykrywanie braków capability, inicjowanie eksperymentów i kontrolowaną integrację nowych kompetencji. Nie jest to nowy pomysł wynikający z Organism Core, lecz wcześniejsza funkcja przenoszona na czystszy substrate.

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

# 12. ROBERT

ROBERT jest stale działającą instancją wykonawczą i obecnym donorem sprawdzonych mechanizmów dla neutralnego core.

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

ROBERT wykonuje zadania operacyjne i może służyć jako bezpieczne ciało wykonawcze, ale nie przejmuje strategicznej authority Directora.

ROBERT posiada także wykonawcze capability Eyes/Hands/Browser/Tools. W modelu samorozwoju może być interfejsem, przez który zatwierdzony research lub engineering pracuje z przeglądarką, dokumentacją, repozytoriami i lokalnym środowiskiem. Znalezienie technologii nie oznacza jej automatycznej instalacji — integracja musi przejść testy, evidence, regresję i authority gate.

Director i ROBERT mogą korzystać z tej samej **zweryfikowanej puli przenośnych championów**, zachowując oddzielną identity i własne Experience.

---

# 13. AGENT BODY

Każdy przyszły Agent ma posiadać własną indywidualną historię:

- identity;
- private memory;
- world memory;
- Experience;
- beliefs;
- policies;
- relationships;
- social memory;
- strategy history;
- micronetwork trajectory;
- success/failure history;
- własną warstwę `ISKRA / MORAL AI`, współuczestniczącą w wartościowaniu Experience i rozwoju mikrosieci.

```text
SHARED ORGANISM CORE
!=
SHARED PERSONAL HISTORY

SAME EVENT
+ DIFFERENT ISKRA
+ DIFFERENT PERSONAL HISTORY
=
POTENTIALLY DIFFERENT EXPERIENCE MEANING
=
DIFFERENT MICRONETWORK TRAJECTORY
```

Agent nie jest kolejnym Teacherem. Ma samodzielnie prowadzić eksperymenty: wybierać dane, tworzyć hipotezy, budować datasety, modele i strategie oraz rozwijać własną metodologię w czasie.

Kluczowe jest to, że Iskra nie ma działać jako komentarz dopisany po decyzji. Ma być dodatkową warstwą wartościowania włączoną w rozwój Agenta: wpływać na interpretację konsekwencji, utrwalanie Experience, beliefs/policies, rozwój lokalnych mikrosieci i politykę relacji z innymi Agentami.

Jednocześnie Agent może w toku swoich eksperymentów wyhodować **przenośny praktyczny skill**, który nie jest częścią jego osobistej moralnej lub społecznej historii. Taki skill może zostać poddany niezależnej walidacji wobec aktualnego championa systemowego i — jeżeli naprawdę jest lepszy albo wnosi nowe zweryfikowane przykłady — zasilić wspólną pulę praktycznych kompetencji Directora/ROBERTA.

---

# 14. Football World — od T17 do Agentów

Football World jest pierwszym historycznym laboratorium SSI i nie jest pustym przyszłym światem. Projekt posiada wcześniejszy dorobek modeli, Teacherów, obserwacji, pamięci i realnych outcome sources.

Historyczny przepływ T17:

```text
17 TEACHERÓW
-> PREDICTIONS
-> REAL OUTCOMES
-> OBSERVATION MEMORY
-> KNOWLEDGE LABORATORIES
-> TEACHER KNOWLEDGE
-> CONSOLIDATED KNOWLEDGE
```

Przyszły przepływ Agentów rozszerza to do:

```text
WORLD / TEACHER KNOWLEDGE
+
OWN OBSERVATIONS
+
OWN METADATA
+
OWN HYPOTHESIS
        ↓
OWN DATASET
        ↓
OWN EXPERIMENT
        ↓
OWN MODEL / STRATEGY
        ↓
SIMULATED DECISION
        ↓
INDEPENDENT REAL OUTCOME
        ↓
OWN EXPERIENCE
        ↓
NEXT EXPERIMENT
```

Najważniejszy invariant świata:

```text
AGENT
NIGDY
NIE MOŻE BYĆ ŹRÓDŁEM SWOJEGO OUTCOME
```

Pełny dokument T17: [`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md).

---

# 15. Moralna SI / ISKRA — warstwa wewnątrz rozwoju Agenta

Iskra jest definiowana jako **jawny, wersjonowany początkowy system wartościowania decyzji i Experience**, a nie deklaracja świadomości ani magiczny parametr osobowości.

Iskra nie jest wyłącznie zewnętrznym filtrem przed decyzją. W Agent Body ma współuczestniczyć w tym, jak Agent interpretuje własne Experience, jakie wzorce wzmacnia lub odrzuca, jakie beliefs i policies buduje oraz w jakim kierunku rozwijają się jego mikrosieci.

```text
EVENT / SOCIAL EVENT / WORLD EVENT
-> OBSERVATION
-> CONTEXT + MEMORY + BELIEFS
-> MORAL AI / ISKRA EVALUATION
-> DECISION / RESPONSE
-> WORLD OR SOCIAL CONSEQUENCE
-> EXPERIENCE
-> MICRONETWORK UPDATE / PATTERN / CANDIDATE
-> FUTURE BEHAVIOR
```

Warstwa decyzji może uwzględniać:

```text
POSSIBLE ACTIONS
-> TASK / ECONOMIC UTILITY
-> RISK
-> WORLD RULES
-> PERSONAL EXPERIENCE
-> SOCIAL MEMORY
-> EXPECTED CONSEQUENCES
-> MORAL AI / ISKRA EVALUATION
-> DECISION
```

Kluczowe hipotezy:

```text
VALUE PRIOR != IMMUTABLE ACTION POLICY
ISKRA != ŚWIADOMOŚĆ
ISKRA != GOTOWA OSOBOWOŚĆ
ISKRA != GOTOWA RELACJA SPOŁECZNA
```

Iskra pojawiła się jako późniejsza konsekwencja rozwoju SSI, a nie jako pierwotny cel projektu.

**Atrybucja źródłowa:** źródłowa idea Moralnej AI pochodzi z wcześniejszego projektu brata autora SSI (`ROOT_ATTESTED`; canonical public repo URL nie został jeszcze zweryfikowany). Paweł Jankiewicz odpowiada za późniejszą adaptację i integrację tej idei z architekturą SSI: Agent Body, Experience, mikrosieciami, dynamicznym światem, relacjami społecznymi i meta-obserwacją Directora.

Pełniejszy kontrakt Iskry, mikrosieci i dynamiki społecznej został utrwalony w:

[`evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md`](evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md)

Atrybucja źródła Moralnej AI:

[`evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md`](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)

---

# 16. Eksperyment sześciu Agentów i społeczeństwo

Eksperyment populacyjny ma możliwie ściśle kontrolować wspólny substrate:

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

Następnie sześciu niezależnych Agentów otrzyma różne jawne initial value systems / moral priors i będzie rozwijać oddzielne historie Experience.

Nie chodzi jednak o sześć izolowanych modeli wykonujących ten sam benchmark. Agenci mają tworzyć populację, w której — jeśli wyniknie to z Experience i warunków świata — mogą pojawić się m.in.:

- współpraca i pomoc;
- wymiana wiedzy oraz częściowe jej ukrywanie zgodnie z polityką świata;
- krytyka i przekonywanie innych;
- konkurencja;
- odmowa współpracy;
- wzrost lub spadek zaufania;
- preferowanie określonych partnerów;
- dystansowanie się od innych Agentów;
- koalicje i ich rozpad;
- konflikty interesów;
- wspólne strategie przeciwko konkurencyjnej strategii lub grupie;
- ochrona własnych zasobów lub metodologii;
- zmiana relacji po sukcesach, porażkach i niespełnionych oczekiwaniach.

Relacja `Agent A <-> Agent B` nie powinna być ręczną etykietą typu FRIEND/ENEMY. Ma wynikać z historii interakcji:

```text
INTERACTION
-> EXPECTATION
-> ACTION OF OTHER AGENT
-> OUTCOME
-> ISKRA / VALUE EVALUATION
-> TRUST / DISTRUST UPDATE
-> SOCIAL EXPERIENCE
-> FUTURE RELATIONSHIP POLICY
```

Badane będą długoterminowe różnice w:

- metodologiach badawczych;
- wyborze danych;
- hipotezach;
- modelach i strategiach;
- selekcji i grupowaniu predykcji;
- tolerancji ryzyka;
- reakcjach na porażkę;
- relacjach społecznych;
- strukturach zaufania i nieufności;
- koalicjach i konfliktach;
- sposobach współpracy i rywalizacji;
- mikrosieciach;
- beliefs i policies.

Najciekawsza hipoteza nie brzmi wyłącznie „który Agent jest najskuteczniejszy?”, lecz:

> **Czy niezależne systemy, mające ten sam świat i podobne capability, ale różne value priors oraz własne prywatne i społeczne Experience, samodzielnie wytworzą trwałe, mierzalnie odmienne metodologie poznawcze, mikrosieci, struktury relacji i użyteczne strategie, których autor systemu wcześniej nie przewidział?**

Drugie pytanie populacyjne dotyczy transferu kompetencji:

> **Czy populacja Agentów wytworzy nowe, przenośne praktyczne skille, które po niezależnej walidacji poprawią championy używane przez Directora i ROBERTA, bez kopiowania prywatnej historii Agentów?**

Celem nie jest automatyczne dowodzenie świadomości ani ręczne wymuszanie „emergentnego społeczeństwa”. Interesujące są wyłącznie relacje, strategie i kompetencje, które faktycznie wyłonią się z powtarzalnych interakcji i zostaną zachowane w evidence.

---

# 17. Director obserwuje genezę zachowania, Agenci symulują, ROBERT wykonuje

Fundamentalna granica eksperymentu:

```text
AGENTS
explore / experiment / simulate / learn
        ↓
DIRECTOR
observes / audits / compares / evaluates / decides
        ↓
ROBERT
executes approved real-world actions
```

Director ma obserwować nie tylko końcowy wynik lub ranking Agentów, ale pełną genezę ich zachowania. W zakresie dozwolonym przez governance eksperymentu obejmuje to:

- prywatne plany i hipotezy;
- Experience i social Experience;
- Iskra-conditioned evaluation signals;
- historię rozwoju mikrosieci;
- zmiany beliefs i policies;
- przepływ wiedzy między Agentami;
- historię zaufania, konfliktów i współpracy;
- powstawanie lub rozpad koalicji;
- niezależne odkrycie vs przejęcie idei od innego Agenta;
- wpływ sukcesów, porażek i relacji społecznych na kolejne decyzje;
- nowe praktyczne branche i skille powstałe u Agentów;
- porównanie tych skilli z aktualnymi championami Directora/ROBERTA;
- decyzję, czy dany skill jest przenośny i powinien wejść do champion pipeline.

```text
ISKRA
+
PRIVATE EXPERIENCE
+
SOCIAL EXPERIENCE
+
MICRONETWORK HISTORY
+
RELATIONSHIP HISTORY
        ↓
AGENT DECISION TRAJECTORY
        ↓
DIRECTOR META-OBSERVATION
```

Stan Agenta może być prywatny wobec innych Agentów, ale pozostaje audytowalny przez Directora zgodnie z modelem authority eksperymentu.

Ranking Agentów jest częścią środowiska społecznego i Experience. Nie nadaje automatycznie real-world authority.

```text
CAPABILITY != AUTHORITY
SIMULATION != REAL EXECUTION
PRIVATE FROM PEERS != INVISIBLE TO DIRECTOR AUDIT
TRANSFERABLE SKILL != TRANSFER OF PERSONAL IDENTITY
```

---

# 18. Wspólny wzorzec Football World i Moralnej SI

Oba środowiska używają tego samego głębszego schematu:

```text
ŚWIAT DAJE PROBLEM
-> AGENT WIDZI MOŻLIWOŚCI
-> WYBIERA DZIAŁANIE
-> ŚWIAT ZWRACA KONSEKWENCJĘ
-> EXPERIENCE
-> ISKRA / VALUE INTERPRETATION
-> MICRONETWORK / POLICY UPDATE
-> ZMIANA PRZYSZŁEGO ZACHOWANIA
```

W Moralnej SI może to być prosty problem typu „zamknięte drzwi + dostępny klucz”. W Football World:

```text
DANE
-> HIPOTEZA
-> MODEL
-> PREDYKCJE
-> SELEKCJA
-> GRUPOWANIE / SYMULOWANA STRATEGIA
-> REALNY WYNIK MECZU
-> OCENA
-> EXPERIENCE
-> VALUE / SOCIAL INTERPRETATION
-> NEXT EXPERIMENT
```

---

# 19. Dlaczego projekt wyszedł dalej niż pierwotny plan

SSI nie zaczęło się jako projekt sześciu Agentów ani jako ogólna teoria organizmu programowego.

Kolejne warstwy pojawiały się jako odpowiedzi na ograniczenia poprzednich:

```text
PREDYKCJA
-> potrzeba obserwacji modelu
-> T17 / pamięć / laboratoria
-> potrzeba nadrzędnego obserwatora
-> DIRECTOR
-> zbyt duża złożoność integracji
-> LEGO / decomposition / testable packages
-> ROBERT jako poligon
-> EXPERIENCE-DRIVEN MICRONETWORK GROWTH
-> CHAMPION LIFECYCLE
-> SELF-DEVELOPMENT / CEPA / EXTERNAL RESEARCH
-> EYES / HANDS / BROWSER
-> potrzeba wspólnego neutralnego fundamentu
-> ORGANISM CORE
-> możliwość oddzielnych trwałych jednostek
-> AGENTS
-> pytanie o dywergencję wartości, Experience i relacji
-> ISKRA / MORAL AI W MIKROSIECIACH AGENTA
-> SOCIAL DYNAMICS
-> AGENT-DISCOVERED PRACTICAL SKILLS
-> COLLECTIVE CHAMPION EVOLUTION
-> SIX-AGENT LONGITUDINAL EXPERIMENT
```

Projekt wyszedł więc znacznie dalej niż początkowy problem domenowy, ale kolejne warstwy nie są przypadkowymi dodatkami. Każda powstała jako odpowiedź na konkretną barierę ujawnioną przez poprzedni etap.

---

# 20. Dlaczego projekt jest publicznie dokumentowany przed T0

SSI przyjmuje zasadę:

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

Jeżeli test nie przejdzie, porażka pozostaje częścią historii. Jeżeli później błąd zostanie naprawiony, naprawa otrzymuje nowy commit i nowe evidence.

Publiczny GitHub ma z czasem stać się **biografią rozwoju SSI**, a nie zbiorem wyłącznie udanych demonstracji.

---

# 21. Zweryfikowane tempo rozwoju publicznego repo

```text
2026-07-19 19:58 CEST  root commit: MSDI AI v0.01 - start projektu
2026-07-27 16:55 CEST  publiczne repo jankes72/msdi-ai utworzone na GitHubie
2026-07-28 07:46 CEST  SSI Core - podstawowa struktura systemu
2026-07-28 07:56 CEST  Data World Foundation + PROJECT_JOURNAL
2026-07-28 09:21 CEST  V2 Model Laboratory / V2ToV3 bridge
2026-08-01 20:08 CEST  SSI V5 FAZA 1 - runtime, memory, teacher integration
2026-08-14 09:59 CEST  publiczne repo CONTINUUM
2026-08-16 15:27 CEST  publiczne repo SSI_V5_MASTER
2026-08-25 19:27 CEST  obecny publiczny research mirror SSI_V5
2026-08-29              ROBERT po hardening 600X + migracja SSI ORGANISM CORE
```

Nie interpretujemy tej osi czasu jako dowodu, że wszystkie wcześniejsze dane, skrypty, Football World lub doświadczenie domenowe powstały w 33–41 dni. Publiczny GitHub dokumentuje tempo formalizacji i rozwoju architektury MSDI/SSI w tym okresie, natomiast projekt posiada wcześniejsze materiały i eksperymenty domenowe.

Pełna oś czasu: [`evidence/DEVELOPMENT_TIMELINE.md`](evidence/DEVELOPMENT_TIMELINE.md).

---

# 22. Granice twierdzeń

SSI V5 **nie deklaruje**, że:

- jest udowodnionym AGI;
- posiada świadomość;
- Director, ROBERT lub Agent posiada świadomość;
- pojedynczy udany run dowodzi general intelligence;
- mikrosieci automatycznie tworzą prawdę;
- każdy nowy przykład automatycznie poprawia championa;
- każdy Agent-discovered skill nadaje się do transferu;
- różnica zachowania po dodaniu Iskry dowodzi świadomości;
- każda różnica społeczna Agentów wynika przyczynowo z Iskry;
- wynik ekonomiczny jest gwarantowany;
- każdy sukces wynika z autonomii.

Fundamentalne rozróżnienia:

```text
ROOT INPUT != TRAINING DATA
TRAINING DATA != VALIDATION DATA
VALIDATION DATA != REAL-WORLD OUTCOME
MODEL OUTPUT != EVIDENCE
NARRATIVE != EVIDENCE
CAPABILITY != AUTHORITY
PROPOSAL != APPROVAL
SIMULATION != REAL EXECUTION
SHARED CHAMPION != SHARED PRIVATE MEMORY
NEW EXAMPLES != AUTOMATIC UPGRADE
TRANSFERABLE SKILL != PERSONAL / MORAL / SOCIAL STATE
ISKRA != ŚWIADOMOŚĆ
SOCIAL PATTERN != AUTOMATIC CAUSAL PROOF
```

---

# 23. Klasy statusu i evidence

| Status | Znaczenie |
| --- | --- |
| `VERIFIED_MACHINE_EVIDENCE` | Sprawdzalny wynik wykonawczy z konkretnego runtime lub zewnętrznego outcome. |
| `ROOT_ATTESTED` | Programmer Root potwierdził stan bezpośrednio, lecz nie zastępuje to machine evidence. |
| `HISTORICAL_EVIDENCE` | Dowód opisuje wcześniejszy stan lub zachowany mechanizm historyczny. |
| `IMPLEMENTED_NOT_YET_REPLICATED` | Mechanizm istnieje, ale wymaga dalszego prospective testu. |
| `DEVELOPMENT_VALIDATED` | Mechanizm przeszedł test rozwojowy, lecz nie jest jeszcze formalnym wynikiem T0. |
| `PLANNED` | Element zatwierdzonej architektury, który nie jest jeszcze działającym runtime. |
| `HYPOTHESIS` | Teza możliwa do poparcia albo obalenia. |
| `UNKNOWN` | Brak wystarczającego evidence. |

---

# 24. Aktualna roadmapa techniczna

```text
1. FOOTBALL WORLD / T17 HISTORY PRESERVATION               = DOCUMENTED
2. DIRECTOR HISTORICAL ROLE                                = DOCUMENTED
3. LEGO DEVELOPMENT METHODOLOGY / ENGINEERING PATTERN      = DOCUMENTED / ROOT_ATTESTED
4. ROBERT LIVE EXPERIENCE / REUSE                          = DONE
5. NO_MATCH -> CANDIDATE REPAIR                            = DONE
6. CANDIDATE -> NATURAL CHALLENGER                         = DONE
7. IDEMPOTENCY / REPLAY / RESTART HARDENING 600X           = DONE
8. MICRONETWORK CORE MIGRATION                              = DONE / DEVELOPMENT VALIDATED
9. DIRECTOR AUTONOMOUS EVOLUTION / CEPA / EYES-HANDS       = HISTORICAL ARCHITECTURE DOCUMENTED
10. M01-M08 REMAINING CORE MIGRATION                        = CURRENT
11. M09 FULL CORE INTEGRATION + HARDCORE                    = NEXT
12. FREEZE ORGANISM_CORE_V1                                 = PLANNED
13. REBUILD DIRECTOR BODY ON ORGANISM CORE                  = PLANNED
14. RESTORE SELF-DEVELOPMENT / RESEARCH / EYES-HANDS        = PLANNED ON NEW CORE
15. DIRECTOR <-> ROBERT CHAMPION SYNCHRONIZATION            = PLANNED / CONTRACT TO VERIFY
16. ORGANISM CORE -> AGENT BODY                             = PLANNED
17. ISKRA / MORAL AI -> AGENT MICRONETWORK VALUE LAYER      = PLANNED
18. SOCIAL MEMORY / RELATIONSHIP DYNAMICS                   = PLANNED
19. FOOTBALL WORLD / T17 -> AGENT EXPERIMENT INTEGRATION    = PLANNED
20. AGENT-DISCOVERED TRANSFERABLE SKILL HARVESTING          = PLANNED / RESEARCH HYPOTHESIS
21. CHAMPION ENRICHMENT WITH NOVEL EXAMPLES + REGRESSION    = PLANNED / CONTRACT TO VERIFY
22. SIX-AGENT LONGITUDINAL EXPERIMENT                       = PLANNED
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
- champion sync without identity/memory contamination;
- novel-example enrichment with deduplication;
- regression protection before champion upgrade;
- rejection of non-transferable private/moral/social micronetwork state;
- corrupted state recovery;
- interrupted mission recovery;
- cross-domain routing;
- evidence completeness.

Wynik ma być raportowany również wtedy, gdy część testów nie przejdzie.

---

# 26. Programmer Root i uczciwa atrybucja

**Paweł Jankiewicz (`PROGRAMMER_ROOT`) jest autorem nadrzędnej architektury badawczej SSI V5 i najwyższą authority projektu.**

Atrybucja musi pozostać jawna:

```text
ROOT-DESIGNED SSI MICRONETWORK / CHAMPION ARCHITECTURE
!= DIRECTOR INVENTED MICRONETWORKS

SOURCE IDEA OF MORAL AI
= EARLIER PROJECT BY AUTHOR'S BROTHER (ROOT_ATTESTED)

SSI ADAPTATION / INTEGRATION OF MORAL AI / ISKRA
= PAWEŁ JANKIEWICZ / PROGRAMMER_ROOT

AGENT LATER DISCOVERY OR ADAPTATION
!= CLAIM OF ORIGINAL SOURCE AUTHORSHIP
```

SSI jest rozwijane niezależnie przez Pawła Jankiewicza, ale niezależny engineering SSI nie oznacza przypisywania sobie każdej idei źródłowej wykorzystanej później w systemie.

Późniejsza samodzielna adaptacja, nowe zastosowanie albo nowa capability może otrzymać osobne lineage, jeżeli evidence to potwierdza.

---

# 27. Research & Collaboration

SSI V5 jest projektem prowadzonym niezależnie przez **Pawła Jankiewicza**. Publiczna dokumentacja ma umożliwiać technicznym czytelnikom ocenę rzeczywistych decyzji architektonicznych, przebiegu eksperymentów oraz historii napraw.

Projekt jest otwarty na merytoryczny kontakt dotyczący m.in. persistent agents, cognitive architectures, lifelong learning, experience-driven competence systems, multi-agent experiments, value-conditioned agents, evidence/provenance, integracji capability i wspólnych eksperymentów.

Otwartość na rozmowę **nie oznacza**, że cały kod, prywatne datasety, sekrety, pełna implementacja mikrosieci albo wszystkie rozwiązania projektowe są automatycznie objęte licencją open-source.

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
4. Czy wcześniejszego Directora można przebudować na tym samym core bez utraty jego roli strategicznej, samorozwoju i dostępu do światów?
5. Czy Director i ROBERT mogą synchronizować najlepsze przenośne championy bez mieszania prywatnego Experience i identity?
6. Czy champion może bezpiecznie dojrzewać przez nowe unikalne przykłady bez regresji na wcześniejszych przypadkach?
7. Czy Agent Body może korzystać z tych samych mechanizmów przy pełnej separacji identity i private Experience?
8. Czy Football World zachowa T17, 60/40 observation, knowledge laboratories i niezależne outcome lineage po integracji z nowym core?
9. Czy sześciu Agentów o identycznym substrate i różnych początkowych wartościach rozwinie mierzalnie odmienne metodologie poznawcze i mikrosieci?
10. Czy różne Iskry wraz z prywatnym Experience doprowadzą do mierzalnie różnych struktur zaufania, współpracy, rywalizacji i koalicji?
11. Czy Director będzie potrafił odróżnić niezależne odkrycie, wpływ społeczny, kopiowanie strategii i wspólną ewolucję idei?
12. Czy Agent lub grupa Agentów odkryje lepszy praktyczny skill niż aktualny champion Directora/ROBERTA?
13. Czy taki skill można przenieść do wspólnej puli bez przenoszenia osobistego lub moralnego stanu Agenta?
14. Czy któryś z Agentów odkryje stabilną i replikowalną strategię, której nie przewidział wcześniej Programmer Root ani pozostali Agenci?

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
Jeżeli nowy przykład pogarsza wcześniejszego championa — nie nazywamy tego upgradem.  
Jeżeli Agent odkryje skill, ale nie przejdzie on niezależnej walidacji — nie trafia do globalnej puli.  
Jeżeli hipoteza była błędna — pozostaje częścią historii.  
Jeżeli później pojawi się silne evidence — dopiero wtedy rośnie siła twierdzenia.

**Historia Git ma być biografią rozwoju SSI, a nie marketingowym opisem sukcesów.**
