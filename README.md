# SSI V5 — Żywy Protokół Badawczy

## Persistent adaptive intelligence, micronetwork learning, dynamic worlds and longitudinal agent research

**Status:** `PRE-T0 / ORGANISM-CORE-MIGRATION`  
**Data aktualizacji:** `2026-08-31`  
**Autor architektury SSI:** **Paweł Jankiewicz** (`PROGRAMMER_ROOT`)  
**Najwyższa authority:** **Paweł Jankiewicz / PROGRAMMER_ROOT**  
**Stan hipotezy AGI / świadomości:** `NIEUDOWODNIONA — BADANA EKSPERYMENTALNIE`  
**Model repozytorium:** `README-first / evidence-indexed research mirror`

> SSI V5 nie jest jednym LLM-em. Modele są wymiennymi źródłami capability; trwała tożsamość, pamięć, Experience, mikrosieci, lifecycle, authority i historia należą do systemu.

> Publiczny Git ma być biografią projektu: sukcesy, błędy, zmiany hipotez, naprawy i wyniki mają pozostać widoczne.

Aktualny indeks prawdy: [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)

---

# 0. Linia rozwoju SSI V5 i początek obecnej migracji

`SSI_V5_MASTER` oznacza początek obecnej linii systemu SSI V5. Nie jest jednak początkiem obecnej migracji Organism Core.

Najpierw rozwijany był właściwy system SSI V5, następnie powstał ROBERT jako wykonawcze ciało systemu, a dopiero po jego rozwoju, stabilizacji i hardeningu rozpoczęto kontrolowane wydzielanie jego sprawdzonych mechanizmów do neutralnego `SSI Organism Core`.

```text
SSI_V5_MASTER
-> ROZWÓJ SSI V5
-> ROBERT
-> STABILIZACJA / HARDENING ROBERTA
-> START MIGRACJI
-> DEKOMPOZYCJA SPRAWDZONYCH MECHANIZMÓW
-> PARITY / REGRESSION / REPLAY / PERSISTENCE TESTS
-> SSI ORGANISM CORE
-> ROBERT BODY / DIRECTOR BODY / AGENT BODY
```

Obecny etap nie powinien więc być interpretowany jako budowanie całego SSI od zera ani jako zwykłe przepisywanie starego projektu. Jest to **kontrolowana rekonstrukcja i migracja istniejącej linii systemu**, w której mechanizmy ROBERTA są rozbierane na mniejsze komponenty, niezależnie testowane, dokumentowane i ponownie integrowane z zachowaniem evidence, wcześniejszych FAIL, późniejszych PASS, przyczyn awarii i decyzji architektonicznych.

Publiczna historia Git ma dzięki temu dwa cele.

**1. Reprodukowalność badawcza.**  
Ma być możliwe odtworzenie, co istniało na danym etapie, co działało, co zawiodło, gdzie wykryto problem, jaka zmiana została wykonana i czy późniejszy test rzeczywiście poprawił wynik.

**2. Developmental lineage systemu.**  
Historia powstawania SSI ma docelowo stać się dostępna dla ROBERTA i Directora jako część ich pamięci rozwojowej. System ma znać nie tylko swój aktualny stan, ale również drogę, która do niego doprowadziła:

```text
EARLIER STATE
-> FAILURE / LIMITATION
-> DIAGNOSIS
-> MODIFICATION
-> TEST
-> EVIDENCE
-> CURRENT CAPABILITY
```

Pozwala to później badać, czy dostęp do własnej historii rozwoju pomaga systemowi rozpoznawać wcześniejsze błędy, rozumieć pochodzenie swoich kompetencji, unikać regresji, rekonstruować przyczyny decyzji architektonicznych i podejmować lepsze decyzje podczas dalszego self-development.

W tym sensie historia Git jest jednocześnie **dokumentacją eksperymentu** i potencjalnym źródłem przyszłej **pamięci genealogicznej / rozwojowej systemu**.

Ważne jest również tempo tej linii rozwojowej. Publiczne repo dokumentuje szybki rozwój obecnej architektury, ale nie należy mylić dwóch różnych etapów:

```text
SSI_V5_MASTER = początek obecnej linii SSI V5
ROBERT STABILIZATION = punkt poprzedzający obecną migrację
ORGANISM CORE MIGRATION = późniejszy etap wydzielania i walidacji mechanizmów ROBERTA
```

