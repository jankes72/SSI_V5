# SSI V5 — EXPERIMENTAL ORIGINS AND ENGINEERING EVOLUTION

**Status:** `HISTORICAL_EVIDENCE / ROOT_ATTESTED / EVIDENCE_TO_EXPAND`  
**Data:** `2026-08-29`  
**Autor SSI:** Paweł Jankiewicz / `PROGRAMMER_ROOT`

## 1. Dlaczego ten dokument istnieje

Publiczna historia SSI nie powinna sprawiać wrażenia, że obecna architektura została wymyślona od zera w kilka tygodni albo że powstała wyłącznie przez użycie współczesnych LLM-ów. Obecne szybkie tempo formalizacji SSI wyrasta z wcześniejszych, wieloletnich eksperymentów autora z danymi piłkarskimi, predykcją, obserwacją zachowania modeli, własnymi metodami przeliczania oraz praktycznym testowaniem strategii.

GitHub potwierdza formalizację architektury MSDI/SSI od lipca 2026. Wcześniejsza historia eksperymentów domenowych jest obecnie `ROOT_ATTESTED` i będzie wzmacniana machine evidence po dołączeniu zachowanych kodów, danych i wyników z MSI.

## 2. Punkt wyjścia: nie „zbudować AI”, tylko zrozumieć zachowanie predykcji

Pierwotne pytanie było praktyczne:

```text
DANE
-> MODEL
-> PREDYKCJA
-> REALNY OUTCOME
-> CO MODEL FAKTYCZNIE ROBI?
```

Sama skuteczność końcowa nie była wystarczająca. Autor obserwował, że model może być użyteczny również wtedy, gdy jego błąd jest systematyczny — np. określona predykcja dokładnego wyniku może historycznie wskazywać powtarzalny kierunek odwrotny.

To prowadziło do analizy nie tylko `trafione / nietrafione`, lecz także:

- grup podobnych predykcji;
- exact-score hit rate;
- directional hit rate;
- systematycznych odchyleń;
- zmian pomiędzy kolejnymi generacjami;
- stabilności tej samej predykcji po retrainingu;
- przypadków, w których nowa generacja zmieniała wcześniejszą odpowiedź;
- historii tego samego meczu/przypadku w kolejnych obserwacjach;
- warunków, w których pozornie błędny model niósł użyteczny sygnał.

## 3. 60% training / 40% unseen observation

Jednym z historycznych mechanizmów było rozdzielenie danych na część używaną do treningu i część pozostawioną do późniejszej obserwacji. Celem nie było jedynie zmierzenie accuracy, lecz obserwowanie zachowania wyszkolonej sieci na danych, których nie używała do treningu.

```text
60% TRAINING
-> MODEL / TEACHER GENERATION

40% UNSEEN OBSERVATION
-> PREDICTIONS
-> REAL OUTCOMES
-> MEMORY OF OBSERVATION
-> KNOWLEDGE
```

W obserwacji zapisywana była historia predykcji i jej zmian między generacjami. Jeżeli ten sam przypadek pojawiał się ponownie w warstwie obserwacyjnej, system mógł porównać wcześniejszą i aktualną predykcję oraz zachować informację o zmianie.

## 4. Generacja jako historyczny stan kompetencji

Generacja Teachera nie jest traktowana wyłącznie jako numer treningu. Jest historycznym snapshotem zachowania modelu, który może mieć inną wartość niż późniejsza generacja.

```text
TEACHER G_n
-> PREDICTION PROFILE
-> OBSERVATION HISTORY
-> GROUP STATISTICS
-> EXACT-SCORE BEHAVIOR
-> DEVIATIONS
-> REAL OUTCOMES
```

Późniejsze `G_n+1` może zachowywać się inaczej. Dlatego stara generacja może pozostać cenna jako osobny artefakt badawczy i jako wejście do późniejszej strategii Agenta.

## 5. Knowledge Collector

Teacher nie powinien być redukowany do pojedynczej odpowiedzi. Jego wiedza obejmuje obserwacje o tym, jak zachowuje się określona klasa predykcji, jaki jest rozkład outcome, jaki wynik lub kierunek był najczęstszy, jakie odchylenia pojawiały się między generacjami oraz jak stabilna była dana charakterystyka.

Historycznie z tego podejścia powstały artefakty obserwacji, Knowledge Laboratories i knowledge collectors opisane szerzej w `FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`.

## 6. Wirtualne rozliczanie strategii

