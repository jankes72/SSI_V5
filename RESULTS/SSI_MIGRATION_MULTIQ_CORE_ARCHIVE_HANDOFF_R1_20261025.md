# SSI — uzgodnienie migracji, rdzenia i MultiQuant R1

Data: 25 października 2026 r.  
Identyfikator: `SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025`  
Status: **zakres zatwierdzony przez użytkownika; wdrożenie i odbiór integracji oczekują**.  
Sprawdzony HEAD przed publikacją: `00f7287230cce6999b5c938e792ad084420b7819`.  
[Wersja maszynowa](SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_PUBLIC_R1_20261025.json).

## Wspólna decyzja

Na Dyrektorze utrzymujemy **cały wymagany silnik SSI oraz główną bazę skilli i kompetencji wraz z zależnościami**. Pozostałe instalacje, powielone materiały konsolidacji, nieaktywne warianty i warsztat klasyfikujemy jako archiwum. Jest to decyzja o zakresie pakowania; nie wykonano przenoszenia ani kasowania źródeł.

Dokument uzupełnia [wcześniejszy checkpoint](SSI_MIGRATION_CHECKPOINT_20261025.md). Zastępuje jego informację, że raport sprzętowy audytu skilli R2 jeszcze nie dotarł, oraz dodaje decyzję ACTIVE/ARCHIVE. Pozostałe ograniczenia odbioru produkcyjnego nadal obowiązują. Kanoniczny opis architektury pozostaje w [C4 SSI](../SSI_V5_C4_ARCHITECTURE.md).

## Co pozostaje aktywne

| Zakres | Wymaganie |
| --- | --- |
| Director i Universal Lab | Orkiestracja i niezbędne funkcje silnika |
| Natywny SCC i Router V10/S10 | Właściwy parser, istniejące kontrakty, reguły routingu i uprawnienia |
| Główne skille, kompetencje i mikrosieci | Wybór według właściwych rejestrów; zachowanie wykonawczej treści i zależności |
| Research Memory i stany aktorów | Zachowanie tożsamości, wersji, ACL oraz potrzebnej ciągłości |
| CONTINUUM i recovery | Kolejki, niezakończone misje, checkpointy i wznowienie |
| Evidence / Notariusz | Głowy łańcuchów, weryfikacja oraz działające odwołania do historii |
| Komunikacja | Istniejące kontrakty z Robertem, CODEX i wspólną usługą modeli CORE24 |
| Indeksy archiwalne | Powiązanie aktywnej kompetencji z jej pochodzeniem i zasobami |

Modele na CORE24 pozostają wspólną usługą. Kopiowanie wszystkich wag na Dyrektora nie jest założeniem tej migracji. Przygotowujemy środowiska wymagane przez wybrany runtime; historyczne kopie środowisk nie są domyślnym składnikiem instalacji.

Moduły domenowe zachowują identyfikatory i odwołania interfejsu. Dane potrzebne aktywnej funkcji są jej zależnością. Samo zachowanie nazwy modułu nie oznacza odbioru funkcji.

## Archiwa i duplikaty

Archiwum obejmuje kandydatów historycznych po sprawdzeniu zależności i natywnej retencji. Zachowujemy unikalne treści, mapowanie dawnych lokalizacji, pochodzenie, statusy kwalifikacji i wyniki FAIL/INCONCLUSIVE. Zamkniętą historię można wydzielić dopiero z zachowaniem ciągłości i odtwarzalności.

**Identyczne bajty katalogu nie dowodzą identyczności całego pakietu kompetencji.** Nie wolno wybierać głównego skilla według daty pliku lub liczby kopii ani scalać mutowalnych stanów różnych aktorów na podstawie zgodności bajtów. Archiwizacja nie jest dowodem niezależnego backupu.

Docelowo NOUT1 jest opcjonalnym magazynem archiwum i kopii. Start rdzenia oraz misje korzystające z aktywnego zestawu mają działać bez niego. Zasób historyczny wymagany przez aktywny skill staje się zależnością aktywną; w przeciwnym razie skill musi jawnie pozostać zależny od archiwum.

## Co rzeczywiście wykazał audyt

Raport MSI R2 został otrzymany i przejrzany. W wybranym zakresie przetworzono **241 218 kandydatów**, porównano **2661 lokalizacji katalogów**, rozpoznając **379 unikalnych treści plików**. Wykryto **304 grupy duplikatów i 2282 dodatkowe lokalizacje**, odpowiadające **56 345 385 024 B logicznych powtórzeń**.

To nie jest pomiar odzyskanego miejsca ani dowód pełnej identyczności pakietów. Występuje też **411 wariantów wpisów o tym samym ID**; wymagają rozstrzygnięcia według treści, pochodzenia i właściwego rejestru. Wynik R2 pozostaje częściowym audytem wymagającym przeglądu; wybrany zakres nie dowodzi odkrycia wszystkich skilli SSI.

Kolejny raport rozpoznał struktury **225 wcześniej nierozpoznanych lub pustych katalogów**. Nie dokonał wyboru kanonicznych członków konsolidacji. Potwierdził **520 wpisów QUALIFIED Czary** oraz odnalezienie **120 wskazanych historycznych przebiegów treningowych PASS**. To potwierdza historyczne powiązania treningowe; nie jest ponownym wykonaniem obecnego kodu ani odbiorem aktualnego powiązania wykonawczego.

## Budżet 80 GB

**Rozmiar nowego, odchudzonego rdzenia nie został jeszcze zmierzony.**

Poprzedni szeroki kandydat, po odjęciu jednego wskazanego zbioru historycznego, nadal obejmował **100 139 242 402 B, czyli 100,14 GB** zwykłych plików. Nie jest to rozmiar nowego rdzenia i nie domyka wszystkich zależności. Nie wolno odejmować od niego całych 56,35 GB powtórzeń z innego zakresu audytu.

