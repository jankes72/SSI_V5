# SSI V5 — Start Here for Grant and Technical Reviewers

Jeżeli oceniasz SSI V5 jako grantodawca, sponsor, badacz lub niezależny recenzent techniczny, zacznij od poniższych materiałów zamiast próbować czytać całe repozytorium od początku.

## Najważniejsza rzecz do zrozumienia o V10

V10 **nie jest przede wszystkim mechanizmem przyspieszającym**. Jest projektowany jako **stateful predictive competence & recovery router**.

Jego zadaniem jest łączyć:

```text
CURRENT TASK / WORLD STATE
+ VERIFIED MICRONETWORK COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
-> NEXT ROUTE / STRATEGY
```

Dlatego system ma nie tylko znajdować znaną kompetencję, ale również rozpoznawać, że dana ścieżka już zawiodła i nie powinna być ślepo powtarzana bez nowego evidence.

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE
+ SAME STRATEGY
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

Możliwa reakcja to reuse poprawnych klocków, zmiana kompozycji LEGO, wybór alternatywnego Championa, dodatkowa weryfikacja albo canonical `FULL_FLOW`.

Zmierzony speedup Testu 3 jest ważny, ale jest **efektem jednej części mechanizmu**, nie pełną definicją V10.

## 1. Najczęstsze pytania i odpowiedzi

[`GRANT_REVIEWER_FAQ.md`](GRANT_REVIEWER_FAQ.md)

FAQ odpowiada m.in. na pytania:

- co dokładnie jest badane w SSI V5;
- czym mikrosieci różnią się od RAG, cache i zwykłej pamięci agenta;
- dlaczego V10 nie powinien być interpretowany wyłącznie jako cache lub speed optimization;
- jak V10 wykorzystuje state, attempt history, outcomes i failure signatures;
- czym jest anti-loop / recovery i dlaczego system nie powinien powtarzać tej samej nieskutecznej strategii;
- czym jest zbiorowa inteligencja i jak nowe evidence może wzbogacać Championów;
- dlaczego mikrosieci są wielozadaniowe i wieloprzestrzeniowe;
- jak mogą dynamicznie powstawać nowe gałęzie kompetencji;
- jak działa `Experience -> Candidate -> Challenger -> Champion`;
- co dzieje się przy błędnym Championie / false reuse;
- czym są CONTINUUM i LEGO;
- jak działa metodologia dekompozycji, migracji, testów, regresji i rekonstrukcji publicznego eksperymentu;
- dlaczego Test 2 był potrzebny przed Testem 3;
- jakie są ograniczenia obecnych wyników i co mogłoby sfalsyfikować hipotezę SSI.

## 2. V10 — stateful predictive competence & recovery routing

[`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)

Ten dokument definiuje V10 jako warstwę predykcyjnego i stanowego wyboru kompetencji oraz recovery. Obejmuje:

- predictive matching;
- confidence gating;
- `REUSE_TOP1`, `VERIFY_TOPK`, alternatives i `FULL_FLOW`;
- attempt/outcome history;
- failure-aware routing;
- anti-loop;
- recovery decision;
- feedback / route compilation;
- współpracę z dynamiczną kompozycją LEGO;
- przykład `BUILD TETRIS -> TEST -> FAILURE -> CHANGE ROUTE -> RETEST` oraz późniejsze `ROBERT PLAYS -> ACTION -> OUTCOME -> NEXT DECISION`.

Dodatkowe pytania i odpowiedzi:

[`V10_PREDICTIVE_ROUTING_FAQ.md`](V10_PREDICTIVE_ROUTING_FAQ.md)

## 3. Evidence index

[`evidence/README.md`](evidence/README.md)

## 4. Pełny stress-test lifecycle / persistence

[`evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md)

## 5. V10 Hybrid Router — Test 3

[`evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md`](evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md)

Raw summary:

[`evidence/router_v10_test3/H_TEST3_RESULTS.json`](evidence/router_v10_test3/H_TEST3_RESULTS.json)

## 6. Jak interpretować sekwencję testów

```text
TEST 1
wcześniejszy / lżejszy przepływ

-> TEST 2
pełniejszy przepływ mikrosieci i lifecycle

-> TEST 3
pełna architektura eksperymentalna + V10 routing
```

Test 2 nie był próbą uzyskania najlepszego czasu. Jego rolą było dostarczenie evidence, że szerszy przepływ, lifecycle, persistence, replay/restart i related mechanisms faktycznie działają przed wprowadzeniem selektywnego routingu.

Test 3 badał, czy system może następnie używać zweryfikowanych krótszych ścieżek dla znanych przypadków bez mierzalnego spadku poprawności w kontrolowanym zakresie.

Nie należy jednak redukować znaczenia V10 do tej optymalizacji. Docelowa funkcja routingu obejmuje również **stan zadania, historię wykonania, outcomes, failure signatures i recovery**, tak aby system mógł zmienić strategię zamiast mechanicznie wracać do znanej, ale nieskutecznej ścieżki.

Obecny Test 3 pokazuje działanie exact/similarity routing i selektywnej weryfikacji, ale dedykowany test anti-loop powinien jeszcze celowo wymuszać repeated failures, alternative routes, restart i persistence historii błędu.

## 7. Ważne ograniczenie interpretacyjne

SSI V5 jest eksperymentalnym systemem badawczym. Aktualne wyniki nie stanowią dowodu AGI, świadomości, uniwersalnej poprawności ani produkcyjnej gotowości.

Celem repozytorium jest budowanie możliwie audytowalnego łańcucha:

```text
HYPOTHESIS
-> IMPLEMENTATION
-> FAILURE
-> ROOT CAUSE
-> FIX
-> TEST
-> EVIDENCE
-> NEXT HYPOTHESIS
```

Krytyka metodologiczna, nieudane replikacje i wskazanie słabych punktów są mile widziane.
