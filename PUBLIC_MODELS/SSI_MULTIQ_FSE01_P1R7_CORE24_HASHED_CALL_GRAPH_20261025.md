# SSI MultiQuant FSE-01 — P1R7: rzeczywisty graf wywołań aktywnego CORE24

**Data:** 2026-10-25  
**Dowód:** właściciel przesłał wynik statycznego audytu Python `ast` uruchomionego przez MSI SSH do rzeczywistego serwera CORE24. Raport powstał z odczytu logu; nie było niezależnego SSH autora.  
**Zakres:** 5 plików aktywnego pakietu `ssi_core24`, ograniczona analiza funkcji, SHA-256 bajtów plików, importów i symboli `Call`; **nie uruchamiano modułów ani modelu**.  
**Status:** `P1R7_STATIC_GRAPH_AND_FILE_HASHES_RECORDED / CORE24_APP_ENTRYPOINT_CONFIRMED / MULTIQUANT_DYNAMIC_BINDING_UNVERIFIED / FSE_MODEL_EXECUTION_NO`.

## Odczyt bezpośredni

Skrypt sprawdził: `__main__.py`, `api.py`, `engine.py`, `runtime.py` i `store.py`. Wszystkie pliki zostały odczytane, a `ast.parse` zakończył się poprawnie. SHA-256 odnotowano w prywatnym logu operatora; publiczna publikacja nie powiela pełnych fingerprintów prywatnej implementacji.

| Plik | Kluczowy fragment statycznego grafu, ograniczony do nazw symboli |
| --- | --- |
| `__main__.py` | `main` wywołuje m.in. `ArgumentParser`, `QueueStore`, `ollama_ping`, `route`, `serve`, `worker_loop`. |
| `api.py` | `serve` wywołuje `APIServer`, `QueueStore`, `api_token_path`, `local_only_bind`, `serve_forever`; `do_POST` wywołuje `_auth`, `_read_json`, `add`, `route` oraz `quick_contact_response`. |
| `engine.py` | `infer_local_kind` jest wywoływane przez `route`; `route` wykonuje także walidację `InvalidRequest`, `check_id`. |
| `runtime.py` | `ollama_ping` oraz `ollama_chat` wywołują `urlopen`; `ollama_chat` stosuje `Request` i JSON. `exclusive_worker` używa `flock`; `_perform` wywołuje `ask`, `claim`, `finish`; `worker_loop` wywołuje `QueueStore`, `_perform`, `exclusive_worker`, `recovery_check`. |
| `store.py` | `add` wywołuje `route`, `connect`, `execute`, `sha256`, `uuid4`. |

**Wspierany wniosek:** istnieje aktywny rdzeń CORE24 `API / routing / durable queue / worker / Ollama client`. Audyt wykazuje **symbole i możliwe ścieżki**, ale samo statyczne AST nie potwierdza faktycznie wykonanej kolejki misji, aktualnego stanu ACL ani realnego wywołania konkretnego modelu. Pośredni przepływ jest wstępnie zrekonstruowany jako: `HTTP API → router → QueueStore → worker_loop → _perform → callback ask → model/backend`.

## Punkt rozstrzygający: callback `ask`

Z funkcji `_perform` widoczne jest `ask(...)`. **Nie wskazano jeszcze źródła/bindingu symbolu `ask`** ani argumentów wywołania `_perform`. Nie należy stwierdzać, że `ask` **na pewno** równa się `ollama_chat`, choć jest to hipoteza możliwa do łatwej falsyfikacji przez punktową analizę AST.

- `ollama_chat` istnieje i ma HTTP client calls.
- W poprzednim P1R6 dla skontrolowanych siedmiu plików nie pokazano bezpośredniego importu modułu o nazwie `MultiQuant` ani `SCC`.
- Brak jawnego importu **nie jest** globalnym dowodem braku dynamicznego adaptera. Także kwantyzacja **offline** może dostarczać gotowe GGUF bez jakiegokolwiek importu kodu Q/D w czasie inferencji.
- Oddzielny GGUF IQ2_XXS 70B pozostaje poza dawnym katalogiem 13 tagów Ollama. Nie ma dowodu, że to właśnie ta waga jest obsługiwana przez bieżące `ollama_chat`.

## Aktualne bramki

| Bramka | Status |
| --- | --- |
| `P1R7_STATIC_CALL_GRAPH` | **PASS — w badanym zakresie 5 plików** |
| `CORE24_API_AND_WORKER_ACTIVE` | **PASS — niezależny audyt systemd/proc z P1R5/P1R6** |
| `ASK_CALLBACK_BINDING` | **PENDING** |
| `CANONICAL_MULTIQ_ENGINE_LOCATED_AND_RUNNING` | **PENDING** |
| `DIRECTOR_NATIVE_SCC_ROUTER_TO_MULTIQ` | **PENDING** |
| `CORE24_70B_IQ2_DYNAMIC_EXECUTION` | **NOT_RUN** |
| `WEBSHOP_MULTIPORT_E2E` | **PENDING** |

## Minimalny następny audyt P1R8

1. **Statycznie**, bez `import` badanego modułu, ustalić argumenty/nazwy przekazywane do `_perform` w `worker_loop` i zdefiniowanie/wiązanie `ask`, tak by oddzielić standardowe `ollama_chat` od potencjalnego adaptera MultiQuant.
2. Sprawdzić tylko nazwy deklarowanych strategii modeli i obecność powiązań z osobnym GGUF 70B (bez odczytu sekretów, endpointów, wag, prywatnych promptów).
3. Osobno wytypować istniejący kanoniczny moduł `MultiQuant` dla offline Q/D oraz ewentualnych operacji on-mission, z wersją i śladem wykonania. Nie tworzyć nowego SCC ani dublującego się worker.
4. Dopiero po tym planować jedno izolowane żądanie `SCC/Router → MultiQuant → CORE24 70B → Evidence`; nie uznawać samej inferencji standardowego Ollama za kwalifikację autorskiej metody.

**Operator:** `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE`. Nie wykonywano zmian usług, przenoszenia wag ani GPU.

## Powiązania

- [P1R6: CORE24 entrypoint i import graph](SSI_MULTIQ_FSE01_P1R6_CORE24_STATIC_IMPORT_CALL_GRAPH_20261025.md).
- [P1R5: runtime symbol inventory](SSI_MULTIQ_FSE01_P1R5_RUNTIME_SYMBOLS_OPERATOR_20261025.md).
- [FSE networking + migration handoff](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [FSE-01 Issue #5](https://github.com/jankes72/SSI_V5/issues/5).
