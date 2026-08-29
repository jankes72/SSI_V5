# SSI V5 — geneza i rzeczywista ewolucja projektu

**Status:** `HISTORICAL_EVIDENCE / ROOT_ATTESTED`  
**Data zapisu:** `2026-08-29`  
**Autor architektury:** Paweł Jankiewicz (`PROGRAMMER_ROOT`)  

> Ten dokument rozdziela dwie rzeczy, które łatwo pomylić: **historyczną genezę SSI** oraz **obecną techniczną kolejność migracji do SSI ORGANISM CORE**. ROBERT nie był początkiem SSI. Obecna migracja ROBERT -> CORE -> nowy Director Body jest etapem przebudowy starszego, znacznie wcześniejszego systemu.

---

## 1. Początek nie był od ROBERTA ani od Agentów

SSI wyrósł z wieloletnich eksperymentów domenowych związanych przede wszystkim z **piłką nożną, predykcją wyników i realnym sprawdzaniem rezultatów**.

Pierwszym problemem nie było stworzenie ogólnego „agenta AI”. Problem był praktyczny:

```text
DANE PIŁKARSKIE / RYNKOWE
-> MODELE
-> PREDYKCJE
-> REALNE WYNIKI
-> ANALIZA TEGO, DLACZEGO MODEL DZIAŁA LUB NIE DZIAŁA
```

Autor uzyskiwał dodatnie rezultaty w części realnych prób, ale poziom i stabilność wyników nie były satysfakcjonujące. Zamiast traktować problem jako zwykłe „wytrenuj lepszy model”, projekt zaczął rozwijać mechanizmy obserwacji samych modeli i uczenia się z ich zachowania.

---

## 2. Football World i T17

Z tego etapu wyrósł system **T17 — 17 Teacherów w dwóch rodzinach modeli (12 + 5)**.

Teacher nie był wyłącznie `model.h5`. Każdy model posiadał własną historię, niewidziane dane obserwacyjne, predykcje, pamięć obserwacji i osobne Laboratorium Wiedzy.

Kluczowy przepływ:

```text
DANE
-> 60% TRAINING
-> MODEL TEACHER

40% UNSEEN OBSERVATION
-> PREDYKCJA
-> REALNY OUTCOME
-> PAMIĘĆ ZACHOWANIA TEACHERA
-> ANALIZA KLAS / PEWNOŚCI / ODCHYLEŃ / PAMIĘCI
-> KOLEKTOR WIEDZY
-> KONSOLIDACJA
-> WIEDZA DLA MODELU DOCELOWEGO
```

To był ważny krok od klasycznej metryki accuracy do pytania:

```text
NIE TYLKO: czy model trafił?
ALE: kiedy jest wiarygodny, gdzie się myli, jak zmienia confidence i czego można nauczyć się z jego zachowania?
```

Pełny opis T17 jest zachowany w:

[`evidence/FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md`](FOOTBALL_WORLD_T17_TEACHER_SYSTEM.md)

---

## 3. Dlaczego powstał Director

Wraz ze wzrostem liczby modeli, danych, wyników, pamięci, laboratoriów i zależności problem przestał być problemem pojedynczej predykcji.

Potrzebna była nadrzędna warstwa, która mogła:

- obserwować wiele źródeł jednocześnie;
- analizować wyniki modeli i eksperymentów;
- zachowywać długą historię;
- łączyć wiedzę zamiast tylko wybierać pojedynczy output;
- decydować, co ma zostać wykonane;
- kontrolować narzędzia i niższe warstwy wykonawcze;
- uczyć się z realnych outcomes.

Tak powstał **Director**.

Director był rozwijany **przed ROBERTEM** i był projektowany jako nadrzędny system dla rosnącej architektury SSI.

---

## 4. Dlaczego Hermes przestał wystarczać

Hermes pozostawał użytecznym mechanizmem wykonawczym/delegacyjnym, lecz skala SSI zaczęła przekraczać model prostego wykonawcy:

