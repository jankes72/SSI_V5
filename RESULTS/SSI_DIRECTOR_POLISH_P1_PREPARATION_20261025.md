# SSI DIRECTOR — przygotowanie Polish P1

**Data:** 2026-10-25  
**Status:** `PREPARATION_ONLY / HOST_AUDIT_PENDING / NO_PRODUCTION_ACTIVATION`  
**Punkt odniesienia:** [MultiQuant FSE P1R8, commit 0d3e3cb](https://github.com/jankes72/SSI_V5/commit/0d3e3cbe5126d5c764d7c4fce78442ee979e3f0e).

Użytkownik zlecił równoległe dopracowanie Dyrektora podczas pracy toru MultiQuant. „Polish” oznacza tutaj dopracowanie i odbiór istniejącego SSI. Jest to plan i przygotowanie narzędzia odczytu, bez deklaracji wdrożenia lub gotowości pierwszego produktu.

## Uzupełnienie: zatwierdzony wynik kontroli

**[Podsumowanie P1 zatwierdzone do publikacji](SSI_DIRECTOR_POLISH_P1_APPROVED_REVIEW_20261025.md)** potwierdza 5/5 plików zgodnych z M9 i wskazuje brak integracji wykonawcy oraz weryfikacji dowodów w zbadanej ścieżce A26. Odczyt plików wykonano; powiązanie z aplikacją, kompletna misja i budżet 80 GB pozostają otwarte. Poniżej zachowano wcześniejszy plan jako historyczny punkt wyjścia.

## Stan wyjściowy i podział prac

- [Checkpoint migracji](SSI_MIGRATION_CHECKPOINT_20261025.md): M8R1 — **107 testów kontraktowych PASS / SHADOW_ONLY**. M9 — przygotowane materiały, bez wykonanych szkoleń w tamtym etapie; historia wymaga rozliczenia.
- [Manifest R1](SSI_CORE_MANIFEST_R1_REVIEW_20261025.md): **78,30 GB** to szeroki wariant planistyczny po osobnym wydzieleniu historii Git, przed rezerwą i narzutem. Nie jest rozmiarem odebranego rdzenia ani pomiarem zwolnionego miejsca.
- [MultiQuant P1R8](../PUBLIC_MODELS/SSI_MULTIQ_FSE01_P1R8_CALLBACK_INJECTION_DISCOVERY_20261025.md): potwierdzono statyczny punkt callback wykonawcy CORE24. Tożsamość rzeczywiście wiązanego adaptera wymaga rozstrzygnięcia; nie jest to potwierdzenie aktywnego MultiQuant ani wykonania 70B.
- Tor Dyrektora przygotowuje powiązania rodzimego SCC, Routera, Research Memory, kompetencji, uprawnień, checkpointów i Evidence. Tor MultiQuant identyfikuje silnik i adapter wykonawczy. Oba tory zachowują własne wyniki do wspólnej próby misji.

## Przygotowane teraz

Przygotowano prywatną paczkę kontrolną P1 uruchamianą z MSI przez istniejącą konfigurację SSH Dyrektora. Tożsamość serwera jest porównywana z wcześniejszym prywatnym punktem odniesienia przed odczytem usług. Paczka nie zmienia konfiguracji SSH ani nie akceptuje automatycznie nowego klucza hosta.

Zakres to metadane do 48 systemowych usług SSI i statyczny odczyt do 160 kandydatów Python, po maksymalnie 2 MiB. Raport zawiera hashe, importy, nazwy definicji i kandydackie ścieżki; prywatny kod nie trafia do tego repozytorium. Nie odczytuje baz ani środowiska procesów i nie zapisuje surowych parametrów startowych.

**10 lokalnych testów narzędzia PASS.** Sprawdzają m.in. odmowę odczytu na niewłaściwym hoście, ograniczenie wielkości, analizę bez wykonania kodu i pominięcie wartości parametrów startowych. To testy narzędzia na danych syntetycznych, nie nowe testy kontraktowe Dyrektora ani odczyt VPS. **Paczka nie została wykonana na serwerze w tym etapie.**

Brak kandydata pod jedną ścieżką nie dowodzi braku komponentu. Import lub obecność pliku nie dowodzą aktywnego powiązania. Usługi użytkownika, endpointy aplikacji, kolejki, współbieżność i odtworzenie pozostają poza kontrolą P1. W przypadku nierozpoznanego wrappera potrzebny będzie punktowy dalszy odczyt.

## Kolejność dopracowania i wymagany dowód

| Etap | Konkretna praca | Wymagany odbiór | Obecny status |
|---|---|---|---|
| P1 — punkt startu | Powiązać usługę i rewizję z właściwym SCC, Routerem i pamięcią; odróżnić pliki przygotowane od aktywnych | Metadane oraz hashe źródeł, następnie potwierdzenie rzeczywistego wywołania | Narzędzie przygotowane; odczyt hosta oczekuje |
| P2 — główne kompetencje | Wybrać wersjonowaną bazę głównych skilli wraz z kodem, danymi i zależnościami | Ślad pochodzenia; dowód dla konkretnej wersji; zachowane tożsamości aktorów i statusy rejestrów | Oczekuje; historyczne QUALIFIED nie zastępuje odbioru obecnego wykonania |
| P3 — historia i szkolenia | Uzgodnić materiały M9 z kanoniczną historią i kolejką | Wykaz wykonanych, przerwanych i nowych przypadków, bez automatycznego replay na podstawie brakującego wpisu | Oczekuje |
| P4 — odporność | Sprawdzić checkpoint, odtworzenie i ponowienie tej samej misji | Zachowany identyfikator, ciągłość Evidence, brak podwójnych skutków po retry | Oczekuje |
| P5 — wspólny produkt | Połączyć rodzimy kontrakt SCC i Router z wersjonowanym adapterem MultiQuant oraz wykonawcą | Jedna rzeczywista nieprodukcyjna misja ze skorelowanym wynikiem i dowodem wywołania modułu | Zależne od ustaleń drugiego toru |
| P6 — dysk i niezależność | Złożyć kompletny aktywny rdzeń, wyodrębnić archiwum, zmierzyć narzut i rezerwę | Rdzeń + wymagany narzut + 10 GB zapasu ≤ 80 GB; misja i wznowienie przy niedostępnym MSI/NODE01, z dostępnymi wymaganymi VPS/API | Oczekuje |

W istniejących kontraktach trzeba potwierdzić odpowiedniki identyfikatora misji, rewizji kontraktu, checkpointu i Evidence, limitów zasobów oraz uprawnień. To lista wymagań odbioru, **nie nowy schemat SCC ani zmiana nazw pól**. LangGraph i n8n pozostają planowanymi adapterami; samo przygotowanie tej listy nie wdraża ich.

Próby odmowy uprawnień, przekroczenia czasu, niedostępności wykonawcy i powtórzenia requestu muszą zachować jednoznaczny stan zadania. Model bazowy i wariant MultiQuant mają osobne wyniki jakości, czasu, pamięci oraz kosztu. Dostępność HTTP 200 pozostaje odrębnym dowodem transportowym.

## Punkt współpracy z MultiQuant

Wspólna kolejność odbioru z [wcześniejszej odpowiedzi migracji](SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md) pozostaje: **NETWORK_BASIC_PASS → APP_ROUTING_PASS → E2E_SCC_MULTIQ_WEBSHOP_PASS**. Przygotowanie P1 nie nadaje żadnego z tych statusów.

Do spięcia potrzebne są: kanoniczna wersja silnika/adaptera, wskazanie istniejącego kontraktu i punktu wywołania, obsługa wyniku/błędu oraz korelacja z checkpointem i Evidence. Szczegóły infrastruktury i kod pozostają w prywatnym przekazaniu. Przed łączeniem należy ponownie odczytać najnowszy commit i indeks.

**W tym etapie:** brak zmian usług, uruchomień modeli lub szkoleń, usuwania plików, przenoszenia archiwów, promocji skilli i aktywacji produkcyjnej. Rozmiar gotowego rdzenia i pełna misja nadal niepotwierdzone.
