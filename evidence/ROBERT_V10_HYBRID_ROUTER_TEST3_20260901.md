# ROBERT V10 Hybrid Router — Test 3 / Adaptive Routing Validation

**Data walidacji:** 2026-09-01  
**Zakres:** ROBERT / micronetwork full stack / V10 adaptive routing  
**Status:** `DEVELOPMENT_VALIDATED — scoped adaptive routing test`  
**Tryb porównania:** 600 przypadków / 40 rund / 15 przypadków na rundę

## Dlaczego istnieją trzy testy

Te trzy przebiegi nie są trzema próbami wykonania tego samego celu wydajnościowego. Każdy etap miał inny cel eksperymentalny i dopiero razem tworzą ciąg dowodowy.

### Test 1 — uboższy / wcześniejszy przepływ

Publiczny baseline 600X:

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 67.85
PASS:             true
```

Ten etap pokazywał stabilność wcześniejszego, lżejszego przebiegu lifecycle.

### Test 2 — pełny przepływ rozszerzonej mikrosieci

Test 2 celowo uruchamiał szerszy przepływ: większy stan Experience oraz pełniejszy lifecycle candidate -> challenger -> persistence -> replay/retry/restart/concurrency.

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 126.65
start experiences: 5195
end experiences:   5195
PASS:             true
```

W tej sekwencji badawczej Test 2 należy interpretować jako **dowód istnienia i spójności pełnego przepływu**, a nie jako docelowy benchmark szybkości. Dłuższy czas względem wcześniejszej, uboższej wersji jest zgodny z wykonaniem szerszego zakresu pracy. Sam czas nie jest jedynym dowodem użycia warstw — właściwym evidence są również zachowane state counters, replay, restart, persistence, concurrency i lifecycle checks.

Test 2 był potrzebny przed routingiem: najpierw należało wykazać, że pełna ścieżka naprawdę działa, zanim system zacznie ją inteligentnie omijać dla przypadków, które nie wymagają całego flow.

### Test 3 — kompletny układ mikrosieci z V10 Hybrid Router

Test 3 zachowuje tę samą główną geometrię stress-testu:

```text
cases_total:       600
rounds:             40
cases_per_round:    15
duration_seconds: 57.61
PASS:             true
```

Routing:

```text
REUSE_TOP1:          534
VERIFY_TOPK:          66
ESCALATE_FULL_FLOW:    0
CREATE_SKILL_PATH:     0
fallback_count:        0
```

Kontrola znanych przypadków:

```text
correctness_matched:     100
correctness_total_known: 100
correctness_rate:        1.0
```

Latency foreground:

```text
p50: 20.612 ms
p95: 23.902 ms
```

V10:

```text
lookups:             600
cache_exact_hits:    100
similarity_hits:     434
route_compilations:  133
errors:                0
```

## Porównanie czasu

| Etap | 600 przypadków | Czas | Interpretacja |
|---|---:|---:|---|
| Test 1 | PASS | 67.85 s | wcześniejszy, lżejszy przepływ |
| Test 2 | PASS | 126.65 s | pełny przepływ rozszerzonej mikrosieci |
| Test 3 | PASS | 57.61 s | pełny układ z V10 i selektywnym routingiem |

Test 3 był:

- około **2.20x szybszy od Testu 2**;
- około **54.5% krótszy czasowo od Testu 2**;
- około **15.1% szybszy od Testu 1**, mimo że powstał po rozszerzeniu systemu o routing i pełniejszą strukturę.

## Co ten wynik pokazuje

W badanym zakresie wynik wspiera następujący model:

```text
INPUT
-> V10 ROUTER
-> EXACT CACHE / SIMILARITY ROUTE
-> REUSE_TOP1 albo VERIFY_TOPK
-> CANONICAL MICRONETWORK RESULT
-> FEEDBACK / ROUTE COMPILATION
```

Pełna ścieżka nadal istnieje jako część architektury, lecz dla przypadków rozpoznanych przez router nie musi być uruchamiana bez potrzeby.

Najważniejszym wynikiem nie jest sam rekord czasu, lecz jednoczesne wystąpienie:

```text
SAME TEST GEOMETRY
+ 100/100 KNOWN CORRECTNESS
+ 0 FALLBACKS
+ 534 DIRECT REUSE ROUTES
+ 66 VERIFY ROUTES
+ LOWER TOTAL DURATION
```

## Dlaczego Test 2 był konieczny

Bez Testu 2 szybszy Test 3 byłby trudny do interpretacji. Nie byłoby wiadomo, czy system rzeczywiście posiada pełny rozszerzony przepływ, czy po prostu nigdy go nie wykonuje.

Sekwencja eksperymentalna jest więc celowa:

```text
TEST 1
wcześniejszy / lżejszy przebieg

-> TEST 2
pełny przepływ rozszerzonej mikrosieci

-> TEST 3
pełny układ + dynamiczny routing
```

Test 2 pokazuje, że pełna ścieżka istnieje i zachowuje spójność. Test 3 pokazuje, że po dodaniu routera system może korzystać z krótszej ścieżki dla rozpoznanych przypadków bez utraty poprawności w badanym zakresie.

## Ważne ograniczenia

Ten wynik nie dowodzi, że V10 będzie szybszy dla każdego możliwego workloadu ani że cały SSI jest production-ready.

W szczególności:

- pomiar dotyczy konkretnego zestawu 600 przypadków i aktualnego stanu danych;
- `100/100 correctness` dotyczy kontrolowanej części znanych przypadków w tym teście;
- brak `FULL_FLOW` w tym przebiegu nie dowodzi, że pełna eskalacja nigdy nie będzie potrzebna;
- `background_stats.completed = 599` przy `submitted = 600` oznacza, że snapshot końcowy został zapisany przy jednym zadaniu tła nieoznaczonym jeszcze jako completed; nie jest to ukrywane;
- przyszłe testy powinny celowo zawierać nowe, konfliktowe i adversarial cases wymagające eskalacji.

Status powinien być interpretowany jako:

**`DEVELOPMENT_VALIDATED — adaptive routing produced a faster scoped 600-case run while preserving measured known-case correctness.`**

## Publiczne evidence

- wcześniejszy 600X: `evidence/robert_600x/HARDCORE_600X_SUMMARY.json`
- pełny Test 2: `evidence/ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_2026-08-31.md`
- Test 3 raw summary: `evidence/router_v10_test3/H_TEST3_RESULTS.json`
- Test 3 baseline snapshot: `evidence/router_v10_test3/A_BASELINE.json`

Stary beta-run V10, który wykazał błędy routingu, pozostaje częścią lokalnej historii rozwojowej, ale nie jest przedstawiany jako finalny wynik Testu 3. Jego istnienie jest istotne metodologicznie: obecny PASS nastąpił po wykryciu i naprawie realnej regresji routera, a nie jako wynik pierwszej próby.
