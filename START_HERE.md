# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Autor architektury:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Status:** `T0 BASELINE RECORDED / PRE-ISKRA / ACTIVE RESEARCH`  
**Data aktualizacji:** `2026-09-05`  
**Aktualny baseline eksperymentalny:** `T0 / BODY_FROZEN / PRE-ISKRA`  
**Najnowszy zamknięty test walidacyjny:** `TEST 5 / SSI BODY FINAL CONVERGENCE / DEVELOPMENT_VALIDATED`  
**Stan AGI / świadomości:** `NIEUDOWODNIONY — BADANY EKSPERYMENTALNIE`

## Najważniejsza aktualizacja — T0

Projekt ma już publicznie zapisany punkt startowy następnej serii eksperymentów:

[`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md)

oraz oczyszczone machine evidence:

[`evidence/BODY_FROZEN_T0_20260905/`](evidence/BODY_FROZEN_T0_20260905/)

```text
T0 = BODY_FROZEN / PRE-ISKRA
CONTINUUM = CLOSED
23/23 CONTINUUM TESTS PASS
22/22 MAIN SCENARIOS PASS
19/19 E2E CLOSURE PASS
26/26 FINAL GUARD PASS
ACTIVE FAILURES = 0
INVARIANT VIOLATIONS = 0
OPEN BLOCKERS = 0

BODY SNAPSHOT = 1781 files / 587 Python files retained privately
MICRONETWORKS = 8
MODULES = 8
LAYERS = 3
V10 = ACTIVE
```

**T0 nie jest TEST 6.** Jest zamrożonym punktem odniesienia. TEST 5 pozostaje ostatnim zamkniętym testem walidacyjnym.

## Co teraz będzie badane

```text
T0
-> T1 NO-ISKRA controlled transfer
-> T1 ISKRA variants from the same T0
-> T2 competence consolidation / promotion experiment
```

Pierwszy T1 ma być celowo bardzo kontrolowany: system dostaje przygotowany zestaw `Micronetworks + V10` jako klocki LEGO, gotową receptę, adaptery i kryteria PASS/FAIL i ma przenieść technologię do bezpiecznej cywilnej symulacji dronów. Tutaj badamy transfer według znanej recepty, nie kreatywność.

Drugi eksperyment ma zmniejszyć ilość scaffolding: podobna klasa transferu, ale bez pełnych gotowych kodów i z większą odpowiedzialnością systemu za mapowanie, implementację i testy.

Późniejszy test open-ended ma sprawdzić, czy system potrafi znaleźć nowe zastosowanie bez podania mu odpowiedzi.

## T2 — dlaczego jest ważny

T2 ma osobno sprawdzić mechanizm porównywania i konsolidacji kompetencji powstałych w niezależnych liniach.

```text
NEW SKILLS / STRATEGIES
-> EVIDENCE + BENCHMARK COMPARISON
-> DEDUPLICATION
-> CANDIDATE / CHALLENGER / CHAMPION
-> MORE CASES IF AMBIGUOUS
-> CONTROLLED PROMOTION
-> UPGRADED DESCENDANT BODY
```

Jeżeli kilka linii stworzy kompetencję równoważną, system nie powinien bezmyślnie tworzyć duplikatów. Powinien zwiększyć evidence/data coverage i prosić o dodatkowe przypadki, jeśli wynik nie pozwala uczciwie wybrać Championa.

T0 pozostaje niezmieniony jako kontrola.

## Aktualny zamknięty test — TEST 5

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

TEST 5 weryfikuje scoped local SSI BODY control/integration path. Nie dowodzi production readiness całego SSI, uniwersalnej niezawodności, AGI ani świadomości.

Evidence:

- [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md)
- [`evidence/TEST5_FINAL_RESULT_20260903.json`](evidence/TEST5_FINAL_RESULT_20260903.json)

## Czym jest SSI V5

SSI V5 bada, czy kompetencja może być utrzymywana i rozwijana przez system ponad pojedynczym modelem/promptem.

```text
MODEL / TOOL
-> EXPERIENCE
-> MICRONETWORK
-> CANDIDATE
-> CHALLENGER
-> VALIDATION
-> CHAMPION
-> V10 ROUTING
-> OUTCOME
-> HISTORY
-> NEXT DECISION
```

Modele są wymiennymi źródłami capability. Trwały stan, evidence, lifecycle kompetencji, routing, CONTINUUM i historia należą do systemu SSI.

## Role — nie mieszać

```text
BODY_FROZEN T0
= zamrożony organizm eksperymentalny / punkt startowy

AGENTS
= chodzą po światach, mają własne CONTINUUM i laboratoria,
  budują dane/metadane, strategie i kompetencje

DIRECTOR
= obserwuje, audytuje, porównuje, rankinguje i ocenia wyniki

ROBERT
= osobne ciało wykonawcze/runtime/narzędzia
```

Słabsze strategie mogą zostać odrzucone, ale ich historia pozostaje jako evidence. Najlepsze dojrzewają i mogą wytwarzać skille/kompetencje przeznaczone do późniejszej kontrolowanej promocji.

## V10 w jednym zdaniu

**V10 jest stateful predictive competence & recovery routerem**, który przy decyzji może uwzględniać bieżący stan, zweryfikowaną kompetencję, historię prób, outcome, failure signatures i confidence.

```text
SAME STATE
+ SAME FAILURE
+ SAME ROUTE
+ NO NEW EVIDENCE
=> DO NOT BLINDLY REPEAT
```

Pełny opis: [`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)

## Jak czytać repo

1. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — aktualny T0.
2. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — wejście dla grantu/review.
3. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md) — aktualny truth index.
4. [`evidence/BODY_FROZEN_T0_20260905/README.md`](evidence/BODY_FROZEN_T0_20260905/README.md) — sanitized T0 evidence.
5. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md) — ostatni zamknięty validation test.
6. [`README.md`](README.md) — pełny research front door.
7. [`evidence/README.md`](evidence/README.md) — indeks evidence.

## Zasada epistemiczna

```text
NO EVIDENCE -> UNKNOWN
INSUFFICIENT EVIDENCE -> ABSTAIN
CONFLICTING EVIDENCE -> PRESERVE CONFLICT
WEAK PASS CONTRACT -> SUPERSEDE, DO NOT ERASE
NEW EVIDENCE -> REVISION
```

**Aktualna prawda:** integracyjne closure doprowadziło projekt do zamrożonego T0. Teraz zaczyna się seria eksperymentów transferu, porównania i późniejszej konsolidacji kompetencji.