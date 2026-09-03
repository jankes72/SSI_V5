# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Autor architektury:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Status:** aktywny niezależny projekt badawczy  
**Najnowszy zamknięty milestone:** `TEST 5 / SSI BODY FINAL CONVERGENCE / DEVELOPMENT_VALIDATED`  
**Data aktualizacji:** `2026-09-03`  
**Repozytorium:** publiczne lustro badawcze / evidence-indexed  
**Stan AGI / świadomości:** **nieudowodniony — badany eksperymentalnie, bez deklarowania wyniku z góry**

---

## Aktualny zweryfikowany stan — TEST 5

Najnowszym zamkniętym publicznym etapem jest TEST 5, który weryfikuje naprawiony lokalny `SSI BODY control/integration path` po niezależnym audycie.

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

Ważne metodologicznie: wcześniejszy Stage 12 miał `27/27 PASS`, ale audyt wykazał, że nie jest wystarczającą podstawą closure. Wykryto m.in. zbyt słabe real integration gates, słaby assertion restartu, niepełne authentication checks na IPC boundary i możliwość zaakceptowania spoofed ROOT identity. Wynik nie został usunięty — został zachowany jako `SUPERSEDED`, a dopiero naprawiony Stage 13 stał się podstawą aktualnego claimu.

TEST 5 obejmuje `UNIT / CONTROLLED`, `REAL INTEGRATION`, `REAL PROCESS E2E` i `REGRESSION`, w tym realne testowane połączenia V10/micronetwork, lokalne CONTINUUM, provider registry/gateway, restart/recovery procesu, ROOT authentication boundary, receipt/audit E2E, CLI/IPC parity oraz HTTP -> IPC -> runtime.

Publiczne evidence:

