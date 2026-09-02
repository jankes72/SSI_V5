# SSI V5 — Micronetwork Migration & Repair Lineage

**Status publiczny:** `PRE-CLOSURE / FINAL CONTRACT TEST PENDING`  
**Data:** `2026-09-02`  
**Zakres:** `ROBERT micronetworks + V10 routing + M00–M09 integration`  
**Charakter:** publiczny zapis badawczo-inżynieryjny; pełne raw evidence pozostaje w lokalnym/private SSI Evidence Storage.

> Ten dokument celowo nie ogłasza jeszcze `MICRONETWORK_MIGRATION_CLOSED = TRUE`. Ostatni test doprecyzowujący kontrakt metryki Test3 jest wykonywany oddzielnie i zostanie dopisany po uzyskaniu jednoznacznego machine evidence.

---

## 1. Dlaczego ten zapis istnieje

Celem nie jest pokazanie wyłącznie końcowego PASS. Celem jest zachowanie pełnego engineering lineage:

```text
STAN POCZĄTKOWY
-> EKSPERYMENT
-> WYKRYTA NIESPÓJNOŚĆ
-> MACHINE EVIDENCE
-> DIAGNOZA
-> NAPRAWA
-> RETEST
-> REGRESJA
-> FINALNY TEST KONTRAKTU
-> DOPIERO POTEM CLOSURE
```

Ten sam zapis ma dwie funkcje:

1. **dla grantodawcy / recenzenta** — pozwala ocenić, czy projekt zachowuje błędy, root cause, poprawki i retesty zamiast publikować tylko korzystny wynik;
2. **dla przyszłego Directora / SSI Self-Model** — stanowi pamięć inżynierską wyjaśniającą, dlaczego dany mechanizm istnieje i jakie warunki muszą zostać zachowane przy późniejszym controlled self-development.

---

## 2. Rozdzielenie źródeł evidence

W lokalnym ROBERCIE istnieją dwie celowo rozdzielone warstwy evidence:

```text
EVIDENCE/
= HISTORYCZNE / BEFORE
= nie jest nadpisywane po naprawie


evidence/
= REPAIR / AFTER / CLOSURE CANDIDATE
= aktualne testy naprawcze i regresyjne
```

To rozdzielenie jest metodologicznie istotne. Późniejszy PASS nie kasuje wcześniejszego failure ani błędnego kontraktu testowego.

Publiczny GitHub jest mirror-em badawczym, dlatego przechowuje przede wszystkim opis, indeksy i claim boundaries; pełne lokalne JSON/JSONL/logi mogą pozostawać poza publicznym repo.

---

## 3. BEFORE — co wykazało historyczne evidence

Historyczne Test3A/Test3B w `EVIDENCE/` pokazały ważny problem metodologiczny: **status wykonania `PASS` nie gwarantował jeszcze zgodności `expected_route` z `actual_route`**.

To oznaczało, że poprzedni test mógł potwierdzić zakończenie wykonania, ale nie udowadniał wystarczająco mocno poprawności decyzji routingu V10.

W konsekwencji wcześniejszy wynik nie został usunięty ani przepisany. Został zachowany jako:

```text
HISTORICAL_EVIDENCE
-> ujawnia słabszy kontrakt testowy
-> uzasadnia naprawę
-> staje się częścią lineage
```

To jest ważny element falsyfikowalności projektu: test, który okazuje się zbyt słaby, nie jest retrospektywnie przedstawiany jako wystarczający.

---

## 4. DIAGNOZA — główne klasy problemów

Audyt naprawczy wskazał kilka powiązanych problemów:

- Router V10 nie stosował w pełni wymaganych progów `min_confidence_for_reuse` i `min_success_ratio_for_reuse`;
- `REUSE_TOP1` wymagał mocniejszego capability gate i dowodu realnego wykonania mikrosieci;
- runtime nie inicjalizował i nie wywoływał pełnego `V10LearningFlow`;
- przepływ M00–M09 wymagał jawnego bridge/callsite evidence;
- `robert/micronetworks.py` nie powinien utrzymywać równoległego silnika względem canonical core;
- domena techniczna `test` nie powinna wejść do production selection;
- `CHAMPION` bez wykonywalnych wag nie powinien pozostać aktywnym Championem;
- interface auth wymagał fail-closed zamiast fail-open;
- IdentityManager wymagał bezpieczniejszego concurrent write / atomic update;
- systemd i testy zawierały stare ścieżki ROBERTA;
- kontrakt Test3 musiał weryfikować correctness routingu, background failures i real execution, nie tylko końcowy status.

---

## 5. REPAIR — co zmieniono

Naprawa objęła m.in.:

### V10 Router

- realne użycie progów samples / confidence / success ratio;
- capability lookup przed `REUSE_TOP1`;
- eskalację do full flow, gdy bramka nie jest spełniona;
- target capability seeding i warmup tylko dla wykonywalnych capability.

### ROBERT Runtime

