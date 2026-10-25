# SSI MultiQuant FSE-01 — P1R5: uruchomione moduły CORE24 i statyczny inwentarz kandydatów

**Data:** 2026-10-25  
**Dowód:** operator uruchomił read-only AST/proc/systemd na pierwszym VPS MultiQuant/Robert i na CORE24, przekazał pełny wynik konsoli. Ten raport opisuje wynik operatora, nie samodzielny SSH ani uruchomienie modeli.  
**Status:** `P1R5_RUNNING_CORE24_APP_IDENTIFIED / PROPRIETARY_MULTIQ_ENGINE_NOT_VERIFIED / E2E_NOT_RUN`.  
**Zachowanie systemu:** `MODEL_EXECUTION=NO`; `PRODUCTION_CHANGES=NONE` według logu.

## Pierwszy VPS MultiQuant / historyczny Robert

Z filtrowanej listy usług: aktywny **tunel SSH do wspólnej usługi modeli**. `EXECUTABLE=ssh`, nie aktywny silnik modelu. Odczyt płytkiego drzewa Python znalazł:

- Dwie wersje **kandydata workera SSI ROBERT/CODEX** w katalogu staging; obie deklarują funkcję `main`, jedna `validate` i `checks_passed`. Nie wykazano aktywnej usługi ani procesu workera.
- Dwa historyczne warianty `mission_control_r12.py` (interfejsy m.in. `bind`, `capabilities`, `route` i operacje rekordu/job); dwa warianty `mission_luna_r14.py`, interfejs `route`. To kod kandydujący do misji Roberta, **nie dowód, że jest głównym MultiQuant**.
- Dwa pliki menedżera źródeł R20 oraz manager R21. W P1R2 ich nazwy funkcji były związane z preflight, źródłami, konwersją i weryfikacją.

**Wniosek:** nie ma dowodu działań natywnego autorskiego engine MultiQuant na pierwszym VPS. Wykaz nie obejmuje każdego procesu i źródła na tym serwerze.

## CORE24

Usługi rzeczywiście aktywne:

| Klasa | Odczyt | Ograniczenie |
| --- | --- | --- |
| SSI CORE24 API | Python3, moduł uruchamiany jako `ssi_core24`; PID operatora 40868 | Nie potwierdzono jeszcze dokładnego podpolecenia i pełnej ścieżki obsługi żądania. |
| SSI CORE24 worker | Python3, moduł uruchamiany jako `ssi_core24`; PID operatora 40867 | Sam moduł i nazwa serwisu nie oznaczają autorskiego silnika MultiQuant. |
| Ollama | Binarka Ollama aktywna, PID operatora 39215 | Backend generatywny; brak inferencji 70B w badanej próbie. |

W katalogu obecnej instalacji CORE24 statyczne AST wskazało:

- `api.py` — klasy/interfejsy `APIServer`, `APIHandler`, `serve`.
- `runtime.py` — `InferenceUncertain`, `OllamaUnavailable`, `ollama_ping`, `ollama_chat`, `exclusive_worker`, `_perform`, `worker_loop`.
- `engine.py` — `InvalidRequest`, `check_id`, `infer_local_kind`, `route`, `quick_contact_response`.

W katalogach MultiQuant V7 zidentyfikowano m.in. `dual_queue_r3.py` (`DualQueue`, `selftest`) i `dual_queue_r6.py` (`RetrievalBlocked`, `safe_get`, `guarded_delete`, `run`); w historycznych labach SCC/R8 są statyczne walidatory, ewaluatory i `04_NATIVE_WORKER.py` z pomiarem RSS i cgroup.

**Wniosek:** CORE24 posiada **rzeczywiste aktywne procesy SSI API/worker** oraz liczne **statyczne źródła** MultiQuant. Nie zidentyfikowano jeszcze połączenia tych dwóch grup (import, call site, autoryzowany adapter), a więc **nie wolno deklarować `MultiQuant Engine ACTIVE`**. Nazwy `route`, `worker_loop` czy `dual_queue` bez mapy wywołań nie są dowodem ścieżki wykonania.

## Następny minimalny dowód — FSE-P1R6

**Cel:** sprawdzić wyłącznie istniejący runtime API/worker CORE24 i dwie konkretne ścieżki kodu MultiQuant, bez nowych usług lub instalacji.

1. Zidentyfikować bezpiecznie rzeczywiste **podpolecenia** istniejących procesów `python3 -m ssi_core24`, bez ujawniania dowolnych argumentów, zmiennych środowiskowych, tokenów lub portów.
2. Wykonać **statyczną analizę AST** katalogu CORE24: jakie moduły importuje oraz gdzie występują referencje do `runtime`, `engine`, `Ollama`, `MultiQuant`, `dual_queue`, `SCC` i autorskiego adaptera. AST nie jest dowodem dynamicznego wywołania. Nie importować żadnych plików projektu, tylko parsować.
3. Analogicznie odczytać **wyłącznie jawne nazwy** modułów i interfejsów dwóch znalezionych `dual_queue` oraz stagingowego workera Roberta. Nie publikować prywatnego kodu, promptów ani szczegółów implementacji.
4. Jeśli istniejący, używany przez aktywny worker adapter zostanie zidentyfikowany — wykonać w osobnej zgodzie prosty preflight auth/checkpoint i jeden nieprodukcyjny test. Jeśli nie — raportować `ADAPTER_NOT_BOUND` i zlecić staging implementacji z zachowaniem natywnego SCC, Router i Evidence.

**Nie zamieniać** fizycznego położenia GGUF i `llama-cli` w potwierdzenie aktywności autorskiego MultiQuant. Historyczna referencja BF16 96/96 pozostaje oddzielnym wynikiem modelu. Nie kopiować 70B GGUF, nie uruchamiać przez Ollama 13 tagów ani nie zmieniać aktywnych usług podczas audytu.

## Odnośniki

- [P1R4 audyt dwóch serwerów](SSI_MULTIQ_FSE01_P1R4_TWO_VPS_ENGINE_RUNTIME_SURVEY_20261025.md).
- [Macierz trzech VPS i webshop](SSI_FSE01_THREE_VPS_NETWORK_WEBSHOP_ACCEPTANCE_R1_20261025.md).
- [Raport połączeń i wspólna koordynacja](../RESULTS/SSI_FSE01_THREE_VPS_OPERATOR_CONNECTIVITY_AND_MIGRATION_REPLY_20261025.md).
- [Odpowiedź modelu migracyjnego](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).

**Publikacja publiczna zawiera wyłącznie klasy źródeł, ograniczone nazwy symboli i statusy; szczegóły implementacji pozostają prywatne.**
