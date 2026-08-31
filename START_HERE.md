# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Autor architektury:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Status:** aktywny niezależny projekt badawczy  
**Repozytorium:** publiczne lustro badawcze / evidence-indexed  
**Stan AGI / świadomości:** **nieudowodniony — badany eksperymentalnie, bez deklarowania wyniku z góry**

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

Plan porównawczy:

```text
BODY SIMPLE
→ testy
→ evidence
→ frozen snapshot

BODY HARD / FULL MICRONETWORK STRUCTURE
→ te same lub porównywalne testy
→ evidence
→ frozen snapshot

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
→ ROBERT
→ AGENTS
```

Pełna historia i techniczne szczegóły znajdują się w głównym [`README.md`](README.md) oraz katalogu [`evidence/`](evidence/).

---

## Jak czytać repozytorium?

Najlepsza kolejność:

1. **Ten plik — `START_HERE.md`** — szybkie zrozumienie projektu.
2. **`README.md`** — pełny żywy protokół badawczy.
3. **`CURRENT_TRUTH_INDEX.md`** — aktualny indeks tego, co jest hipotezą, planem i zweryfikowanym stanem.
4. **`AUTHOR_CONTEXT.md`** — kontekst autora.
5. **`evidence/`** — wyniki, raporty, snapshoty, testy i historia eksperymentów.

---

## Zasada epistemiczna SSI

```text
NO EVIDENCE → UNKNOWN
INSUFFICIENT EVIDENCE → ABSTAIN
CONFLICTING EVIDENCE → PRESERVE CONFLICT
NEW EVIDENCE → REVISION
REPLAY → REBUILD
```

Projekt ma dokumentować również niepowodzenia i wyniki negatywne. Brak oczekiwanego zachowania jest wynikiem eksperymentu, a nie powodem do ukrywania przebiegu.

---

## Aktualny cel

Najbliższym celem jest ukończenie i zamrożenie kolejnych porównywalnych wersji SSI Body, a następnie przejście przez CONTINUUM, Tetris, Eyes/Hands i Agent Body / Iskra przed próbą skalowania do wielu równoległych, długotrwałych Agentów.

Największym przyszłym ograniczeniem eksperymentu ma być nie brak koncepcji, lecz możliwość zapewnienia wielu izolowanym Agentom porównywalnego compute, storage, model access i czasu działania.

---

**SSI V5 nie przedstawia nieudowodnionych właściwości jako faktów. Repozytorium ma pokazywać rozwój hipotez przez kolejne zamrożone stany, testy i evidence.**
