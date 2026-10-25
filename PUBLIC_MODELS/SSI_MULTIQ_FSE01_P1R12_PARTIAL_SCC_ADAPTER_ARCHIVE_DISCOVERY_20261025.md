# SSI MultiQuant FSE-01 — P1R12 PARTIAL: istniejący kod adaptera SCC w archiwum MSI

**Data:** 2026-10-25  
**Źródło:** wynik lokalnego audytu operatora MSI, przytoczony w rozmowie. Nie wykonano zdalnego odczytu MSI przez autora raportu.  
**Status:** `P1R12_FIRST_ARCHIVE_LISTED / PYTHON_AST_NOT_EXECUTED / FIVE_ARCHIVES_NOT_INSPECTED / FSE_E2E_PENDING`.  
**Zmiany:** nie uruchomiono modułów ani modeli, brak rozpakowywania i zmian produkcyjnych w zakresie zakończonej części narzędzia.

## Pierwsze archiwum rzeczywiście otwarte

**Archiwum:** `SSI_MULTIQ_SCC_ADAPTER_R1_20261018.zip`.  
**Wynik:** `STATUS=OPENED_READ_ONLY`, `ENTRY_COUNT=12`.

Zarejestrowane pliki istotne dla odnalezienia istniejącej integracji:

| Rodzaj | Zawartość ZIP | Bajty (niekompresowane) |
| --- | --- | ---: |
| Potencjalny most SCC | `adapter/bridge.py` | 6 551 |
| Potencjalna pamięć adaptera | `adapter/memory.py` | 6 447 |
| Potencjalne CLI | `cli.py` | 2 574 |
| Testy | `tests/test_adapter.py` | 6 247 |
| Kontrakt | `CONTRACT_ADAPTER_R1.md` | 6 850 |
| Plan | `INTEGRATION_PLAN_R1.md` | 4 137 |
| Inwentaryzacja kontraktów | `01_SURVEY_CONTRACTS_READ_ONLY.py` | 1 022 |
| Test runner | `TEST_OFFLINE.sh` | 649 |
| README i fixture | `README_PL_EN.txt`, `fixtures/qwen15b_operator_report_example.json` | według logu 3 330 B i 2 816 B |

Pozostałe dwa z 12 wpisów: `.gitignore` i `adapter/__init__.py`.

**Granica dowodu:** jest to ZIP z realnymi plikami adaptera, a nie sam dokument. **Nie zweryfikowano jeszcze, co implementują funkcje**, czy adapter jest kompatybilny z aktualnym SCC Dyrektora, czy działa na pierwszym VPS MultiQuant, ani czy obsługuje CORE24 70B. Nazwa pliku `bridge.py` nie potwierdza aktywnego mostu.

## Dlaczego skrypt przerwał

Po wydrukowaniu listy 12 wpisów narzędzie zakończyło się `AttributeError: 'ZipInfo' object has no attribute 'compressed_size'`. Poprawna nazwa atrybutu standardowej biblioteki Python to **`ZipInfo.compress_size`**. Błąd pochodzi z udostępnionego przez asystenta skryptu audytowego, a **nie** z pakietu MultiQuant lub błędu odczytu ZIP.

Wskutek tego:

- **0/6 archiwów** ukończyło etap AST w tej próbie;
- **1/6** archiwum miało potwierdzony odczyt listy wpisów;
- **5/6** pozostałych archiwów nie było jeszcze odwiedzonych przez skrypt;
- końcowy znacznik `FSE_P1R12_ARCHIVE_INSPECTION_COMPLETE` nie wystąpił.

Nie przyznajemy całościowego `P1R12_PASS`.

## Następne P1R12-R2 (bez zmian)

Przygotowany poprawiony skrypt opiera się na `compress_size` i ma ograniczenia wielkości ZIP, liczby wpisów, rozmiaru pojedynczego pliku Python, relacji rozmiaru kompresji oraz sumarycznego budżetu odczytu. Działa **tylko do odczytu**: central directory + podzbiór bezpiecznych członków ZIP + statyczny `ast.parse` w pamięci, bez zapisu wypakowanych plików, importowania modułów, wywoływania `TEST_OFFLINE.sh`, CLI, sieci lub modeli. Wynik powtórki zrealizuje dopiero operator na MSI.

Następny krok po poprawnym skanie: klasyfikacja `MISSION_ADAPTER` vs `EXPERIMENT_FIXTURE` vs `OFFLINE_QD_ENGINE`, oraz weryfikacja istniejącego kontraktu `ssi.mission.goal.r1 / ssi.mission.intent.r1` z Dyrektorem **bez dublowania SCC**. Jeśli adapter jest gotowym kandydatem, nadal wymaga oddzielnego staging, wersji, testów ACL/checkpoint/Evidence i jednej prawdziwej misji FSE.

**Nadal otwarte:** kanoniczny autorski engine MultiQuant na pierwszym VPS, podłączenie do Dyrektora, zdalny wykonawca 70B na CORE24, realne MultiPort/webshop, test end-to-end i odtwarzanie stanu. P1R9 wykazał, że bieżący worker CORE24 domyślnie używa `ollama_chat`.

## Powiązane dowody

- [P1R11 — wykrycie paczek na MSI](SSI_MULTIQ_FSE01_P1R11_MSI_SOURCE_AND_ARCHIVE_CANDIDATES_20261025.md).
- [P1R9 — domyślny backend CORE24](SSI_MULTIQ_FSE01_P1R9_CORE24_DEFAULT_OLLAMA_CALLBACK_RESOLVED_20261025.md).
- [P1R6 — CORE24 importy](SSI_MULTIQ_FSE01_P1R6_CORE24_STATIC_IMPORT_CALL_GRAPH_20261025.md).
- [FSE-01 Issue #5](https://github.com/jankes72/SSI_V5/issues/5).

**Granica publiczna:** bez archiwum i jego prywatnego kodu, surowego logu, adresów, kluczy, danych klienta i sekretów. Ten dokument jest **cząstkowym raportem o spisie ZIP**, nie odbiorem integracji.
