# Migracja SSI na serwery — stan udokumentowany na 25.10.2026

**Migracja osiągnęła etap zweryfikowanych przygotowań serwerowych, działającego podglądu Universal Lab i częściowo zabezpieczonych danych lokalnych. Pełne przełączenie produkcyjne oraz odtworzenie całego SSI nie są jeszcze potwierdzone.**

Dokument aktualizuje publiczny obraz prac na podstawie przekazanych raportów operatora i lokalnych testów narzędzi. Rozdziela wynik wykonania, staging, test oprogramowania oraz plan. Nie wykonano nowego połączenia do serwerów na potrzeby tej publikacji.

## Potwierdzone etapy serwerowe

| Obszar | Udokumentowany wynik | Granica potwierdzenia |
| --- | --- | --- |
| Dyrektor M1–M7 | Przeniesione partie źródeł i materiałów; uruchomiony odbiorowy podgląd Universal Lab oraz wejście Hermesa | Nie jest to pełny produkcyjny cutover ani odbiór rzeczywistych odpowiedzi Hermesa i wszystkich mostów |
| Dyrektor M8R1 | **107/107 testów kontraktowych PASS** w izolacji na VPS; wynik `M8R1_NATIVE_CONTRACTS_VERIFIED_SHADOW_ONLY` | Zadania syntetyczne i jednorazowe bazy; nie wykonywano inferencji. Natywne wykonanie Routera V10/S10 i podpisy Notariusza nie zostały tym testem potwierdzone |
| Dyrektor M9 | **20 plików wejściowych sprawdzonych**, ponownie skontrolowane 72 pliki bazowe M8; `M9_TRAINING_INPUTS_STAGED_RECONCILIATION_REQUIRED` | Materiały do szkoleń są przygotowane; w tym etapie wykonano **0 szkoleń, 0 wywołań modeli i 0 aktywacji produkcyjnych** |
| Robert P3A/P3B | Przygotowanie izolowanego runtime i zaliczony wcześniejszy test integracyjny | Brak związania kanonicznego stanu i aktywacji konsumenta kolejki |
| Robert P3C R2 | **Worker self-test PASS**, `P3C_CANDIDATE_STAGED_VERIFIED_DISABLED` | Usługa workera nie została zainstalowana; konsument kolejki nie wystartował; state binding nie został wykonany; 0 wywołań modeli w tym etapie |
| CORE24 | Dostęp do katalogu **13 tagów modeli** w badanych połączeniach | Metadane nie są dowodem wykonania misji każdym modelem ani aktualnej kwalifikacji jakości |
| SCC R17/A34 | **67 lokalnych testów offline PASS** dla badanego źródła i kontraktów | To odrębny audyt oprogramowania, nie odbiór produkcyjnego wykonania misji na serwerach |

Raport M8R1 został teraz odczytany z przekazanego ZIP-a; liczba 107 i granice izolacji są zgodne z wcześniejszą publiczną notatką. M9 jest kolejnym etapem przygotowania danych, a nie następnym benchmarkiem. Poprawiony P3C R2 rozlicza wcześniejszy bloker stagingu Roberta, zachowując stan **DISABLED**.

Nie sumujemy 107 testów kontraktowych, 67 testów SCC i testów narzędzi kopii jako jednej próby gotowości całego SSI.

## SCC i połączenia języka misji — ustalenia R11.1

**SSI MultiQuant V7.16 R11.1: odnaleziono publiczną dokumentację SCC A27 z 14.10.2026.** Autor/operator zgłosił w tamtej publikacji wdrożenie i działanie modułu deklaratywnego. Dokument opisuje parser, walidację, planowanie oraz powiązania z istniejącymi mechanizmami SSI. Nie jest to dowód aktualnego stanu parsera na serwerze Dyrektora po migracji.

Ograniczony audyt nazewnictwa na serwerze modeli/eksperymentów CORE24 nie wykazał pasujących plików parsera/schematu SCC ani powiązanych nazw usług w sprawdzanych lokalizacjach `/opt` i `/srv`. **Brak trafień tego audytu nie oznacza nieobecności SCC w SSI.** Badany serwer pełni rolę modeli i eksperymentów; parser lub źródła mogą znajdować się na Dyrektorze, w archiwum lub pod inną nazwą. Wskazanie aktualnego autorytatywnego parsera pozostaje osobną bramką.

### Zachowany kontrakt języka