```text
TASK
-> TOOL
-> RESULT
```

Rosnący system wymagał czegoś bliższego:

```text
WIELE ŚWIATÓW
+ WIELE MODELI
+ WIELE EKSPERYMENTÓW
+ PERSISTENT MEMORY
+ REAL OUTCOMES
+ LINEAGE
+ LOCAL COMPETENCE
+ AUTHORITY
+ DŁUGOTERMINOWA ADAPTACJA
```

Integracja wszystkiego bezpośrednio w rosnącym Directorze stała się zbyt złożona. Nie wszystkie połączenia działały stabilnie, a kolejne warstwy zwiększały koszt diagnozy i ryzyko tworzenia równoległych mechanizmów.

Problemem nie był brak funkcji, lecz **zbyt duża liczba funkcji i zależności spiętych naraz**.

---

## 5. ROBERT powstał później jako kontrolowana migracja i poligon

ROBERT nie był pierwotnym Directorem ani początkiem SSI.

Powstał później poprzez wydzielenie/migrację mechanizmów Directora do środowiska, w którym można było:

- zachować potrzebne capability;
- podłączyć narzędzia i modele;
- testować mechanizmy bez ciągłego ryzyka dla całego Directora;
- brutalnie sprawdzać persistence, Experience, lifecycle, replay i restart;
- usuwać sprzężenia i zależności;
- znaleźć minimalny wspólny mechaniczny substrate.

W uproszczeniu:

```text
FOOTBALL WORLD / T17
        |
        v
rosnąca wiedza + potrzeba nadrzędnej kontroli
        |
        v
DIRECTOR
        |
        v
coraz większa liczba zależności i integracji
        |
        v
ROBERT
kontrolowana migracja / uproszczony poligon wykonawczy
        |
        v
HARDENING
Experience / micronetworks / lifecycle / replay / restart / evidence
        |
        v
SSI ORGANISM CORE
```

---

## 6. Dlaczego powstaje SSI ORGANISM CORE

Eksperymenty na ROBERCIE pokazały, że część mechanizmów nie powinna należeć wyłącznie do jednego Directora ani jednego wykonawcy.

Mechanizmy takie jak:

- identity interfaces;
- persistent memory;
- Experience;
- capability resolution;
- micronetwork lifecycle;
- checkpoint/recovery;
- evidence/lineage;
- authority interfaces;

mogą tworzyć neutralny, wspólny korpus.

Dlatego obecna kolejność techniczna wygląda tak:

```text
ROBERT
-> sprawdzone mechanizmy
-> SSI ORGANISM CORE
-> ROBERT BODY
-> DIRECTOR BODY
-> AGENT BODY
```

To **nie jest kolejność historycznego powstania projektu**. Jest to kolejność obecnej przebudowy architektonicznej.

---

## 7. Director po migracji nie będzie „nowym pomysłem”

Po ustabilizowaniu neutralnego core mechanizmy wrócą do przebudowanego Director Body.

Nie oznacza to stworzenia Directora po ROBERCIE. Oznacza to **wymianę starego, nadmiernie sprzężonego mechanicznego fundamentu Directora na sprawdzony neutralny substrate**.

Docelowo:

```text
SSI ORGANISM CORE
+
DIRECTOR PROFILE
+
STRATEGIC AUTHORITY
+
GLOBAL WORLD ACCESS
+
OWN MEMORY / EXPERIENCE
=
PRZEBUDOWANY DIRECTOR BODY
```

Następnie Director może zostać ponownie spięty z pełnym SSI: światami, sieciami, T17/Teacher knowledge, mikrosieciami, Agentami i warstwami wykonawczymi.

---

## 8. Dlaczego powstają Agenci

Pierwotny Football World wykorzystywał modele i Teacherów. Kolejny krok nie polega jedynie na dodaniu następnych modeli.

