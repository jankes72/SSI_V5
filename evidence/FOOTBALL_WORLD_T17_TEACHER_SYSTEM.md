# Football World — historyczny system T17 Teacher Knowledge

**Status evidence:** `HISTORICAL_EVIDENCE / ROOT_ATTESTED`  
**Zakres:** starsza architektura SSI / Football World  
**Znaczenie:** mechanizm historyczny do zachowania podczas migracji do obecnej architektury SSI V5  
**Autor architektury:** Paweł Jankiewicz (`PROGRAMMER_ROOT`)

> Ten dokument utrwala starszy mechanizm Football World, który poprzedza obecną formalizację `SSI ORGANISM CORE`. Nie oznacza on, że cały T17 jest obecnie aktywny w canonical runtime. Opisuje zachowaną strukturę, artefakty i kontrakt uczenia, które nie powinny zostać zgubione podczas migracji.

---

## 1. T17 — 17 wyspecjalizowanych Teacherów

T17 składał się z **17 Teacherów należących do dwóch rodzin modeli: 12 + 5**.

### Rodzina A — `dataBase_futbol_trend` (12)

1. `dataBase_futbol_trend` — Teacher zbiorczy / pełny obraz trendu;
2. `siec_01_zmiana_kursow` — zmiana kursów;
3. `siec_02_amplituda` — amplituda ruchu;
4. `siec_03_tempo` — tempo zmian;
5. `siec_04_max_wahanie` — maksymalne wychylenia;
6. `siec_05_start_raw` — surowe wartości początkowe;
7. `siec_06_koniec_raw` — surowe wartości końcowe;
8. `siec_07_log_start` — logarytmiczne reprezentacje wartości startowych;
9. `siec_08_log_koniec` — logarytmiczne reprezentacje wartości końcowych;
10. `siec_09_ratio_start` — relacje / ilorazy na początku;
11. `siec_10_ratio_koniec` — relacje / ilorazy na końcu;
12. `siec_11_statystyka` — cechy statystyczne i zagregowane.

### Rodzina B — `kursy_przygotowane` (5)

13. `kursy_przygotowane` — Teacher zbiorczy oparty na przygotowanych kursach;
14. `siec_01_start_kursow` — kursy startowe;
15. `siec_02_koniec_kursow` — kursy końcowe;
16. `siec_03_zmiana_kursow` — różnica start → koniec;
17. `siec_04_procent_kursow` — względne / procentowe zmiany kursów.

Kluczowa własność T17 polegała na tym, że jeden problem nie był obserwowany przez pojedynczy model. Każdy Teacher reprezentował inny punkt widzenia na ten sam mecz i ten sam proces rynkowo-sportowy.

---

## 2. Kontrakt 60% / 40%

Historyczny przepływ rozdzielał trening od późniejszej obserwacji:

```text
DANE ŹRÓDŁOWE
      |
      v
BUDOWA / TRENING
      |
      +-------------------------+
      |                         |
      v                         v
60% TRAINING              40% OBSERVATION
      |                         |
      v                         v
MODEL TEACHER           DANE NIEWIDZIANE
                                |
                                v
                           PREDYKCJA
                                |
                                v
                         REALNY OUTCOME
                                |
                                v
                      PAMIĘĆ OBSERWACJI
```

40% obserwacyjne nie było traktowane jako zwykłe przedłużenie treningu. Służyło do obserwowania zachowania już zbudowanego Teachera na niewidzianych przypadkach.

---

## 3. Fizyczne artefakty Teachera

Typowy Teacher posiadał strukturę zbliżoną do:

```text
siec_03_tempo/
|
|-- model.h5
|-- metadata.json
|-- klasy.json
|-- historia.json
|
|-- walidacja_40_procent.csv
|
|-- predykcje/
|   |-- predykcja_grupy.csv
|   `-- predykcja_z_wynikiem.csv
|
`-- obserwacja/
    |-- ocena.json
    `-- pamiec_obserwacji.json
