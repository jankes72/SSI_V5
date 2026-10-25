# SSI MultiQuant V7 — Publiczny raport eksperymentalny 70B / 8 GiB

**Data:** 2026-10-25  
**Projekt:** SSI MultiQuant V7  
**Status:** wyniki eksperymentalne — niekwalifikowane produkcyjnie  
**Zakres publikacji:** wyłącznie wyniki, ogólna metodologia i ograniczenia; bez kodu źródłowego i prywatnego know-how.

## Cel

Zmierzyć wykonalność inferencji modelu klasy 70B na serwerze CPU z ograniczeniem pamięci procesu i udokumentować koszt pamięci oraz operacji dyskowych. Nie jest to twierdzenie o wynalezieniu kwantyzacji, mapowania pamięci ani streamingu SSD.

## Konfiguracja wariantu CPU / IQ2_XXS

- Model: **Meta Llama 3.1 70B Instruct**, plik GGUF, kwantyzacja **IQ2_XXS** (~2.0625 bpw).
- Rozmiar pliku: **19,097,389,632 B** (~17.79 GiB / 19.10 GB).
- Silnik: **llama.cpp**, commit **9d1878a**, kompilacja CPU.
- VPS: **4 vCPU, 16 GB klasy RAM, Debian 12**; bez GPU.
- Limit cgroup: **8 GiB pamięci** oraz **8 GiB limitu swapu** w wariantach 8 GiB. Limit cgroup **nie jest równoznaczny** z fizyczną maszyną wyposażoną tylko w 8 GiB RAM.
- Próba jakościowa: krótka odpowiedź na „What is 2 plus 2? Answer only with the number.”; odpowiedź referencyjna „4”.
- Poprawny szablon konwersacji Llama 3.1 Instruct; pojedynczy przebieg.

## Wyniki zweryfikowane na podstawie logów eksperymentów

| Etap | Limit pamięci | Czas ścienny | Odpowiedź | Status |
|---|---:|---:|---|---|
| V7.4 | 12 GiB | 8 min (timeout) | niepoprawna / nieukończona | INCONCLUSIVE (124) |
| V7.5 | 12 GiB | 295.09 s | niepoprawna; format wywołania narzędzia | TECHNICAL PASS / ANSWER FAIL |
| V7.8 | 12 GiB | **141.587 s** | **4** | PASS (exit 0) |
| V7.10 | 8 GiB | **117.816 s** | **4** | PASS (exit 0) |
| V7.11 | 8 GiB | **116.920 s** | **4** | PASS (exit 0); 57 próbek monitoringu |
| V7.13 | 8 GiB | **127.310 s** | **4** | PASS (exit 0); 62 próbki, IOAccounting=yes |

Prędkość generowania raportowana przez CLI: około **0.1 tok./s**. Są to pojedyncze, krótkie próby jakościowe, nie pełny benchmark użyteczności, rozumowania ani długiego kontekstu.

## Telemetria V7.11–V7.14

- Maksimum użycia pamięci cgroup: **8 GiB** (osiągnięty limit).
- Przykładowe maksimum cache plikowego w V7.11: **7.888 GiB**.
- Swap zaobserwowany w próbkach: około **0.058–0.059 GiB**.
- V7.11: **192,974** dodatkowych major page faults oraz **16,864,834** odwołań `workingset_refault_file`.
- V7.13: **195,976** dodatkowych major page faults, **16,711,252** `workingset_refault_file`, **471,914** zdarzeń `memory.events max`; **brak OOM / OOM kill**.
- W V7.14 zweryfikowano **62/62** próbki I/O przypisane do cgroup oraz monotoniczność licznika:
  - `rbytes` początkowo **791,486,464 B**, końcowo **76,454,150,144 B**.
  - Delta odczytów: **75,662,663,680 B**, czyli **70.466 GiB**.
  - Delta operacji odczytu: **1,151,036**.

**Zastrzeżenie pomiarowe:** raport końcowy systemd-run podawał ~1.0 MB odczytów, podczas gdy odczyty `io.stat` w toku działania wskazywały ~70.466 GiB. Liczniki `io.stat` w próbkach były monotoniczne, ale rozbieżność sposobu rozliczania I/O wymaga osobnej analizy. Odczyty cgroup nie są równoznaczne z dowodem, że każdy bajt pochodzi wyłącznie z wag modelu; nie wyciągamy jeszcze wniosku o 4-krotnym odczytaniu konkretnych tensorów.

## Główna referencja bazowa BF16 — test wykonany 2026-10-25

**Status:** `BF16_BASELINE_SMOKE_PASS_POD_STOPPED`.

Oryginalny **Meta Llama 3.1 70B Instruct w BF16, bez kwantyzacji**, został pobrany, załadowany i sprawdzony na RunPod. Jest przyjęty jako **główny model bazowy do kolejnych porównań odpowiedzi SSI MultiQuant V7**. Procedura uruchomienia, wykonania pytania, zapisu wyników na komputerze operatora i wysłania polecenia zatrzymania Poda została wykonana poprawnie.

