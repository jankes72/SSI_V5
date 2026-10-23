# SSI BLOKS — plan i punkt wznowienia (18.10.2026)

Status: dokument kierunkowy. Migracja produkcyjna: NOT_READY.

> **Aktualizacja 23.10.2026:** przygotowanie środowiska Dyrektora i testy M8R1 zostały wykonane. Obowiązujący punkt kontynuacji jest po zaliczonym M8R1, nie przed transferem kodu. Zobacz [raport migracji M1–M8R1](../RESULTS/SSI_DIRECTOR_MIGRATION_M1_M8R1_20261023.md) i dopisek na końcu tego dokumentu. Poniższe starsze etapy zachowano jako historię; pełne przełączenie produkcyjne nadal nie zostało odebrane.

## Trzy rownolegle obszary
1. **BLOKS Warehouse**: katalogowanie historycznych zasobow, rodowod, warianty, integralnosc, kwalifikacja, zaleznosci i bezpieczny reuse.
2. **BLOKS MultiControl Global**: wspolny mechanizm kontroli kompozycji dla Dyrektora, CODEX-a, Roberta, mikrosieci, MultiQuant i laboratoriow. Tryb SHADOW_ONLY: kontroluje, proponuje i zglasza HOLD, ale nie wykonuje misji ani nie modyfikuje rejestrow.
3. **SCC Integration**: zgodne polaczenie z istniejacym natywnym jezykiem SCC, parserem i kontraktami, bez zastapienia ich nowym systemem.

## Trwale ustalenia
- Nowa nazwa **BLOKS**; dawne nazwy zostaja tylko w historycznych artefaktach dla kompatybilnosci.
- Mikrosieci powstaly przed LEGO Decomposer/Pocket/META; tamte mechanizmy sluzyly odkrywaniu, rozkladowi, kwalifikacji i ponownemu wykorzystaniu.
- Zachowujemy historyczne ID oraz wszystkie warianty. ID bez hasha moze byc niejednoznaczne; wowczas HOLD zamiast automatycznego wyboru.
- Identyczna nazwa symbolu lub wspolny projekt nie potwierdza krawedzi zaleznosci; trzeba sprawdzic import, definicje, pochodzenie i kontrakt.
- Rejestry Championow mikrosieci, Pocket i MultiQuant pozostaja oddzielne, bez domniemanego mapowania i automatycznych promocji.
- Dyrektor odpowiada za misje i decyzje; CODEX i Robert maja odrebne role. MultiControl nie zastępuje Routera, SCC, notariusza ani autoryzacji.
- Cel migracji: niezalezne serwery Dyrektor, CODEX, Robert; lokalne maszyny jako opcjonalne rozszerzenia. Chronimy prywatne archiwa i kod.
- Publiczny GitHub: dokumentacja kierunkowa, wyniki zbiorcze i dowody bez kodu prywatnego, sekretow lub inwentarzy.

## Udokumentowany stan R9.121
- 15417 rekordow historycznego magazynu, 15415 unikalnych ID; dwa ID maja po dwa odrebne warianty.
- Dwa magazyny: indeksy identyczne SHA-256; 15417/15417 plikow indeksowanych poprawnych w kazdym (audyt R9.118).
- 7146 rekordow z zaleznosciami, razem 24249 wpisow; w tym 10832 prostych nazw symboli.
- R9.121: 6561 pojedynczych kandydatow ze wspolnego projektu, 1946 wielokrotnych, 2325 bez wspolnego projektu, 16 bez zgodnej nazwy. To kandydaci, NIE potwierdzone polaczenia.
- Produkcyjny binding natywnego SCC: NIEPOTWIERDZONY.
- Gate produkcyjny: NOT_READY.

## Najblizszy krok
R9.122: Warehouse bada statycznie definicje i importy; MultiControl waliduje propozycje i warianty offline; SCC Integration bada kontrakty i punkty integracji. Wymagane testy, shadow-parity, dowody, kontrola uprawnien, rollback i jawna decyzja przed wdrozeniem.

**Punkt wznowienia:** kontynuowac trzy tory rownolegle, nie przepisywac historycznych danych i nie uznawac wyniku shadow za wdrozenie produkcyjne.


---

## Aktualizacja migracyjna — R9.122–R9.134 (18.10.2026)

**Cel:** zachować istniejące mechanizmy i domknąć integrację, a nie odbudowywać działające funkcje. Poniższe wyniki pochodzą z audytów statycznych i przekazanych raportów; nie stanowią potwierdzenia wdrożenia produkcyjnego.

### BLOKS Warehouse i MultiControl Global

