# SSI MultiQuant V7 — Publiczny raport eksperymentalny 70B / 8 GiB

**Data:** 2026-10-25  
**Projekt:** SSI MultiQuant V7  
**Status:** wyniki eksperymentalne — niekwalifikowane produkcyjnie  
**Zakres publikacji:** wyłącznie wyniki, ogólna metodologia i ograniczenia; bez kodu źródłowego i prywatnego know-how.

## Cel

Zmierzyć wykonalność inferencji modelu klasy 70B na serwerze CPU z ograniczeniem pamięci procesu i udokumentować koszt pamięci oraz operacji dyskowych. Nie jest to twierdzenie o wynalezieniu kwantyzacji, mapowania pamięci ani streamingu SSD.

## Konfiguracja referencyjna

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

## Wnioski i ograniczenia

1. Inferencja krótkiej odpowiedzi modelu 70B IQ2_XXS zakończyła się poprawnie przy **MemoryMax=8 GiB** i skonfigurowanym swapie.
2. Występuje znaczna presja pamięci i intensywne operacje I/O. To potencjalny kierunek optymalizacji, **nie potwierdzony jeszcze wzrost szybkości**.
3. Zmiana limitu 12 → 8 GiB nie została udowodniona jako przyczyna zmiany czasu wykonania; stan page cache i inne warunki mogły się różnić.
4. Bardzo silna kwantyzacja może pogarszać jakość; pojedyncza poprawna odpowiedź nie oznacza porównywalnej jakości z oryginalnym modelem.
5. Testy dotyczą zwykłego `llama.cpp`; **autorskie mechanizmy MultiQuant V7 nie są jeszcze zweryfikowane jako szybsze**.

## Kolejne etapy

- **V7.15:** kontrolowane porównanie sposobów ładowania danych przy jednakowym modelu, zadaniu i budżecie pamięci. **Status: zaplanowany / w toku, bez opublikowanych wyników.**
- Powtórzenia w porównywalnych warunkach, rozdzielenie efektu cache i I/O, dłuższe zadania, walidacja jakości.
- Ewaluacja potencjalnych optymalizacji SSI MultiQuant dopiero po mierzalnej poprawie względem niezmienionego punktu odniesienia.

## Polityka informacji

Repozytorium publiczne zawiera wyłącznie wyniki, ograniczenia, ogólną metodologię i statusy. Kod, autorskie algorytmy, konfiguracja wrażliwej infrastruktury i wewnętrzny know-how nie są publikowane.