Udokumentowana notacja zaczyna się od `SSI_MISJA 1` i kończy `KONIEC`. Obejmuje m.in. projekt, zadanie, strategię i jej wersję, domenę, wejście, cel, hash kontekstu, kryterium odbioru i limit kroków. Zachowuje istniejące identyfikatory `ssi.mission.goal.r1` i `ssi.mission.intent.r1`.

Publikacja A27 podaje **22 odtworzone testy Python i 10 asercji kontraktu JavaScript**, bez wywołań dostawców modeli. To historyczna walidacja modułu deklaracji i planowania liniowego, odrębna od 107 testów M8R1 oraz 67 testów audytu SCC. Nie ponawiano jej w ramach tej publikacji. Pełne wykonanie Championów, ogólne instrukcje imperatywne, rozgałęzienia i równoległe programy nie są potwierdzonym wynikiem A27.

### Mapa powiązań i granice odbioru

| Powiązanie | Rola w misji SSI | Co jest udokumentowane teraz |
| --- | --- | --- |
| SCC → kontrakt celu i intencji | Deklaracja celu, strategii, kryteriów i ograniczeń | Publiczna referencja A27 opisuje parsowanie, walidację i konwersję do istniejącego kontraktu; aktualny parser na Dyrektorze wymaga wskazania i weryfikacji |
| Kontrakt misji → Router V10 / S10 | Wybór kompetencji, wersji i trybu wykonania | To natywne mechanizmy docelowego obiegu. Test M8R1 nie wywoływał rzeczywistego V10 ani S10; nie stanowi odbioru wykonania przez Router |
| SCC ↔ Research Memory | Odczyt zapisanego kontekstu i historii, powiązanie doświadczeń z misją | A27 opisuje odczyty kontekstu; M8R1 potwierdza syntetyczny roundtrip, ACL i idempotencję na jednorazowej bazie. Ciągłość pamięci produkcyjnej i podpisy wymagają osobnego odbioru |
| SCC ↔ MultiQuant | Powiązanie zadania z wersją modelu, wariantem Q/D i dowodami jakości | Istnieje ograniczony adapter obserwacyjny testowany w M8R1. R11.1 dostarcza referencję formatu; natywna misja SCC wykonująca produkcyjne Q/D i odbierająca wynik nie jest tu potwierdzona |
| Misja → ROBERT / CODEX → CORE24 | Wykonanie narzędziowe i uprawnione użycie wspólnych modeli | Robert ma zweryfikowanego, wyłączonego kandydata; dostęp do 13 tagów jest metadanymi. Pełny cykl delegacji i inferencji czeka na odbiór |
| SCC / CONTINUUM ↔ LangGraph | Proponowane prowadzenie etapów, checkpointów i wznowień | Plan adaptera, bez nowego potwierdzenia wdrożenia |
| Biblioteka zasobów ↔ n8n | Proponowana synchronizacja wersjonowanych skilli i artefaktów | Plan integracji; n8n nie przejmuje decyzji Routera ani promocji kompetencji |

**Najbliższy krok dla języka:** przypiąć właściwy parser i wersję kontraktu na Dyrektorze, sprawdzić zgodność z referencją A27 oraz późniejszymi zachowanymi źródłami, a następnie odebrać jedną misję przez rzeczywiste komponenty. Nie zastępować natywnego SCC syntetyczną strukturą JSON z eksperymentu MultiQuant.

Źródła publiczne:
- [SCC A27 — opis modułu, kontraktów i pochodzenia mechanizmów, 14.10.2026](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md).
- [MultiQuant V7.16 R11.1 — odkrycie dokumentacji i luka w weryfikacji aktualnego runtime](../PUBLIC_MODELS/SSI_MULTIQ_V7_16_R11_1_SCC_CONTRACT_DISCOVERY_20261025.md).

## Magazyn i zabezpieczenie danych

Na lokalnym węźle magazynowym potwierdzono zapis i odczyt danych oraz łącznie około **12 GiB aktywnego swapu**. Swap nie zwiększa VRAM. Raporty klientów potwierdzają dostęp MSI i Lenovo/NOUT2 przez Tailscale. Dostęp wszystkich VPS do tego magazynu i powiązanie go z runtime SSI nie mają jeszcze osobnego odbioru.

### Lenovo / NOUT2

Raport głównej kopii podaje:
- archiwum obejmujące **151 440 plików**;
- **1765 osobnych kopii SQLite**, odtworzonych i ponownie otwartych przez narzędzie operatora;
- brak zgłoszonych błędów tar oraz kopii SQLite.