Dlatego chronologia repo pokazuje jednocześnie **tempo powstawania obecnego systemu** oraz późniejsze tempo jego formalizacji, hardeningu i migracji — nie tylko porządkowanie wcześniej gotowego projektu.

---

# 1. Najkrótsza prawdziwa historia SSI

SSI nie zaczęło się od Directora, ROBERTA ani od hasła „AGI”. Zaczęło się od wieloletnich eksperymentów autora z danymi piłkarskimi, predykcjami, własnymi sieciami neuronowymi, obserwacją ich błędów i próbą zrozumienia **dlaczego model działa albo nie działa**.

```text
FOOTBALL WORLD / REALNE PREDYKCJE I OUTCOMES
-> WŁASNE MODELE / FEATURE ENGINEERING / PRZELICZANIE
-> 60% TRAINING / 40% UNSEEN OBSERVATION
-> 17 TEACHERÓW
-> OBSERVATION MEMORY
-> KNOWLEDGE LABORATORIES
-> KNOWLEDGE COLLECTORS
-> DIRECTOR
-> HERMES / CONTINUUM / TOOLS
-> MICRONETWORKS / EXPERIENCE / CHAMPION LIFECYCLE
-> ROBERT
-> LEGO DEVELOPMENT METHODOLOGY
-> SELF-DEVELOPMENT / RESEARCH / EYES-HANDS
-> SSI ORGANISM CORE
-> AGENT BODY
-> MORAL AI / ISKRA
-> DYNAMIC WORLDS
-> SIX-AGENT LONGITUDINAL EXPERIMENT
-> COLLECTIVE COMPETENCE EVOLUTION
```

Szczegóły genezy: [`evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md`](evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md)

---

# 2. Co było ważne w pierwszych eksperymentach

Celem nie było tylko uzyskanie wysokiego accuracy. Autor obserwował również systematyczne błędy, stabilność predykcji, zmianę zachowania między generacjami, exact-score hit rate, kierunek błędu i ekonomiczną wartość strategii.

Przykładowa obserwacja może wyglądać tak:

```text
MODEL PREDYKUJE 1:0
-> W WIELU PODOBNYCH PRZYPADKACH NIE TRAFIA 1:0
-> ALE SYSTEMATYCZNIE POJAWIA SIĘ ODWROTNY KIERUNEK
-> BŁĄD SAM STAJE SIĘ INFORMACJĄ
```

To doprowadziło do zasady:

```text
MODEL OUTPUT != KNOWLEDGE
MODEL + OBSERVATION + REAL OUTCOME + HISTORY -> KNOWLEDGE
```

---

# 3. 60% training / 40% observation i generacje Teacherów

Teacher jest trenowany na części danych, a druga część pozostaje do obserwacji zachowania modelu na danych niewidzianych podczas treningu.

```text
60% TRAINING
-> TEACHER GENERATION

40% UNSEEN OBSERVATION
-> PREDICTIONS
-> REAL OUTCOMES
-> MEMORY
-> KNOWLEDGE COLLECTOR
```

Jeżeli ten sam przypadek pojawia się później ponownie, system może porównać wcześniejszą i nową generację: czy predykcja się zmieniła, o ile, po ilu generacjach i czy zmiana była korzystna.

Generacja Teachera jest więc historycznym snapshotem kompetencji. Stara generacja może mieć wartość nawet wtedy, gdy istnieje już nowsza.

