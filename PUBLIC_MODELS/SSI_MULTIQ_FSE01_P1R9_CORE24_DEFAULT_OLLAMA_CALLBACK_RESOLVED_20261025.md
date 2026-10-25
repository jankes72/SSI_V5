# SSI MultiQuant FSE-01 — P1R9: domyślny backend CORE24 Workera zidentyfikowany

**Data:** 2026-10-25  
**Dowód:** pełny wynik read-only audytu AST z MSI na CORE24 dostarczony przez operatora. Autor raportu nie łączył się SSH, nie wykonywał inferencji.  
**Status:** `P1R9_DEFAULT_WORKER_CALLBACK_STATIC_PASS / DEFAULT_BACKEND_OLLAMA_CHAT / CANONICAL_MULTIQ_ENGINE_PENDING / FSE70B_NOT_RUN`.  
**Zmiany produkcyjne:** operator potwierdził `MODEL_EXECUTION=NO` i `PRODUCTION_CHANGES=NONE`.

## Rozstrzygający wynik P1R9

- `runtime.worker_loop` deklaruje parametry `once, ask, storage`; domyślny `ask` ma wartość **`None`**, podobnie `storage`. Wartość domyślna `once` została zredagowana.
- W ciele `worker_loop` AST potwierdził przypisanie **`adapter = ask or ollama_chat`**, jako `BoolOp:Or` z operandami `Name:ask` i `Name:ollama_chat`.
- W pliku `__main__.py` istniejący punkt wejścia wywołuje `worker_loop` z **0 argumentów pozycyjnych** i tylko **argumentem nazwanym `once`**; **`ask` nie jest tam przekazywane**.
- Wcześniejszy P1R8 potwierdził wywołanie `_perform(s, adapter, prev)`, a `_perform` korzysta z `ask(job[...], job[...])`.

**Wniosek:** dla odczytanego źródła aktywnego pakietu `ssi_core24` domyślnie uruchamiany Worker (`python3 -m ssi_core24 worker`) używa `ollama_chat` jako callbacku do komunikacji z backendem, ponieważ `ask=None` i `None or ollama_chat` wybiera `ollama_chat`. Konstrukcja pozwala *programistycznie* podać inny callback, ale **nie potwierdza, że jakikolwiek autorski adapter MultiQuant został już wdrożony lub wywołany**. To jest ocena kodu i punktu wejścia, nie ślad przeprowadzonej misji.

## Wnioski architektoniczne

1. CORE24 jest rzeczywistym endpointem wykonawczym **API → routing → kolejka SQLite → Worker → Ollama**, nie zidentyfikowanym kanonicznym autorskim silnikiem MultiQuant.
2. Dla FSE-01 rozróżnić **MultiQuant offline** (Q/D i przygotowanie wag modelu) od opcjonalnych **modułów on-mission** (np. kontrola jakości, routing, pamięć, segmentowe Q/D); w żadnym przypadku nazwa `engine.py` CORE24 nie czyni z niego automatycznie autorskiego MultiQuant.
3. 70B IQ2_XXS GGUF jest osobnym plikiem ~19,1 GB na CORE24 i **nie był zarejestrowany jako jeden z wcześniejszych 13 tagów Ollama**. Obecny callback `ollama_chat` sam nie dowodzi, że wybrany GGUF jest dostępny w trwającej ścieżce wykonania.
4. Wymóg właściciela: **SSI DIRECTOR/SCC/Router → kanoniczny MultiQuant na pierwszym VPS → model na CORE24 → Evidence/Notariusz**. Przepływ nadal nie ma zweryfikowanego punktu wejścia autorskiego silnika.
5. Po zakończeniu P1R9 **nie powtarzać** mini-audytów CORE24 callbacku; następny etap to **odnalezienie oryginalnego kodu/artefaktów MultiQuant**, jego wersji, procesu/CLI i istniejącego (albo brakującego) adaptera na właściwym VPS.

## Następna bramka — P1R10: kanoniczny MultiQuant

**Read-only / no GPU / no inference:** porównać konkretne źródła i manifesty offline-Q/D na pierwszym VPS MultiQuant i CORE24; wskazać jeden autorytatywny pakiet, punkt wejścia, wersję/commit, rodzaj operacji (offline model build vs runtime module), status zainstalowania i możliwą trasę do CORE24. W razie braku autorskiego silnika na pierwszym VPS zgłosić `MULTIQ_ENGINE_NOT_DEPLOYED`, nie zastępować go menedżerem źródeł R20/R21, Workerm CORE24 ani gołym `llama-cli`.

Potem: kontrolowany, jawnie zaakceptowany staging bez ingerencji w produkcję, pojedyncza misja natywnego SCC z mission ID, ACL, checkpoint/recovery i Evidence, a dopiero na końcu porównanie CPU 70B plain vs faktycznie aktywne moduły MultiQuant przy tych samych warunkach.

## Ścieżka dowodowa

- [P1R8: miejsce wstrzykiwania callbacku](SSI_MULTIQ_FSE01_P1R8_CALLBACK_INJECTION_DISCOVERY_20261025.md).
- [P1R7: graf wywołań CORE24](SSI_MULTIQ_FSE01_P1R7_CORE24_HASHED_CALL_GRAPH_20261025.md).
- [P1R6: runtime i importy](SSI_MULTIQ_FSE01_P1R6_CORE24_STATIC_IMPORT_CALL_GRAPH_20261025.md).
- [Akceptacja 3 VPS](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [Odpowiedź migracji](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).
- [Issue #5 FSE-01](https://github.com/jankes72/SSI_V5/issues/5).

**Granica publikacji:** bez konfiguracji hostów, prywatnego kodu, kodu kwantyzacji, surowych logów, adresów, dostępu lub danych klientów.