- R9.122–R9.130: analizowano 10 832 odwołania do prostych symboli w historycznych artefaktach. Ustalono, że same zbieżności nazw, projektów i importów nie są wiarygodnym dowodem krawędzi wykonawczych.
- R9.126: analiza większych źródeł zmniejszyła liczbę przypadków bez dostępnego kontekstu źródłowego do 6. Pozostałe przypadki wymagają kwalifikacji semantycznej, nie są dowodem uszkodzenia magazynu.
- R9.128–R9.129: odnotowano 6 307 deklaracji na poziomie modułu, 26 powiązań lokalnych składniowo, 4 493 bez lokalnego powiązania i 6 bez kontekstu. To klasyfikacje audytora, nie potwierdzone przejścia mikrosieci.
- R9.130: inwentaryzacja importów wykazała tysiące deklaracji w źródłach, ale zero zatwierdzonych powiązań z deklaracjami BLOKS. Uznano, że należy szukać rzeczywistych reguł routingu i rejestrów, zamiast mnożyć heurystyki.
- MultiControl Global nadal pracuje w trybie **SHADOW_ONLY / HOLD_FOR_VERIFIED_BINDINGS**: proponuje i kontroluje, bez mutacji rejestrów lub zgody na wykonanie.

### Router V10, S10, kompetencje i powiązania misji

- R9.131: rozpoczęto ukierunkowane badanie historycznych routerów, skilli i rejestrów. Wynik był częściowy wskutek ograniczeń czasu i liczby kandydatów.
- R9.132: analiza statyczna potwierdziła istnienie interfejsów Routera V10 związanych z podejmowaniem decyzji, uczeniem na rezultatach, rozgrzewaniem i podsumowaniem; wskazała również mechanizmy cache tras, podobieństwa, pewności, wyboru kontekstowego, kwalifikacji i wymiany Championów.
- R9.133: znaleziono statyczne odwołania runtime do Routera V10 i resolvera kompetencji, w tym konstrukcję obiektu routera. **Nie oznacza to potwierdzenia działającego procesu ani pełnego przebiegu misji.**
- R9.134: odnaleziono ślady Research Memory, Notariusza, CONTINUUM, kompetencji i rejestrów. Audyt miał ograniczenia czasu/kandydatów; pełna mapa wywołań i przepływu dowodów nadal pozostaje do potwierdzenia.
- **S10** traktujemy jako historyczny obszar mikrosieci i mechanizmów kwalifikacji; nie zakładamy istnienia odrębnej usługi „Router S10” bez dowodu w źródłach.

### Decyzje architektoniczne

1. **Nie pobierać i nie przebudowywać CONTINUUM bez konieczności.** To starszy istniejący moduł SSI: należy jedynie potwierdzić zgodność wersji i aktywne powiązania z obecnym runtime.
2. **Research Memory nie jest tym samym co Richter's Memory.** Badamy istniejącą pamięć i jej powiązania z Routerem V10, kompetencjami, Championami, Notariuszem oraz historią misji.
3. **Nie przenosić Routera V10 bez otaczających mechanizmów:** notaryzacji, uprawnień, checkpointów, rejestrów, odtwarzania stanu i dowodów.
4. **SCC ma odczytywać możliwości i decyzje istniejącego routera przez zgodny adapter**; nie dublujemy algorytmów routingu i nie przebudowujemy natywnego parsera.
5. **Richter's Memory pozostaje ostatnim etapem** — jego integrację planujemy dopiero po rozstrzygnięciu istniejących połączeń.
6. Docelowo **trzy niezależne VPS** obsługują Dyrektora, CODEX-a i Roberta; urządzenia lokalne są rozszerzeniami i zapleczem danych. Zachować osobne rejestry Championów, centralne logowanie i istniejące mosty.
7. Publiczne repozytorium utrzymuje tylko plan, neutralne metryki i dowody; nigdy prywatne źródła, sekrety, lokalne ścieżki lub pełne operacyjne inwentarze.

### Bramy i kolejność działań

- **R9.135:** wąski, tylko-odczytowy audyt rzeczywistych punktów integracji Router V10 ↔ Research Memory ↔ Capability Resolver ↔ Notariusz; CONTINUUM wyłącznie jako istniejąca zależność, bez ponownego wdrożenia.
- **R9.136:** zgodny adapter SCC ↔ Router V10 + kontrola BLOKS MultiControl; test misji w trybie SHADOW_ONLY z identyfikatorami, dowodami i izolacją.
- **R9.137:** analiza i integracja Richter's Memory jako osobnego, ostatniego etapu.
- **Po etapach:** preflight VPS obejmujący backup, procedurę rollback, shadow parity, zgodność interfejsów, autoryzację, notariusza, kosztorys i brak zależności krytycznych od maszyn lokalnych.

