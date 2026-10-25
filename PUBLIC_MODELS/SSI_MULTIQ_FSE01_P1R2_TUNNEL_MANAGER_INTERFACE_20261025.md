# SSI MultiQuant FSE-01 — P1R2: tunel do modeli i interfejsy R20/R21

**Data:** 2026-10-25. **Źródło:** dostarczony przez właściciela log z pierwszego VPS MultiQuant. **Zakres:** read-only, bez bezpośredniej inspekcji zdalnej przez autora raportu.

**Status:** `MODEL_API_TUNNEL_HTTP_200 / R20_R21_SOURCE_PRESENT / MULTIQUANT_MISSION_ENGINE_UNVERIFIED / MODEL_EXECUTION_NO`.

## Potwierdzone obserwacje

| Badany element | Wynik |
| --- | --- |
| Zarejestrowana jednostka tunelowa do modeli | Enabled; w chwili odczytu `ActiveState=active`, `SubState=running`, `Result=success`, `NRestarts=0`. |
| Lokalny forward SSH | Wykryto aktywny port loopback; numer i konfiguracja pozostają w prywatnym logu. |
| Niegenerujący odczyt REST `/api/tags` przez forward | **HTTP 200**. To dowód, że na ścieżce tunelu odpowiedział endpoint zgodny z API Ollama; nie dowodzi jeszcze, że docelowy serwer to na pewno konkretny CORE24 ani że aktywne moduły MultiQuant wykonały misję. |
| Pierwszy manager R20 | **22 566 B**, statyczne AST wskazuje m.in. `get_source_metadata`, `remote_plan`, `sha256_file`, `resource_gate`, `resumable_download`. |
| Drugi manager R20 | **23 146 B**, analogiczne nazwy części interfejsów; nie potwierdzono identyczności plików. |
| R21 manager | **17 572 B**, statyczne AST wskazuje m.in. `preflight`, `install_deps`, `prepare`, `convert`, `validate_output`, `verify_artifact`, `runtime`, `publish`. Same nazwy funkcji nie potwierdzają uruchomionego brokera misji. |
| Inference / production changes | `MODEL_EXECUTION=NO`; `PRODUCTION_CHANGES=NONE` według logu. |

## Znaczenie dla uruchomienia FSE

1. Na pierwszym VPS działa most do API modeli. Nie oznacza to automatycznie obsługi osobnego GGUF 70B przez ten endpoint; wcześniejsze `ollama list` na CORE24 pokazywało 13 innych tagów, a GGUF 70B znajduje się poza tą listą.
2. R20/R21 odpowiadają budowaniu źródeł, konwersji i weryfikacji artefaktów. Aby stwierdzić uruchomienie autorskiego silnika MultiQuant potrzebne są **entrypoint, aktywny adapter/worker, ślad wywołania modułów i rzeczywisty transport do wybranego modelu**.
3. Dla produktu FSE obowiązuje decyzja właściciela: **nie uruchamiać direct `llama-cli` jako dowodu FSE**. Kontrola plain CPU B pozostaje możliwa jako niezależny baseline; test produktu C musi wykazać faktycznie uruchomione moduły MultiQuant.
4. Lokalny port tunelu i HTTP 200 nie stanowią dowodu tożsamości serwera docelowego. Kolejny etap read-only porównuje publicznie nieszkodliwe metadane tagów i digestów z niezależnym odczytem CORE24, bez generowania i bez wyświetlania sekretów/URL konfiguracji usługi.

**Bramka:** `P1R2_TUNNEL_CONNECTIVITY_PASS; ENGINE_IDENTITY_PENDING; 70B_FSE_P2_NOT_RUN`.

**Następne działanie:** odczytać przez tunel listę nazw i digestów bez generowania oraz porównać ją z niezależnym odczytem backendu modeli. Odrębnie znaleźć/zweryfikować kanoniczny entrypoint silnika MultiQuant — używanie dostępnego API Ollama nie jest równoznaczne z tym, że `R21` uruchomił 70B.

**Źródła powiązane:** [P1R audyt pierwszego VPS](SSI_MULTIQ_FSE01_P1R_FIRST_VPS_ENGINE_DISCOVERY_20261025.md), [korekta routingu](SSI_MULTIQ_FSE01_SERVER_ROUTING_CORRECTION_R1_20261025.md), [FSE-01 plan](SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md), [BF16 B1](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md).

**Publiczna granica:** kod, logi, wewnętrzne ścieżki, parametry tunelu, adresy i dane rozliczeniowe wyłącznie prywatnie.