Początkowo zgłoszono dwie uwagi do kompletności. Typ pliku o rozszerzeniu sugerującym bazę wyjaśniono jako zwykły tekst. Pominięty osobny system plików zabezpieczono dodatkowym przebiegiem: **37 plików i jedna dodatkowa kopia SQLite**, bez zgłoszonych błędów lub pominięć. Uzupełnienie ma status `NODE_BACKUP_SUPPLEMENT_VERIFIED`.

**Bieżąca ocena znanego zakresu NOUT2: `INVENTORIED_SCOPE_BACKED_UP_RESTORE_PENDING`.** Nie jest to dowód odkrycia wszystkich danych komputera, jednej wspólnej chwili dla wszystkich baz ani odtworzenia działającego SSI. Archiwa danych nie były niezależnie ponownie odczytywane w środowisku publikacji; odczytano raporty o weryfikacji wykonanej przez narzędzie operatora.

### MSI — rzeczywisty rozmiar i zatrzymana kopia

Audyt metadanych wybranego zakresu wykazał **2 708 523 pliki i 477,50 GiB źródeł**. W osiągalnym wybranym zakresie nie zgłoszono błędów odczytu, pominięć ani brakujących ścieżek. Nie potwierdzono jednak pełnego odkrycia wszystkich lokalizacji SSI.

Największe obszary:
- drzewo robocze robotyki: **323,51 GiB**;
- główne drzewo SSI: **83,64 GiB**;
- dodatkowe drzewo instalacyjne: **23,15 GiB**;
- dwa badane magazyny wag modeli: łącznie około **39,30 GiB**.

W obrębie robotyki dwa rozłączne poddrzewa mirror i kandydatów do ponownego użycia zajmują razem **322,58 GiB**. Są priorytetem porównania zawartości. Ich nazwy nie dowodzą zbędności lub identyczności.

Audyt przytoczył wybrane metadane wcześniejszego raportu kopii: skrypt oszacował **643,86 GiB wymaganego miejsca**, obejmując źródła, osobne kopie SQLite, narzut i rezerwę. Przy historycznie dostępnych **443,35 GiB** brakowało około **200,51 GiB**. To budżet skryptu, nie prognoza rozmiaru skompresowanej kopii.

Przebieg MSI zatrzymał się na bramce pojemności. **Nie ma zweryfikowanej kopii MSI.** Metadane tego zatrzymania pochodzą pośrednio z kolektora audytu; oryginalnego ZIP-a zatrzymanej kopii nie odczytano osobno.

## Audyt skilli po kolejnych konsolidacjach

Audyt rozmiarów znalazł duże grupy kandydatów o takim samym rozmiarze, lecz nie obliczał hashy ich treści. Nie opublikowano na tej podstawie liczby duplikatów ani zbędnych skilli.

Pierwszy audyt zawartości skilli **R1** znalazł **150 000 kandydatów**, po czym zakończył się `CANDIDATE_LIMIT` przed porównywaniem plików: **0 bajtów odczytanej treści kandydatów, 0 porównanych katalogów**. Zera w polach wynikowych nie oznaczają braku duplikatów, braku sprawnych skilli lub braku historycznych dowodów.

Sprawdzono zgodność hashy uruchomionego kodu i zakresu R1 z wydaną paczką. Przyczyna dotyczyła organizacji narzędzia: limit listy kandydatów przerywał przebieg przed etapem analizy.

Przygotowano poprawkę **R2**, która:
- przechowuje kolejkę ścieżek w prywatnym tymczasowym indeksie zamiast dużej listy w RAM;
- nie ma wcześniejszego limitu 150 000 kandydatów;
- analizuje katalogi i wskazane artefakty przed pozostałymi plikami bloków;
- raportuje znalezione, przetworzone i nieprzetworzone pliki oraz luki zakresu;
- zachowuje porównania częściowe, jeśli dalsze przetwarzanie osiągnie inny limit.

**R2: 27 lokalnych testów PASS**, w tym przypadek ponad 150 000 kandydatów, przetwarzanie po limicie skanu i zachowanie wyników po limicie wyjścia. **Raport wykonania R2 na MSI nie został jeszcze otrzymany.**

