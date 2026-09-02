# SSI V5 — Public Evidence Index

Ten katalog zawiera publiczne artefakty evidence dla najważniejszych etapów przed T0.

Zasada: README opisuje hipotezy, architekturę i interpretację; pliki w `evidence/` mają pokazywać surowe lub możliwie bezpośrednie wyniki maszynowe, root cause, hashe, snapshoty oraz instrukcje reprodukcji.

## Micronetwork migration / repair lineage — PRE-CLOSURE

Nowy zapis badawczo-inżynieryjny:

[`MICRONETWORK_MIGRATION_REPAIR_LINEAGE_PRE_CLOSURE_20260902.md`](MICRONETWORK_MIGRATION_REPAIR_LINEAGE_PRE_CLOSURE_20260902.md)

Dokument opisuje pełny przebieg:

```text
BEFORE / HISTORICAL EVIDENCE
-> słabszy kontrakt Test3 i wykryta niezgodność routingu
-> DIAGNOSIS
-> REPAIR
-> V10 / runtime / M00-M09 / lifecycle / persistence / security fixes
-> RETEST
-> repeated Test3 / restart / regression / canonical-state checks
-> FINAL TEST3 METRIC-CONTRACT AUDIT (PENDING)
-> dopiero potem FINAL CLOSURE
```

Status jest celowo `PRE-CLOSURE`. Ostatni test doprecyzowujący znaczenie pola `failed` w powtarzanym Test3 nie został jeszcze wpisany jako zakończony. Po jego wykonaniu lineage zostanie uzupełniony o finalny machine-evidence verdict zamiast retrospektywnego wygładzania wcześniejszych wyników.

Ten case jest jednocześnie:

- materiałem dla grantodawcy / recenzenta pokazującym drogę `failure -> diagnosis -> repair -> retest`;
- engineering memory dla przyszłego Directora / CEPA, aby system mógł rozumieć genezę swoich komponentów i tworzyć lepsze propozycje controlled self-development bez uzyskiwania automatycznej authority do samodzielnego wdrażania zmian.

---

## Kanoniczna interpretacja V10 przed czytaniem wyników

Test 3 nie powinien być interpretowany wyłącznie jako "router zrobił to około 2× szybciej".

V10 jest projektowany jako **stateful predictive competence & recovery router**:

```text
CURRENT STATE
+ VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ CONFIDENCE
-> ROUTE / STRATEGY DECISION
```

Jego pełna rola obejmuje więc nie tylko reuse/verify/full-flow, ale także wykorzystanie historii wykonania do unikania ślepego powtarzania znanej nieskutecznej ścieżki.

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE
+ SAME STRATEGY
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

Obecny Test 3 mierzy tylko część tej funkcji: exact/similarity routing, selektywne reuse/verify, route compilation, latency i correctness w kontrolowanym known subset. Dedykowany benchmark anti-loop/recovery pozostaje do wykonania.

Pełna definicja: [`../V10_PREDICTIVE_ROUTING.md`](../V10_PREDICTIVE_ROUTING.md).

## Dostępne zestawy

### `robert_600x/`
Evidence dla naprawy i stress-testu idempotency/replay/restart ROBERTA przed migracją do neutralnego core.

Zawiera:
- finalny wynik 600X;
- root cause duplikacji i `NoneType.get`;
- raw torture results dla promotion/replay/retry/restart/null/concurrency;
- snapshoty stanu BEFORE/AFTER;
- jawnie zachowaną rozbieżność `5 vs 6 challengers`.

Te wcześniejsze replay/retry/restart testy są istotne również dla przyszłego anti-loop V10, ponieważ historia failure i outcome musi przetrwać na tyle długo, aby wpływać na kolejną decyzję zamiast znikać po restarcie.

### `ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`
Drugi etap 600X — pełniejszy przepływ rozszerzonej mikrosieci i lifecycle na większym stanie Experience.

Cel tego etapu nie był czysto wydajnościowy. Test 2 miał przede wszystkim wykazać, że szersza ścieżka lifecycle rzeczywiście działa jako całość: candidate/challenger, persistence, replay, retry, restart, concurrency i spójność stanu.

Wynik:
- `600/600 PASS`;
- `126.65 s`;
- `5195 Experience` przed i po finalnym stress-runie;
- `0` duplication failures;
- `0` half-promoted objects.

### `ROBERT_V10_HYBRID_ROUTER_TEST3_20260901.md`
Trzeci etap — kompletny układ mikrosieci z adaptacyjnym routingiem V10.

