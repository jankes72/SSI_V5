> **AUDYT AKTUALNY R9 (17.10.2026):** RunPod API wskazało jeden zatrzymany Pod z GPU **NVIDIA A40 (48 GB VRAM)** oraz **30 GB dysku kontenera** (a nie wcześniej zakładane 24 GB VRAM i 40 GB dysku). Status trwałego wolumenu, RAM, vCPU i jednostka opłaty nadal wymagają potwierdzenia. Pod nie został uruchomiony, modele nie zostały przebudowane. **Najnowsza decyzja i blokery: [SSI MultiQuant A40 R9](SSI_MULTIQUANT_RUNPOD_A40_48GB_R9_20261017.md).**

# SSI MultiQuant R8 — GPU 24 GB jako warsztat, MODELS 24/7 jako produkcja

**Data planu:** 2026-10-17. **Status:** propozycja architektury i procesu zaakceptowana kierunkowo; **NIE URUCHOMIONO nowego Poda, kwantyzacji, transferu wag ani zmiany routingu**. Poprzedni plan R7 (bezpośrednia kwantyzacja na serwerze MODELS) zostaje zastąpiony w zakresie miejsca przygotowania wag.

## Ostateczny podział zasobów dla pierwszej serii

- **RunPod GPU 24 GB VRAM, wlaczany na zadanie** — warsztat SSI MultiQuant do przygotowania 13 nowych wariantow wag, analizy ważności tensorów, generowania `imatrix`, kontroli zgodnosci i przygotowania paczek do transportu. Preferowany jeden job na raz, bez ingerencji w aktywne zadania Bonsai/pozostalych modeli RunPod. Koszty GPU i dysku liczymy osobno.
- **SSI MODELS 24/7 (4 vCPU, ok. 15 GiB RAM + 12 GiB swap, 60 GB wolnego dysku po wlaczeniu swapu, stan z audytu operatora)** — wyłącznie aktualne 13 modelowych wariantow produkcyjnych, oraz gotowe 13 nowych wersji, dopuszczonych osobno do bramki. Produkcyjny VPS **nie pobiera pelnych wag i nie kwantyzuje**; jedynie rejestruje podpisane i zgodne wyniki.
- **SSI DIRECTOR VPS** — decyzja o tym, kiedy uzyc modelu, planowanie zadan, zatwierdzenie zmiany routingu, autoryzacja misji; brak dodatkowych modeli inferencyjnych na tym VPS.
- **SSI ROBERT VPS/NODE-01** — konsumuje wyniki i korzysta z wolnej mocy dla swoich misji, lecz nie wykonuje pierwszej serii kwantyzacji. Piec dodatkowych wyspecjalizowanych modeli Roberta pozostaje **wyłącznie planem**, bez wag, publikacji i wdrozenia.
- **GPU 48 GB** — odrebny, platny zasob SSI; NIE jest domyslnym fallbackiem. Uruchomienie w tym projekcie wymaga osobnej decyzji i limitu kosztowego.

## Co GPU realnie przyspiesza

**Wazne: 24 GB VRAM != 24 GB RAM systemowego**. Sam program `llama-quantize` w standardowym przeplywie GGUF wykonuje znaczna czesc konwersji na CPU i wymaga wystarczajacego RAM hosta. Zysk GPU dotyczy przede wszystkim `llama-imatrix -ngl ...` (kalkulacji aktywacji i waznosci wag), uruchamiania modeli do kontroli runtime i ewentualnie narzedzi rzeczywiscie wspierajacych GPU. Nie obiecujemy 13 automatycznych konwersji ani tego, ze 24 GB VRAM rozwiaze braki dysku lub RAM.

