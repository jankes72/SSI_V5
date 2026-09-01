# V10 Stateful Predictive Competence & Recovery Router — Reviewer FAQ

## Czy V10 jest tylko routerem lub cache'em?

Nie. V10 jest projektowany jako **stanowy, predykcyjny router kompetencji i recovery**. Oprócz similarity i confidence uwzględnia znaczenie historii prób, wcześniejszych outcomes oraz znanych failure signatures przy wyborze kolejnej ścieżki działania.

```text
CURRENT STATE
+ AVAILABLE VERIFIED COMPETENCE
+ ATTEMPT HISTORY
+ PRIOR OUTCOMES / FAILURES
-> V10
-> REUSE / VERIFY / ALTERNATIVE / FULL_FLOW
```

Exact-cache jest tylko jedną z możliwych ścieżek.

## Co dokładnie przewiduje V10?

Na poziomie architektonicznym V10 estymuje nie tylko dopasowanie istniejącej kompetencji do aktualnego problemu, ale również to, **czy dana ścieżka nadal ma sens w kontekście historii wykonania**.

Wynikiem decyzji może być:

- `REUSE_TOP1`;
- `VERIFY_TOPK`;
- wybór alternatywnej kompetencji lub kompozycji LEGO;
- zablokowanie ślepego retry znanej nieskutecznej ścieżki;
- `FULL_FLOW` dla unknown/conflict/low-confidence.

## Dlaczego historia prób jest ważna?

W zadaniach wieloetapowych samo podobieństwo wejścia jest niewystarczające. System powinien wiedzieć, że dana strategia była już użyta w porównywalnym stanie i jaki przyniosła rezultat.

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

To jest podstawowa idea anti-loop w V10.

## Co oznacza anti-loop?

Anti-loop oznacza, że system ma nie kręcić się w kółko przez wykonywanie tej samej nieskutecznej strategii bez nowej informacji.

Po wykryciu powtarzającego się negatywnego outcome V10 powinien rozważyć:

```text
BLOCK SAME ROUTE
OR
MODIFY PARAMETERS / LEGO COMPOSITION
OR
SELECT ALTERNATIVE CHAMPION
OR
VERIFY TOP-K
OR
ESCALATE TO FULL_FLOW
```

To odróżnia rolę V10 od prostego mechanizmu "znajdź podobne i użyj ponownie".

## Jak V10 współpracuje z LEGO?

LEGO rozkłada duży problem na małe klocki. V10 pomaga zdecydować, które sprawdzone klocki można ponownie użyć, które należy zmienić oraz kiedy dotychczasowa kompozycja prowadzi do powtarzającego się błędu.

```text
GOAL
-> LEGO BLOCKS
-> EXECUTION
-> TEST
-> FAILURE
-> HISTORY / OUTCOME
-> V10
-> REUSE GOOD BLOCKS
-> REPLACE / RECONFIGURE BAD PATH
-> RETEST
```

## Dlaczego Tetris jest dobrym przykładem?

Bo pozwala pokazać dwie różne warstwy działania.

Najpierw ROBERT może budować i naprawiać Tetrisa:

```text
BUILD -> TEST -> FAILURE -> DIAGNOSIS -> ROUTE CHANGE -> RETEST
```

Później ROBERT może sam grać:

```text
BOARD STATE -> PERCEPTION -> COMPETENCE SELECTION -> ACTION -> OUTCOME -> NEXT STATE
```

Jeżeli określona strategia w porównywalnym stanie wielokrotnie daje zły rezultat, wcześniejszy outcome powinien wpływać na następną decyzję.

## Czy główną zaletą V10 jest szybkość?

Nie. Szybkość jest ważnym efektem ubocznym poprawnego reuse.

Główne znaczenie V10 jest szersze:

```text
FAST ACCESS
+ SAFE REUSE
+ HISTORY-AWARE DECISION
+ FAILURE-AWARE RECOVERY
+ ANTI-LOOP
```

Test 3 pokazał `57.61 s` wobec `126.65 s` Testu 2 w danym zakresie, ale redukowanie V10 do tego wyniku byłoby niepełnym opisem architektury.

## Jakie publiczne evidence jest już dostępne?

Test 3 zarejestrował:

```text
lookups:             600
cache_exact_hits:    100
similarity_hits:     434
route_compilations:  133
REUSE_TOP1:          534
VERIFY_TOPK:          66
fallback_count:        0
errors:                0
known correctness: 100/100
```

Wcześniejsze stress-testy lifecycle obejmowały również replay, retry, restart, concurrency, persistence i idempotency.

## Czy publiczne testy udowodniły już pełny anti-loop?

Nie. To ważna granica twierdzeń.

Obecne evidence wspiera routing, replay/persistence hardening i selektywne reuse/verify, ale dedykowany benchmark musi jeszcze celowo wywoływać:

- ten sam failure signature;
- podobny state;
- powtarzaną nieskuteczną strategię;
- alternatywną ścieżkę recovery;
- restart i ponowną próbę po restarcie.

Dopiero wtedy można ilościowo raportować skuteczność anti-loop.

## Jakie metryki są właściwe dla V10?

Nie tylko latency.

Najważniejsze przyszłe metryki to:

- false-reuse rate;
- false-escalation rate;
- routing precision/recall;
- confidence calibration;
- repeated-failure suppression rate;
- blind-retry rate;
- recovery success rate;
- alternative-route selection rate;
- persistence of failure history;
- final task correctness;
- time/cost saved versus canonical full flow.

## Najkrótsza odpowiedź dla recenzenta

**V10 nie jest tylko szybszym routerem. Jest warstwą decyzji nad trwałą kompetencją: wykorzystuje stan, confidence, historię prób i outcomes, aby zdecydować co ponownie użyć, co zweryfikować, czego nie powtarzać oraz kiedy zmienić strategię lub wrócić do pełnego flow.**

Publiczna dokumentacja opisuje tę funkcję bez ujawniania prywatnego kodu V10 ani pełnego silnika mikrosieci.
