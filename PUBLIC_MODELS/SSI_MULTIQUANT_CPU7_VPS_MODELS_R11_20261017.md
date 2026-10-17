# SSI MultiQuant R11 — pierwsze 7 kandydatów na istniejącym VPS MODELS 24/7

**Data decyzji operatora:** 2026-10-17.  
**Status:** zaakceptowany zakres i przygotowanie planu; **zero potwierdzonych nowych wag**.  
**Nadrzędna decyzja:** produkować **pojedynczo na SSI MODELS VPS (4 vCPU, ~15 GiB RAM, 12 GiB swap, ostatni audyt ~59 GB wolnego dysku)**, bez RunPoda i bez dodatkowych płatnych serwerów. Istniejące 13 modeli Ollama pozostaje produkcyjnie dostępne.

> R11 doprecyzowuje R10: zamiast pełnej trzynastki teraz realizujemy **pierwszą siódemkę modeli <=4B**, a 6 większych wariantów odkładamy do czasu uruchomienia docelowej współpracy DIRECTOR / ROBERT / SSI CODEX / Charlie / Iskry / systemów szkoleń. Plan zakłada etapowe progi jakości i odłożenie wariantów technicznie/licencyjnie niewykonalnych, nie fikcyjne deklarowanie 7/7 gotowych.

## 1. Ścisła lista 7 z 13 istniejących tagów

| Kolejność robocza | Oryginalny tag Ollama (nienaruszalny) | Rozmiar z ostatniego `ollama list` | Wskazany checkpoint źródłowy / warunek | Stan początkowy |
|---|---|---:|---|---|
| 1 | `qwen2.5-coder:1.5b-instruct-q4_K_M` | 986 MB | `Qwen/Qwen2.5-Coder-1.5B-Instruct` (Apache-2.0); potwierdzić revision i tokenizer | PILOT_READY_FOR_PREFLIGHT |
| 2 | `qwen3:1.7b-q4_K_M` | 1.4 GB | `Qwen/Qwen3-1.7B` (Apache-2.0); źródło i revision do zatwierdzenia | SOURCE_REVIEW |
| 3 | `hermes3:3b-llama3.2-q4_K_M` | 2.0 GB | `NousResearch/Hermes-3-Llama-3.2-3B`, licencja pochodna Llama 3.x / warunki Meta; należy zweryfikować zgodność konkretnej wersji | LICENSE_REVIEW |
| 4 | `qwen2.5-coder:3b-instruct-q4_K_M` | 1.9 GB | `Qwen/Qwen2.5-Coder-3B-Instruct`, **Qwen Research License: tylko non-commercial, komercja wymaga osobnego pozwolenia** | RESEARCH_ONLY |
| 5 | `qwen3.5:4b-q4_K_M` | 3.3 GB | `Qwen/Qwen3.5-4B` (Apache-2.0), vision / mmproj zgodność i walidacja multimodalności obowiązkowa | ARCH_CHECK |
| 6 | `tev1:0.8b-q8_0` | 833 MB | Pochodzenie i format **niepotwierdzone**; natywny typed-decision SSI System One, zachować typowany kontrakt | SOURCE_UNKNOWN |
| 7 | `d1:3b` | 3.7 GB | Pochodzenie i format **niepotwierdzone**; System One + vision projector, nie tworzyć wybrakowanego tekstowego zamiennika | SOURCE_UNKNOWN |

Kolejność pierwszych kroków: **1.5B → 1.7B**, potem warianty zgodne licencyjnie/technicznie według realnego obciążenia. Nie oznacza to, że przy mniejszej liczbie parametrów model ma automatycznie mniejszy peak RAM w konwersji.

### Publiczne źródła do sprawdzenia licencji i instrukcji

- https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct
- https://huggingface.co/Qwen/Qwen3-1.7B
- https://huggingface.co/NousResearch/Hermes-3-Llama-3.2-3B
- https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct/blob/main/LICENSE
- https://huggingface.co/Qwen/Qwen3.5-4B
- https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md
- https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md

