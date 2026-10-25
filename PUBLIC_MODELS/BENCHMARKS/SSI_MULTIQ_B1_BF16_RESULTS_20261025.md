# SSI MultiQuant B1 — zweryfikowana referencja Llama 3.1 70B BF16

**Data:** 2026-10-25  
**Przebieg:** `SSI_BF16_B1_20261025T135837Z`  
**Status:** `BF16_ARM_VERIFIED_COMPLETE_POD_STOPPED_PAIRING_PENDING`

Wykonano pełny tor referencyjny **A: BF16_GPU_REFERENCE**: pięć prób pilotażowych i **32 zadania w trzech kolejnych powtórzeniach**. Niezależne ponowne ocenienie odpowiedzi zapisanych w archiwum dało **32/32 w każdym powtórzeniu, łącznie 96/96**. Pilot uzyskał 5/5 i nie wchodzi do wyniku 96/96. Nie ma pominiętych prób, błędnych odpowiedzi, timeoutów ani OOM.

Jest to weryfikacja archiwum operatora, spójności dowodów i ponowne obliczenie ocen; nie jest niezależnym powtórzeniem obliczeń na drugiej instalacji. Wynik stanowi empiryczną bazę do kolejnych eksperymentów SSI. Nie dowodzi jeszcze przewagi MultiQuant ani równoważnej jakości wariantu IQ2_XXS.

- [Dane maszynowe: agregaty, oceny przypadków, hashe promptów i tokenów](SSI_MULTIQ_B1_BF16_PUBLIC_EVIDENCE_20261025.json).
- [Zamrożone 32 pytania i wzorce ocen](SSI_MULTIQ_B1_SUITE_32_20261025.jsonl).
- [Protokół B1 R1](SSI_MULTIQ_70B_BF16_IQ2_AND_MODULES_PROTOCOL_B1_R1_20261025.md).
- [Historyczna referencja pojedynczego pytania i próby CPU](../SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md).

## Wynik jakościowy

| Kategoria | Liczba różnych zadań | Powtórzenie 1 | Powtórzenie 2 | Powtórzenie 3 |
|---|---:|---:|---:|---:|
| Matematyka | 8 | 8/8 | 8/8 | 8/8 |
| Magazyn | 8 | 8/8 | 8/8 | 8/8 |
| Ekstrakcja | 6 | 6/6 | 6/6 | 6/6 |
| Pytania ze źródłem | 6 | 6/6 | 6/6 | 6/6 |
| Syntetyczne teksty przypominające SCC | 4 | 4/4 | 4/4 | 4/4 |
| **Razem** | **32** | **32/32** | **32/32** | **32/32** |

Ocena `normalized_exact.r1`: Unicode NFC, normalizacja białych znaków i casefold, następnie ścisła zgodność ze wzorcem; bez tolerancji liczbowej. Sprawdzono ponownie surowe odpowiedzi względem oryginalnych wzorców JSONL, a nie wyłącznie flagi `CORRECT` z raportu. Dla każdego zadania wszystkie trzy przebiegi wygenerowały identyczne ID tokenów wyjściowych.

**96 wywołań to trzy powtórzenia tych samych 32 prostych, publicznych zadań**, nie 96 niezależnych pytań. Nie wyznaczamy na tej podstawie ogólnej jakości modelu ani przedziału ufności dla reprezentatywnego zbioru użytkowników. Cztery przykłady SCC dotyczą syntetycznych tekstów, a nie natywnego parsera, wykonania misji czy integracji całego SSI.

## Konfiguracja referencji

| Parametr | Wartość |
|---|---|
| Model | `meta-llama/Llama-3.1-70B-Instruct` |
| Rewizja modelu i tokenizera | `1605565b47bb9346c5515c34102e054115b4f98b` |
| Precyzja | BF16, bez kwantyzacji |
| Sprzęt | 2 × NVIDIA A100-SXM4-80GB; host 32 vCPU, deklarowane 500 GB RAM |
| Rozmieszczenie modelu | Wyłącznie GPU 0 i 1, bez CPU/disk offload |
| Wagi | 30 plików safetensors, 141 107 497 872 B ≈ 131,417 GiB |
| Silnik | Transformers 4.57.6; PyTorch 2.8.0+cu128; Accelerate 1.12.0; SDPA |
| Generacja | Greedy, `do_sample=false`, `num_beams=1`, seed 0, `max_new_tokens=96`, `use_cache=true` |
| Zakończenie | EOS `[128001,128008,128009]`; pad `128009`; repetition penalty 1,0 |
| Dopuszczony kontekst | 4096 tokenów; nie jest to test maksymalnego kontekstu modelu |
| Timeout pojedynczego zapytania | 30 s; żadna próba go nie osiągnęła |

