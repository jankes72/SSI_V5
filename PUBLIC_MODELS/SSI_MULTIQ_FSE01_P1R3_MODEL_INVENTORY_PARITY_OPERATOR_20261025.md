# SSI MultiQuant FSE-01 — P1R3 potwierdzenie zgodności katalogów modeli

**Data:** 2026-10-25  
**Źródło:** właściciel/operator potwierdził w rozmowie, że obie wartości `INVENTORY_SHA256` z kontroli P1R3 są identyczne. **Same wartości hash oraz pełne wyjście polecenia nie zostały przekazane do niezależnego odczytu.**  
**Status:** `P1R3_INVENTORY_HASH_EQUAL_OPERATOR_CONFIRMED / MODEL_ENGINE_UNVERIFIED / INFERENCE_NOT_RUN`

## Dokładny zakres potwierdzenia

Skrypt P1R3 wykonywał dwa osobne żądania `GET /api/tags`: jedno przez lokalny tunel na pierwszym VPS MultiQuant, drugie bezpośrednio na CORE24. Parsował odpowiedzi JSON do posortowanych par `(nazwa_modelu, digest)` i liczył SHA-256 z tej listy. Operator potwierdził **identyczne wartości** wynikowych hashy.

**Wniosek uprawniony:** w zakresie danych zwróconych przez oba endpointy operator zaobserwował zgodne zestawy par nazwa/digest (zakładając brak błędu wykonania skryptu i poprawne odczyty JSON). To silny dowód zgodnego widoku katalogu Ollama przez tunel i z CORE24.

**Granice:**
- Nie przedstawiamy konkretnej wartości SHA-256 — nie została dostarczona; jest to dowód **operator-reported**, nie independent console readback.
- Nie uznajemy hashy za sekrety ani klucze SSH; to sumy kontrolne listy tagów.
- Zbieżny katalog nie jest kryptograficznym potwierdzeniem tożsamości fizycznego backendu; zgodne rejestry lub mirror mogą wyglądać identycznie.
- Wcześniejszy odczyt CORE24 pokazywał 13 tagów Ollama i osobny plik Llama 70B IQ2_XXS GGUF. Zgodność katalogów nie dowodzi, że **ten GGUF 70B jest serwowany** przez Ollamę.
- Samo `GET /api/tags` nie uruchamia generowania i **nie potwierdza aktywnego silnika SSI MultiQuant ani wykonania jego modułów**.
- Nie zmieniono statusu benchmarków IQ2 plain / MultiQuant-enabled: **oba pełne B1 CPU i ablation pozostają pending**.

## Decyzja dalsza

**Bramka transportowa `P1R3_MODEL_INVENTORY_PARITY` przechodzi w stan `OPERATOR_CONFIRMED`.** Wdrożenie FSE jest nadal wstrzymane przed inferencją, dopóki nie odnajdziemy i nie zweryfikujemy prawdziwego *kanonicznego* punktu wejścia MultiQuant na pierwszym VPS albo nie wykażemy faktycznej bieżącej lokalizacji tego silnika.

**Następny krok FSE-P1R4:** tylko do odczytu wyszukać rejestry/entrypointy `MultiQuant runner/adapter/worker`, ich stan oraz kontrakty z CORE24; nie wykonywać managerów R20/R21 w trybie konwersji i nie uruchamiać direct `llama-cli` jako wyniku produktu.

## Odwołania

- [P1R2 tunel i R20/R21](SSI_MULTIQ_FSE01_P1R2_TUNNEL_MANAGER_INTERFACE_20261025.md)
- [P1R pierwszy VPS](SSI_MULTIQ_FSE01_P1R_FIRST_VPS_ENGINE_DISCOVERY_20261025.md)
- [Korekta przepływu FSE](SSI_MULTIQ_FSE01_SERVER_ROUTING_CORRECTION_R1_20261025.md)
- [FSE-01 etap startowy](SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md)

**Brak nowych danych produkcyjnych lub kluczy w publikacji.**