Oficjalne zrodla:
- [llama.cpp quantization](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md)
- [llama.cpp imatrix, GPU offload](https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md)
- [RunPod Pod CLI and disk/stop options](https://docs.runpod.io/runpodctl/reference/runpodctl-remove-pods)
- [RunPod: zatrzymany Pod a dostepnosc GPU, wolumeny sieciowe](https://docs.runpod.io/pods/troubleshooting/zero-gpus)

## Kolejka R8

1. Potwierdzic aktualny stan istniejacego Poda 24 GB: GPU, **system RAM**, wolny lokalny dysk (szczegolnie w kontekscie poprzednich konfiguracji ~40 GB), wolumeny, dzialajaca kolejke Bonsai, ewentualny koszt postoju/utrzymania dysku. Nie uruchamiac zasobu przed audytem i wycena.
2. Zachowac z audytu operatora 13 oryginalnych tagow i ich SHA256; **11 roznych konfiguracji bazowych** w tym dwie pary Q3/Q4 (Hermes 8B oraz Qwen2.5-Coder 7B). Nie zmieniac produkcyjnej Ollamy.
3. Podczas pracy Poda: pobrac po jednym odpowiadajacym danemu oryginalowi **legalnym FP16/BF16** z poprawna architektura, revision i tokenizerem. Nie kopiowac obecnego Q3/Q4 i nie udawac, ze zyskano jakosc przez rekwantyzacje; jednoznacznie wskazac licencje i manifest.
4. Przygotowac male, zatwierdzone, pozbawione sekretow próbki tekstowe z zakonczonych rzeczywistych misji do `imatrix`, bez wydawania tokenow na testowe generacje. Wymagane wsparcie modelu/formatu. Nie przenosic bez zezwolenia obrazow i danych partnerow ani zawartosci prywatnych mikrosieci.
5. Obliczyc `imatrix` z GPU offloadem tam, gdzie to dostepne. Skompresowac source GGUF na CPU (ewentualnie zgodnym akcelerowanym narzedziem) wedlug **SSI MultiQuant**: precyzja per tensor, model-aware, nie tylko najnizsze Q.
6. Jednorazowo zweryfikowac zgodnosc formatu, pelny model + dodatki (np. projektor multimodalny D1), podpis/sume SHA256, realny rozmiar, wskazana wersje konwertera i decyzje walidacyjne System One, bez podwojnej inferencji realnych misji.
7. Wyslac **tylko gotowy kwant i artefakty pochodzenia** po SSH/TLS na SSI MODELS; najpierw staging, odrebny tag, stan `CANDIDATE_DISABLED`. Aktywacja tylko po odbiorze/akceptacji wlasciwej produkcyjnej bramki. Zachowac dotychczasowe 13 tagow, endpointy, autoryzacje i rollback.
8. W normalnych misjach Director/Robert nowy model dostaje realne zadania (bez dublowania zadania dla benchmarku). Notariusz zapisuje model/digest, typ zadania, anonimowa klase mikrosieci, czas, wynik PASS/FAIL/INCONCLUSIVE, koszt i fallback. Przed publikacja agregacja i anonimizacja.
9. Po potwierdzonym transferze plikow i bezpiecznym checkpointcie **wylaczyc GPU gdy kolejka jest pusta**, zamiast naliczac koszty. Stan wolumenu i koszt postoju sprawdzac odrebnie — skasowanie tymczasowego Poda moze usunac dane z nieutrwalonego magazynu.

## Kryteria bezpieczenstwa

- **13 starych modeli nietknietych**, produkcyjny serwer nie jest builderem.
- **13 nowych wariantow to cel, nie gotowe artefakty**; te same dwie pary bazowe mozna zaliczac tylko jako nowe odrebne warianty, nie aliasy.
- 5 przyszlych Roberta: `PLANNED_UNSELECTED`, bez uruchomienia, bez pozornych ocen.
- Kazdy element skomplikowany (Qwen3.5/Qwen35, LFM2/MoE, natywne D1/Tev1 z System One, obraz/projektor) wymaga kwalifikacji silnika i zadania decyzyjnego.
- Ustalic przed startem budzet GPU, czas graniczny, auto-stop i ilosc pamieci masowej. **Nie podwyzszac bez zgody kosztu ani nie dotykac produkcyjnego Routera i prywatnych mikrosieci.**
- Publiczne repo zawiera tylko plan, listy i pozniej anonimowe statystyki; nie zawiera wagi, kodu prywatnego, sekretow ani danych misji.

**Najwazniejsze:** *RunPod 24 GB przygotowuje wagowe warianty; SSI MODELS 24/7 stale pracuje; Director i Robert kwalifikuja modele podczas faktycznych misji, a Notariusz zapisuje rezultaty.*


## Usciślenie celu: 24 GB GPU do budowy, 16 GB CPU do wykonania, 48 GB GPU jako punkt odniesienia

**Dyspozycja operatora z 17.10.2026:** Wykorzystać istniejący kontener RunPod **24 GB VRAM / zgłoszone 40 GB dysku** do przygotowania **13 nowych wariantów SSI MultiQuant**, a następnie dostarczyć ukończone modele na niezależny, całodobowy serwer SSI MODELS z ~15 GiB fizycznego RAM i 12 GiB SWAP. Istniejące 13 tagów Ollama pozostaje nienaruszone. Model lub modele uruchamiane na odrębnym Podzie **48 GB VRAM** są **jakościowym wzorcem dla konkretnych decyzji**, a nie gwarancją równoważnych zdolności po kompresji.

**Dwa różne procesy**: (1) Kwantyzacja z właściwego, licencjonowanego checkpointu wysokiej precyzji, z kalibracją `imatrix` na reprezentatywnych, autoryzowanych danych z rzeczywistych misji, jeśli format to obsługuje; zachowuje liczbę parametrów, optymalizuje precyzję tensorów. (2) Destylacja/specjalizacja: jeśli chcemy przenosić wybrane umiejętności większego modelu, musimy mieć legalnie dostępne, zweryfikowane przykłady poprawnych decyzji i odrębnie dostroić mniejszy model. **Kwantyzacja sama nie zmienia 27B/80B w 1B/3B i nie gwarantuje jakości odpowiedzi z 48 GB GPU.** Wykorzystanie płatnego 48 GB Poda do tworzenia danych nauczyciela wymaga oddzielnej zgody i budżetu.

**40 GB dysku kontenera to nie 40 GB RAM systemowego ani trwały wolumen.** Proces dużego modelu może wymagać jednocześnie oryginalnych wag BF16/F16 (~14-16+ GB dla 7-8B), roboczego GGUF, docelowego kwantu, miejsca na biblioteki i cache, co może przekroczyć 40 GB. Należy przetwarzać po jednym modelu, zweryfikować RAM hosta, wolny dysk, trwałość `/workspace`, koszt GPU i pozostałe zadania na tym samym Podzie. Gdy brakuje zasobów, nadać status `BLOCKED_RESOURCE`, bez automatycznego zwiększania kosztów.

**VPS MODELS** otrzymuje tylko gotowe, podpisane manifestem i osobno zweryfikowane kwantyzacje. Nowy model wchodzi do bramki jako `CANDIDATE_DISABLED`; wymagane niezależne zatwierdzenie przed prawdziwymi misjami. Notariusz zbiera rzeczywiste wyniki bez sztucznego dublowania obliczeń. **12 GiB SWAP nie zamienia 15 GiB RAM w 27 GiB szybkiego RAM; nie wolno opierać rutynowej inferencji na swapie.** 13 oryginałów + do 13 nowych mogą być przechowywane na dysku, ale nie oznacza to jednoczesnego załadowania do pamięci.

**5 przyszłych modeli Roberta** pozostaje wyłącznie planem, bez nowych wag lub dystrybucji. Żadna konwersja, dostrajanie, instalacja ani uruchomienie płatnego GPU nie nastąpiły w wyniku niniejszej aktualizacji.
