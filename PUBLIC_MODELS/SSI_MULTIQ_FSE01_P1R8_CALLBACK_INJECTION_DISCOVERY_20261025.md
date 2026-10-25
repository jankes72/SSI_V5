# SSI MultiQuant FSE-01 — P1R8: wstrzykiwany callback wykonawcy CORE24

**Data:** 2026-10-25  
**Źródło dowodu:** operator przekazał pełny wynik ograniczonej statycznej analizy AST przez SSH z MSI do rzeczywistego CORE24. Autor raportu nie wykonywał SSH ani inferencji.  
**Status:** `P1R8_INJECTABLE_ASK_CALLSITE_CONFIRMED / ADAPTER_BOOLEAN_BINDING_FOUND / ADAPTER_TARGET_PENDING / NO_70B_GENERATION`.  
**Zmiany na serwerze:** `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE` według logu.

## Zobaczone fakty

| Element | Wynik P1R8 |
| --- | --- |
| `__main__.main` | Wywołuje `worker_loop`; **brak pozycyjnych argumentów** pokazanych w logu. Skrypt nie raportował argumentów nazwanych ani ich braku. |
| `runtime.ollama_chat` | Parametry `model, user_text, max_tokens, timeout`; ostatnie dwa posiadają wartości domyślne, ale same literały zostały zredagowane. |
| `runtime._perform` | Parametry `s, ask, prefer`; wywołuje `s.claim()`, `ask(job[...], job[...])`, kilka wywołań `s.finish(...)`. To dowód **statycznego callsite**, nie ukończonego zadania na modelu. |
| `runtime.worker_loop` | Parametry `once, ask, storage` — wszystkie trzy mają wartości domyślne, typ i treść literałów nie były wypisane. |
| `runtime.worker_loop` | Przypisanie `adapter = <BoolOp>`; operator nie wydrukował typu operacji (`or` vs `and`) ani operandów. |
| `runtime.worker_loop` | Wywołuje `_perform(s, adapter, prev)`, w wyniku czego funkcja przekazana przez zmienną `adapter` trafi do parametru `ask` funkcji `_perform`. |

## Co z tego wynika, a co nie

**Potwierdzona konstrukcja:** w istniejącym, aktywnym pakiecie `ssi_core24` przewidziano parametr `ask` przekazywany do realnego wywołania backendu `_perform`. To pozwala traktować ten punkt jako **kandydata do integracji adaptera**, bez stwierdzania, że jest już autorskim runtime MultiQuant.

**Jeszcze nie wynika:** czym jest `adapter`. `BoolOp` może oznaczać np. `ask or ollama_chat`, lecz to tylko hipoteza. Wywołanie `worker_loop` w `__main__.main` nie miało argumentów pozycyjnych, ale nie kontrolowano jeszcze **keyword args** ani wartości domyślnej `ask`. Nie wolno automatycznie deklarować, że produkcyjny Worker kieruje wszystko do `ollama_chat` ani że aktywnie korzysta z MultiQuant.

**Granica FSE:** sam plik 70B IQ2_XXS GGUF na CORE24 pozostaje poza dawną listą 13 tagów Ollama. Nie ma potwierdzenia, że obecny `ssi_core24.worker` ma go w ścieżce wykonania. Dostępny parametr callback nie jest dowodem implementacji autorskich modułów ani natywnego SCC.

## Następny punktowy audyt P1R9 — rozstrzygnięcie konkretnego `BoolOp`

**Tylko AST bez importowania modułu**, odczytać:

1. Dokładnie typ `adapter = <BoolOp>` (`Or`/`And`) i **bezpieczne typy i nazwy operandów** (`Name(ask)`, `Name(ollama_chat)`, `Lambda`, `Call`, `Constant<REDACTED>`); nie wypisywać wartości literałów.
2. Dla argumentu `worker_loop(once, ask, storage)` oznaczyć czy domyślne `ask` jest `None`, bez ujawniania innych domyślnych wartości.
3. Sprawdzić czy wywołanie `worker_loop` z `__main__.main` zawiera **jakiekolwiek keyword arguments** (same ich nazwy), oraz czy istnieją inne bezpośrednie `worker_loop` callsites w tej samej paczce.
4. Jeżeli wyjdzie `adapter = ask or ollama_chat`, `ask=None` i `worker_loop()` bez keywords, odnotować: **domyślny lokalny CORE24 Worker używa `ollama_chat` w tym fragmencie implementacji** (nadal tylko static-program path); MultiQuant musi być osobno potwierdzony jako poprzedzający etap przygotowania GGUF lub jawny, bezpieczny adapter misji.
5. Osobno zachować autorytet SCC Dyrektora, a później jeden rzeczywisty nieprodukcyjny request `SCC/Router→MultiQuant→CORE24→Evidence`, z kontrolą ACL, checkpointem i dowodem wywołania modułu.

**Nie uruchamiać 70B, nie zmieniać usług, nie przenosić wag i nie deklarować `FSE_PRODUCTION_READY`.**

## Powiązane dowody

- [P1R7 — statyczny graf wywołań](SSI_MULTIQ_FSE01_P1R7_CORE24_HASHED_CALL_GRAPH_20261025.md).
- [P1R6 — uruchomione wejścia `ssi_core24`](SSI_MULTIQ_FSE01_P1R6_CORE24_STATIC_IMPORT_CALL_GRAPH_20261025.md).
- [Trzy VPS — obserwacje transportowe](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [Odpowiedź toru migracyjnego](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).
