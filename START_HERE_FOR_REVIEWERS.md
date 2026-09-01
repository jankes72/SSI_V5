# SSI V5 — Start Here for Grant and Technical Reviewers

Jeżeli oceniasz SSI V5 jako grantodawca, sponsor, badacz lub niezależny recenzent techniczny, zacznij od poniższych materiałów zamiast próbować czytać całe repozytorium od początku.

## 1. Najczęstsze pytania i odpowiedzi

[`GRANT_REVIEWER_FAQ.md`](GRANT_REVIEWER_FAQ.md)

FAQ odpowiada m.in. na pytania:

- co dokładnie jest badane w SSI V5;
- czym mikrosieci różnią się od RAG, cache i zwykłej pamięci agenta;
- dlaczego V10 nie powinien być interpretowany wyłącznie jako cache;
- czym jest zbiorowa inteligencja i jak nowe evidence może wzbogacać Championów;
- dlaczego mikrosieci są wielozadaniowe i wieloprzestrzeniowe;
- jak mogą dynamicznie powstawać nowe gałęzie kompetencji;
- jak działa `Experience -> Candidate -> Challenger -> Champion`;
- co dzieje się przy błędnym Championie / false reuse;
- czym są CONTINUUM i LEGO;
- jak działa metodologia dekompozycji, migracji, testów, regresji i rekonstrukcji publicznego eksperymentu;
- dlaczego Test 2 był potrzebny przed Testem 3;
- jakie są ograniczenia obecnych wyników i co mogłoby sfalsyfikować hipotezę SSI.

## 2. V10 predictive routing

[`V10_PREDICTIVE_ROUTING.md`](V10_PREDICTIVE_ROUTING.md)

Ten dokument wyjaśnia, że V10 nie jest wyłącznie cache'em ani prostym routerem. Opisuje warstwę predykcyjnego dopasowania, confidence gating, wybór między `REUSE_TOP1`, `VERIFY_TOPK` i `FULL_FLOW`, feedback/route compilation oraz rolę V10 jako pierwszej warstwy ochrony przed `false reuse`.

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

W interpretacji V10 należy dodatkowo uwzględnić warstwę predykcyjną: router estymuje dopasowanie istniejącej kompetencji i poziom confidence, a wynik tej oceny prowadzi do reuse, dodatkowej weryfikacji albo pełnego flow. Obecny Test 3 pokazuje działanie exact/similarity routing i selektywnej weryfikacji, ale dalsze testy powinny celowo obejmować unknown, conflicting i adversarial cases, aby mierzyć false-reuse rate i jakość calibration.

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
