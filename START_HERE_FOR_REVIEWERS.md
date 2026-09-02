# SSI V5 — Start Here for Grant and Technical Reviewers

Jeżeli oceniasz SSI V5 jako grantodawca, sponsor, badacz lub niezależny recenzent techniczny, zacznij od poniższych materiałów zamiast próbować czytać całe repozytorium od początku.

## Najnowszy zamknięty etap: TEST 4 — ROOT Terminal / Authority / Recovery

**Status:** `DEVELOPMENT_VALIDATED / ROOT_TERMINAL_MIGRATION_CLOSED`  
**Data zamknięcia:** `2026-09-02`

Najlepszy punkt wejścia:

[`evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md`](evidence/TEST4_ROOT_TERMINAL_AUTHORITY_E2E_RECOVERY_20260902.md)

Finalny machine-readable closure:

[`evidence/TEST4_ROOT_TERMINAL_FINAL_CLOSURE_20260902.json`](evidence/TEST4_ROOT_TERMINAL_FINAL_CLOSURE_20260902.json)

Najważniejszy wynik:

```text
final regression = 461/461 PASS
authority boundary = PASS
full pipeline E2E = 1000/1000 PASS
concurrency = 1000 commands / 20 workers PASS
real process restart = 20/20 PASS
physical receipts = 2000 for 1000 commands
receipt duplicates = 0
receipt orphans = 0
receipt missing = 0
open_blockers = []

ROOT_TERMINAL_MIGRATION_CLOSED = TRUE
ROOT_TERMINAL_CANONICAL = TRUE
FINAL_PASS = TRUE
```

TEST 4 jest szczególnie istotny metodologicznie, ponieważ pierwszy closure-candidate nie został przyjęty wyłącznie na podstawie raportu PASS. Audyt evidence wykrył słabsze lub niejednoznaczne dowody dla authentication boundary, concurrency, process restart i receipt accounting. Kontrakt został zaostrzony, brakujące punkty poprawiono lub doprecyzowano, a następnie wykonano retesty aż do `FINAL_CLOSURE_V4`.

Granice wyniku są jawne: stress-test 1000× używa `CONTROLLED_E2E_BACKEND` do deterministycznego testowania pipeline systemowego, natomiast restart 20× używa realnego procesu ROBERTA. Kanały realtime i remote pozostają `NOT_IMPLEMENTED / OUT OF SCOPE` i nie są przedstawiane jako działające.

Prywatny kod Terminala ROOT, raw logs, lokalne ścieżki, backupy i service definitions nie są publikowane w publicznym research mirror.

## Poprzedni zamknięty etap: Micronetwork Migration / V10 Repair

**Status:** `DEVELOPMENT_VALIDATED / MICRONETWORK_MIGRATION_CLOSED`  
**Data zamknięcia:** `2026-09-02`

Najlepszy punkt wejścia do tego etapu:

[`evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md`](evidence/MICRONETWORK_MIGRATION_FINAL_LINEAGE_20260902.md)

Finalny closure report:

[`evidence/MICRONETWORK_MIGRATION_CLOSURE_REPORT_20260902.md`](evidence/MICRONETWORK_MIGRATION_CLOSURE_REPORT_20260902.md)

Publiczny agregat finalnego Test3 100×:

[`evidence/TEST3_REPEAT_100X_V2_PUBLIC_SUMMARY_20260902.json`](evidence/TEST3_REPEAT_100X_V2_PUBLIC_SUMMARY_20260902.json)

Najważniejszy wynik:

```text
100 runs × 600 cases = 60 000 cases
accounted = 60 000
failed = 0
unresolved_failures = 0
incorrect_routing = 0
background_failures = 0
exceptions = 0
restart = 20/20 PASS
A01-A20 = PASS
open_blockers = []
```

Istotne metodologicznie: wcześniejszy test powtarzalności miał błąd w formule PASS, ponieważ `failed > 0` nie blokowało wyniku PASS. Projekt zachował ten błędny wynik jako historyczne evidence, poprawił kontrakt o `failed == 0` i wykonał pełne 100× ponownie od początku. Dopiero drugi przebieg stał się podstawą zamknięcia migracji.

Prywatny kod ROBERTA/V10, backupy implementacji i service definitions nie są publikowane w publicznym research mirror.

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

Zmierzony speedup historycznego Testu 3 jest ważny, ale jest **efektem jednej części mechanizmu**, nie pełną definicją V10.

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
- współpracę z dynamiczną kompozycją LEGO.

Dodatkowe pytania i odpowiedzi:

[`V10_PREDICTIVE_ROUTING_FAQ.md`](V10_PREDICTIVE_ROUTING_FAQ.md)

## 3. Evidence index

[`evidence/README.md`](evidence/README.md)

## 4. Pełny stress-test lifecycle / persistence

[`evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`](evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md)

## 5. Historyczny V10 Hybrid Router — Test 3

[`evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md`](evidence/ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md)

Ten wynik należy czytać jako historyczny etap przed późniejszym hardeningiem kontraktu Test3 i finalnym migration-closure z 2026-09-02.

## 6. Jak interpretować sekwencję testów

```text
TEST 1
wcześniejszy / lżejszy przepływ

-> TEST 2
pełniejszy przepływ mikrosieci i lifecycle

-> TEST 3
pełna architektura eksperymentalna + V10 routing

-> MIGRATION REPAIR / CONTRACT AUDIT
wykrycie słabego PASS condition

-> TEST3 100x v2
poprawiony kontrakt + 60 000 przypadków

-> MICRONETWORK MIGRATION CLOSED

-> TEST 4 ROOT TERMINAL
migration / authority / full E2E / concurrency / real process restart

-> EVIDENCE AUDIT / HARDENING
pierwszy closure-candidate odrzucony jako niewystarczająco udowodniony

-> FINAL CLOSURE V4
ROOT TERMINAL MIGRATION CLOSED
```

Test 2 nie był próbą uzyskania najlepszego czasu. Jego rolą było dostarczenie evidence, że szerszy przepływ, lifecycle, persistence, replay/restart i related mechanisms działają przed wprowadzeniem selektywnego routingu.

Późniejsze migration-closure oraz TEST 4 pokazują dodatkowo, że sam status PASS nie wystarcza: trzeba audytować również to, **co dokładnie warunek PASS mierzy i czy evidence rzeczywiście dowodzi deklarowanego zachowania**.

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
-> RETEST
-> CURRENT CLAIM BOUNDARY
```

Krytyka metodologiczna, nieudane replikacje i wskazanie słabych punktów są mile widziane.