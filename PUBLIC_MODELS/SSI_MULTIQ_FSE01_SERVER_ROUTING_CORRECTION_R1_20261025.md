# SSI MultiQuant FSE-01 — korekta routingu: najpierw rzeczywisty silnik MultiQuant

**Data:** 2026-10-25  
**Decyzja właściciela:** FSE musi przechodzić przez właściwy **autorski silnik MultiQuant**, działający na ustalonym serwerze sterującym, i **dopiero potem** korzystać z modelu 70B na serwerze wykonawczym. Bezpośrednie wywołanie surowego `llama-cli` na CORE24 nie jest testem FSE.  
**Status:** `ENGINE_ENTRYPOINT_DISCOVERY_REQUIRED / DIRECT_CORE24_FSE_P2_STOPPED`  
**Zakres:** korekta dokumentacyjna, bez uruchamiania modeli i bez zmian usług. 

## Potwierdzone położenie danych / procesów (różne zakresy dowodu)

| Serwer i rola | Co faktycznie potwierdzono | Czego nie potwierdzono |
| --- | --- | --- |
| VPS z aliasem SSH `ssi-robert-vps` / rola ROBERT–MultiQuant | Historyczny prywatny audyt **2026-10-23**: skrypty zarządzania R20/R21 oraz około 11 GB źródeł/artefaktów Offline MICRO; VPS był **tymczasowo przeznaczony na MultiQuant** w ówczesnej decyzji użytkownika. | Że działa tam **bieżący** główny engine/daemon/broker MultiQuant, że jest połączony z CORE24, że to obecnie aktywna rola produkcyjna. Historyczna decyzja wyraźnie **nie potwierdzała wdrożenia agenta ROBERT** na tej maszynie. |
| CORE24 / wspólny VPS modeli CPU | 2026-10-25 P1: GGUF Llama 3.1 70B IQ2_XXS **19,097,389,632 B**, ~15 GiB RAM hosta, 2 GiB zram, ~12 GiB swap disk. P1C: plik wykonywalny `llama-cli` wewnątrz drzewa kompilacji **MultiQuant/llama.cpp**, 13 tagów Ollama, brak załadowanych modeli w `ollama ps`. | Że znaleziony `llama-cli` zawiera autorskie mechanizmy MultiQuant lub że bezpośrednia inferencja uruchamiałaby je. Brak dowodu wykonania natywnego adaptera MultiQuant, aktualnej wersji binarki, limitu 8 GiB procesu i relacji do węzła orkiestracji. |
| SSI DIRECTOR | Architektura/handoff: misja SCC, Router V10/S10, Research Memory, delegowanie i Evidence jako zamierzony przepływ. | Aktualny natywny end-to-end binding SCC↔MultiQuant, działający na serwerach w ramach tej próby. |

Uwaga: prywatne raporty migracyjne i publiczny handoff wymagają **aktualnego inwentarza hostów i ich ról**. Alias nie jest dowodem uruchomionego modułu. Nie ujawniać adresów i prywatnych ścieżek w publicznym repo.

## Właściwe wykonanie FSE

**Cel funkcjonalny:** `SSI DIRECTOR (SCC/Router) → canonical SSI MultiQuant engine/broker (do zweryfikowania na węźle MultiQuant) → CORE24 model 70B GGUF / CPU worker → MultiQuant scoring/telemetry/evidence → SCC mission result`.

To **docelowy przepływ do potwierdzenia**, a nie deklaracja istniejącego połączenia. Gdy aktywny silnik okaże się faktycznie na CORE24 zamiast na serwerze ROBERT/MultiQuant, zidentyfikować **jeden kanoniczny entrypoint** i uzgodnić go z właścicielem; nie tworzyć duplikatu i nie migrować modułów tylko na podstawie nazwy katalogu.

Istotne rozróżnienie:
- **A:** referencja BF16 z GPU: wykonana 32×3, 96/96; dowody już opublikowane.
- **B:** IQ2 CPU plain, bez autorskich modułów, jako niezależna kontrola jakości i zasobów.
- **C:** **ten sam** model IQ2/CPU/backend/cgroup, lecz faktycznie uruchamiany **przez MultiQuant z włączonymi i udokumentowanymi modułami**.
- **FSE nie wolno kwalifikować na podstawie samego B**. Przewaga autorskiej metody wymaga pomiaru **B vs C**, nie GPU vs CPU ani syntetycznego adaptera bez połączenia z silnikiem.

## Bramka następna: `FSE-P1R` (routing discovery, read-only)

**1. VPS MultiQuant / ROBERT:** sprawdzić live hostname/rolę; obecne ścieżki źródeł MultiQuant, nazwy entrypointów `manager`, `runner`, `router`, `worker`, `api`; procesy/usługi i dokumentowane adresy backendów **bez wypisywania sekretów**. Weryfikować artefakty źródłowe R20/R21, ale nie uznawać ich automatycznie za aktywne FSE runtime.

**2. CORE24:** już wiadomo, że model i CPU llama-cli istnieją. Ustalić endpoint/wykonawcę, który odpowiada na zlecenia MultiQuant, nie uruchamiając przy tym 70B. Nie zmieniać działających usług Ollama, CORE24 API i worker.

**3. Połączenie:** wybrać kanoniczny entrypoint, potwierdzić handshake/router i politykę kosztu, zabezpieczyć prywatne manifesty. Wykonać dopiero wtedy jeden ograniczony test **end-to-end MultiQuant → CPU 70B** z capture statusu wywołania modułu, wymaganą telemetrią oraz checkpointem.

**STOP:** nie odpalać direct `llama-cli -m` jako FSE-P2; nie deklarować gotowości runtime ani przewagi MultiQuant; nie kopiować 19 GB wag na inny VPS bez wymagania/oceny; nie zmieniać usług, swapu lub stanu produkcyjnego. Dotychczasowe P1/P1B/P1C zachowują wartość **audytu serwera modeli**, a nie dowodu działania całego FSE.

## Dowody

- [P1 host/model/swap](SSI_MULTIQ_FSE01_P1_CORE24_READONLY_PREFLIGHT_20261025.md).
- [P1B usług/inference limits](SSI_MULTIQ_FSE01_P1B_RUNTIME_DISCOVERY_20261025.md).
- [BF16 B1](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md).
- [FSE kickoff (wcześniejszy plan, uzupełniony tą korektą)](SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md).
- Prywatny dokument źródłowy: `jankes72/SSI_QWEN35_9B_IMAGE_BUILDS`, `docs/SSI_MULTIQ_VPS_HANDOFF_INVENTORY_20261023.md` (nie kopiować prywatnej zawartości).