**Gotowość do kolejnych pytań:** konfiguracja oraz procedura zostały zweryfikowane w jednym teście. Pod po teście zatrzymano; panel RunPod potwierdził `Compute: Not running`, `Container storage: Not running` i **łącznie $0.00/h**. Następna seria wymaga ponownego uruchomienia zasobu GPU, odtworzenia środowiska i pobrania oraz załadowania wag na dysk tymczasowy. Zapisany wynik referencyjny pozostaje dostępny niezależnie od stanu Poda.

### Konfiguracja i wynik referencji

| Parametr / pomiar | Zweryfikowana wartość |
|---|---|
| Repozytorium modelu | `meta-llama/Llama-3.1-70B-Instruct` |
| Rewizja modelu | `1605565b47bb9346c5515c34102e054115b4f98b` |
| Precyzja i rozmieszczenie | BF16; parametry na dwóch GPU; bez CPU/disk offload |
| GPU | 2 × NVIDIA A100-SXM4-80GB |
| Pliki wag | 30 plików safetensors; **141,107,497,872 B** ≈ 141.107 GB ≈ **131.417 GiB** |
| Prompt użytkownika | `What is 2 plus 2? Answer only with the number.` |
| Odpowiedź / ocena | **4 / PASS** |
| Liczba tokenów wejściowych po szablonie | 49 |
| Wygenerowane tokeny | 2, w tym token zakończenia; ID: `[19, 128009]` |
| Czas zapytania z prefill | **0.718169 s** |
| Pobieranie modelu | **482.785402 s** |
| Ładowanie modelu | **19.649262 s** |
| Łączny czas mierzony przez skrypt inferencji | **503.848592 s**; bez uruchamiania Poda i instalacji zależności |
| Szczyt alokacji PyTorch na GPU 0 / GPU 1 | 70,581,917,184 B / 70,581,127,680 B |
| Suma szczytów alokacji GPU | **131.468 GiB**; suma maksimów dla dwóch GPU |
| Szczyt RSS procesu na hoście | 11,110,174,720 B ≈ **10.347 GiB**; osobna metryka od VRAM i pamięci cgroup |

**Ustawienia generacji:** `do_sample=false`, `num_beams=1`, `max_new_tokens=16`, `use_cache=true`, seed `0`, `eos_token_id=[128009]`, `pad_token_id=128009`. Użyto szablonu konwersacji dołączonego do przypiętej rewizji tokenizera, z dodaniem nagłówka odpowiedzi asystenta. Lista wiadomości zawierała jedno pytanie użytkownika; sam szablon dodał domyślną wiadomość systemową z datami. Pełny wyrenderowany prompt oraz tokeny zapisano w wyniku.

**Środowisko:** PyTorch `2.8.0+cu128`, Transformers `4.57.6`, Accelerate `1.12.0`, huggingface-hub `0.36.0`, safetensors `0.8.0`; attention SDPA. Czas zapytania obejmuje prefill i generację po załadowaniu modelu, z synchronizacją obu GPU przed i po pomiarze.

### Dowody i integralność

Prywatna paczka operatora: `SSI_RUNPOD_REFERENCE_20261025T121932Z.zip`. Zawiera `result.json`, `result.sha256`, `run.log` i `status.json`. Sprawdzono poprawność CRC archiwum, zgodność SHA-256 pliku wyniku z manifestem i statusem oraz zgodność danych wyniku z rekordem w logu.

SHA-256 oryginalnego `result.json`:

`190603823f22a61820f0690a61e93b1cf05d3a56f37347f97aff7731448843e9`

SHA-256 wyrenderowanego promptu:

`ff044216792522473fb12039d464e35cf984286dd7f588ef98907e99dda65ac1`

W lokalnym statusie zapisano `reference_completed=true`, `stop_requested=true` i kod wyjścia polecenia zatrzymania `0`. Pole `billing_zero_verified=false` w tym pliku opisuje stan wiedzy skryptu w chwili zapisu: skrypt nie sprawdzał panelu rozliczeń. **Późniejsza, odrębna kontrola panelu RunPod potwierdziła zatrzymanie i $0.00/h**; oryginalnych plików dowodowych nie zmieniano. Zerowa stawka dotyczy zatrzymanego Poda po teście, a nie kosztu zakończonego przebiegu.

Paczka źródłowa pozostaje prywatna. Ten publiczny wpis udostępnia wyniki, metodologię i identyfikatory integralności; nie zawiera adresów infrastruktury, identyfikatora Poda, kluczy, tokenów, kodu wykonawczego ani wag modelu.

### Znaczenie dla porównań SSI MultiQuant V7