Przyszły Agent ma posiadać:

- własną identity;
- private memory;
- własne Experience;
- własne hipotezy;
- własne datasety i metadata;
- własne eksperymenty;
- własne modele i strategie;
- własną historię sukcesów i porażek;
- własną trajektorię mikrosieci;
- relacje społeczne z innymi Agentami.

W Football World Agent może samodzielnie badać dane, wybierać Teacher knowledge, tworzyć nowe cechy, budować własne metodologie predykcji i symulować strategie.

```text
WORLD
-> OBSERVATION
-> OWN HYPOTHESIS
-> OWN EXPERIMENT
-> OWN MODEL / STRATEGY
-> SIMULATED DECISION
-> INDEPENDENT OUTCOME
-> EXPERIENCE
-> NEXT EXPERIMENT
```

Director obserwuje pełną trajektorię i lineage, a nie tylko końcowy ranking.

---

## 9. Iskra — projekt wyszedł dalej niż pierwotny plan

Iskra nie była początkiem projektu. Pojawiła się jako późniejsza konsekwencja pytania:

> Co się stanie, jeżeli podobne systemy otrzymają ten sam świat i podobne capability, ale różne początkowe systemy wartości oraz oddzielne historie Experience?

Celem nie jest stworzenie „losowych osobowości”. Iskra ma być jawnym, wersjonowanym initial value prior wpływającym na ocenę możliwych decyzji.

Sześciu Agentów może wejść do tego samego Football World, ale po czasie rozwinąć różne:

- metodologie badawcze;
- strategie selekcji danych;
- modele;
- sposoby grupowania predykcji;
- reakcje na porażki;
- tolerancję ryzyka;
- relacje społeczne;
- mikrosieci;
- przekonania i polityki działania.

Najciekawsza hipoteza nie brzmi:

```text
CZY AGENT TRAFI WIĘCEJ MECZÓW?
```

lecz:

```text
CZY NIEZALEŻNE SYSTEMY,
MAJĄCE TEN SAM ŚWIAT,
ALE RÓŻNE VALUE PRIORS I WŁASNE EXPERIENCE,
SAMODZIELNIE WYTWORZĄ TRWAŁE,
MIERZALNIE RÓŻNE METODOLOGIE POZNAWCZE
I ODKRYJĄ UŻYTECZNE STRATEGIE,
KTÓRYCH AUTOR SYSTEMU WCZEŚNIEJ NIE PRZEWIDZIAŁ?
```

To jest kierunek, który wyszedł znacznie dalej niż początkowy cel związany z poprawą predykcji piłkarskich.

---

## 10. Director obserwuje, Agenci symulują, ROBERT wykonuje

Przyszłe Agenty są przede wszystkim jednostkami eksperymentalnymi. Mogą szeroko badać, symulować i rozwijać własne strategie, ale nie otrzymują automatycznie authority do działań w realnym świecie.

```text
AGENTS
explore / experiment / simulate / learn
        |
        v
DIRECTOR
observes / audits / compares / evaluates / decides
        |
        v
ROBERT
executes approved real-world actions
```

Stan prywatny Agenta może być prywatny wobec innych Agentów, ale pozostaje audytowalny przez Directora zgodnie z modelem authority eksperymentu.

Ranking Agentów jest elementem środowiska społecznego i Experience, a nie mechanizmem automatycznego nadawania real-world authority.

---

## 11. Wspólny wzorzec Football World i Moralnej SI

Football World i późniejsza Moralna SI używają tego samego głębszego schematu:

```text
ŚWIAT DAJE PROBLEM
-> SYSTEM WIDZI DOSTĘPNE MOŻLIWOŚCI
-> AGENT WYBIERA
-> ŚWIAT ZWRACA KONSEKWENCJĘ
-> EXPERIENCE
-> ZMIANA PRZYSZŁEGO ZACHOWANIA
```

W Moralnej SI może to być np. problem „zamknięte drzwi + dostępny klucz”.