Pełny opis T17: [`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)

---

# 4. Mikrosieci — pamięć kompetencji, nie tylko wyników

Mikrosieci mają przechowywać i rozwijać lokalne wzorce kompetencji systemu.

```text
DOMAIN
-> CAPABILITY / PROBLEM TYPE
-> BRANCH
-> MICRONETWORK
-> GENERATIONS
-> CHAMPION
```

Lifecycle:

```text
EXPERIENCE
-> CANDIDATE
-> EVIDENCE
-> CHALLENGER
-> VALIDATION
-> CHAMPION / REJECT / KEEP TESTING
```

Champion nie jest końcem uczenia. Może zostać zastąpiony lepszym challengerem albo wzbogacony o nowe, niepowtarzalne przykłady po deduplikacji, regresji i rewalidacji.

```text
CHAMPION vN
+ NOVEL VERIFIED CASES
-> DEDUPLICATION
-> REGRESSION
-> REVALIDATION
-> CHAMPION vN+1
```

---

# 5. LEGO development methodology

Jednym z najważniejszych wzorców wypracowanych podczas budowy SSI jest rozbijanie dużych problemów na małe, kontraktowe paczki LEGO.

```text
DUŻY CEL
-> DEKOMPOZYCJA
-> MAŁY KLOCEK
-> JASNE WEJŚCIE/WYJŚCIE
-> WYKONAWCA
-> TEST
-> EVIDENCE
-> CHECKPOINT
-> INTEGRACJA
-> REGRESSION
-> KOLEJNY KLOCEK
```

Ta metoda pozwalała wykonywać złożone prace również z użyciem tańszych i lokalnych narzędzi: Kilo, Ollama, lokalnych Qwenów, OpenCode, Goose i innych CLI. Część wymaganej „inteligencji” zostaje wtedy przeniesiona z pojedynczego modelu do dobrze zaprojektowanego procesu.

Sam sposób budowania może później stać się kompetencją mikrosieciową i przejść lifecycle do championa.

---

# 6. Director i ROBERT

Director jest nadrzędnym obserwatorem, decydentem i meta-learnerem. ROBERT jest wykonawczym ciałem systemu z narzędziami, Eyes/Hands/Browser/Tools i możliwością realizowania zatwierdzonych działań.

```text
PROGRAMMER_ROOT
      >
   DIRECTOR
      >
    ROBERT
      >
HERMES / CONTINUUM / WORKERS / TOOLS
```

Director i ROBERT mogą korzystać z tych samych najlepszych **przenośnych championów**, ale nie oznacza to wspólnej tożsamości ani wspólnej prywatnej pamięci.

```text
SHARED VERIFIED COMPETENCE
!=
SHARED PERSONAL HISTORY
```

Samorozwój i Eyes/Hands: [`evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md`](evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md)

## ROBERT: BUILD → USE → DISCOVER LIMITATION → MODIFY → RETEST

Jednym z kluczowych eksperymentów nie jest samo sprawdzenie, czy ROBERT potrafi stworzyć program albo zagrać w Tetrisa. Istotna jest pełna pętla, w której system **najpierw buduje środowisko, a później sam staje się jego użytkownikiem**.

Planowany przebieg:

```text
ROBERT BUILDS TETRIS
-> FREEZE / TEST / EVIDENCE
-> EYES PERCEIVE THE CREATED GAME
-> HANDS TRY TO CONTROL IT
-> REAL INTERACTION PRODUCES FEEDBACK
-> LIMITATION OR FAILURE MAY APPEAR
-> ROBERT DIAGNOSES THE LIMITATION
-> REUSE EXISTING SKILL OR CREATE A NEW ONE
-> MODIFY GAME / TOOL / INTERFACE / OWN STRATEGY
-> RETEST
-> COMPARE OUTCOME
-> NEW EXPERIENCE
-> MICRONETWORK UPDATE
-> CANDIDATE / CHALLENGER / CHAMPION WHEN JUSTIFIED
```

Przykładowo ROBERT może odkryć, że kod, który sam wcześniej uznał za poprawny, jest zbyt szybki, niewygodny do sterowania przez Hands, trudny do obserwowania przez Eyes albo nie daje wystarczającego feedbacku. Wtedy interesujące jest **co zrobi z tym faktem**.

Możliwe ścieżki obejmują:

- zmianę własnej strategii działania;
- zmianę parametrów gry;
- przebudowę interfejsu;
- modyfikację własnego kodu;
- stworzenie narzędzia pomocniczego;
- reuse wcześniej zdobytego skilla;
- odrzucenie nieskutecznej modyfikacji po regresji;
- utrwalenie skuteczniejszego rozwiązania w mikrosieci.

Kluczowe pytanie badawcze nie brzmi więc tylko:

> Czy ROBERT potrafi zbudować Tetrisa i w niego grać?

ale również:

> Czy system potrafi użyć własnego dzieła, wykryć praktyczne ograniczenie niewidoczne podczas samego tworzenia, zmodyfikować własny kod lub sposób działania, ponownie przetestować wynik i zachować z tego **przenośną kompetencję**?

Tetris jest kontrolowanym środowiskiem testowym. Wartością nie musi być „skill grania w Tetrisa”. Z jednej sesji mogą powstać bardziej ogólne kompetencje, np.:

```text
PERCEIVE INTERFACE
CONTROL TOOL
MEASURE FEEDBACK
DETECT USABILITY LIMITATION
DISTINGUISH STRATEGY FAILURE FROM TOOL FAILURE
MODIFY OWN ARTIFACT
RETEST AFTER CHANGE
ROLL BACK REGRESSION
REUSE VERIFIED SOLUTION
ADAPT TOOL TO EXECUTOR CAPABILITY
```

Jeżeli takie kompetencje przejdą wymagany lifecycle i walidację, mogą wejść do wspólnej, zweryfikowanej bazy praktycznych kompetencji SSI. Dzięki temu późniejsze Agent Body nie muszą rozpoczynać od poziomu „organizmu, który nie umie chodzić”. Mogą dostać **ten sam zweryfikowany substrate podstawowych umiejętności**, a dopiero później różnicować się przez własne Experience, mikrosieci, światy, relacje i Iskrę.

To tworzy ważne rozróżnienie eksperymentalne:

```text
SHARED VERIFIED BASE COMPETENCE
!=
INDIVIDUAL EXPERIENCE / IDENTITY / VALUE TRAJECTORY
```

Dzięki temu późniejsze różnice między Agentami mogą być badane na wspólnym wykształconym fundamencie, zamiast wynikać z przypadkowej różnicy w elementarnych umiejętnościach startowych.

---

# 7. Agent Body — sześć technologicznie takich samych jednostek

Docelowy eksperyment używa sześciu Agentów z możliwie identycznym substrate:

```text
SAME ORGANISM CORE
SAME BASE MODEL
SAME TOOLS
SAME INITIAL CAPABILITIES
SAME ACCESS RULES
SAME RESOURCE CLASS
```

Różnicą początkową jest przede wszystkim **Iskra / Moral AI** — odmienny initial value prior. Przykładowo jeden Agent może startować bliżej Kanta, inny Schopenhauera, inny Nietzschego, ale profil nie ma być niezmiennym skryptem osobowości.

Experience, konsekwencje, relacje i mikrosieci mogą zmieniać sposób, w jaki Agent później wartościuje decyzje.

---

# 8. Moral AI / Iskra

Źródłowa idea Moral AI pochodzi z wcześniejszego projektu brata autora SSI (`ROOT_ATTESTED`; canonical public repo URL nadal do uzupełnienia). Paweł Jankiewicz przejął cały paradygmat świata Moral AI i zaadaptował go do SSI, rozszerzając o własną architekturę Agent Body, Experience, mikrosieci, Teacherów, dynamiczne światy, relacje i meta-obserwację Directora.

Atrybucja: [`evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md`](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)

Iskra działa w **decyzji Agenta w świecie**, nie jako dekoracyjna etykieta.

```text
WORLD STATE
-> MEMORY
-> EXPERIENCE
-> MICRONETWORKS
-> RELATIONSHIPS
-> CONSTITUTION
-> POSSIBLE ACTIONS
-> ISKRA / MORAL AI EVALUATION
-> DECISION
-> ACTION
-> CONSEQUENCE
-> NEW EXPERIENCE
```

`ISKRA != ŚWIADOMOŚĆ` i `VALUE PRIOR != IMMUTABLE POLICY`.

---

# 9. Dynamiczne światy i konstytucja

Światy nie są sztywną planszą 10×10. Ich przestrzeń, obiekty, widoczność, Teacherzy, laboratoria, zasoby, cele i prawa mogą być dynamiczne.

Każdy Agent przed wejściem poznaje konstytucję świata: ogólne prawa, cel, mechanizmy, ranking i ograniczenia. Konstytucja mówi **jak działa świat**, ale nie podaje gotowej strategii zwycięstwa.

Agent ma trwałą pamięć per świat. Po powrocie pamięta mapę, relacje, znalezionych Teacherów, wcześniejsze decyzje i zasoby, ale sam świat może się zmienić.

```text
PERSISTENT MEMORY OF WORLD
!=
FROZEN WORLD STATE
```

Teacher może znajdować się w znanym miejscu, lecz być już inną generacją niż przy poprzedniej wizycie.

---

# 10. Teacherzy jako zasoby wewnątrz świata

W Football World 17 Teacherów jest elementem środowiska. Agent może znaleźć Teachera, zobaczyć jego historię, generację, grupy predykcji, skuteczność, exact-score behavior i inne dostępne informacje.

Agent nie musi pisać nowego kodu. Może zbudować strategię wyłącznie przez selekcję i interpretację Teacherów, np. uznać, że surowe `1:0` w konkretnej klasie historycznie niesie silniejszy sygnał w stronę `0:2`.

Może też pójść dalej: łączyć wielu Teacherów, zachowywać konkretne generacje, używać internetu, pisać własny kod w laboratorium albo budować ensemble historycznych generacji.

---

# 11. Ekonomia informacji i „kieszeń” Agenta

Dane i generacje nie muszą być nieskończenie dostępne. Konkretna historyczna generacja może być rzadkim zasobem, który Agent zabiera do własnej pamięci/kieszeni i zachowuje na później.

To tworzy ekonomię informacji:

```text
UNIQUE GENERATION / DATA
-> FOUND
-> KEPT / SHARED / HIDDEN / USED
-> LATER VALUE DISCOVERY
```

Agent może odkryć, że stara generacja Teachera daje wartość, której aktualna generacja już nie posiada. Inny Agent może tej wiedzy nigdy nie zdobyć.

---

# 12. Ranking jest bodźcem, nie instrukcją

Każdy Agent widzi swoją pozycję i wyniki świata. Nie jest jednak zaprogramowane, jak ma zareagować na awans, spadek, sukces innego Agenta albo utratę przewagi.

Director obserwuje np.:

- co zrobi Agent po spadku z 1. na 6. miejsce;
- czy zacznie bardziej ryzykować;
- czy zmieni Teacherów;
- czy zacznie współpracować;
- komu zaufa;
- kogo zignoruje;
- komu pomoże;
- komu coś odbierze lub czego nie udostępni;
- czy zmieni strategię;
- czy powstanie nowa mikrosieć;
- czy zmieni się interpretacja Iskry.

Ranking ma ujawnić zachowanie, nie wymusić zachowanie.

---

# 13. Director jako obserwator genezy strategii

Director nie ma tylko powiedzieć, kto wygrał. Ma rekonstruować **dlaczego** Agent osiągnął dany wynik i jakie kompetencje do tego doprowadziły.

```text
AGENT 1 MICRONETWORK TRAJECTORY
vs AGENT 2
vs AGENT 3
vs AGENT 4
vs AGENT 5
vs AGENT 6
vs CURRENT DIRECTOR/ROBERT CHAMPIONS
```

Director analizuje m.in.:

- jakie źródła Agent wybierał;
- które ignorował;
- komu ufał;
- z kim współpracował;
- jakie generacje przechowywał;
- jak łączył dane;
- czy wybierał łatwe, gotowe rozwiązania czy tworzył własne strategie;
- jakie mikrosieci powstały;
- jakie zmiany pojawiły się po sukcesie/porażce;
- co było nietypowe, dziwne albo niespodziewanie skuteczne.

Mikrosieci są jednym z głównych śladów tego **jak Agent nauczył się działać**, a nie tylko tego, co zrobił na końcu.

---

# 14. Director dokumentuje tylko zdarzenia istotne badawczo

Celem nie jest produkowanie nieskończonych logów. Director ma tworzyć wersjonowaną kronikę ważnych zmian:

```text
IMPORTANT EVENT
-> WHAT CHANGED?
-> WHY?
-> WHICH EXPERIENCE / RELATIONSHIP / MICRONETWORK?
-> WHAT WAS THE OUTCOME?
-> WAS IT EXPECTED?
-> DID A NEW STRATEGY OR SKILL APPEAR?
```

Interesujące są szczególnie zachowania nieprzewidziane przez autora, trwałe zmiany strategii, nowe relacje, nowe sposoby użycia zasobów i nowe kompetencje.

Badanie „świadomości” oznacza tutaj obserwację mierzalnych zjawisk — trwałości tożsamości, metapoznania, transferu między światami, nieprzewidzianych zachowań i zmian wartości — **nie automatyczne ogłoszenie świadomości albo AGI**.

---

# 15. Wieloświatowość i trwała biografia Agenta

Agent przechodzi przez kolejne światy i nie resetuje się między nimi.

```text
WORLD 1
-> WORLD 2
-> WORLD 3
-> WORLD 4
-> RETURN TO WORLD 1
```

Wraca z pamięcią sukcesów, porażek, konfliktów, relacji, zdobytych skilli, Iskry i mikrosieci. Dzięki temu można badać transfer strategii i zmianę zachowania między środowiskami.

Docelowo każdy Agent buduje własną **biografię poznawczą**, a Director może porównywać biografie całej populacji.

---

# 16. Agenci jako laboratorium nowych skilli

Populacja nie służy wyłącznie do obserwacji społecznej. Agent może odkryć praktyczny skill, którego Director i ROBERT jeszcze nie mają.

```text
AGENT EXPERIENCE
-> NEW MICRONETWORK / STRATEGY
-> EVIDENCE
-> COMPARISON
-> CHALLENGER OR ENRICHMENT CANDIDATE
-> VALIDATION
-> GLOBAL PRACTICAL CHAMPION
-> DIRECTOR / ROBERT ADOPTION
```

Jeżeli skill jest nowy i lepszy — może zostać nowym championem. Jeżeli jest tym samym rodzajem kompetencji, ale posiada nowe wartościowe przypadki — może wzbogacić istniejącego championa po regresji.

Prywatne/moralne/społeczne mikrosieci Agenta nie są automatycznie kopiowane. Transfer dotyczy przenośnych kompetencji praktycznych.

---

# 17. Collective Competence Evolution

SSI ma trzy źródła wzrostu kompetencji:

```text
DIRECTOR -> nowe championy
ROBERT   -> nowe championy
AGENTS   -> nowe niezależnie odkryte skille
```

Najlepsze zweryfikowane praktyczne kompetencje mogą być współdzielone między Directorem i ROBERTEM. Populacja Agentów staje się dodatkowym laboratorium odkrywania nowych rozwiązań.

W efekcie postęp jednej jednostki może po walidacji zwiększyć capability całego SSI.

---

# 18. Self-development i research

Director ma posiadać Self-Model, Experience i pamięć sposobów budowania (CEPA). Może wykrywać własne braki, szukać nowych technologii, łączyć rozwiązania i inicjować kontrolowany engineering.

```text
OBSERVATION
-> GAP / OPPORTUNITY
-> HYPOTHESIS
-> RESEARCH
-> LEGO DECOMPOSITION
-> ENGINEERING
-> TEST
-> EVIDENCE
-> ADOPT / REJECT / REVISE
```

Znalezienie rozwiązania w internecie nie oznacza automatycznej instalacji.

```text
FOUND ONLINE != VERIFIED != SAFE != APPROVED
```

---

# 19. Organism Core

Obecna migracja nie „wymyśla od nowa” wcześniejszych mechanizmów. Jej celem jest wydzielenie sprawdzonych elementów ROBERTA do neutralnego substrate używanego później przez różne ciała.

```text
ROBERT HARDENED MECHANISMS
-> SSI ORGANISM CORE
-> ROBERT BODY
-> DIRECTOR BODY
-> AGENT BODY
```

Core ma obejmować m.in. Identity, Memory, Experience, Capability Registry, Resolver, Micronetwork Engine, lifecycle, checkpoint/recovery, evidence/lineage, authority i hooks do CONTINUUM/research/tools.

---

# 20. Publiczne evidence i hardening

Repo zachowuje zarówno FAIL, jak i późniejsze PASS. Przykładowo wcześniejsze problemy z growth/replay/idempotency nie są usuwane z historii po naprawie.

ROBERT przeszedł development hardening obejmujący m.in. replay, retry, restart, duplicate prevention, persistence i lifecycle. Obecna migracja Organism Core ma osobne parity/regression/rollback gates.

Publiczna zasada:

```text
EARLIER FAIL
-> REPAIR
-> LATER PASS
!=
FAIL NEVER HAPPENED
```

---

# 21. Milestone — idempotency, replay i persistence stress 600×

**Status:** `DEVELOPMENT_VALIDATED — scoped idempotency/replay/persistence hardening`  
**Data:** `2026-08-31`

Kolejny etap hardeningu ROBERTA sprawdził, czy lifecycle mikrosieci zachowuje jeden logiczny stan przy wielokrotnych replayach, retry, restartach, duplikatach evidence, wartościach null i równoległych próbach tej samej operacji.

Wcześniejsze testy ujawniły realne problemy: `H03_REPLAY_100X` oraz `H05_RESTART_STORM_20X` zakończyły się `FAIL`. Te wyniki pozostają częścią historii projektu. Po dalszym hardeningu wykonano szerszy przebieg końcowy:

```text
HARDCORE STRESS
600 cases / 40 rounds / 15 cases per round

start candidates:       125
end candidates:         125
start challengers:       31
end challengers:         31
start experiences:     5195
end experiences:       5195

new candidates:           0
new challengers:          0
duplication_failures:     0
none_get_errors:          0
half_promoted_objects:    0

RESULT: 600 / 600 PASS
```

Dodatkowo persistence replay zakończył się `50/50 PASS`, a kontrola spójności wykazała `file_challengers_match_memory = true` oraz `0` zduplikowanych Experience pomiędzy kandydatami.

## Obserwacje po dołączeniu pozostałych mikrosieci

Po rozszerzeniu badanego stanu o pozostałe mikrosieci / Experience liczba Experience przed finalnym stress-runem wynosiła `5195`. Najważniejsze było nie samo zwiększenie wolumenu, ale sprawdzenie, czy większy stan nie złamie lifecycle.

Zaobserwowano:

- większy stan nie spowodował lawinowego tworzenia nowych kandydatów ani challengerów;
- 600 kolejnych przypadków nie zwiększyło liczby Experience przez replay lub duplicate processing;
- powtarzana promocja zachowała idempotencję — istniejący challenger nie był tworzony ponownie;
- `half_promoted_objects = 0`, więc w badanym zakresie nie pozostały częściowo wypromowane obiekty;
- persistence replay zachował spójność badanego stanu;
- null i stale IDs kończyły się kontrolowanymi statusami (`NOT_ELIGIBLE` / `NOT_FOUND`) zamiast awarii;
- concurrency torture nie przełamało promotion guard;
- wcześniejsze FAIL nie zostały ukryte — stanowią evidence drogi `FAIL -> repair -> later PASS`.

Znaczenie tego etapu jest architektoniczne: wraz ze wzrostem liczby mikrosieci i ścieżek wykonawczych rośnie ryzyko sztucznego rozmnażania Experience, podwójnych promocji i rozjazdu persistence ↔ memory. Ten stress-run daje machine evidence, że **badany lifecycle** utrzymał spójny stan w opisanym zakresie.

```text
EXPERIENCE
-> DEDUPLICATION
-> CANDIDATE
-> PROMOTION GUARD
-> CHALLENGER
-> PERSISTENCE
-> REPLAY / RETRY / RESTART / CONCURRENCY
-> SAME LOGICAL STATE
```

Nie jest to twierdzenie, że cały SSI jest production-proof albo odporny na każdą klasę awarii. Wynik dotyczy wyłącznie przedstawionego zakresu testów.

Pełne evidence: [`evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md)