```

Znaczenie artefaktów:

- `model.h5` — model predykcyjny Teachera;
- `metadata.json` — konfiguracja i opis wejść/modelu;
- `klasy.json` — mapowanie klas wyjściowych;
- `historia.json` — historia treningu;
- `walidacja_40_procent.csv` — wydzielone dane obserwacyjne;
- `predykcja_z_wynikiem.csv` — historyczne połączenie predykcji z outcome;
- `pamiec_obserwacji.json` — pamięć zachowania Teachera w kolejnych obserwacjach.

---

## 4. Pamięć zachowania Teachera

`pamiec_obserwacji.json` nie była tylko raportem accuracy. Zachowywała obserwacje pozwalające badać m.in.:

- czy Teacher zmienił predykcję;
- czy zmienił poziom pewności;
- czy wzrost pewności był uzasadniony;
- czy wysoka pewność korelowała z trafnością;
- na jakich typach przypadków Teacher regularnie się mylił;
- jak zmieniało się jego zachowanie w kolejnych obserwacjach.

Fundamentalne rozróżnienie:

```text
PREDICTION SCORE
!=
KNOWLEDGE ABOUT MODEL BEHAVIOR
```

---

## 5. Laboratorium Wiedzy

Każdy Teacher posiadał osobny obszar analiz, np.:

```text
laboratorium/
`-- dataBase_futbol_trend/
    `-- siec_03_tempo/
        |-- analiza_klas.json
        |-- analiza_odchylen.json
        |-- analiza_pamieci.json
        |-- analiza_pewnosci.json
        |-- analiza_pewnosci_klasy.json
        |-- analiza_przyszlych_predykcji.csv
        `-- kolektor_wiedzy.json
```

Warstwy odpowiadały na różne pytania:

- `analiza_klas.json` — dla których klas Teacher jest silny lub słaby;
- `analiza_pewnosci.json` — relacja confidence ↔ rzeczywista trafność;
- `analiza_pewnosci_klasy.json` — kalibracja confidence osobno dla klas;
- `analiza_odchylen.json` — rodzaj i wielkość błędu;
- `analiza_pamieci.json` — zachowanie modelu w kolejnych obserwacjach;
- `analiza_przyszlych_predykcji.csv` — materiał do dalszej kontroli;
- `kolektor_wiedzy.json` — skonsolidowana wiedza o zachowaniu konkretnego Teachera.

---

## 6. Dwie postacie Teachera

T17 rozdzielał dwie rzeczy:

```text
MODEL TEACHER
= model.h5
= zdolność do predykcji

WIEDZA TEACHERA
= kolektor_wiedzy.json
= wiedza zdobyta przez obserwację zachowania modelu
```

Dalszy system nie musiał więc kopiować wag Teachera ani traktować każdej jego predykcji jako jednakowo wartościowej. Mógł korzystać z informacji typu:

```text
Teacher jest mocny w sytuacji A
Teacher jest słaby w sytuacji B
wysoki confidence w klasie C jest wiarygodny
w przypadku D Teacher systematycznie przeszacowuje
```

To jest mechanizm:

```text
TEACHER -> OBSERVATION -> MEMORY -> ANALYSIS -> KNOWLEDGE
```

a nie tylko:

```text
TEACHER -> LABEL / ACCURACY
```

---

## 7. Konsolidacja wiedzy T17

W warstwie zbiorczej występowały m.in.:

```text
PAMIEC_MODEL_POZNAWCZY.json
WIEDZA_DLA_MODELU_DOCELOWEGO.json
```

`WIEDZA_DLA_MODELU_DOCELOWEGO.json` mogła zawierać m.in.:

- rekomendację Teachera;
- confidence;
- wagi dla klas `gospodarze / remis / goście`;
- poziom i liczbę przykładów wykorzystanych ze świata;
- reguły `warunek -> konsekwencja -> pewność`.

Przykładowy rodzaj reguły:

```text
JEŻELI określony feature znajduje się w danym zakresie
TO określony kierunek outcome występuje częściej
PEWNOŚĆ = wartość wynikająca z evidence
```

T17 miał więc prowadzić od wielu wyspecjalizowanych perspektyw do jawnej, analizowalnej wiedzy, a nie wyłącznie do jednego zbiorczego wyniku modelu.

