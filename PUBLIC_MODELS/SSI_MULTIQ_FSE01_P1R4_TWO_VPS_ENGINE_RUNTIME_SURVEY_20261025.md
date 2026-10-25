# SSI MultiQuant FSE-01 — P1R4: rzeczywisty przegląd punktów wejścia na dwóch VPS

**Data:** 2026-10-25  
**Dowód:** operator wkleił pełny wynik komendy MSI→2 VPS; publikacja nie oznacza samodzielnego SSH ani instalacji wykonanej przez autora raportu.  
**Status:** `P1R4_STATIC_AND_SERVICE_INVENTORY_COMPLETE / CANONICAL_MULTIQ_ENGINE_NOT_IDENTIFIED / FSE_P2_NOT_RUN`.  
**Zmiany:** `MODEL_EXECUTION=NO` oraz `PRODUCTION_CHANGES=NONE` według logu operatora.

## Odczyt na pierwszym VPS (rola MultiQuant/Robert)

- Odpowiedziała maszyna powiązana z historycznym węzłem materiałów R20/R21.
- **Jedyna wykazana w filtrze SSI aktywna usługa:** tunel do API modeli; usługa ma aktywny PID.
- Odczyt katalogów ograniczony do wskazanych lokalizacji wykazał historyczny kandydat runtime ROBERT, źródła migracyjne, oddzielny runtime testowy i przygotowawczy, środowisko Offline MICRO oraz drzewa źródeł R20, L21, R21. **Obecność kandydata Roberta nie dowodzi aktywacji workera Roberta.**
- W czterech wskazanych katalogach managerów odczyt wykazał dwa pliki `01_R20_SOURCE_MANAGER.py` (odpowiednio **22 566 B**, **23 146 B**) oraz `01_R21_MANAGER.py` (**17 572 B**). Nie potwierdza to aktywnego silnika misji.
- W części `ACTIVE RUNTIME PROCESSES` nie było pasujących wierszy z **ograniczonego filtra nazw procesów**. Nie jest to pełny inwentarz procesów wszystkich nazw ani dowód braku kodu MultiQuant na dysku.
- W badanym podzbiorze nazw nie wykazano usługi `MultiQuant engine/worker/API`. Nie wykonywano menedżerów.

## Odczyt CORE24 — modeli i wykonawców

- **Ollama**: aktywny PID; **CORE24 API**: aktywny PID **40868**; **CORE24 Worker**: aktywny PID **40867**, oba procesy Python3.
- Dla obu usług API/Worker wskazano wspólny katalog roboczy `/opt/ssi-core24/current`; to silna przesłanka istnienia używanej instalacji wykonawczej, **nie** potwierdzenie, że implementuje autorskie moduły MultiQuant.
- Istnieją katalogi MultiQuant, jego wariantu V7 oraz wielu historycznych laboratoriów SCC/quant/AB i R8/R9.
- W sekcji `CANDIDATE ENGINE FILES` na dwóch korzeniach MultiQuant nie znaleziono pliku pasującego do ograniczonego wzorca nazw, ale skrypt nie objął pełnym przeglądem `/opt/ssi-core24/current` i katalogów eksperymentalnych.
- Wcześniejszy P1C znalazł rzeczywisty plik `llama-cli` w osobnym drzewie kompilacji MultiQuant na CORE24, a P1 plik 70B IQ2_XXS **19 097 389 632 B**. Żaden z tych faktów sam w sobie nie potwierdza autorskiej ścieżki silnika FSE.

## Ograniczenia i wniosek

**P1R4 wyraźnie zawęża następne poszukiwania do uruchomionego API/Workera CORE24 oraz istniejących, lecz nieprzypiętych do działającej usługi źródeł R20/R21 i archiwum eksperymentów.** Nie ma podstaw do przypisania nazwy `MultiQuant Engine` do któregokolwiek aktywnego Pythona bez sprawdzenia jego kodu startowego, klas i kontraktów.

Pomiary transportu z wcześniejszego audytu: 3/3 MSI→VPS SSH, 6/6 między-VPS TCP22, 3/3 HTTP 200 `/api/version`. **To nie jest FSE mission readiness.**

**Nowy raport migracji w prywatnym repozytorium** (`3aa80003fc5faec6172283f4a2a6c9fddbab327f`, 25.10) utrwala poprzedni dowód łączności trzech VPS, lecz nadal oznacza natywne SCC/MultiQuant routing, Roberta, 80 GB i pełny backup/restore jako PENDING. Nie traktujemy prywatnego repozytorium jako publicznego źródła kodu.

## Kolejna bramka P1R5 — tylko odczyt

1. Dla aktywnych jednostek CORE24 API i Worker: odczytać `MainPID`, `WorkingDirectory`, **zanonimizowaną klasę startu** (program + nazwa modułu lub pliku, bez argumentów i sekretów), pliki `.py` z aktualnego katalogu roboczego oraz nazwy interfejsów AST. **Nie uruchamiać modelu ani nie importować skryptów.**
2. Przejrzeć płytko katalogi projektowe R15/R21/CORE24 na obu węzłach, wykrywać `manager/engine/adapter/worker/router/scc` z ograniczonym budżetem odczytu, pamiętać o prefiksach `01_R...`.
3. Wskazać **jeden** autorytatywny `MultiQuant entrypoint`, konkretną wersję/commit i istniejący adapter do modelu 70B oraz SCC. Gdy brak — jawnie `ENGINE_NOT_DEPLOYED` i dopiero potem oddzielna decyzja wdrożeniowa.
4. Po przeglądzie wykonać osobno tylko **jedną nieprodukcyjną misję FSE** z `mission_id`, checkpointem, ACL, realnym dowodem wejścia do autorskiego modułu i rezultatem z CORE24/Evidence.
5. Nie nazywać bezpośredniego `llama-cli` produktem FSE, nie promować niezweryfikowanych modułów i nie dublować parsera SCC.

## Powiązane źródła

- [FSE P1R3 — zgodność katalogu modeli](SSI_MULTIQ_FSE01_P1R3_MODEL_INVENTORY_PARITY_OPERATOR_20261025.md).
- [Wspólna macierz trzech VPS](SSI_FSE01_THREE_VPS_NETWORK_WEBSHOP_ACCEPTANCE_R1_20261025.md).
- [FSE-01 — korekta routingu](SSI_MULTIQ_FSE01_SERVER_ROUTING_CORRECTION_R1_20261025.md).
- [Raport transportu i odpowiedź migracji](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [Odpowiedź modelu migracyjnego](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).

**Granica publiczna:** bez IP, kluczy, konfiguracji tuneli, prywatnych wrapperów, kodu i pełnych ścieżek środowiska. Szczegółowy operatorski log pozostaje na MSI.