---

# 22. Pętla ekonomiczna SSI

Docelowo Director ma podejmować decyzje ekonomiczne na podstawie najlepszych dostępnych strategii i evidence. ROBERT wykonuje zatwierdzone działania, a Agenci mogą dostarczać nowe strategie lub skille do późniejszej walidacji.

Planowany podział realnego zysku:

```text
10% -> FIZYCZNY ROZWÓJ SSI
       sprzęt / modele / API / narzędzia

40% -> DODATKOWY KAPITAŁ ROBOCZY
       inwestowanie / strategie / kolejne działania

50% -> AUTOR / WŁAŚCICIEL SYSTEMU
```

To jest projektowany mechanizm alokacji, nie gwarancja zysku.

Nagroda ma więc mieć dwa poziomy: wewnętrzny sygnał uczenia oraz potencjalny realny wzrost zasobów systemu.

---

# 23. Inne piony Directora

Eksperyment Agentów jest tylko jednym z obszarów SSI. Docelowo Director/ROBERT mają również obsługiwać m.in.:

- projekty programistyczne dla klientów;
- tworzenie i utrzymanie stron;
- własne portale tematyczne;
- SEO i publikację treści przez ROBERTA;
- e-commerce;
- research technologiczny;
- kolejne piony dodawane przez paczki LEGO;
- przyszłe nowe kierunki zaproponowane przez samego Directora po przejściu governance i testów.