---

## 8. Pełny historyczny przepływ

```text
17 TEACHERÓW
      |
      +-- 12 x dataBase_futbol_trend
      |
      `-- 5 x kursy_przygotowane
              |
              v
       MODELE + METADATA
              |
              v
       40% UNSEEN OBSERVATION
              |
              v
          PREDYKCJE
              |
              v
        REALNY OUTCOME
              |
              v
      PAMIĘĆ OBSERWACJI
              |
              v
      LABORATORIUM WIEDZY
              |
              +-- klasy
              +-- odchylenia
              +-- pamięć
              +-- confidence
              +-- confidence / klasa
              `-- przyszłe predykcje
              |
              v
      KOLEKTOR WIEDZY TEACHERA
              |
              v
       KONSOLIDACJA T17
              |
              v
     PAMIEC_MODEL_POZNAWCZY
              |
              v
 WIEDZA_DLA_MODELU_DOCELOWEGO
```

---

## 9. Związek z przyszłymi Agentami

W obecnej architekturze SSI ten historyczny mechanizm może zostać wykorzystany jako źródło wiedzy i materiał eksperymentalny dla przyszłych Agentów.

Agent nie musi bezmyślnie kopiować Teachera. Docelowo może:

```text
WORLD / TEACHER KNOWLEDGE
+
OWN OBSERVATIONS
+
OWN METADATA
+
OWN FEATURES
+
OWN HYPOTHESIS
        |
        v
OWN DATASET
        |
        v
OWN EXPERIMENT
        |
        v
OWN MODEL / STRATEGY
        |
        v
SIMULATED DECISION
        |
        v
INDEPENDENT REAL OUTCOME
        |
        v
OWN EXPERIENCE
```

Sześciu trwałych Agentów może dzięki temu rozwijać różne metodologie badawcze mimo wejścia do tego samego świata.

Director ma obserwować nie tylko ranking końcowy, ale również pełne lineage eksperymentów, rozwój strategii, mikrosieci, prywatne historie Agentów oraz wpływ wcześniejszych Experience i systemów wartości na decyzje.

---

## 10. Authority i real-world execution

Eksperyment Agentów pozostaje oddzielony od realnego wykonania:

```text
AGENTS
explore / simulate / learn
        |
        v
DIRECTOR
observes / evaluates / decides
        |
        v
ROBERT
executes approved real-world actions
```

Agent może tworzyć predykcje, symulowane strategie i eksperymentalne kombinacje decyzji. Sam ranking lub wysoka skuteczność nie nadają mu automatycznie real-world authority.

To samo rozróżnienie dotyczy Moralnej SI / Iskry: Agent może podejmować decyzje w środowisku eksperymentalnym i uczyć się z konsekwencji, ale capability nie jest równoznaczne z authority.

```text
CAPABILITY != AUTHORITY
SIMULATION != REAL EXECUTION
```

---

## 11. Znaczenie dla migracji SSI V5

Podczas przebudowy obecnego MASTER-a nie należy zachować wyłącznie zasady `60% training / 40% observation`.

Do zachowania jest pełniejszy mechanizm:

```text
OBSERVATION
-> MEMORY
-> BEHAVIOR ANALYSIS
-> KNOWLEDGE COLLECTOR
-> CONSOLIDATED KNOWLEDGE
```

To jest historyczny mechanizm domenowy Football World, który może zostać później odwzorowany na neutralnych interfejsach `SSI ORGANISM CORE`, bez kopiowania prywatnej historii jednego Agenta do innych Agentów.

---

## 12. Granice twierdzeń

Ten dokument nie twierdzi, że:

- T17 jest obecnie w pełni podłączony do canonical runtime SSI V5;
- 17 Teacherów jest obecnie aktywnych produkcyjnie;
- historyczne predykcje gwarantują przyszłą skuteczność;
- mechanizm dowodzi AGI lub świadomości;
- Agent uzyskuje authority do realnych działań finansowych.

Dokument utrwala **historyczny projekt, zachowane artefakty i mechanizm badawczy**, który ma znaczenie dla dalszej integracji Football World.