**Aktualny gate:** `NOT_READY`. Należy odróżniać znaleziony kod, statyczny punkt wywołania, test offline i aktywne działanie produkcyjne. Żaden z nich nie zastępuje pozostałych.

**Punkt wznowienia:** R9.135 — tylko brakujące połączenia, żadnych pełnych skanów katalogów ani przebudowy historycznych modułów.

---

## Doprecyzowanie migracji — Organizer, Świat piłki i Hipnoza (18.10.2026)

**Podstawa:** bieżąca decyzja właściciela oraz ponownie odczytany [Football World / Świat Hipnozy 01 — status z 16.09.2026](../FOOTBALL_WORLD_CURRENT_STATUS_20260916.md), w szczególności sekcje „Existing Football organizer as source” i „Director integration”. Dokument źródłowy opisuje sąsiedni Organizer jako źródło odczytywane przez adapter; nie jest dowodem dzisiejszego odbioru VPS. Ogólne zasady ciągłości pozostają w [planie migracji serwerowej](../SSI_V5_MIGRACJA_SERWERY_ROBERT_R1_20261017.md).

### Rola i położenie

`Organizer_swiat_Pilki` jest wymaganym zasobem danych domenowych dla interfejsu „Świat piłki” / „Hipnoza”, historycznie opisanego jako Football World / Świat Hipnozy 01. Nie klasyfikować całego katalogu jako archiwum do pozostawienia wyłącznie na MSI, nie utożsamiać go z SCC Memory ani z dodatkowym aktorem. Zachować jego własną historię i autorstwo Pawła Jankiewicza.

Docelowo katalog ma być w uzgodnionym wspólnym drzewie SSI, obok środowisk aktorów wdrażanych na danym serwerze oraz historycznego magazynu `lego_poket`. Nie wkładać go do pamięci jednego agenta ani do starej zagnieżdżonej kopii instalatora. Nie zmienia to przydziału Roberta, CODEX-a lub modeli do innych uzgodnionych serwerów i nie scala pamięci aktorów. Dokładna ścieżka wdrożeniowa oraz mapowanie ewentualnego wolumenu należą do prywatnego manifestu.

### Powiązanie z interfejsem i wykonaniem

W manifeście zachować relację: wejście „Świat piłki” / „Hipnoza” w interfejsie → właściwy istniejący backend/obserwator świata → adapter źródła → kanoniczny Organizer. Rzeczywiste identyfikatory tras, konfigurację i punkt montowania ustalić z działającego wydania; nie wymyślać nowych endpointów. Samo sąsiedztwo katalogów nie zastępuje konfiguracji czytnika.

Zachować opisany w źródle adapter tylko do odczytu. Stan świata i prywatne historie aktorów pozostają oddzielne; współdzielenie źródła nie oznacza dowolnego prawa zapisu dla wszystkich agentów. Brak albo niedostępność wymaganego źródła ma być widoczna jako `NOT_CONNECTED` dla tej funkcji, bez pustej bazy zastępczej, cichego przełączenia na starą kopię lub udawanego sukcesu. Nie blokować z tego powodu niezależnych misji SSI.

SCC ma korzystać z istniejących uprawnionych operacji świata przez zgodny adapter, a nie samodzielnie otwierać dowolne pliki Organizera. Powiązania z S10/V10, mikrosieciami i Research Memory zachowują dotychczasowe kontrakty i zasady kwalifikacji; ten dopisek nie dowodzi ich wykonania ani nie uruchamia ponownego FLOW.

### Istniejąca kopia i utrzymanie

Właściciel zgłosił wcześniejsze przesłanie Organizera na serwer. Zachować tę kopię i rozliczyć ją przed kolejnym transferem. **Bez ponownego wysyłania całego katalogu, nadpisywania baz, usuwania plików lub tworzenia drugiego Organizera na podstawie samego rozmiaru folderu.** Najpierw potwierdzić docelową lokalizację, zawartość, wersję i właściciela zapisów; nie ogłaszać transferu zweryfikowanego bez odpowiedniego dowodu.

Objąć ten zasób monitoringiem, kopią zapasową i cotygodniowym przeglądem utrzymania. Kontrola ma rozróżniać dostępność katalogu, możliwość odczytu przez właściwą usługę i rzeczywisty odczyt danych przez interfejs. Retencja logów nie uprawnia do usuwania danych Organizera. MSI pozostaje włączonym archiwum/panelem/warsztatem; operacyjny dostęp serwerowych funkcji świata nie może opierać się wyłącznie na lokalnej kopii MSI.