Autor prowadził także wcześniejsze eksperymenty, w których różne modele/strategie otrzymywały własne nazwy i wykonywały wirtualne predykcje exact-score. Wyniki były rozliczane względem kursu i kosztu/stawki, aby obserwować nie tylko accuracy, lecz również długoterminową wartość ekonomiczną strategii.

To prowadziło do ważnego rozróżnienia:

```text
HIGH ACCURACY != POSITIVE ECONOMIC VALUE
LOW EXACT-SCORE HIT RATE != AUTOMATICALLY USELESS SIGNAL
```

Nie jest to deklaracja gwarantowanej przewagi finansowej. Jest to historia metodologii, z której później wyrosło podejście SSI do real outcome, Experience i długoterminowej oceny strategii.

## 7. Ewolucja sposobu programowania autora

Autor nie zaczynał od rozbudowanych systemów wielomodułowych. Wcześniejsze narzędzia były często pojedynczymi skryptami Python wykonywanymi liniowo; duży program był dzielony na logiczne części (`część 1`, `część 2`, `część 3`, `część 4`) i oznaczany tak, aby można było z niego wydobywać kolejne dane i etapy przeliczania.

Ta praktyka dekompozycji poprzedza obecne LEGO packages. Dzisiejszy wzorzec:

```text
DUŻY PROBLEM
-> MAŁE CZĘŚCI
-> JAWNE WEJŚCIA/WYJŚCIA
-> WYKONANIE
-> TEST
-> CHECKPOINT
-> INTEGRACJA
```

jest rozwinięciem praktycznego sposobu pracy, a nie wyłącznie techniką promptowania LLM.

## 8. Własny kod przeliczania i cechy sieci

Autor posiada wcześniejszy kod przeliczania sieci i dane dotyczące skuteczności własnych feature engineering / weighting / transformation mechanisms. Szczegółowa architektura tych obliczeń nie jest tutaj rekonstruowana z pamięci, ponieważ kod źródłowy pozostaje obecnie na MSI i nie został w tej aktualizacji ponownie zweryfikowany.

Status tej części:

```text
EXISTS ACCORDING TO AUTHOR = ROOT_ATTESTED
DETAILED IMPLEMENTATION = NOT YET RE-VERIFIED IN THIS PUBLIC UPDATE
NEXT STEP = INSPECT SOURCE CODE + ADD MACHINE-CHECKABLE EVIDENCE
```

README nie powinien na tej podstawie udawać dokładnej wiedzy o liczbie warstw, transformacjach lub formułach, których nie potwierdzono ponownie z kodu.

## 9. Związek z mikrosieciami SSI

Mikrosieci nie powstały w próżni. Ich logika — obserwować zachowanie, zachowywać historię, wykrywać stabilne wzorce, porównywać generacje, gromadzić evidence i dopiero potem wzmacniać kompetencję — wyrasta z wcześniejszej praktyki obserwowania modeli domenowych.

```text
PREDICTION HISTORY
-> OBSERVATION MEMORY
-> PATTERN
-> KNOWLEDGE

później:

EXPERIENCE
-> MICRONETWORK BRANCH
-> CANDIDATE
-> CHALLENGER
-> CHAMPION
```

Nie są to mechanizmy identyczne, ale istnieje wyraźna ciągłość metodologiczna.

## 10. Dlaczego tempo 2026 nie oznacza „miesiąca doświadczenia”

Publiczny Git dokumentuje bardzo szybki rozwój formalnej architektury MSDI/SSI w 2026. Nie dokumentuje jednak początku zainteresowania autora analizą danych, predykcją ani wcześniejszych eksperymentów domenowych.

Uczciwe publiczne stwierdzenie brzmi:

> Obecna architektura SSI została formalnie rozwinięta bardzo szybko, lecz bazuje na wcześniejszych eksperymentach autora z danymi, predykcją, obserwacją modeli i własnymi programami. Publiczne dowody tych wcześniejszych etapów są niepełne i będą uzupełniane artefaktami źródłowymi zamiast retrospektywnego dopowiadania szczegółów.

## 11. Zasada evidence

```text
AUTHOR MEMORY / ROOT ATTESTATION
!= MACHINE EVIDENCE

OLD SOURCE CODE
+ DATA
+ TIMESTAMPS
+ OUTPUTS
+ REPRODUCTION
-> STRONGER HISTORICAL EVIDENCE
```

Ten dokument zachowuje genezę metodologii bez zamiany osobistej historii autora w niezweryfikowany marketing.