Przed tą sesją operator jawnie zniósł wcześniejszy globalny limit czasu i kosztu. Zestaw pytań, kolejność, reguła oceny i ustawienia generacji pozostały bez zmian. Po pilocie wykonano pełne 32×3 bez dostrajania modelu do wyników. KV cache był tworzony od nowa dla każdego zapytania; model pozostawał załadowany. Pierwsze pytanie pilota nie miało wcześniejszego rozgrzania inferencji.

## Czas i zasoby

| Pomiar | Wartość / zakres |
|---|---:|
| Pobieranie wag | 460,853 s — 7 min 40,9 s |
| Ładowanie modelu | 16,125 s |
| Cały skrypt inferencji: pobranie, ładowanie, pilot i seria | 508,477 s — 8 min 28,5 s |
| Od uruchomienia lokalnego launchera do żądania zatrzymania | około 535,457 s — 8 min 55,5 s |
| Pełna pętla 96 wywołań po pilocie | 28,472 s |
| Suma czasów `generate` dla 96 wywołań | 28,169 s |
| Czas odpowiedzi p50 / p95 | **0,244743 s / 0,447384 s** |
| Czas odpowiedzi min / max | 0,224696 s / 0,753632 s |
| TTFT p50 / p95 | 0,142910 s / 0,144603 s |
| Prefill p50 / p95 | 0,141433 s / 0,143066 s |
| Mediana tokenów/s, z prefill i tokenem końca | 8,618 |
| Wygenerowane tokeny w pełnej serii | 243, wliczając tokeny zakończenia |
| Suma CPU-seconds pełnej serii | 28,292 |
| Szczyt alokacji PyTorch GPU 0 / GPU 1 | 70 601 726 976 B / 70 599 641 600 B |
| Szczyt rezerwacji PyTorch GPU 0 / GPU 1 | 70 617 399 296 B / 70 617 399 296 B |
| Szczyt RSS procesu | 11 556 020 224 B ≈ 10,762 GiB |
| Szczyt pamięci cgroup Poda od początku jego życia | 144 276 684 800 B ≈ 134,368 GiB |
| Szczyt swapu cgroup w zapisanych licznikach | 0 B |
| Przyrost major page faults w 96 próbach | 0 |

Pełna seria trwała od **14:07:02,345568 do 14:07:30,817538 UTC** (15:07 czasu polskiego). Czasy zapytań obejmują prefill i generację na już załadowanym modelu, synchronizację GPU oraz narzut instrumentacji. Nie obejmują uruchomienia Poda, instalacji zależności ani pobierania wag. Percentyle obliczono interpolacją liniową po 96 wywołaniach. Tokeny/s dotyczą bardzo krótkich odpowiedzi i nie są miarodajnym benchmarkiem długiej generacji ani przepustowości z batchingiem.

Zebrano 49 próbek dla każdej GPU w przedziale pełnej serii. Mediany użycia wyniosły 48% i 49%; największe zaobserwowane wartości 58% i 59%. Żądany odstęp próbkowania wynosił 0,5 s plus czas wykonania narzędzia. Próbki mogą pomijać krótkie szczyty; nie są całką energii ani dokładnym pomiarem każdego zapytania. Dodatkowe agregaty mocy i pamięci są w pliku JSON.

**RSS procesu, VRAM i pamięć cgroup są różnymi metrykami.** Cgroup obejmuje także cache plikowy i inne procesy Poda; nie należy interpretować 10,762 GiB RSS jako całego zużycia RAM przez środowisko ani porównywać bezpośrednio VRAM z limitem 8 GiB na CPU. Surowe liczniki I/O obejmują kilka warstw urządzeń, więc nie sumowano ich bez walidacji w jeden wynik odczytów dysku.

## Zatrzymanie i koszt