### Kryteria odbioru tego powiązania

1. Prywatny manifest wskazuje jeden kanoniczny Organizer i jego właściwe położenie przy środowiskach SSI; wcześniej przesłana kopia została rozliczona bez utraty danych.
2. Oba wskazane wejścia interfejsu korzystają z właściwego zasobu przez istniejącą usługę/adapter, a nie z pustego lub historycznego zamiennika.
3. Odczyt zachowuje identyfikatory i historię; uprawnienia nie rosną wskutek wspólnego katalogu. Adapter obserwacji nie modyfikuje źródła.
4. Test braku źródła pokazuje jawny brak połączenia; restart przywraca właściwe powiązanie. Sam HTTP 200 nie oznacza poprawnego odczytu świata.
5. Backup i odtworzenie obejmują spójny stan wymaganych baz, plików i odniesień. Monitoring raportuje ten zasób osobno.

**Stan tego dopisku:** wymaganie migracyjne zapisane; bez przenoszenia danych, zmian usług lub potwierdzenia produkcyjnej integracji. Nie są to wykonane testy.

**Punkt kontynuacji:** rozliczyć istniejącą kopię Organizera i jej powiązanie z interfejsem w bieżącym wydaniu migracyjnym, zamiast traktować serwer jako pusty lub ponawiać szerokie skanowanie całego SSI.

---

## Wykonana migracja u Dyrektora — aktualizacja 23.10.2026

Pełny zapis etapów i ich granic: **[SSI DIRECTOR — M1–M8R1](../RESULTS/SSI_DIRECTOR_MIGRATION_M1_M8R1_20261023.md)**. Podstawą są raporty i terminal operatora, nie nowe testy wykonane przy publikacji notatki.

**Wykonano:** transfer i weryfikację 1595 plików kodu, kontrolowaną poprawkę i złożenie kopii, uruchomienie odbiorowego WWW, przywrócenie Hermesa przed logowaniem z kontrolą przypięcia modelu, transfer 17 archiwów MultiQ i przygotowanie 45 plików kandydatów. M8R1 zaliczyło izolację i **107 testów na VPS: 23 + 39 + 16 + 29**.

**Aktualny punkt kontynuacji: `M8R1_NATIVE_CONTRACTS_VERIFIED_SHADOW_ONLY`.** Nie powtarzać zaliczonych etapów ani budować zastępczego SCC, routerów lub pamięci. Następne zadanie to jedna rzeczywista, uprawniona ścieżka obserwacyjna misji i powiązanie jej wyników z istniejącymi rejestrami i Research Memory. R9 pozostaje doradcą, a `HOLD_NO_ELIGIBLE_MODEL` nie jest awarią ani zgodą na domyślną kwalifikację modeli.

Wynik 107 PASS dotyczy kontraktów, syntetycznych zadań i jednorazowych baz. Nie stanowi testu jakości LLM ani pełnego odbioru V10/S10, wszystkich mikrosieci, zakładek i mostów. Generowanie odpowiedzi Hermesa i pełny cykl rzeczywistego konta mają osobny odbiór. ZIP z najnowszym wynikiem M8R1 nie został jeszcze odczytany; podstawą tej liczby jest terminal właściciela.

**Późniejsze uzgodnienie ról serwerów:** DIRECTOR — Dyrektor i Universal Lab; ROBERT — Robert oraz niezależny CODEX; MODELS/CORE24 — usługi modeli. Zastępuje to wcześniejszy plan osobnego VPS CODEX-a, bez deklarowania ukończonego wdrożenia wszystkich wykonawców. MSI nadal działa jako panel, archiwum i warsztat, NODE-01 jest opcjonalnym rozszerzeniem, Lenovo pozostaje poza aktywną infrastrukturą. Wycofany SSI Start nie jest przywracany.

**Nadal do odbioru:** rzeczywiste kwalifikacje i połączenia misji, pełny zakres Universal Lab z konferencją, tłumaczeniami i uprawnieniami, pamięci i mikrosieci, Organizer, ciągłość Notariusza, backup/odtworzenie, monitoring oraz cotygodniowe utrzymanie. Nie kopiować ponownie Organizera w ciemno, nie resetować kont, nie podpisywać zaległości nowym kluczem i nie powtarzać dawnych misji.

**Pełne przełączenie produkcyjne: niewykonane / `NOT_READY`.** Aktualizacja dokumentacji nie zmienia usług, modeli, baz ani publicznego przekierowania.