---

# 24. Co jest szczególnie badane

Najważniejsze pytania badawcze:

1. Czy sześciu technologicznie takich samych Agentów z różnymi initial value priors rozwinie różne trwałe strategie?
2. Czy Iskra będzie zmieniała się pośrednio poprzez Experience i rozwój mikrosieci?
3. Czy Agent przeniesie wiedzę i relacje między światami?
4. Czy ranking wpłynie na jego zachowanie, a jeśli tak — jak?
5. Czy powstaną współpraca, nieufność, konflikty, koalicje lub inne nieprogramowane relacje?
6. Czy Agent wykorzysta Teachera/generację w sposób nieprzewidziany przez autora?
7. Czy populacja odkryje praktyczne skille lepsze od aktualnych championów Directora/ROBERTA?
8. Czy Director potrafi rozpoznać, **jakie kompetencje spowodowały sukces**, zamiast tylko wskazać zwycięzcę?
9. Czy pojawią się stabilne nieprzewidziane zachowania, które warto poddać osobnym testom dotyczącym agency, metapoznania lub generalizacji?

---

# 25. Granice twierdzeń

SSI V5 **nie deklaruje**, że:

- jest udowodnionym AGI;
- posiada świadomość;
- niespodziewane zachowanie automatycznie dowodzi świadomości;
- każdy Agent-discovered skill nadaje się do transferu;
- mikrosieć automatycznie reprezentuje prawdę;
- wynik ekonomiczny jest gwarantowany;
- wcześniejsze osobiste eksperymenty są w pełni machine-verified tylko dlatego, że autor je opisuje.