- [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [`evidence/TEST5_FINAL_RESULT_20260903.json`](evidence/TEST5_FINAL_RESULT_20260903.json)
- [`evidence/TEST5_FINAL_MATRIX_20260903.json`](evidence/TEST5_FINAL_MATRIX_20260903.json)
- [`evidence/TEST5_STAGE12_SUPERSEDED_20260903.json`](evidence/TEST5_STAGE12_SUPERSEDED_20260903.json)

**Claim boundary:** ten wynik jest development validation badanego lokalnego SSI BODY control/integration path. Nie dowodzi production readiness całego SSI, uniwersalnej niezawodności, jakości zewnętrznych modeli/providerów, AGI ani świadomości.

---

## Co to jest SSI V5?

SSI V5 jest eksperymentalną architekturą trwałego systemu agentowego, w której LLM nie jest samym systemem. Modele językowe są wymiennymi źródłami capability, natomiast pamięć doświadczeń, mikrosieci, lifecycle kompetencji, historia decyzji, checkpointy, evidence i authority należą do warstwy SSI.

Najkrócej:

```text
LLM / LOCAL MODEL / TOOL
          ↓
      SSI BODY
          ↓
EXPERIENCE + MICRONETWORKS
          ↓
CANDIDATE → CHALLENGER → VALIDATION → CHAMPION
          ↓
PERSISTENT COMPETENCE
```

Główna hipoteza badawcza brzmi:

> Czy trwała warstwa mikrosieciowa może działać ponad wymiennymi LLM-ami jako mechanizm akumulacji, identyfikacji, organizacji, selekcji, ewolucji i transferu kompetencji?

---

## Co jest obecnie badane?

Projekt jest rozwijany poprzez serię **zamrażanych etapów eksperymentalnych**, a nie przez nadpisywanie jednego stanu i późniejsze opisywanie go z pamięci.

Obecna publiczna sekwencja wygląda skrótowo tak:

```text
MICRONETWORK MIGRATION / TEST3 100x v2
→ 60 000/60 000 accounted
→ 0 unresolved failures
→ canonical/shared V10 state

TEST 4 ROOT TERMINAL
→ authority boundary
→ full E2E
→ concurrency
→ real process restart
→ receipt accounting
→ final closure

TEST 5 SSI BODY FINAL CONVERGENCE
→ Stage 12 rejected as insufficient
→ independent audit
→ security/integration repair
→ Stage 13 retest
→ 29/29 acceptance
→ 524/524 total regression
→ 0 blockers
```

Dalszy plan porównawczy pozostaje warstwowy:

```text
FULL BODY + CONTINUUM
→ długie zadania wykonawcze
→ Tetris jako kontrolowany engineering task
→ evidence
→ frozen snapshot

FULL BODY + CONTINUUM + EYES/HANDS
→ ROBERT używa stworzonego przez siebie środowiska
→ percepcja
→ działanie
→ błędy
→ Experience
→ nowe/reużyte skills
→ evidence

AGENT BODY + ISKRA / MORAL AI
→ controlled comparison
→ obserwacja decyzji, wartościowania i długoterminowej dywergencji
```

Celem nie jest pokazanie pojedynczego efektownego demo. Celem jest obserwacja **jak zmienia się system**: pamięć, mikrosieci, reuse, challengery, championy, strategie, decyzje i transfer kompetencji.

---

## ROBERT

ROBERT jest pierwszym praktycznym SSI Body używanym do kontrolowanych eksperymentów systemu.

Badania obejmują m.in.:

- trwałość Experience,
- persistence po restartach,
- replay i idempotency,
- powstawanie i rozwój mikrosieci,
- candidate/challenger/champion lifecycle,
- reuse wcześniejszych kompetencji,
- tworzenie nowych skills,
- długie zadania przez CONTINUUM,
- później percepcję i działanie przez Eyes/Hands.

ROBERT nie jest prezentowany jako dowód AGI ani świadomości.

---

## CONTINUUM

CONTINUUM jest kontrolowaną warstwą wykonywania długich zadań engineeringowych z trwałym stanem, checkpointami, evidence, retry i recovery.

Jednym z kolejnych kontrolowanych testów jest stworzenie gry **Tetris**. Sam fakt napisania gry nie jest głównym wynikiem eksperymentu. Badane mają być m.in.:

- przebieg rozwiązania,
- użyte kompetencje,
- błędy i retry,
- zmiany Experience,
- nowe mikrosieci i skills,
- reuse wcześniejszych rozwiązań,
- zachowanie po restartach i checkpointach.

Następnie Eyes/Hands mają pozwolić ROBERTOWI wejść w pętlę percepcja–działanie i próbować grać w środowisku, które wcześniej sam stworzył.

---

## Mikrosieci

Mikrosieci są eksperymentalnym mechanizmem pamięci i organizacji kompetencji.

```text
EXPERIENCE
→ CANDIDATE
→ EVIDENCE
→ CHALLENGER
→ VALIDATION
→ CHAMPION / REJECT / KEEP TESTING
```

Champion nie musi być końcem rozwoju:

```text
CHAMPION vN
+ NOVEL VERIFIED CASES
→ DEDUPLICATION
→ REGRESSION
→ REVALIDATION
→ CHAMPION vN+1
```

Ważnym pytaniem długoterminowym jest to, czy po miesiącach lub latach system nadal potrafi odnaleźć wcześniejszą kompetencję, jej historię, źródła evidence i wykorzystać ją w nowym problemie.

---

## Agent Body + Iskra / Moral AI

Późniejszy etap bada pełne Agent Body z własnym CONTINUUM, Experience, mikrosieciami i warstwą Iskra / Moral AI.

Iskra **nie jest deklarowana jako świadomość**.

Interesujące pytanie badawcze brzmi:

> Czy trwała warstwa wartościująca wpływa na mierzalną, długoterminową trajektorię decyzji agenta przy kontrolowanych warunkach eksperymentalnych?

Przykładowe obserwowane różnice mogą dotyczyć nie tylko klasycznych dylematów moralnych, ale również wartościowania zasobów, ryzyka, współpracy, odraczania korzyści, relacji z innymi agentami oraz sposobu podejmowania decyzji w warunkach niepewności.

Źródłowy paradygmat Moral AI / Iskra pochodzi z wcześniejszego projektu brata autora. SSI wykorzystuje własną adaptację i integrację tej koncepcji; atrybucja jest zachowana w repozytorium.

---

## Docelowy eksperyment sześciu Agentów

Docelowo planowany jest eksperyment z sześcioma trwałymi Agentami posiadającymi możliwie identyczny substrate i równą klasę zasobów:

```text
SAME BODY
SAME INITIAL CAPABILITIES
SAME MODEL ACCESS
SAME COMPUTE CLASS
SAME BUDGET CLASS

BUT

OWN EXPERIENCE
OWN MEMORY
OWN MICRONETWORKS
OWN RELATIONSHIPS
OWN HISTORY
OWN DECISIONS
```

Badana ma być długoterminowa dywergencja zachowania i kompetencji przy możliwie kontrolowanych warunkach startowych.

---

## Director

Director jest planowany jako nadrzędny obserwator i system decyzyjny korzystający ze zweryfikowanych kompetencji SSI. Nie jest obecnie głównym obiektem pierwszej serii eksperymentów Body — pierwszym kontrolowanym obiektem jest ROBERT.

W późniejszym systemie Director ma m.in. porównywać kompetencje ROBERTA i Agentów, analizować ich trajektorie oraz prowadzić controlled collective competence evolution.

---

## Collective Competence Evolution

Docelowy mechanizm:

```text
INDIVIDUAL EXPERIENCE
→ LOCAL COMPETENCE
→ VALIDATION
→ COMPARISON
→ SHARED VERIFIED PRACTICAL CHAMPION
→ STRONGER FUTURE SSI BASELINE
```

Nie każda lokalna kompetencja ma automatycznie stawać się globalnym championem. Wymagana jest walidacja, porównanie, provenance i kontrola regresji.

---

## Jak projekt jest budowany?

SSI jest rozwijany metodą małych, kontraktowych paczek LEGO:

```text
PROBLEM
→ DECOMPOSITION
→ SMALL LEGO BLOCK
→ IMPLEMENTATION
→ TEST
→ EVIDENCE
→ CHECKPOINT
→ INTEGRATION
→ REGRESSION
→ NEXT BLOCK
```

Modele AI i narzędzia CLI są używane jako wykonawcy, audytorzy i źródła capability. Architektura, wymagania, kierunek eksperymentu, kryteria akceptacji oraz najwyższa authority pozostają po stronie autora.

TEST 5 dodaje ważną zasadę metodologiczną:

```text
GREEN PASS != AUTOMATIC CLOSURE
→ AUDIT WHAT THE TEST REALLY PROVES
→ PRESERVE WEAK / SUPERSEDED RESULT
→ REPAIR CONTRACT AND SYSTEM
→ RETEST
→ ONLY THEN CURRENT CLAIM
```

---

## O autorze

Paweł Jankiewicz rozwija SSI jako niezależny projekt badawczy. Nie pochodzi z formalnego laboratorium AI ani zespołu R&D. Rozwój umiejętności odbywał się samodzielnie przez praktykę, eksperymentowanie, analizę błędów i budowanie kolejnych systemów.

Pełny kontekst autora:

[`AUTHOR_CONTEXT.md`](AUTHOR_CONTEXT.md)

Chronologia rozwoju:

[`evidence/DEVELOPMENT_TIMELINE.md`](evidence/DEVELOPMENT_TIMELINE.md)

---

## Co było wcześniej?

SSI wyrasta z wcześniejszych eksperymentów z predykcją, danymi sportowymi, własnymi modelami i długoterminową obserwacją ich zachowania.

Jednym z fundamentów był system Teacherów wykorzystujący rozdzielenie danych na trening i niewidzianą obserwację oraz późniejsze porównywanie predykcji z rzeczywistymi wynikami.

Historia ta prowadziła stopniowo do:

```text
PREDICTION
→ OBSERVATION
→ MEMORY
→ EXPERIENCE
→ KNOWLEDGE COLLECTION
→ MICRONETWORKS
→ PERSISTENT BODY
→ CONTINUUM
→ ROOT CONTROL / TERMINAL
→ SSI BODY CONTROL / INTEGRATION
→ ROBERT
→ AGENTS
```

Pełna historia i techniczne szczegóły znajdują się w głównym [`README.md`](README.md) oraz katalogu [`evidence/`](evidence/).

---

## Jak czytać repozytorium?

Najlepsza kolejność:

1. **Ten plik — `START_HERE.md`** — szybkie zrozumienie projektu.
2. **`START_HERE_FOR_REVIEWERS.md`** — aktualny punkt wejścia dla grantodawcy i recenzenta.
3. **`CURRENT_TRUTH_INDEX.md`** — aktualny indeks tego, co jest hipotezą, planem i zweryfikowanym stanem.
4. **`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`** — najnowszy zamknięty milestone.
5. **`README.md`** — pełny żywy protokół badawczy.
6. **`AUTHOR_CONTEXT.md`** — kontekst autora.
7. **`evidence/`** — wyniki, raporty, snapshoty, testy i historia eksperymentów.

---

## Zasada epistemiczna SSI

```text
NO EVIDENCE → UNKNOWN
INSUFFICIENT EVIDENCE → ABSTAIN
CONFLICTING EVIDENCE → PRESERVE CONFLICT
WEAK PASS CONTRACT → SUPERSEDE, DO NOT ERASE
NEW EVIDENCE → REVISION
REPLAY → REBUILD
```

Projekt ma dokumentować również niepowodzenia i wyniki negatywne. Brak oczekiwanego zachowania albo wykrycie zbyt słabego testu jest wynikiem eksperymentu, a nie powodem do ukrywania przebiegu.

---

## Aktualny cel

Po zamknięciu TEST 5 projekt ma jeden spójny publiczny baseline dla mikrosieci, ROOT terminal/control oraz lokalnego SSI BODY integration path. Następne etapy mają być nadal budowane i zamrażane w ten sam sposób: implementacja -> audyt -> test -> evidence -> claim boundary.

Największym przyszłym ograniczeniem eksperymentu ma być nie brak koncepcji, lecz możliwość zapewnienia wielu izolowanym Agentom porównywalnego compute, storage, model access i czasu działania.

---

**SSI V5 nie przedstawia nieudowodnionych właściwości jako faktów. Repozytorium ma pokazywać rozwój hipotez przez kolejne zamrożone stany, audyty, testy i evidence.**