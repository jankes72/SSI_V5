# SSI MultiQuant FSE-01 — P1R11: skrypty MSI R19–R21 i odnalezione archiwa adaptera SCC

**Data:** 2026-10-25  
**Dowód:** wynik użytkownika z jednorazowego lokalnego audytu MSI, wykonany przez `ast.parse`, SHA-256 i metadane katalogu pobranych. Autor raportu nie wykonywał audytu na MSI samodzielnie.  
**Status:** `P1R11_MSI_SOURCES_AST_PASS / ADAPTER_ARCHIVE_CANDIDATE_FOUND / CANONICAL_MULTIQ_ENGINE_STILL_UNVERIFIED / FSE_P2_NOT_RUN`.  
**Bez zmian:** `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE` według logu.

## Wynik: konkretne pliki MSI

| Plik (tylko nazwa) | Bajty | AST | Wykryty `if __name__ == '__main__'` | Funkcje top-level (ograniczone) |
| --- | ---: | --- | --- | --- |
| `SSI_MULTIQ_V7_16_R19.py` | 9 022 | PASS | False | `sha`, `snapshot`, `child`, `state` |
| `SSI_MULTIQ_V7_16_R20.py` | 11 965 | PASS | False | `sha`, `snapshot`, `args`, `worker`, `counts` |
| `SSI_MULTIQ_V7_16_R21.py` | 14 479 | PASS | False | `digest`, `snapshot`, `canon`, `spec`, `child_args`, `worker`, `row_count`, `record`, `parallel` |
| `SSI_MULTIQ_BASELINE_BRIDGE_B1.py` | 14 089 | PASS | True | `sha256`, `make_suite`, `canonical`, `find_zip`, `read_checked_archive`, `run_selftest`, `main` |
| `SSI_MULTIQ_ACTIVE_ARCHIVE_R5.py` | 10 873 | PASS | True | `parse_memory`, `parse_swaps`, `parse_zram`, `pressure`, `make_counter`, `is_db`, `scan`, `self_test`, `main` |
| `SSI_R9_113_SCC_LEGO_MULTIQ_READ_ONLY.py` | 9 135 | PASS | True | `stat`, `scan`, `inspect_py`, `index_info`, `zip_info`, `main` |

Hashy plików nie kopiujemy do publicznego opisu — pełne dokładne SHA-256 znajdują się w prywatnym logu operatorskim MSI. AST PASS nie jest dowodem działania modułu ani zgodności z produkcyjnym SCC.

**Ostrzeżenie:** R19/R20/R21 nie mają typowego strażnika `__main__`. Z uwagi na `subprocess` i `sqlite3` **nie importować ich w celach audytu**: import mógłby wykonać kod top-level. R19–R21 mają zgodny z wcześniejszymi raportami profil narzędzi izolowanych eksperymentów checkpointów/kolejek, ale nie potwierdzono ich jako kanonicznego MultiQuant engine.

## Archiwa istotne dla integracji

Lokalny audyt nazw plików zwrócił **33** archiwa z filtrem `multiq/multiquant/qwen9b`. Wybrane kandydatury:

- `SSI_MULTIQ_SCC_ADAPTER_R1_20261018.zip` (**19 134 B**) — priorytet do przeglądu, ponieważ nazwa wskazuje adapter SCC.
- `SSI_MULTIQ_R9_124_KOD_DO_INTEGRACJI_20261018T182626Z.zip` (**18 224 B**) — potencjalny kod integracji.
- `SSI_MULTIQ_R9_125_DUAL_WORKER_CANDIDATE_20261018.zip` (**29 720 B**) — kandydat dwóch wykonawców.
- `SSI_MULTIQ_R9_124_MSI_SOURCE_HANDOFF_20261018.zip` (**7 344 B**) — możliwa przekazywana struktura źródeł.
- `SSI_MULTIQ_R1_R9_REAL_TEST_R8_R9_20261021.zip` (**20 617 B**) — historyczne testy, wymagają rozróżnienia od kodu operacyjnego.
- `SSI_SCC_MULTIQ_TRAINING_INTAKE_R1_20261023_PRIVATE.zip` (**73 366 B**) — materiał SCC/trening; nie zakładać, że zawiera runtime.
- `SSI_MULTIQ_MULTISESSION_PRIVATE_BACKUP_R1_R9_20261020.tar.gz` (**106 586 566 B**) — zachowane źródło wielosesyjne, obecnie **nieprzeglądane, niemigrowane i nierozpakowywane**.

**Istnienie i nazwa ZIP nie dowodzą kompletności adaptera, kompatybilności SCC ani wdrożenia.** Dotychczas nie otwierano wnętrza archiwów.

## Priorytet P1R12

**Jeden odczyt metadanych kilku wskazanych ZIP na MSI, bez wypakowywania na dysk lub uruchamiania kodu**:

1. Zweryfikować, czy archiwa SCC_ADAPTER_R1, R9_124_KOD_DO_INTEGRACJI, R9_125_DUAL_WORKER i R9_124_MSI_SOURCE_HANDOFF zawierają `README`, `manifest`, kod Python i konkretne entrypointy; dodatkowo porównać R1_R9_REAL_TEST i SCC_TRAINING_INTAKE.
2. Dla małych plików Python czytać bezpiecznie **tylko AST**, ujawniając w prywatnym logu nazwy klas/funkcji/importów, nie kod, literały, adresy, prompty i sekrety.
3. Rozdzielić `EXPERIMENTAL_FIXTURE` / `OFFLINE_QD_ENGINE` / `MISSION_ADAPTER` / `DEPLOYED_RUNTIME`. Ostatnia klasa wymaga oddzielnego dowodu uruchomienia na VPS; obecność pliku nie wystarczy.
4. Jeżeli istnieje rzeczywisty adapter SCC, najpierw wskazać jego kanoniczny kontrakt i wersję, a dopiero potem planować integrację na **pierwszym VPS MultiQuant** z wykonawcą CORE24; bez duplikowania parsera Dyrektora.

Nie uruchamiać R19–R21, `llama-cli`, 70B, GPU; nie modyfikować systemd, wag i działających kontenerów. Backupów ani historycznych plików nie kasować. Wyniki prywatnej inspekcji kodu pozostają prywatne.

## Referencje

- [P1R10 — odkrycie źródeł MSI](SSI_MULTIQ_FSE01_P1R10_MSI_V716_SOURCES_VS_VPS_MANAGERS_20261025.md).
- [P1R9 — rzeczywisty wybór callbacku CORE24](SSI_MULTIQ_FSE01_P1R9_CORE24_DEFAULT_OLLAMA_CALLBACK_RESOLVED_20261025.md).
- [Uzgodnienia migracyjne](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).
- [Issue FSE-01 #5](https://github.com/jankes72/SSI_V5/issues/5).

**Publiczny materiał zawiera wyłącznie wyniki, nazwy wskazanych artefaktów i ograniczenia; nie zawiera kodu implementacji, adresów hostów, danych klienta ani sekretów.**