Test 3 zachowuje tę samą główną geometrię porównania (`600 / 40 / 15`), ale dodaje szybki routing do znanych tras i selektywną weryfikację zamiast uruchamiania pełnego flow dla każdego przypadku.

Wynik:
- `600/600 PASS`;
- `57.61 s`;
- `534 × REUSE_TOP1`;
- `66 × VERIFY_TOPK`;
- `0 × FULL_FLOW` w tym konkretnym przebiegu;
- `0` fallbacków;
- `100/100` correctness dla kontrolowanej części znanych przypadków.

Porównanie trzech etapów:

```text
TEST 1 — wcześniejszy / lżejszy flow:        67.85 s
TEST 2 — pełny rozszerzony flow:             126.65 s
TEST 3 — pełny układ + adaptacyjny routing:   57.61 s
```

Interpretacja metodologiczna:

```text
TEST 1
-> pokazanie wcześniejszego, lżejszego przebiegu

TEST 2
-> dowód, że pełny rozszerzony przepływ istnieje i zachowuje spójność

TEST 3
-> dowód, że po dodaniu V10 system może dla rozpoznanych przypadków korzystać z krótszych tras bez utraty zmierzonej poprawności
```

**Ważne:** ostatni punkt nie jest pełną definicją V10. Stateful anti-loop/recovery wymaga osobnego testu z powtarzanymi failure signatures, alternatywnymi trasami, zmianą kompozycji LEGO oraz persistence historii błędu po restarcie.

Raw evidence Testu 3 znajduje się w `evidence/router_v10_test3/`.

### `organism_core_m00_micronetworks/`
Evidence pierwszej kontrolowanej migracji Micronetwork Engine z ROBERTA do neutralnego `SSI ORGANISM CORE`.

Zawiera:
- final verdict;
- state hashes BEFORE/AFTER;
- state separation proof;
- rollback proof;
- zasady reprodukcji/parity.

### `PRE_T0_LAYERED_SELF_DEVELOPMENT_AND_INFRASTRUCTURE_PROTOCOL_20260830.md`
Protokół porządkujący aktualny eksperyment warstwowy ROBERTA i kolejne porównania PRE-T0.

Opisuje:
- baseline uproszczonego ROBERTA;
- pomiar czasu, błędów, retry, model switching, LEGO rebuilds i checkpoint returns;
- śledzenie skilli, mikrosieci oraz `candidate -> challenger -> champion`;
- porównania `baseline -> kolejna capability layer -> ponowny pomiar`;
- Hello World i Tetris jako kontrolowane zadania wykonawcze;
- Eyes/Hands jako osobny eksperyment wymagający własnego machine evidence;
- Technology Memory / External Technology Knowledge Store;
- uczenie wzorców samorozwoju przez LEGO i champion lifecycle;
- rolę Tailscale jako warstwy przenośności między lokalnymi węzłami i przyszłymi serwerami;
- drogę `single execution -> multi-worker -> multi-CONTINUUM -> distributed infrastructure`;
- ekonomiczny wzrost realnych capability SSI poprzez compute, storage i infrastrukturę;
- granicę między publicznym evidence a prywatną implementacją.

Tetris jest szczególnie użyteczny jako przyszły demonstrator V10, ponieważ pozwala osobno obserwować:

```text
BUILD / REPAIR
-> LEGO COMPOSITION
-> FAILURE
-> RECOVERY ROUTING
-> RETEST
```

oraz później:

```text
PLAY
-> BOARD STATE
-> COMPETENCE SELECTION
-> ACTION
-> OUTCOME
-> NEXT DECISION
```

## Ograniczenia

Publiczny evidence mirror nie zawiera sekretów, API keys, tokenów, prywatnych danych ani pełnego prywatnego runtime. Publikowane artefakty mają umożliwiać kontrolę twierdzeń bez ujawniania wrażliwych danych.

Publiczne evidence nie powinno być używane do twierdzenia, że pełny anti-loop V10 jest już uniwersalnie udowodniony. Jest to aktualnie kontrakt architektoniczny wspierany częściowym evidence, który wymaga dedykowanego benchmarku recovery.

## Reguła metodologiczna

```text
CLAIM
-> PUBLIC EVIDENCE POINTER
-> REPRODUCTION / CHECK
-> RESULT
```

Jeżeli evidence jest niepełne albo zawiera niespójność, jest to zapisywane jawnie zamiast wygładzane retrospektywnie.