## 2. Produkcja jako seria kontrolowana, bez zaburzeń inferencji

**Założenie:** już zainstalowane narzędzia `/opt/ssi-multiquant/llama.cpp/build/bin/llama-quantize` i `llama-imatrix` są CPU-only, zrealizowane podczas wcześniejszego audytu. `llama.cpp` checkout przechowuje swój commit w `/opt/ssi-multiquant/llama_cpp_commit.txt`. `llama.cpp` nie może być potajemnie uaktualniane przy każdym jobie.

1. **READ_ONLY_PREFLIGHT**: `hostname=ssi`, `ollama active`, sprawdzenie wszystkich 13 tagów, `ollama ps`, `free -m`, `df -Pm /`, istnienie narzędzi, status systemd, miejsce na dane robocze i limity. Żadnych zmian.
2. **SOURCE_LICENSE_CHECK**: checkpoint pasujący do obecnego modelu, hash upstream revision, tokenizer, licencja. Tylko legalny oryginał BF16/FP16; nigdy kaskadowe `Q4 → Q3` udawane jako nowa wysokiej jakości kwantyzacja.
3. **PILOT**: jeden 1.5B w odrębnym `/opt/ssi-multiquant/jobs/`, żadne pliki w magazynie Ollama. Wirtualne środowisko Python wyłącznie dla konwersji, bez zmiany pip globalnego. Praca `nice/ionice` i z ograniczonymi wątkami. Przy <~9 GiB `MemAvailable`, <~18 GB wolnego dysku lub niespodziewanym wysokim obciążeniu = `WAITING_FOR_RESOURCES`. Twarde limity pamięci (systemd cgroup) przed niezależnym uruchomieniem joba.
4. **GGUF & QUANT**: źródłowe HF `safetensors` → wysokiej precyzji GGUF → nowy quant. Wariant kontrolny Q4_K_M z zachowaniem wyższej precyzji ważnych tensorów lub Q5_K_M w zależności od potrzeb. `imatrix` dopiero z rzeczywistą, zgodną polityką prywatności i licencji próbką. `imatrix` to kalibracja, **nie trening**.
5. **ARTIFACT_VERIFIED**: manifest pochodzenia, `sha256sum`, faktyczny rozmiar pliku, test zgodności GGUF z Ollama, zużycie pamięci, blokada kandydata w bramce.
6. **CANARY**: włączać osobno, za zgodą Dyrektora, obserwować prawdziwe zadania (Notariusz), porównywać z poprzednim wariantem i przewidzieć powrót do poprzedniego modelu.
7. **NEXT**: dopiero po zakończeniu jednego wariantu. Pliki przejściowe zachować do potwierdzenia odbioru; nigdy automatycznie usuwać archiwum cudzych materiałów.

**Obciążenie:** 4 vCPU i 15 GiB RAM **wystarczają do próby 1.5B**, ale nie są gwarancją 7/7. Tryb domyślny to maksymalnie jeden proces budowania i 1–2 wątki, wyłączony priorytet wysokiej mocy. Jeżeli aktualne modele zaczynają zużywać zasoby, przerwać przed następnym checkpointem, nie wyłączać Ollama. **12 GiB swap jest buforem awaryjnym, nie ekwiwalentem dodatkowego szybkiego RAM.**

**Dysk:** ostatnio ~59 GB wolne. Budować pojedynczo, nie pobierać w jednym kroku wszystkich 7 BF16/FP16. Nawet 4B multimodal może mieć duży working set. Bez wykorzystania RunPod i bez automatycznej zmiany konfiguracji.

## 3. Druga seria — 6 odłożonych wariantów

Odłożyć:
- `deepseek-coder:6.7b-instruct-q4_K_M`
- `lfm2.5:8b-a1b-q4_K_M`
- `hermes3:8b-llama3.1-q3_K_M`
- `hermes3:8b-llama3.1-q4_K_M`
- `qwen2.5-coder:7b-instruct-q3_K_M`
- `qwen2.5-coder:7b-instruct-q4_K_M`

