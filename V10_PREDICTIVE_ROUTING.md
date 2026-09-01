# V10 — Stateful Predictive Competence & Recovery Router

## Status

`DEVELOPMENT_VALIDATED — scoped adaptive-routing / replay / persistence evidence; dedicated anti-loop and adversarial validation still required`

## Najważniejsza definicja

V10 nie jest projektowany jako zwykły cache, prosty semantic router ani tylko optymalizacja czasu. Jego podstawową rolą jest **stanowy wybór dalszej strategii działania** na podstawie bieżącego problemu, istniejących kompetencji, historii prób, wcześniejszych outcomes, failure signatures i poziomu confidence.

Najkrócej:

```text
V10
= PREDICTIVE COMPETENCE ACCESS
+ STATE / HISTORY AWARENESS
+ CONFIDENCE GATING
+ FAILURE-AWARE ROUTING
+ ANTI-LOOP / RECOVERY DECISION
+ FEEDBACK-DRIVEN ROUTE UPDATE
```

Przyspieszenie może być skutkiem poprawnego reuse zwalidowanej kompetencji, ale **nie jest nadrzędnym znaczeniem V10**.

## Dlaczego V10 powstał

W długim zadaniu wykonawczym — np. podczas budowy programu z klocków LEGO, naprawy artefaktu albo późniejszej pracy ROBERTA w środowisku takim jak Tetris — samo znalezienie "podobnej odpowiedzi" nie wystarcza.

System musi rozróżnić m.in.:

- co już zostało wykonane;
- jaka strategia została użyta;
- który klocek / Champion / route był już próbowany;
- jaki był outcome;
- czy wystąpił ten sam failure signature;
- czy ponowienie tej samej ścieżki ma sens;
- czy trzeba wybrać inną kompetencję, inny układ LEGO, dodatkową weryfikację albo pełny flow.

Dlatego routing jest rozumiany szerzej:

```text
ROUTING
!= INPUT SIMILARITY ONLY

ROUTING
= INPUT / TASK STATE
+ HISTORY OF ATTEMPTS
+ PRIOR OUTCOMES
+ FAILURE SIGNATURES
+ AVAILABLE VERIFIED COMPETENCE
+ CURRENT CONFIDENCE
+ RECOVERY OPTIONS
```

## Rdzeń decyzji

Uproszczony kontrakt V10:

```text
CURRENT INPUT / STATE
+ MICRONETWORKS / CHAMPIONS
+ ATTEMPT HISTORY
+ OUTCOMES / FAILURES
        |
        v
V10 STATEFUL PREDICTIVE ROUTING
        |
        +-> HIGH CONFIDENCE + VALID HISTORY
        |      -> REUSE_TOP1
        |
        +-> MEDIUM / AMBIGUOUS
        |      -> VERIFY_TOPK
        |
        +-> REPEATED FAILURE / NEGATIVE OUTCOME
        |      -> BLOCK BLIND RETRY
        |      -> MODIFY ROUTE / SELECT ALTERNATIVE / ESCALATE
        |
        +-> LOW / UNKNOWN / CONFLICT
               -> CANONICAL FULL_FLOW
```

Exact lookup i similarity są tylko częścią tego procesu.

## Anti-loop: nie powtarzać tego samego błędu i oczekiwać innego rezultatu

Jednym z podstawowych wymagań V10 jest ograniczanie bezsensownego zapętlenia wykonania.

Kontrakt architektoniczny można zapisać jako:

```text
SAME / EQUIVALENT STATE
+ SAME FAILURE SIGNATURE
+ SAME STRATEGY / ROUTE
+ NO NEW EVIDENCE

=> DO NOT BLINDLY REPEAT
```

Zamiast tego system powinien przejść do co najmniej jednej z kontrolowanych reakcji:

```text
BLOCK SAME ROUTE
OR
MODIFY PARAMETERS / LEGO COMPOSITION
OR
SELECT ALTERNATIVE CHAMPION / COMPETENCE
OR
VERIFY TOP-K
OR
ESCALATE TO FULL_FLOW
```

To jest ważniejsze niż samo skrócenie czasu odpowiedzi. Router ma pomagać systemowi **zmieniać sposób działania po niepowodzeniu**, a nie tylko szybciej wykonywać tę samą ścieżkę.

## V10 + LEGO

LEGO rozbija duże zadania na małe kontraktowe klocki. V10 ma wspierać wybór i ponowne składanie tych klocków w zależności od stanu pracy.

```text
GOAL
-> LEGO DECOMPOSITION
-> BLOCK A
-> BLOCK B
-> TEST
-> FAILURE
-> FAILURE SIGNATURE / OUTCOME
-> V10
   -> do not repeat ineffective composition blindly
   -> reuse verified block where valid
   -> replace / reconfigure weak block
   -> escalate if no safe route exists
-> RETEST
-> EXPERIENCE
```

W tym znaczeniu V10 nie jest routerem "do jednej rzeczy". Ma działać jako warstwa wyboru kompetencji i recovery w wieloetapowym procesie budowy, naprawy oraz późniejszego używania artefaktów.

## Przykład: budowa i późniejsze granie w Tetrisa

Tetris jest dobrym demonstratorem dlatego, że pozwala oddzielić dwa poziomy pracy.

### 1. ROBERT buduje / naprawia Tetrisa

```text
BUILD
-> TEST
-> FAILURE / LIMITATION
-> DIAGNOSIS
-> V10 CONSULTS HISTORY
-> REUSE GOOD BLOCKS
-> AVOID KNOWN BAD ROUTE
-> MODIFY / REPLACE BLOCK
-> RETEST
-> OUTCOME
-> EXPERIENCE
```