- przekazywanie progów i capability lookup do V10;
- inicjalizację `V10LearningFlow`;
- rejestrację outcome w learning flow;
- spięcie feedbacku z V10 flow;
- realne wykonanie mikrosieci dla reuse zamiast samego skrótu kontrolnego.

### Canonical Micronetwork Engine

- `robert/micronetworks.py` został sprowadzony do cienkiego adaptera/re-exportu canonical core;
- `CHAMPION` bez wag jest degradowany do stanu niewykonywalnego;
- domena `test` jest filtrowana z produkcyjnego `advise`.

### Security / persistence / concurrency

- interface auth działa fail-closed;
- IdentityManager używa unikalnego tempfile, lockingu i atomic replace;
- systemd wskazuje kanoniczny katalog ROBERTA.

### Test contract

Test3 został przebudowany tak, aby rozliczać:

- expected route vs actual route;
- capability gate;
- threshold boundary;
- real execution;
- background failures;
- pełne accounting 600/600.

---

## 6. AFTER — główny wynik naprawionego Test3

Końcowy raport naprawczy dla pojedynczego kanonicznego przebiegu Test3 podał:

```text
total:                    600
accounted:                600
reuse_valid:              227
escalated_and_resolved:   260
full_flow_resolved:       113
failed:                     0
incorrect_routing:          0
background_failures:        0
exceptions:                 0
global_success_ratio:     1.0
PASS:                    True
```

Progi zastosowane przez router:

```text
min_samples_for_reuse      = 3
min_confidence_for_reuse   = 0.7
min_success_ratio_for_reuse= 0.8
```

Boundary tests potwierdziły zasadę:

```text
THRESHOLDS PASS + EXECUTABLE CAPABILITY
-> REUSE_TOP1

ANY REQUIRED GATE FAILS
-> ESCALATE_FULL_FLOW
```

---

## 7. M00–M09 — przepływ warstw

Raport naprawczy oznaczył wszystkie warstwy M00–M09 jako podłączone w badanym flow:

```text
M00 Store
M01 Experience Store
M02 Experience Graph
M03 Lifecycle
M04 Factory
M05 Pattern
M06 Semantic
M07 Safe Routing
M08 Self-Improvement
M09 Persistence
```

Ważnym celem dodatkowego audytu było również ograniczenie ryzyka powstania drugiego, bocznego stanu uczenia. Finalny closure wymaga, aby compatibility bridge nie stał się niezależnym drugim organizmem z własną konkurencyjną prawdą stanu.

---

## 8. Dodatkowe testy naprawcze

W bieżącym zestawie evidence odnotowano również:

- fail-closed auth: brak / pusty / błędny token -> deny;
- concurrency IdentityManager: `400/400` zapisów bez wyjątku i z poprawnym finalnym JSON;
- SQLite integrity dla głównych baz;
- lifecycle transitions;
- poprawione ścieżki systemd;
- test restart/recovery;
- regresję A01–A20;
- powtarzane Test3 jako osobny test stabilności.

Te wyniki są częścią lokalnego `evidence/`. Publiczny mirror nie powinien jednak podnosić statusu do finalnego closure przed zakończeniem ostatniego audytu kontraktu Test3.

---

## 9. Ostatnia wykryta niespójność — dlaczego closure jeszcze czeka

Przy audycie powtarzanego Test3 wykryto, że pole nazwane `failed` pojawiało się w małej liczbie przebiegów mimo jednoczesnego oznaczenia całego runu jako PASS.

Nie wolno rozstrzygnąć tego przez samo przemianowanie pola ani przez osłabienie kryterium PASS.

Ostatni test ma ustalić na podstawie raw evidence i kodu, czy `failed` oznacza:

1. **rzeczywisty unresolved failure** — wtedy test/implementacja wymagają naprawy i pełnego retestu;
2. **stan pośredni, który następnie został prawidłowo rozwiązany przez eskalację** — wtedy trzeba poprawić kontrakt metryk i rozdzielić np. `initial_path_failed` od `unresolved_failures`.

Dlatego obecny status publiczny brzmi:

```text
REPAIR IMPLEMENTED
MAJOR RETESTS PASS
FINAL TEST3 METRIC-CONTRACT CLARIFICATION = PENDING
MICRONETWORK_MIGRATION_CLOSED = NOT YET CLAIMED PUBLICLY
```

Po zakończeniu tego testu do dokumentu zostanie dopisana nowa sekcja z ostatecznym wynikiem i jednoznacznym closure verdict.

---

## 10. Dlaczego ten case jest istotny dla grantodawcy

Ten przypadek pokazuje nie tylko funkcję routera. Pokazuje metodę pracy projektu:

