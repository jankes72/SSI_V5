# SSI V5 — Public Evidence Index

Ten katalog zawiera publiczne artefakty evidence dla najważniejszych etapów przed T0.

Zasada: README opisuje hipotezy, architekturę i interpretację; pliki w `evidence/` mają pokazywać surowe lub możliwie bezpośrednie wyniki maszynowe, root cause, hashe, snapshoty oraz instrukcje reprodukcji.

## Dostępne zestawy

### `robert_600x/`
Evidence dla naprawy i stress-testu idempotency/replay/restart ROBERTA przed migracją do neutralnego core.

Zawiera:
- finalny wynik 600X;
- root cause duplikacji i `NoneType.get`;
- raw torture results dla promotion/replay/retry/restart/null/concurrency;
- snapshoty stanu BEFORE/AFTER;
- jawnie zachowaną rozbieżność `5 vs 6 challengers`.

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

## Ograniczenia

Publiczny evidence mirror nie zawiera sekretów, API keys, tokenów, prywatnych danych ani pełnego prywatnego runtime. Publikowane artefakty mają umożliwiać kontrolę twierdzeń bez ujawniania wrażliwych danych.

## Reguła metodologiczna

```text
CLAIM
-> PUBLIC EVIDENCE POINTER
-> REPRODUCTION / CHECK
-> RESULT
```

Jeżeli evidence jest niepełne albo zawiera niespójność, jest to zapisywane jawnie zamiast wygładzane retrospektywnie.