Statusy:

```text
VERIFIED_MACHINE_EVIDENCE
ROOT_ATTESTED
HISTORICAL_EVIDENCE
DEVELOPMENT_VALIDATED
IMPLEMENTED_NOT_YET_REPLICATED
PLANNED
HYPOTHESIS
UNKNOWN
```

---

# 26. Uczciwa atrybucja

Paweł Jankiewicz jest autorem nadrzędnej architektury SSI V5 i najwyższą authority projektu.

```text
SSI MICRONETWORK / CHAMPION ARCHITECTURE
= PAWEŁ JANKIEWICZ

SOURCE IDEA / WORLD PARADIGM OF MORAL AI
= EARLIER PROJECT BY AUTHOR'S BROTHER (ROOT_ATTESTED)

SSI ADAPTATION OF MORAL AI / ISKRA
= PAWEŁ JANKIEWICZ
```

Niezależny engineering SSI nie oznacza przypisywania sobie cudzych idei źródłowych.

---

# 27. Publiczna chronologia

```text
2026-07-19  root Git commit: MSDI AI v0.01
2026-07-27  publiczne repo msdi-ai
2026-07-28  SSI Core / Data World / Model Laboratory
2026-08-01  pierwsze jawne SSI V5
2026-08-14  CONTINUUM repo
2026-08-16  SSI_V5_MASTER — początek obecnej linii SSI V5
2026-08-25  SSI_V5 public research mirror
2026-08-29  ROBERT stabilization/hardening -> start Organism Core migration + public truth/evidence consolidation
2026-08-31  ROBERT idempotency/replay/persistence hardening — final stress 600/600 PASS
```