```text
PASS NIE KOŃCZY AUDYTU
-> SPRAWDŹ, CO PASS NAPRAWDĘ MIERZY
-> ZACHOWAJ STARE EVIDENCE
-> WYKRYJ NIESPÓJNOŚĆ
-> NAPRAW ROOT CAUSE
-> ZAOSTRZ KONTRAKT TESTU
-> POWTÓRZ TEST
-> SPRAWDŹ PERSISTENCE / RESTART / CONCURRENCY
-> DOPIERO POTEM ZAMKNIJ ETAP
```

Dla oceny grantu wartością jest możliwość prześledzenia drogi od słabszego testu do mocniejszego kontraktu, a nie sam efektowny końcowy numer.

---

## 11. Dlaczego ten case jest istotny dla Directora

Ten sam zapis powinien być częścią przyszłej pamięci engineeringowej SSI.

Director powinien móc zrekonstruować:

```text
DLACZEGO COMPONENT ISTNIEJE
-> JAKI PROBLEM MIAŁ ROZWIĄZAĆ
-> JAK WCZEŚNIEJSZY TEST BYŁ ZA SŁABY
-> JAKIE EVIDENCE UJAWNIŁO BŁĄD
-> JAK ZMIENIONO ARCHITEKTURĘ
-> JAK ZAOSTRZONO TEST
-> JAKIE INVARIANTY MUSZĄ POZOSTAĆ
-> JAKIE WARUNKI MUSZĄ BYĆ SPEŁNIONE PRZED KOLEJNĄ MODYFIKACJĄ
```

To jest podstawa dla przyszłego **supervised self-build / controlled self-development**, a nie pozwolenie na nieograniczoną samomodyfikację.

Inwarianty pozostają nadrzędne:

```text
ROOT = HIGHEST AUTHORITY
KNOWLEDGE != AUTHORITY
CAPABILITY != AUTHORITY
MODEL OUTPUT != AUTHORITY
```

Wiedza o własnej historii konstrukcji może poprawiać hipotezy engineeringowe Directora, ale nie daje mu automatycznie prawa do wdrożenia zmiany do canonical runtime bez wymaganej authority, testów i evidence.

---

## 12. Engineering lesson schema dla przyszłego SSI

Z tego przypadku można zachować ogólny wzorzec:

```text
OBSERVED SUCCESS
-> CHECK WHETHER SUCCESS METRIC IS STRONG ENOUGH

CONFLICTING EVIDENCE
-> PRESERVE CONFLICT
-> DO NOT RETROACTIVELY ERASE OLD RESULT

ROOT CAUSE FOUND
-> CHANGE CANONICAL PATH, NOT CREATE PARALLEL ARCHITECTURE

REPAIR
-> TEST BOUNDARIES
-> TEST REAL EXECUTION
-> TEST PERSISTENCE
-> TEST RESTART
-> TEST CONCURRENCY

METRIC AMBIGUITY
-> RESOLVE SEMANTICS FROM RAW EVIDENCE
-> DO NOT LOWER PASS CRITERIA

ONLY THEN
-> CLOSURE
```

To jest rodzaj wiedzy, którą CEPA / Engineering Memory / Director Self-Model może w przyszłości wykorzystywać do tworzenia lepszych propozycji napraw i rozwoju.

---

## 13. Evidence lineage — prywatne/local pointers

Najważniejsze lokalne artefakty tego etapu obejmują m.in.:

```text
EVIDENCE/
  R03_REPORT.md
  R03_POST_IMPORT_MATRIX_20260901.txt
  R09_FEASIBILITY.json
  R09_FREEZE_MANIFEST.json
  TEST3A_EVIDENCE_20260901/
  TEST3B_EVIDENCE_20260901/


evidence/
  micronetwork_full_stack_experiment/
  FINAL_REPAIR_REPORT.md
  TEST3_REPEAT_100X.*
  RUNTIME_RESTART_20X.*
  REGRESSION_A01_A20.*
  V10_CANONICAL_STATE_TEST.*
  TEST3_FAILED_FIELD_AUDIT.*   # po zakończeniu ostatniego audytu
```

Nazwy te są provenance pointers. Nie wszystkie pliki raw muszą być publikowane w publicznym mirrorze.

---

## 14. Warunek przyszłego finalnego closure

Ostatnia aktualizacja tego case study powinna dopiero wtedy zmienić status na finalny, gdy machine evidence jednoznacznie potwierdzi m.in.:

```text
TEST3_REPEAT = 100/100 PASS
accounted = 600/600 per run
unresolved_failures_total = 0
incorrect_routing_total = 0
background_failures_total = 0
exceptions_total = 0
RESTART = 20/20 PASS
A01-A20 = PASS
parallel_runtime_state = FALSE
parallel_micronetwork_engine = FALSE
parallel_v10_learning_state = FALSE
open_blockers = []
```

Dopiero wtedy publiczny wpis może zostać uzupełniony o:

```text
MICRONETWORK_MIGRATION_CLOSED = TRUE
MICRONETWORK_CANONICAL = TRUE
FINAL_PASS = TRUE
```

**Ten finalny test i wynik zostaną dopisane po zakończeniu obecnej korekty Kilo.**
