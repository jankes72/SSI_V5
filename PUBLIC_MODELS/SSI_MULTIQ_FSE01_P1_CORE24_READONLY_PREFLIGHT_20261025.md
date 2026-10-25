# SSI MultiQuant FSE-01 — P1 odczyt rzeczywistego CORE24

**Data dowodu operatora:** 2026-10-25 14:23:49 UTC  
**Etap:** `FSE-P1` — tylko odczyt parametrów sprzętowych i plików  
**Źródło:** terminalowy raport operatora przekazany do niezależnego przeglądu; ten wpis nie oznacza bezpośredniego SSH do serwera  
**Status:** `READ_ONLY_INFORMATION_COLLECTED / ENGINE_AND_CGROUP_VERIFICATION_PENDING`  
**Zmiany przez audyt:** `PRODUCTION_CHANGES=NONE` według skryptu operatora  
**Zakres:** jeden rzeczywisty węzeł CPU CORE24, nie cała migracja SSI ani uruchomiona misja FSE

## Fakty potwierdzone w konsoli

| Parametr | Raport |
|---|---:|
| System | Linux, kernel `6.1.0-43-amd64` |
| CPU dostępne dla systemu | `nproc=4` |
| `free -h` całkowity RAM | `15 GiB` (wartość zaokrąglona) |
| `free -h` RAM dostępny przy pomiarze | `15 GiB` (chwilowy odczyt, nie limit procesu) |
| System plików / model | `df -h`: `118G` łącznie, `82G` zajęte, `32G` dostępne, `73%` |
| Jedyny wskazany plik GGUF w badanym katalogu | `Meta-Llama-3.1-70B-Instruct-IQ2_XXS.gguf`; **19,097,389,632 B** |
| Dyskowy swap | `12,582,908 KiB` (~12 GiB), zajęte `13,932 KiB` (~13.6 MiB), priorytet `-2` |
| Swap zram | `2,097,148 KiB` (~2 GiB), **0 KiB swap usage**, priorytet `100` |
| zram logiczny rozmiar | **2,147,483,648 B** = 2 GiB |
| zram mm_stat | `orig_data_size=4,096 B`, `compr_data_size=90 B`, `mem_used_total=8,192 B` |
| Pamięć PSI (some/full) | wszystkie średnie avg10/avg60/avg300 `0.00` przy pobraniu |
| I/O PSI (some/full) | wszystkie średnie avg10/avg60/avg300 `0.00` przy pobraniu |
| `command -v llama-cli` | **not found in PATH** — nie dowodzi braku pliku binarnego ani braku wcześniej zbudowanego llama.cpp |
| Inferencja w tej próbie | **nieuruchomiona** |
| Rewizja bieżącego backendu | **niezweryfikowana** |
| SHA-256 rzeczywistego GGUF | **niepoliczone** |
| Aktywne limitowanie cgroup dla procesu inferencji | **niezweryfikowane** |

Log zawiera finalny znacznik `FSE01_P1_STATUS=READ_ONLY_INFORMATION_COLLECTED` oraz `FSE01_P1_END`. Nie ma w nim wyniku generacji ani kontroli jakości modelu; sama końcowa linia echo nie jest automatycznym pełnym PASS kryteriów wdrożenia.

## Interpretacja techniczna

1. GGUF 70B IQ2_XXS istnieje we wskazanym katalogu, a jego rozmiar **jest spójny** z wcześniejszym R5 i historycznymi wynikami V7. Nie sprawdzono jego hash ani bezpośredniej zgodności pochodzenia wag z BF16.
2. Zram jest **aktywny jako urządzenie swap**, lecz aktualnie nie przechowuje istotnych stron wymienionych; nie wykazano więc w tej próbce przyspieszenia ani zysku pamięci pod obciążeniem. Swap dyskowy stanowi fallback o niższym priorytecie. Sam zapis aktywnego zram nie potwierdza trwałości po restarcie.
3. Średnie PSI równe zeru to **krótka chwila spoczynkowa**, a nie gwarancja bezproblemowego przebiegu przy inferencji 70B.
4. Host pokazuje około 15 GiB RAM, ale wcześniejszy benchmark 8 GiB wykorzystywał **limit pamięci jednostki cgroup** na maszynie klasy 16 GB. Tego ograniczenia nie potwierdzono w obecnym P1; nie wolno ogłaszać uruchomienia na fizycznych 8 GB.
5. Obecne `llama-cli not found in PATH` oznacza tylko niewykrycie polecenia po PATH. Należy sprawdzić znane lokalizacje binarki i specyfikację jednostki wykonawczej **bez** pobierania, reinstalacji, resetowania cache, modyfikacji systemu lub ładowania modelu.

## Bramka FSE-P1 → FSE-P2: czego brakuje

**Następny bezpieczny odczyt:**
- Wyszukać obecne pliki `llama-cli` / `llama-server` w ustalonych katalogach aplikacji oraz `/usr/local/bin`, `/usr/bin` i historycznej lokalizacji źródeł; bez skanowania całego dysku i bez uruchamiania modelu.
- Ustalić ścieżkę binarki, bieżącą wersję/commit oraz zgodność z historycznym llama.cpp `9d1878a` — **nie zakładać** ciągłości.
- Identyfikować **konkretną** jednostkę wykonawczą/serwis i jej `MemoryMax` i `MemorySwapMax`, jeśli istnieje. Nie używać bezrefleksyjnie cgroup samej powłoki SSH jako dowodu limitu inferencji.
- Obliczyć SHA-256 GGUF dopiero w bezpiecznym oknie I/O, bo plik 19 GB powoduje pełny odczyt dysku; hash to osobna operacja, nie warunek odczytu stanu.
- Ocenić wpływ przyszłego testu CPU na obciążenie współdzielonego VPS i dobrać timeout. 96 krótkich zadań może trwać wiele godzin.

**Bramka formalna:** `P1_ENVIRONMENT_PARTIAL_PASS` (dostępny model, RAM/swap/PSI) oraz `P1_ENGINE_CGROUP_IDENTITY_PENDING`; **P2 NOT_RUN**. Nie należy publikować `P1_FULL_PASS` przed uzupełnieniem braków.

## Referencje

- [FSE-01 kickoff i etapy](SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md).
- [BF16 B1 — 32×3 PASS, weryfikacja i ograniczenia](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md).
- [MultiQuant R5 — inventory, bez modyfikacji](SSI_MULTIQ_ACTIVE_ARCHIVE_R5_CORE24_INVENTORY_20261025.md).
- [Historyczne V7 / 8 GiB CPU testy](SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md).

**Publiczna granica:** ten plik celowo nie zawiera prywatnych adresów hostów, nazw wewnętrznych jednostek ani ścieżek wykonywalnych i magazynów. Szczegółowy log pozostaje na MSI.