### 2. ROBERT później sam gra

```text
BOARD STATE
-> PERCEPTION
-> V10 / COMPETENCE SELECTION
-> ACTION
-> OUTCOME
-> EXPERIENCE
-> NEXT STATE
```

Jeżeli określona strategia w porównywalnym stanie systematycznie prowadzi do tej samej porażki, historia outcome powinna wpływać na kolejną decyzję. Celem nie jest wykonanie identycznej akcji jeszcze raz tylko dlatego, że semantycznie "pasuje".

## Mikrosieci i V10 pełnią różne role

```text
MICRONETWORK
= persistent, evolving, validated competence

CANDIDATE -> CHALLENGER -> CHAMPION
= quality / competition lifecycle

V10
= stateful predictive access
+ confidence gate
+ history / outcome-aware route selection
+ anti-loop / recovery decision
```

Wspólnie tworzą pętlę:

```text
EXPERIENCE
-> CANDIDATE
-> CHALLENGER
-> CHAMPION
-> MICRONETWORK
-> V10
-> ACTION / REUSE / VERIFY / FULL_FLOW
-> OUTCOME
-> NEW EXPERIENCE
-> ROUTE / COMPETENCE EVOLUTION
```

## Ochrona przed false reuse

Drugim głównym zagrożeniem jest `false reuse`: użycie wcześniejszej kompetencji w sytuacji, w której wygląda ona podobnie, ale nie jest właściwa.

```text
HIGH CONFIDENCE + VALID CONTEXT
-> REUSE

MEDIUM / AMBIGUOUS
-> VERIFY_TOPK

LOW / UNKNOWN / CONFLICT
-> FULL_FLOW

KNOWN NEGATIVE ROUTE IN COMPARABLE STATE
-> DO NOT BLINDLY REUSE
-> RECOVERY / ALTERNATIVE / ESCALATION
```

Dlatego bezpieczeństwo V10 obejmuje dwa różne problemy:

1. **false reuse** — użycie niewłaściwej kompetencji;
2. **failure loop** — ponowne uruchamianie tej samej nieskutecznej strategii mimo znanego negatywnego outcome.

## Evidence z Testu 3

W opublikowanym Test 3 zarejestrowano:

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

Test 3 pokazuje, że V10 nie działał wyłącznie jako exact-key cache i że selektywny routing potrafił ominąć część kosztownego full-flow w badanym zakresie.

Zmierzony czas `57.61 s` wobec `126.65 s` Testu 2 jest istotnym wynikiem wydajnościowym, ale **nie jest najważniejszą hipotezą V10**.

## Co już pokazano, a czego jeszcze nie pokazano

Publiczne evidence wspiera obecnie m.in.:

- exact + similarity routing;
- selektywne `REUSE_TOP1` i `VERIFY_TOPK`;
- route compilation;
- feedback/state growth;
- wcześniejsze replay/retry/restart/idempotency hardening w lifecycle;
- persistence i odporność na duplikację w badanym zakresie.

Nie należy natomiast jeszcze twierdzić, że publiczne testy udowodniły pełną skuteczność anti-loop w dowolnym dynamicznym zadaniu. Test 3 nie zawierał wystarczającej liczby wymuszonych `FULL_FLOW`, celowo powtarzanych failure signatures ani szerokiego zestawu unknown/conflicting/adversarial cases.

## Najważniejszy następny test: stateful anti-loop + recovery

Kolejny benchmark powinien mierzyć nie tylko szybkość i trafność routingu, ale zmianę strategii po niepowodzeniu:

```text
1. CLEAN STATE
2. TASK / WORLD STATE A
3. ROUTE / STRATEGY X
4. FAILURE SIGNATURE F
5. RECORD OUTCOME
6. SAME OR EQUIVALENT STATE A'
7. V10 SEES HISTORY F + X
8. PROVE: NO BLIND X RETRY WITHOUT NEW EVIDENCE
9. ALTERNATIVE ROUTE / MODIFIED LEGO / VERIFY / FULL_FLOW
10. RETEST
11. MEASURE RECOVERY SUCCESS
12. RESTART
13. VERIFY HISTORY PERSISTENCE
```

Równolegle powinny zostać zbadane:

```text
KNOWN                    -> REUSE_TOP1
AMBIGUOUS                -> VERIFY_TOPK
UNKNOWN                  -> FULL_FLOW
DECEPTIVELY SIMILAR      -> NO FALSE REUSE
REPEATED FAILURE         -> NO BLIND LOOP
NEW EVIDENCE AFTER FAIL  -> CONTROLLED RECONSIDERATION
```

## Metryki, które powinny być raportowane

- routing precision / recall;
- false-reuse rate;
- false-escalation rate;
- confidence calibration;
- repeated-failure suppression rate;
- blind-retry rate;
- recovery success rate;
- alternative-route selection rate;
- time / cost saved versus canonical full flow;
- final task correctness;
- persistence of failure history after restart.

## Najkrótsza definicja grantowa

**V10 jest stanowym, predykcyjnym routerem kompetencji i recovery. Jego zadaniem jest nie tylko szybko znaleźć istniejącą zwalidowaną kompetencję, ale również wykorzystać historię prób i outcomes do wyboru kolejnej ścieżki, uniknąć bezsensownego powtarzania znanej nieskutecznej strategii oraz zdecydować między reuse, weryfikacją, alternatywną kompozycją LEGO i pełnym flow.**

Publiczna dokumentacja opisuje kontrakt i evidence bez ujawniania prywatnej implementacji predyktora ani pełnego silnika mikrosieci.