W Football World:

```text
DANE
-> HIPOTEZA
-> MODEL
-> PREDYKCJE
-> SELEKCJA
-> GRUPOWANIE / SYMULOWANA STRATEGIA
-> REALNY WYNIK MECZU
-> OCENA
-> EXPERIENCE
```

W obu przypadkach Agent ma uczyć się z konsekwencji w świecie, bez automatycznego przejścia od capability do authority.

---

## 12. Rzeczywista historia vs obecna roadmapa

### Historia powstania

```text
PIŁKA NOŻNA / REALNE PREDYKCJE
-> MODELE DOMENOWE
-> T17 TEACHERS
-> 60/40 OBSERVATION
-> MEMORY / LABORATORIES / KNOWLEDGE COLLECTORS
-> DIRECTOR
-> coraz bardziej złożony SSI
-> ROBERT jako migracja/poligon
-> hardening mechanizmów
-> SSI ORGANISM CORE
-> przebudowany DIRECTOR BODY
-> AGENT BODY
-> ISKRA / SIX-AGENT LONGITUDINAL EXPERIMENT
```

### Obecna kolejność inżynieryjna

```text
HARDEN ROBERT
-> EXTRACT NEUTRAL CORE
-> VERIFY ORGANISM_CORE_V1
-> REBUILD DIRECTOR BODY ON CORE
-> BUILD AGENT BODY ON CORE
-> CONNECT WORLDS / T17 / EXPERIMENTS
-> RUN LONGITUDINAL SIX-AGENT STUDIES
```

Oba diagramy są prawdziwe, ale opisują **inne osie czasu**.

---

## 13. Co należy zachować podczas dalszej przebudowy

Nie wolno utracić wcześniejszych mechanizmów tylko dlatego, że obecna implementacja jest przebudowywana.

Szczególnie chronione koncepcyjnie powinny pozostać:

```text
T17 SPECIALIZATION
60/40 TRAINING / OBSERVATION SEPARATION
INDEPENDENT OUTCOMES
TEACHER BEHAVIOR MEMORY
KNOWLEDGE LABORATORIES
KNOWLEDGE COLLECTORS
LINEAGE
AGENT PRIVATE EXPERIENCE
MICRONETWORK TRAJECTORIES
DIRECTOR META-OBSERVATION
CAPABILITY != AUTHORITY
SIMULATION != REAL EXECUTION
```

Nowy design ma te mechanizmy uprościć, uogólnić i poprawnie połączyć — nie wymazać ich historię ani zastąpić równoległymi atrapami.

---

## 14. Najkrótsze podsumowanie genezy SSI

SSI nie zaczęło się jako projekt budowy „AGI” ani systemu sześciu Agentów.

Zaczęło się od praktycznego problemu predykcyjnego w Football World. Próba zrozumienia, dlaczego modele czasem działają, a czasem zawodzą, doprowadziła do Teacherów, pamięci obserwacji, laboratoriów i konsolidacji wiedzy. Rosnąca złożoność wymusiła Directora. Złożoność samego Directora wymusiła kontrolowaną migrację do ROBERTA. Testowanie ROBERTA ujawniło potrzebę neutralnego Organism Core. Neutralny core umożliwił zaprojektowanie niezależnych Agentów, a pytanie o ich długoterminową dywergencję doprowadziło do Iskry i eksperymentu sześciu Agentów.

```text
PREDYKCJA
-> OBSERWACJA
-> WIEDZA
-> DIRECTOR
-> ROBERT
-> ORGANISM CORE
-> AGENTS
-> ISKRA
-> LONGITUDINAL EXPERIMENT
```

Projekt wyszedł więc znacznie dalej niż jego pierwotny problem domenowy, ale kolejne warstwy nie są przypadkowymi dodatkami — każda z nich powstała jako odpowiedź na ograniczenie ujawnione przez poprzednią warstwę.