Nie wykonano deduplikacji, kasowania ani promocji kompetencji. Identyczny plik katalogu, identyczny wpis JSON i identyczny plik kodu są odrębnymi obserwacjami. Żadna z nich sama nie dowodzi identyczności całego pakietu, jego zależności, stanu aktora i uprawnień.

Ocena historycznego PASS wymaga powiązania dowodu z konkretną tożsamością skilla, aktorem, wersją i zawartością artefaktu. Etykieta Champion/Qualified nie zastępuje takiego powiązania. Obecne narzędzie nie wykonuje świeżych testów skilli ani nie odczytuje dowodów zamkniętych wewnątrz źródłowych baz SQLite i archiwów.

## Docelowy podział zasobów — plan migracji

Przy budżecie około 120 GB na VPS przyjęto podział:
- **Dyrektor:** orkiestracja, Universal Lab, aktywna pamięć, kolejki i checkpointy;
- **Robert:** wykonawca oraz odrębna rola CODEX; zasoby eksperymentów MultiQuant;
- **CORE24:** wspólna usługa modeli, bez kopiowania wszystkich wag na pozostałe VPS;
- **lokalny magazyn:** indeksowana biblioteka skilli i mikrosieci, duże zasoby i historia; biblioteka robocza oddzielona od kopii zapasowej;
- **MSI:** panel, warsztat i zachowane źródła oraz archiwum.

To założenie projektowe. **Minimalnych rozmiarów rdzeni VPS jeszcze nie zmierzono.** Budżet musi uwzględniać również system, obrazy, logi, aktywne bazy i rezerwę.

Rdzenie serwerowe mają zachowywać działanie przy niedostępnym komputerze lokalnym. Misje wymagające niepobranej kompetencji lub fizycznego GUI czekają na odpowiedni zasób; dostępne zadania serwerowe mogą być kontynuowane.

Przesłany plan modernizacji łączy **SCC, Router V10, Research Memory, LangGraph i n8n**. Zachowuje natywne role SSI: SCC opisuje misję, Router wybiera kompetencje, Research Memory przechowuje doświadczenia, LangGraph ma wspierać etapy i wznowienia, a n8n synchronizację. **Nie ma w tym raporcie dowodu wdrożenia nowych adapterów LangGraph/n8n ani produkcyjnego zamknięcia tego obiegu.**

## Najbliższe bramki odbioru

1. Wynik R2 i porównanie zawartości skilli; odczyt brakujących dowodów w odpowiednich formatach.
2. Manifest minimalnych rdzeni, aktywnych zależności i wersjonowanej biblioteki zasobów.
3. Zabezpieczenie wszystkich unikalnych danych, kopie pozostałych węzłów i niezależna próba odtworzenia aplikacji.
4. Powiązanie rzeczywistego stanu Roberta, kolejki, checkpointów i ciągłości Evidence/Notariusza.
5. Jedna misja SCC przez pełny obieg: delegacja → kompetencja → narzędzia → wynik → doświadczenie → archiwizacja → restart/recovery bez powielenia skutków.
6. Dopiero po odbiorze: rozszerzenie na macierz modeli i serwerów oraz przygotowane realizacje pilotażowe.

## Pochodzenie i granice publikacji

Szczegóły wyników i SHA-256 źródłowych raportów zapisano w [publicznym podsumowaniu JSON](SSI_MIGRATION_CHECKPOINT_PUBLIC_20261025.json). Hashe umożliwiają rozpoznanie konkretnego raportu; nie zastępują niezależnej atestacji. Prywatne raporty źródłowe pozostają niepubliczne.

Ta publikacja zawiera wyniki i granice ich interpretacji. Nie zawiera kodu autorskiego, baz, prywatnych promptów, danych klienta, poświadczeń, adresów węzłów, UUID dysków ani prywatnych ścieżek.

Powiązane publiczne dokumenty:
- [Dyrektor M1–M8R1 — wcześniejszy raport](SSI_DIRECTOR_MIGRATION_M1_M8R1_20261023.md).
- [Robert P0–P3C — wcześniejszy raport](SSI_ROBERT_MIGRATION_P0_P3C_20261024.md).
- [MultiQuant R11.1 — odrębny zakres odkrywania kontraktu SCC](../PUBLIC_MODELS/SSI_MULTIQ_V7_16_R11_1_SCC_CONTRACT_DISCOVERY_20261025.md).

Starsze raporty zachowują historyczne oceny. Nowy checkpoint nie rozszerza PASS na niebadane obszary ani nie zmienia wyników odrębnych eksperymentów MultiQuant.
