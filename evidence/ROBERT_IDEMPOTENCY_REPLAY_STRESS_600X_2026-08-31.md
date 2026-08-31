# ROBERT — Idempotency, Replay & Persistence Stress Validation (600×)

**Data walidacji:** 2026-08-31  
**Zakres:** ROBERT / micronetwork lifecycle / candidate → challenger / Experience persistence  
**Status końcowy:** `DEVELOPMENT_VALIDATED`  
**Źródło:** lokalny bundle `SSI_ROBERT_IDEMPOTENCY_REPLAY_STRESS_600X_BUNDLE`  

## Cel etapu

Celem etapu było sprawdzenie, czy lifecycle ROBERTA zachowuje jeden spójny stan przy wielokrotnych replayach, retry, restartach, duplikatach evidence, wartościach null oraz równoległych próbach wykonania tej samej operacji.

Badanie dotyczyło przede wszystkim własności operacyjnych systemu, a nie jakości odpowiedzi modelu LLM:

```text
SAME EVENT / SAME EXPERIENCE / SAME PROMOTION
-> RETRY
-> REPLAY
-> RESTART
-> CONCURRENCY
-> PERSISTENCE
-> SAME CONSISTENT STATE
```

## Stan wejściowy

Pierwszy zapis baseline zawierał:

```text
candidate files:     125
challengers:          31
experiences:        4761
```

Przed właściwym finalnym stress-runem liczba Experience wzrosła do `5195`, przy zachowaniu `125` kandydatów i `31` challengerów.

Według opisu autora wzrost ten nastąpił po dołączeniu pozostałych mikrosieci / Experience do badanego stanu (`ROOT_ATTESTED`). Liczby wejściowe i końcowe są natomiast zapisane w machine-generated evidence bundle.

## Wcześniejsze FAIL są zachowane

Etap nie usuwa wcześniejszych niepowodzeń z historii.

### H03 — replay 100×

```text
attempts:   100
added:        0
duplicate:  100
pass:      false
```

### H05 — restart storm 20×

```text
cycles:                  20
all_candidates_match: false
all_challengers_match: true
all_experiences_match: false
all_replay_ok:          true
pass:                  false
```

Te wyniki są istotne badawczo: pokazują, że późniejszy PASS nie jest deklaracją opartą wyłącznie na jednym pozytywnym przebiegu, ale następuje po wcześniej wykrytych problemach replay/restart consistency.

## Testy częściowe, które przeszły

### H02 — promotion 100×

```text
attempts:                    100
new_challenger_results:        0
already_challenger_results:  100
pass:                       true
```

### H04 — retry storm 100×

```text
attempts:                 100
any_new_challenger:     false
all_promotions_idempotent: true
pass:                    true
```

### H07 — duplicate evidence guard

```text
tested:        10
all_duplicate: true
pass:          true
```

### H08 — null contract torture

Przetestowano m.in. `null_evidence`, brak context, stale candidate ID i stale challenger ID. Wszystkie cztery przypadki zakończyły się kontrolowanym statusem zamiast awarią.

### H09 — concurrency torture

```text
threads:              3
attempts_per_thread: 20
errors:               0
all_idempotent:     true
pass:               true
```

## Finalny HARDCORE 600×

Końcowy test wykonał `600` przypadków w `40` rundach po `15` przypadków.

```text
cases_total:              600
rounds:                    40
cases_per_round:           15
duration_seconds:      126.65

start candidates:         125
start challengers:         31
start experiences:       5195

end candidates:           125
end challengers:           31
end experiences:         5195

new candidates:             0
new challengers:            0
duplication_failures:       0
none_get_errors:            0
half_promoted_objects:      0

PASS:                    true
```

## Persistence replay

Dodatkowy test trwałości wykonał `50` przypadków replay:

```text
replay_cases:   50
all_replay_ok: true
pass:          true
```

## Spójność raportu i stanu

Końcowa kontrola wykazała:

```text
final_candidates:                         125
final_challengers:                         31
final_experiences:                       5195
duplicate_experiences_across_candidates:    0
file_challengers_match_memory:           true
duplication_failures:                       0
none_get_errors:                            0
pass:                                    true
```

## Obserwacje po dołączeniu pozostałych mikrosieci

Najważniejszą obserwacją nie jest sama liczba `600/600`, lecz zachowanie systemu po zwiększeniu rzeczywistego stanu Experience.

1. **Większy stan nie spowodował lawinowego wzrostu obiektów lifecycle.** Finalny stress-run rozpoczął i zakończył się z dokładnie `125` kandydatami i `31` challengerami.

2. **Replay nie wygenerował wtórnych Experience.** Po 600 przypadkach liczba Experience pozostała `5195`, a raport końcowy wykazał `0` duplikatów pomiędzy kandydatami.

3. **Promotion zachowała idempotencję.** Powtarzanie promocji istniejącego obiektu nie tworzyło kolejnych challengerów.

4. **Nie pojawiły się obiekty częściowo wypromowane.** `half_promoted_objects = 0` jest ważne, ponieważ brak duplikatu nie wystarcza, jeżeli system może pozostawić niespójny stan pośredni.

5. **Warstwa persistence i stan pamięci pozostały zgodne w badanym zakresie.** `file_challengers_match_memory = true`, a 50/50 persistence replay zakończyło się PASS.

6. **Null/stale inputs zostały obsłużone kontraktowo.** Zamiast wyjątku pojawiały się kontrolowane statusy `NOT_ELIGIBLE` albo `NOT_FOUND`.

7. **Concurrency nie złamało promotion guard.** W teście wielowątkowym nie zanotowano błędów ani konkurencyjnego utworzenia nowego challengera.

8. **Wcześniejsze FAIL pozostają częścią evidence.** H03 i H05 pokazują, że replay/restart consistency wymagały realnego hardeningu; finalny PASS powinien być interpretowany jako wynik późniejszego, szerszego testu, nie jako stwierdzenie, że wcześniejsze problemy nigdy nie istniały.

## Znaczenie architektoniczne

Ten etap wzmacnia tezę, że mikrosieć w SSI nie jest tylko kolekcją wyników modelu, ale częścią trwałego lifecycle, w którym powtarzalne zdarzenia powinny prowadzić do tego samego logicznego stanu.

```text
EXPERIENCE
-> DEDUPLICATION
-> CANDIDATE
-> PROMOTION GUARD
-> CHALLENGER
-> PERSISTENCE
-> REPLAY / RETRY / RESTART
-> SAME LOGICAL STATE
```

Jest to istotne przed dalszym rozszerzaniem liczby mikrosieci, Agent Body i autonomicznych wykonawców, ponieważ bez idempotencji każda dodatkowa ścieżka wykonawcza zwiększałaby ryzyko sztucznego wzrostu Experience, podwójnych promocji i rozjazdu pamięć ↔ pliki.

## Granice wyniku

Ten etap **nie dowodzi**, że cały SSI jest odporny na wszystkie możliwe awarie ani że system jest production-proof.

Wynik oznacza wyłącznie, że badany lifecycle ROBERTA przeszedł opisany zestaw stress/replay/persistence tests w przedstawionym stanie i zakresie.

```text
600/600 PASS
!=
ALL POSSIBLE FAILURES ELIMINATED
```

Status tego etapu powinien więc być interpretowany jako:

**`DEVELOPMENT_VALIDATED — scoped idempotency/replay/persistence hardening`**.