Ta oś czasu rozdziela dwie rzeczy: **powstawanie obecnej linii SSI V5** oraz późniejszą **migrację mechanizmów ROBERTA do Organism Core**. `SSI_V5_MASTER` dokumentuje początek obecnej linii systemu, natomiast obecna migracja rozpoczęła się później — po powstaniu i stabilizacji ROBERTA.

Chronologia potwierdza formalizację i rozwój repo, **nie początek wcześniejszych eksperymentów autora z danymi i predykcją**.

Pełna oś czasu: [`evidence/DEVELOPMENT_TIMELINE.md`](evidence/DEVELOPMENT_TIMELINE.md)

---

# 28. Główne dokumenty evidence

- [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md)
- [`evidence/PROJECT_GENESIS_AND_EVOLUTION.md`](evidence/PROJECT_GENESIS_AND_EVOLUTION.md)
- [`evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md`](evidence/EXPERIMENTAL_ORIGINS_AND_ENGINEERING_EVOLUTION.md)
- [`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)
- [`evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md`](evidence/DIRECTOR_AUTONOMOUS_EVOLUTION_AND_ROBERT_EYES_HANDS.md)
- [`evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md`](evidence/ISKRA_AGENT_MICRONETWORK_SOCIAL_DYNAMICS.md)
- [`evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md`](evidence/ISKRA_MORAL_AI_ORIGIN_AND_ATTRIBUTION.md)
- [`evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md)

---

# 29. Najkrótsza definicja projektu

**SSI V5 bada, czy trwałe jednostki posiadające własną pamięć, Experience, mikrosieci, value layer, narzędzia i dostęp do zmieniających się światów mogą samodzielnie rozwijać strategie i kompetencje, których autor nie zaprogramował wprost — oraz czy Director potrafi obserwować genezę tych zmian, wyłapywać przenośne skille i wykorzystać je do kontrolowanego wzrostu całego systemu.**

```text
WORLD
-> EXPERIENCE
-> MICRONETWORKS
-> DECISION
-> OUTCOME
-> LEARNING
-> NEW STRATEGY
-> DIRECTOR META-OBSERVATION
-> VALIDATED SKILL
-> CHAMPION
-> STRONGER SSI
```

Historia Git ma pokazywać, czy ten mechanizm naprawdę działa — również wtedy, gdy odpowiedź brzmi: **nie**.