- Treść pytania użytkownika jest taka sama jak w opisanych wyżej próbach CPU / IQ2_XXS. W obu wariantach uzyskano odpowiedź **4**.
- Nowy wynik potwierdza wykonanie referencji BF16 dla **jednego krótkiego pytania**. Pełna ocena jakości, długiego kontekstu i użyteczności pozostaje do wykonania.
- Historyczne czasy CPU w tym raporcie są czasami ściennymi przebiegów, natomiast **0.718169 s** mierzy zapytanie GPU po załadowaniu modelu. Nie wyliczamy z tych liczb ilorazu przyspieszenia.
- **131.468 GiB alokacji GPU** i **MemoryMax=8 GiB na CPU** opisują różne zasoby i zakresy pomiaru; nie stanowią bezpośredniego pomiaru procentowej redukcji RAM przez autorskie mechanizmy MultiQuant.
- Pełna zgodność historycznych ustawień generacji i wyrenderowanych promptów CPU z referencją BF16 nie została potwierdzona. Do następnej serii należy przypiąć model i tokenizer, zapisać identyczne wiadomości i szablon, uzgodnić parametry generacji oraz osobno mierzyć pobieranie, ładowanie, prefill i generację.
- Kolejne porównania powinny obejmować większy, z góry ustalony zestaw pytań, powtórzenia i automatyczny zapis odpowiedzi oraz telemetrii obu wariantów. Statusy RAM Guard i syntetycznych testów pamięci SSI są dokumentowane osobno; niniejszy wynik nie zmienia ich zakresu walidacji.

## Referencja BF16 B1 — pełna seria zweryfikowana

**Aktualizacja 2026-10-25:** wykonano 5 prób pilotażowych i pełne 32×3. Niezależne ponowne ocenienie archiwum potwierdziło **32/32 w każdym powtórzeniu, łącznie 96/96**, bez pominięć, timeoutów i OOM. Mediana odpowiedzi: **0,244743 s**, p95: **0,447384 s**, na załadowanym modelu. Pobieranie, ładowanie i skrypt inferencji zajęły **508,477 s**; nie jest to pełny czas płatnego zasobu. Panel RunPod po zakończeniu potwierdził zatrzymanie compute i storage oraz **$0.00/h**.

[Pełny raport B1, metodologia, weryfikacja i ograniczenia](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md) · [Dane maszynowe i hashe do parowania z CPU](BENCHMARKS/SSI_MULTIQ_B1_BF16_PUBLIC_EVIDENCE_20261025.json).

Referencja BF16 jest zakończona. Porównanie CPU/IQ2 oraz przewaga modułów MultiQuant pozostają niepotwierdzone do dostarczenia wyników, zgodności tokenizacji i pochodzenia GGUF. 96 wywołań to trzy powtórzenia 32 zadań; nie jest to ogólny benchmark jakości ani test natywnego SCC.

## Wnioski i ograniczenia

1. Inferencja krótkiej odpowiedzi modelu 70B IQ2_XXS zakończyła się poprawnie przy **MemoryMax=8 GiB** i skonfigurowanym swapie.
2. Występuje znaczna presja pamięci i intensywne operacje I/O. To potencjalny kierunek optymalizacji, **nie potwierdzony jeszcze wzrost szybkości**.
3. Zmiana limitu 12 → 8 GiB nie została udowodniona jako przyczyna zmiany czasu wykonania; stan page cache i inne warunki mogły się różnić.
4. Bardzo silna kwantyzacja może pogarszać jakość; pojedyncza poprawna odpowiedź nie oznacza porównywalnej jakości z oryginalnym modelem.
5. Testy dotyczą zwykłego `llama.cpp`; **autorskie mechanizmy MultiQuant V7 nie są jeszcze zweryfikowane jako szybsze**.

## Kolejne etapy

- **Referencja BF16:** pojedynczy test oraz pełny B1 32×3 wykonane, archiwa zweryfikowane, Pod zatrzymany. Następny etap: zgodność tokenizacji i pochodzenia GGUF oraz wykonanie odpowiadającej serii CPU; ponowne uruchomienie GPU nie jest potrzebne do samego odczytu zapisanej referencji.
- **V7.15:** kontrolowane porównanie sposobów ładowania danych przy jednakowym modelu, zadaniu i budżecie pamięci. **Status: zaplanowany / w toku, bez opublikowanych wyników.**
- Powtórzenia w porównywalnych warunkach, rozdzielenie efektu cache i I/O, dłuższe zadania, walidacja jakości.
- Ewaluacja potencjalnych optymalizacji SSI MultiQuant dopiero po mierzalnej poprawie względem niezmienionego punktu odniesienia.

## Polityka informacji

Repozytorium publiczne zawiera wyłącznie wyniki, ograniczenia, ogólną metodologię i statusy. Kod, autorskie algorytmy, konfiguracja wrażliwej infrastruktury i wewnętrzny know-how nie są publikowane.