Wykonać gdy działa już system DIRECTOR/ROBERT/SSI CODEX/Charlie/Iskry/szkolenia i istnieją zweryfikowane zasoby, jakość decyzji oraz zgoda na koszt wyjątkowego GPU, gdy będzie niezbędny.

## 4. Granice wykonania

- Brak automatycznego startowania RunPod; aktualny Pod A40 był `EXITED`, dodatkowy GPU pozostaje rezerwą, wymagającą osobnej zgody.
- Brak instalacji 7 nowych modeli dopóki nie powstaną **rzeczywiste pliki GGUF** z testami i sha.
- Brak sztucznego potwierdzania `7/7 PASS`, gdy Tev1 / D1 mają nieznane źródła, licencje lub multimodalny runtime.
- Repo publiczne: tylko plan i bezpiecznie agregowane statystyki, **bez wag, kodu prywatnego, kluczy API, adresów wewnętrznych i danych misji**.

**Decyzja:** R11 jest obowiązującą wersją w zakresie kolejności i zasobów produkcji SSI MultiQuant.

## Potwierdzony audyt operatora CPU-7 — READ_ONLY_PREFLIGHT PASS

**17.10.2026, raport uruchomienia `01_AUDYT_READ_ONLY.sh` na VPS MODELS:**

- **Host / zasoby**: jądro Linux Debian 6.1.0-43-amd64, **4 CPU**, **15 GiB RAM** (ok. 15 GiB available w chwili odczytu), **12 GiB swapfile**; **59 GB wolnego miejsca** w systemie plikow.
- **Produkcja**: `ollama` aktywna, wersja 0.40.5, **13/13 oczekiwanych oryginalnych tagów istnieje**, `ollama ps` nie wskazało modeli zaladowanych **w momencie audytu**.
- **Narzędzia**: `git`, `cmake`, `gcc`, `g++`, `python3`, `flock`, `systemd-run`, `llama-quantize`, `llama-imatrix` — obecne. Commit `llama.cpp`: `9d1878a4354e743529fbe09e7350a957f5e39e9a`. 
- **Warianty** (parametry z API Ollama): 1.5B coder `qwen2`, 1.7B qwen3 `qwen3`, Hermes 3B `llama`, coder 3B `qwen2`, Qwen3.5 4B `qwen35`, **Tev1 0.8B `qwen35`**, **D1 3B `lfm2`**. Dokladne pochodzenie i pelna zgodnosc multimodalna Tev1 / D1 wciaz niepotwierdzone; `multimodal_fields=0` w uproszczonym audycie nie przesadza o braku osobnego projektora lub komponentow.
- **Status `PILOT_QWEN15B`**: `NOT_STARTED` — istnieje skrypt, ale operator **nie uruchomil jeszcze `02_PILOT_QWEN15B_CPU.sh`**. Brak nowych kwantów lub danych potwierdzajacych ich jakosc.
- **Kontrola skryptu**: statyczna skladnia Bash OK. `llama.cpp` w wskazanym commicie deklaruje `torch==2.11.0` w wymaganiach konwertera; pakiet `python3-venv` moze wymagać jednorazowej instalacji na minimalnym Debianie. Pojedynczy pilot ma cgroup `CPUQuota=150%`, `MemoryMax=9G`, `MemorySwapMax=0`; to **ogranicza**, ale nie gwarantuje zerowego wplywu na produkcyjny dysk i siec. Podczas prac konieczne monitorowanie `ollama` i zasobow.

Wniosek: **bezpiecznie przechodzimy do przygotowania jednego pilota** dopiero po potwierdzeniu zaleznosci i sprawdzeniu biezacego obciazenia. Nie uruchamiać pozostałych 6 skryptem 1.5B; ich przygotowanie jest oddzielnym etapem.

## Pilot Qwen 1.5B — R11 FIX R2