Skrypt zażądał zatrzymania o **14:07:32,456586 UTC** i zapisał kod wyjścia 0. Log zawiera ostrzeżenie o braku konfiguracji oraz błędy nieobsługiwanej alternatywnej składni CLI; obsługiwana komenda zakończyła się komunikatem zatrzymania. Dlatego sam kod wyjścia nie stanowił jedynego potwierdzenia.

**Odrębna kontrola panelu RunPod o 14:10:10 UTC potwierdziła:** `Compute: Not running`, `Container storage: Not running`, **Total: $0.00/hr**. Nie usuwano żadnego Poda. Nie ma trwałego wolumenu w tej konfiguracji. Wyniki zapisano poza Podem, a oryginalne archiwum pozostawiono bez zmian.

Pole `billing_zero_verified=false` w oryginalnym `status.json` opisuje brak dostępu skryptu do panelu rozliczeń w chwili zapisu. Późniejsza kontrola potwierdza zerową bieżącą stawkę, **nie zerowy koszt zakończonej sesji**. Czas płatnego zasobu obejmował także przygotowanie i oczekiwanie przed launcherem. Szczegółowy koszt dostawcy pozostaje `PENDING_PROVIDER_ITEMIZED_BILL`; nie wyliczamy publicznego kosztu jednostkowego z samego czasu generowania ani zmiany salda konta.

## Integralność i zakres dowodu

Sprawdzono CRC ZIP, wszystkie **11 pozycji SHA-256**, komplet i kolejność 101 rekordów, zgodność rekordów z dziennikiem zdarzeń oraz zgodność środowiska i podsumowania w obu reprezentacjach. Dla 32 przypadków ponownie policzono SHA wyrenderowanego promptu i tablicy tokenów wejściowych, sprawdzono wiadomości względem zamrożonego JSONL i przeliczono oceny oraz percentyle.

| Obiekt | SHA-256 |
|---|---|
| Zamrożony plik pytań JSONL | `7122063baa94f744588a2405d140ea6e26c2941ee8ff7f7dcd199602e58158e8` |
| Oryginalne prywatne archiwum ZIP | `2d5dd7cd5ae74c1098c720af584147458fd8c867ab7cec525985f54a41b30e3b` |
| Oryginalne rekordy prób | `b3bb9f57d0fe77db8191e634592b5a734016c2c7926482a06bc413fc2f400ca8` |
| Oryginalny manifest promptów | `078eb735e61977be516622a0e40ed41e22a2a5fb0cd2ff8bf655f190970cfa56` |
| Szablon konwersacji | `e10ca381b1ccc5cf9db52e371f3b6651576caee0a630b452e2816b2d404d4b65` |

Pozostałe hashe i wyniki dla poszczególnych przypadków zawiera publiczny JSON. Hashe wiążą raport z zachowanymi dowodami; nie zastępują niezależnego powtórzenia badania. Archiwum podaje przypiętą rewizję i rozmiary wag, ale nie zawiera SHA-256 każdego pliku safetensors.

Zachowano rozróżnienie historii prób: wcześniejsza próba B1 zatrzymana na etapie połączenia SSH nie wykonała inferencji i nie należy do tych 101 wywołań. Wcześniejszy pojedynczy test `2+2` miał inny prompt i również nie jest częścią B1.

## Co można teraz porównywać

Referencja BF16 jest zakończona i zachowana. Operator CPU powinien użyć dokładnie tego JSONL, zapisać pochodzenie i SHA GGUF oraz porównać hashe wszystkich 32 wyrenderowanych promptów i wejściowych tablic tokenów z opublikowanymi wartościami. Następnie należy dostarczyć pełne wyniki CPU przy jawnych limitach pamięci, swapie i stanie cache.

Do tego czasu status parowania pozostaje **PENDING**. Porównanie GPU BF16 z CPU IQ2 opisuje dwa różne środowiska. Przypisanie poprawy autorskim modułom wymaga osobnego porównania B/C na tym samym sprzęcie, GGUF i backendzie, z dowodem faktycznego działania modułów. Nie ma obecnie na podstawie tej paczki potwierdzonej przewagi MultiQuant ani kwalifikacji produkcyjnej.

**Publikacja obejmuje wyłącznie wyniki, metodologię, statusy i identyfikatory integralności. Surowe odpowiedzi, logi, kod, dane konta, adresy infrastruktury, identyfikatory zasobów, tokeny i wagi pozostają prywatne.**
