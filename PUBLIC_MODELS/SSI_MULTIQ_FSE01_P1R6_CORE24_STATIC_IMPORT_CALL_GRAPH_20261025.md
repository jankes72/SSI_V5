# SSI MultiQuant FSE-01 — P1R6: statyczna mapa aktywnego pakietu CORE24

**Data:** 2026-10-25  
**Dowód:** pełny wynik operatora z read-only analizy `ast` oraz `/proc` wykonanej przez SSH z MSI na CORE24. Autor raportu nie wykonywał połączenia SSH i nie ma własnego pomiaru hardware.  
**Status:** `CORE24_API_WORKER_ENTRYPOINTS_CONFIRMED / NO_DIRECT_MULTIQ_IMPORT_IN_SCANNED_PACKAGE / CANONICAL_MULTIQ_ENGINE_UNVERIFIED / FSE_P2_NOT_RUN`.  
**Zmiany:** operator zgłosił `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE`.

## Potwierdzone procesy

| Jednostka | PID w logu operatora | Uruchomiony moduł | Podpolecenie |
| --- | ---: | --- | --- |
| `ssi-core24-api.service` | `40868` | `ssi_core24` | `serve` |
| `ssi-core24-worker.service` | `40867` | `ssi_core24` | `worker` |

Katalog Python `ssi_core24` w aktywnym release istnieje. **To rzeczywiste wejścia do CORE24 API/Workera, nie zweryfikowany kanoniczny engine MultiQuant.**

## Odczyt statycznych importów i wywołań AST

| Plik | Importowane moduły (wybrane) | Wykryte wywołania |
| --- | --- | --- |
| `__main__.py` | `api`, `config`, `engine`, `runtime`, `store`, `argparse`, `json`, `os`, `sys` | `main` → `QueueStore`, `ollama_ping`, `route`, `worker_loop` |
| `api.py` | `config`, `engine`, `http.server`, `hmac`, `json`, `store` | `serve` → `QueueStore`; `do_POST` → `route` |
| `engine.py` | `config`, `re` | `route` → `infer_local_kind` |
| `runtime.py` | `config`, `contextlib`, `fcntl`, `json`, `os`, `socket`, `store`, `time`, `urllib.error`, `urllib.request` | `ollama_ping` → `OllamaUnavailable`; `ollama_chat` → `InferenceUncertain`, `OllamaUnavailable`; `worker_loop` → `QueueStore`, `_perform`, `exclusive_worker` |
| `store.py` | `config`, `contextlib`, `datetime`, `engine`, `hashlib`, `json`, `pathlib`, `sqlite3`, `uuid` | `add` → `route` |
| `config.py` | `dataclasses`, `os`, `pathlib` | bez dopasowanego wywołania w filtrze |
| `__init__.py` | brak w raporcie | brak w raporcie |

**Interpretacja:** istnieje działający pakiet `ssi_core24` z API, lokalnym routowaniem, magazynem kolejki, workerem i funkcjami backendu Ollama. Nie ma **jawnego statycznego importu** `multiq`, `multiquant`, `SCC` lub zewnętrznego adaptera w siedmiu skontrolowanych plikach. Wydruk AST podaje jedynie wywołania pasujące do filtra; brak wydrukowanego wywołania nie oznacza, że funkcja nic nie wywołuje. Nie testowano dynamicznego ładowania, konfiguracji, callbacków ani całego grafu procesów; nie możemy zatem twierdzić, że MultiQuant jest nieobecny w całym SSI.

## Ważne rozróżnienie MultiQuant i inferencji

- **Offline quantization/distillation** może przygotowywać specjalne wagi GGUF, a późniejszy backend używa ich bez importowania kodu kwantyzatora w procesie inferencji. W takim przypadku autorski wkład jest w **pochodzeniu artefaktu i porównaniu wyników**, a nie w koniecznym runtime `import multiq`.
- Jeśli FSE-01 ma faktycznie korzystać z **dynamicznych modułów MultiQuant** (fragmentowa Q/D, pamięć hybrydowa, routing lub korekty w trakcie wykonywania), trzeba wykazać ich uruchomienie i ślad w misji. Nie utożsamiać samego pliku IQ2_XXS z aktywnym modułem proprietary MultiQuant.
- Osobny 70B IQ2_XXS GGUF na CORE24 **nie występował** w wcześniej potwierdzonym wykazie 13 tagów Ollama; obecność `ollama_chat` nie dowodzi, że aktualny worker może już generować tą wagą.

## Co rzeczywiście zamknięto

1. `P1R6_ENTRYPOINT_AND_STATIC_IMPORT_GRAPH_PASS` dla CORE24 API/worker.
2. `NETWORK_TRANSPORT_PARTIAL`: wcześniejsze 3/3 MSI SSH, 6/6 TCP 22 oraz 3/3 HTTP 200 /api/version.
3. `MULTIQ_CANONICAL_ENGINE_VERSION_AND_ENTRYPOINT=PENDING`.
4. `SCC_DIRECTOR_TO_MULTIQ_AND_70B_ADAPTER=PENDING`.
5. `E2E_SCC_MULTIQ_WEBSHOP_AND_EVIDENCE=PENDING`.

## Konkretny następny audyt P1R7 (read-only)

1. Odczytać **statycznie** funkcje `main, route, do_POST, add, _perform, worker_loop, ollama_chat` w aktualnym pakiecie CORE24, raportując **tylko nazwy wywołań/importów** (bez argumentów URL, tokenów i kodu źródłowego). Sprawdzić istnienie `importlib`, `subprocess`, dynamicznych bindingów i jawnych odwołań do MultiQuant.
2. Na podstawie istniejących plików V7/experimentów (bez uruchamiania managerów) wskazać kanoniczny skrypt/pakiet odpowiedzialny za **offline MultiQuant**, oddzielając go od aktywnego CORE24 worker. Zidentyfikować właściciela i wersję/manifest GGUF 70B, bez transferu ~19 GB modelu.
3. Jeżeli nie ma używanego adaptera runtime, zaprojektować **minimalne podpięcie**, bez dublowania SCC i bez migracji/zmian produkcyjnych przed osobną bramką.
4. Dopiero później jeden nieprodukcyjny request `DIRECTOR SCC / Router → MultiQuant → CORE24 70B → Evidence`, z metrykami i potwierdzonymi wywołaniami.

**Bezpieczeństwo:** żadnego generowania 70B, zmian workerów/systemd, restartów, instalacji, kopiowania wag, sekretów w publicznym repo, ani płatnych GPU w tej bramce.

## Dokumenty powiązane

- [P1R5 — inwentarz runtime i źródeł](SSI_MULTIQ_FSE01_P1R5_RUNTIME_SYMBOLS_OPERATOR_20261025.md).
- [P1R4 — dwa węzły](SSI_MULTIQ_FSE01_P1R4_TWO_VPS_ENGINE_RUNTIME_SURVEY_20261025.md).
- [3 VPS — realny pomiar](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [Handoff migracji](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).

**Publikowane: wyłącznie pseudonimy usług/plików, nazwy funkcji i statusy; rzeczywiste adresy, konfiguracja, ścieżki prywatne i kod know-how pozostają poza publicznym repozytorium.**