**Raport operatora, 17.10.2026:** przygotowanie `python3-venv` na SSI MODELS zakończone powodzeniem (Python 3.11.2, `ionice` obecny, Ollama aktywna). Skrypt pierwszego pilota uruchomił cgroup (`CPUQuota=150%`, `MemoryMax=9G`, `MemorySwapMax=0`) i potwierdził wolne zasoby. **Nie zbudował jednak modelu**. Dwa potwierdzone problemy:
1. `ollama ps` zgłosiło `panic: $HOME is not defined` po uruchomieniu przez `systemd-run`. Poprzedni skrypt mógł błędnie przepuszczać nieudaną kontrolę aktywnych modeli.
2. `pip` w izolowanym venv (Debian pip 23.0) próbował instalować `torch==2.11.0` wyłącznie z indeksu PyTorch CPU; metadane `typing-extensions` były odrzucone, a zależność `flit_core` nie była dostępna w tym indeksie. Instalacja zależności zakończyła się kodem błędu, zanim pobrano checkpoint HF.

**Poprawka lokalnej paczki `SSI_MULTIQ_CPU7_R11_FIX_R2_20261017.zip`:** nie jest publikowana w repo zawierającym tylko dowody i plany. Zapewnia `HOME=/root` w cgroup, sprawdza aktywne modele poprzez `/api/ps` i w razie problemu kończy się stanem `WAITING_FOR_RESOURCES` (fail-closed). Podnosi `pip` wyłącznie w dedykowanym venv, rozdziela oficjalne CPU-only wheel PyTorch od normalnych zależności PyPI, kontroluje `torch.version.cuda` i `pip check`, używa pośrednich plików `.partial` i blokady nadpisania przy przerwaniu. **Nie dotyka oryginalnych 13 tagów, nie używa RunPod i nie uruchamia zmian Routera.**

**Testy wykonane przed wydaniem:** `bash -n` skryptu OK; kontrola fail-closed z mockami: Ollama idle → kontynuuj, 1 model załadowany → STOP, błąd statusu Ollama → STOP. **Nie wykonano end-to-end na zdalnym VPS.** Po ponownym uruchomieniu konieczne sprawdzenie pełnego logu i rzeczywistego manifestu, nie wnioskować o stanie PASS z samej obecności pliku.


## R11 FIX R2 — pierwszy rzeczywisty kandydat GGUF wykonany 17.10.2026

**Potwierdzone w dostarczonym logu terminala operatora** (to nie jest niezależny odczyt aktualnego serwera):

- Po instalacji `python3-venv` oraz naprawie skryptu `SSI_MULTIQ_CPU7_R11_FIX_R2_20261017.zip` zakończono instalację w izolowanym Python venv: `torch==2.11.0+cpu`, `transformers==4.57.6`, `huggingface_hub==0.36.2`, `gguf==0.19.0`. `pip check`: brak uszkodzonych zależności, a `CPU_ONLY_TORCH_OK` potwierdził brak CUDA wheels.
- Źródło: `Qwen/Qwen2.5-Coder-1.5B-Instruct`; skrypt odczytał rewizję rozpoczynającą się od `2e1fd397ee46e138` i licencję `apache-2.0`. Wagi pobrano do izolowanego katalogu zadania.
- Konwersja oficjalnych wag BF16 → GGUF F16 zakończona; wynik F16 ok. **2944.68 MiB** (tensor data).
- Kwantyzacja zakończona w **196322.56 ms** (ok. 3 min 16 s) na **1 wątku**, z bazowym `Q4_K_M`, precyzją wybranych tensorów `Q5_K`/`Q6_K`. Wygenerowany GGUF **905.13 MiB** dla wag (na dysku raportowany ok. **0.955 GB**).
- **Kandydat fizycznie utworzony:** `/opt/ssi-multiquant/jobs/qwen25-coder-15b/ssi-multiq-qwen25-coder-15b-Q4KM-mix-v1.gguf`.
- **SHA256:** `c8e7a1d6ad88656b24c378e98cb469324c2b9a55c7fd180080c1743ff65672cb`.
- Stan = `CANDIDATE_DISABLED_UNTESTED`. Końcowy log skryptu zgłasza `ollama is still active` i brak ponownej rejestracji oraz zmian istniejących 13 oryginalnych tagów; końcowa niezależna walidacja aktualnej obecności 13 tagów i wykonania inference kandydata jest **jeszcze niewykonana**.
- **Nie twierdzimy, że wariant jest jakościowo lepszy od istniejącego Q4**. Sama kwantyzacja nie zawiera fine-tuningu ani nowego treningu. Następnym krokiem jest **read-only weryfikacja hasha, metadata i stanu usług**, a dopiero później kontrolowany test inference bez zmiany produkcyjnego Routera.

