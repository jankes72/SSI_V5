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
