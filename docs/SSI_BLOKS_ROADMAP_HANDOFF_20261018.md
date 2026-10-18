# SSI BLOKS — plan i punkt wznowienia (18.10.2026)

Status: dokument kierunkowy. Migracja produkcyjna: NOT_READY.

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