### SWAP na trzech VPS — plan warunkowy

Użytkownik przekazał osobną koncepcję `SSI_3VPS_SWAP_MULTIQ_R1_20261017.zip`. Sama nazwa/opis paczki **nie jest dowodem jej zawartości ani wykonania**. **MODELS ma już 12 GiB SWAP**, więc nie należy go dublować. Propozycje na **ROBERT do 8 GiB**, **DIRECTOR do 4 GiB** to wartości niezatwierdzone, zależne od audytu ilości RAM, aktualnego SWAP, filesystem, obciążeń i dysku. Najpierw wyłącznie odczyt `swapon --show`, `free -h`, `df -h`, `systemctl`; bez `--apply`, bez instalacji na ślepo i bez modyfikowania istniejących plików wymiany.

SWAP **nie łączy pamięci trzech VPS**, nie gwarantuje ukończenia treningu i nie zwiększa przepustowości CPU. Director/Robert mogą wykonywać osobne pomocnicze zadania przy zachowaniu SLA misji, a MODELS zostaje inferencyjny. Rozbudowa o pozostałe 6 wariantów i 5 przyszłych modeli Roberta jest nadal odłożona.

## Potwierdzenie integralności operatora — GGUF v3 SHA256 PASS

**17.10.2026, audyt operatora bez zmian na produkcyjnym SSI MODELS VPS:**

- `/opt/ssi-multiquant/jobs/qwen25-coder-15b/ssi-multiq-qwen25-coder-15b-Q4KM-mix-v1.gguf` istnieje, SHA256 po ponownym odczycie **ZGODNY** z manifestem: `c8e7a1d6ad88656b24c378e98cb469324c2b9a55c7fd180080c1743ff65672cb`.
- Nagłówek GGUF = **GGUF v3**, rozmiar pliku **955.05 MB**, manifest podaje `CANDIDATE_DISABLED_UNTESTED`; to potwierdzenie integralności pliku, nie zdolności inferencyjnych ani trafności decyzji.
- `ollama` nadal **active**, lista zawiera komplet **13 pierwotnych tagów**, `ollama ps` nie wskazywał modelu załadowanego w chwili testu.
- Host: **15 GiB RAM (ok. 15 GiB available)**, istniejący **12 GiB SWAP**, zajęte ok. 63 GB, wolne **51 GB**; nie zwalniać plików źródłowych bez potwierdzenia backupu i kolejnej fazy.
- **R11 aktualny stan:** zbudowanych **1/7** kandydatów, zweryfikowanych statycznie **1/7**, zatwierdzonych inferencyjnie **0/7**, produkcyjnych **0/7**.
- **Kolejny konieczny test:** oddzielne narzędzie `llama-completion` na CPU w kontrolowanej transient cgroup; repo `llama.cpp` ma `LLAMA_BUILD_SERVER=OFF`, dlatego **`llama-cli` nie występuje w bieżącej konfiguracji**, podczas gdy `llama-completion` jest wspierane przy `LLAMA_BUILD_TOOLS=ON`. Budowa jednego narzędzia `-j1`, `nice/ionice`; 1 lokalna odpowiedź testowa bez rejestrowania GGUF w Ollamie, bez routingu ani płatnych API. Nie promować automatycznie po jednym smoke teście.