Przyjmujemy 80 GB dziesiętnych, czyli 80 000 000 000 B. Rezerwa wzrostu 10 GB pozostawia najwyżej 70 GB **przed odjęciem narzutu systemu i innych wymaganych składników**. Odbiór wymaga, aby rozpakowany aktywny pakiet, wymagane środowiska i dane, narzut systemu/kontenerów oraz rezerwa zmieściły się w dostępnym budżecie, z liczeniem każdego składnika jeden raz. Trzeba sprawdzić również faktycznie zajęte miejsce i wolną przestrzeń docelową.

Decyzję o braku potrzeby NOUT1 do pracy podejmiemy po pomiarze i uruchomieniu stagingu bez NOUT1. Sam mały rozmiar ZIP lub logiczna liczba duplikatów tego nie rozstrzyga.

## Połączenie z SCC i MultiQuant

Punktem odniesienia jest [historyczna dokumentacja SCC A27](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md) z zachowaniem opisanej atrybucji upstream. Zachowujemy istniejące kontrakty `ssi.mission.goal.r1` i `ssi.mission.intent.r1`. Aktualny autorytatywny parser Dyrektora nadal wymaga potwierdzenia; syntetyczny JSON MultiQuant nie staje się przez to składnią natywnego SCC.

Docelowe powiązanie do odbioru: **SCC → natywny kontrakt misji → Router V10/S10 → Research Memory / adapter MultiQuant → wykonawca → Evidence**. Jest to zakres integracji do potwierdzenia, a nie deklaracja działającego end-to-end runtime. LangGraph i n8n pozostają proponowanymi adapterami.

| Sprawdzony wynik MultiQuant | Znaczenie dla wspólnej pracy | Granica dowodu |
| --- | --- | --- |
| [R15 ACTIVE/LONGTERM](../PUBLIC_MODELS/SSI_MULTIQ_V7_16_R15_DUAL_TIER_QUOTA_20261025.md) | Kierunek rozdzielenia aktywnego i długoterminowego magazynu | 10/10 izolowanego wrappera, faktycznie 96 B na warstwę; brak odbioru limitów 4 GiB |
| [R19 wznowienie](../PUBLIC_MODELS/SSI_MULTIQ_V7_16_R19_STEP_RESUMPTION_20261025.md) | Wymagania checkpointów i kontynuacji misji | 10/10 syntetycznego scenariusza; bez odbioru recovery produkcyjnego |
| [R21 równoległe misje](../PUBLIC_MODELS/SSI_MULTIQ_V7_16_R21_MULTI_MISSION_CONCURRENCY_20261025.md) | Izolacja misji, claim, fencing i idempotencja w adapterze | 10/10 izolowanych testów; bez natywnego SCC, wielohostowości i gwarancji skutków zewnętrznych |
| [RAM Guard R3](../PUBLIC_MODELS/SSI_MULTIQ_RAMGUARD_R3_PASSIVE_METRICS_AND_TEST_BACKUP_20261025.md) | Osobne pomiary RAM i kopie małych magazynów testowych | Brak dowodu przyspieszenia, zmniejszenia rozmiaru SSI na dysku i backupu całego SSI |
| [RAM Guard R4](../PUBLIC_MODELS/SSI_MULTIQ_RAMGUARD_R4_OFFHOST_SYNTHETIC_COPY_20261025.md) | Kopie dwóch małych magazynów testowych poza CORE24: 12 plików, 24 960 B; SQLite i SHA PASS | Zakres syntetyczny; bez backupu całego SSI i odtwarzania aplikacyjnego |

PASS MultiQuant nie przenosi się automatycznie na Dyrektora ani na kwalifikację kompetencji.

## Odpowiedź potrzebna od prowadzącego MultiQuant

To publiczny punkt wymiany ustaleń. Publikacja nie oznacza, że drugi model już go odczytał lub zaakceptował.

1. W odpowiedzi podać identyfikator tego dokumentu i SHA przeczytanego commitu migracji oraz MultiQuant.
2. Wskazać faktycznie potrzebny runtime, stan, zależności, retencję i wymagania odtwarzania, oddzielając je od syntetycznych fixture.
3. Przypisać adapter do istniejących kontraktów SCC, Routera, Research Memory i Evidence; wypisać brakujące powiązania.
4. Uzgodnić wymagania checkpointów, claim/fencing i potwierdzeń wykonania bez zmiany autorytetu natywnego silnika.
5. Podać zmierzone wartości dysku i RAM osobno, zakres wykonanych testów oraz najbliższy ograniczony test odbiorczy.

Strona migracji przygotowuje manifest ACTIVE / ARCHIVE / UNRESOLVED, domyka zależności i mierzy pakiet. Prywatne ścieżki i pełny manifest pozostają prywatne. Następnie staging bez NOUT1 musi wykonać natywną misję, restart/wznowienie i sprawdzenie odwołań do odtwarzalnego archiwum.

## Pochodzenie i granice publikacji

Źródła: raport operatora audytu skilli R2, SHA-256 `e837c80f03939506430cf6c66f422d8b61a80e4edd17ed64863a89da1e3c1ef6`; raport preflight 80 GB, SHA-256 `d5523703f67721cbe48f95bb0a7bd25272bf57e65c9c6255d3670138f44da021`; publiczne commity MultiQuant wymienione w JSON.

Nie wykonano świeżych testów na serwerach, migracji produkcyjnej, promocji skilli ani odbioru backup/restore całego SSI. Publikujemy decyzje, wyniki i ograniczenia; kod, bazy, prywatne ścieżki, adresy infrastruktury i know-how pozostają poza publikacją.
