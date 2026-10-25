# SSI MultiQuant — wspólny benchmark 70B BF16 / IQ2_XXS / moduły SSI, protokół B1 R1

**Data zatwierdzenia protokołu:** 2026-10-25  
**Status:** `PROTOCOL_AND_32_CASES_FROZEN / NO_PAIRED_RUNS_YET`  
**Właściciele torów:** operator BF16 na osobnym RunPod; operator IQ2_XXS na CORE24; koordynacja SSI MultiQuant  
**Źródło pytań:** przygotowany lokalnie `BASELINE BRIDGE B1`; publiczna kopia 32 zadań, *nie prywatny kod*

**Wymagane pliki:**
- [Wszystkie 32 identyczne pytania, wiadomości systemowe i odpowiedzi wzorcowe — JSONL](SSI_MULTIQ_B1_SUITE_32_20261025.jsonl).
- [Kontrakt maszynowy porównań, metryk, kosztów i bramek](SSI_MULTIQ_BF16_IQ2_PAIRED_BENCHMARK_MANIFEST_R1_20261025.json).
- [Publiczna referencja pojedynczego pytania BF16 oraz wariantu CPU](../SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md).
- [R5 — rzeczywisty zakres jednej instalacji MultiQuant na CORE24](../SSI_MULTIQ_ACTIVE_ARCHIVE_R5_CORE24_INVENTORY_20261025.md).

**Zamrożenie zbioru:** `32` przypadki: matematyka `8`, magazyn `8`, ekstrakcja `6`, pytania ze źródłem `6`, **syntetyczne teksty przypominające SCC** `4`. Ostatnie 4 przypadki **nie są** testem natywnego parsera SCC.

```text
SHA-256 pliku JSONL (11440 bajtów):
7122063baa94f744588a2405d140ea6e26c2941ee8ff7f7dcd199602e58158e8

SHA-256 kanonicznej tablicy JSON z lokalnego B1:
8d9ee566d99f95d6f068b877c73d0f077207d5ff3cb8770ef64a1f913d71d553
```

Pierwszy hash został sprawdzony po publikacji przez ponowne odczytanie pliku z GitHuba i niezależne obliczenie SHA-256. **Na obu komputerach musi być identyczny hash pliku JSONL**. Jeżeli plik albo ustawienia się różnią, przerywamy kampanię i nie porównujemy wyników.

## I. Co dokładnie porównujemy — trzy różne pytania

| Tor | Sprzęt / wariant | Pytanie badawcze | Co wolno wnioskować |
| --- | --- | --- | --- |
| **A: BF16_GPU_REFERENCE** | Oryginalny Meta Llama 3.1 70B Instruct BF16, dwie A100 80 GB (RunPod) | Jakość odpowiedzi i rzeczywista cena/czas usługi GPU przy 32 tych samych pytaniach | Empiryczny punkt odniesienia jakości, latencji i kosztu **tego środowiska** |
| **B: IQ2_CPU_PLAIN** | 70B IQ2_XXS GGUF, zwykły llama.cpp na CORE24; deklarowane historycznie 4 vCPU / 16 GB RAM oraz kontrolowany limit cgroup 8 GiB | Jakość i koszt uruchomienia tego samego modelu po silnej kwantyzacji, na innym sprzęcie | Koszt, jakość i dostępność rozwiązania CPU; **nie** przyspieszenie przez MultiQuant |
| **C: IQ2_CPU_MULTIQ_ENABLED** | Dokładnie ten sam GGUF, CORE24, cgroup, backend i ustawienia, **z faktycznie wykonującymi się modułami MultiQuant** | Czy nasze moduły zmieniają czas, obciążenie lub poprawność względem B? | **Tylko B ↔ C na tym samym sprzęcie i modelu** daje podstawę do przypisania zmiany modułom, po kontroli zakłóceń |

**C nie jest dziś zakwalifikowanym ramieniem eksperymentu.** R15–R21 i RAM Guard mierzyły izolowane mechanizmy składowe; brak dowodu, że są wpięte do inferencji 70B. Nie wolno nadać wynikom etykiety „MultiQuant ON”, jeżeli faktycznie działa zwykły llama.cpp. Opcjonalny tor D (`IQ2_CPU_MULTIQ_DISABLED`) jest użyteczny dopiero, gdy powstanie identyczny runtime z prawdziwym przełącznikiem funkcji i dowodem, które moduły działały.

**A ↔ B:** porównanie jakości na identycznych wiadomościach i decyzja biznesowa „ile kosztuje odpowiedź na GPU lub CPU”. Porównanie szybkości jest obserwacją dwóch różnych maszyn, nie dowodem autorskiego przyspieszenia.  
**B ↔ C:** właściwy eksperyment przyczynowy naszych modułów; dodatkowo rozważyć pary z takim samym ustawieniem zram, cache i obciążeniem tła.

## II. Tożsamość modeli, promptów i dekodowania

**BF16:** `meta-llama/Llama-3.1-70B-Instruct`, rewizja `1605565b47bb9346c5515c34102e054115b4f98b`, PyTorch/Transformers, dwie GPU. Poprzedni test BF16 podał odpowiedź `4` w `0.718169 s` *po załadowaniu modelu*; nie jest przebiegiem 32 pytań.

**CPU:** GGUF `IQ2_XXS` o **19 097 389 632 B**. Zapisać SHA-256 pliku, commit rzeczywiście uruchomionego llama.cpp, wersję/rewizję modelu źródłowego i rzeczywisty sposób konwersji. Dopóki wspólne pochodzenie wag nie jest potwierdzone, opisujemy modele jako podobną rodzinę, a nie identyczną rewizję różniącą się wyłącznie kwantyzacją.

W obu środowiskach:
- Wczytać z JSONL **obie wiadomości** (`system` + `user`), bez ich przepisywania lub „ulepszania”. Jawny system B1 brzmi: `Answer with only the requested value. No explanation or additional words.`
- Przypiąć szablon konwersacji **Llama 3.1 Instruct** i tokenizer; zachować identyczne wiadomości, kolejność i odpowiedni `assistant` header. Zapisać SHA-256 **wyrenderowanego promptu**, SHA-256 listy wejściowych ID tokenów, liczbę tokenów wejściowych i identyfikatory EOS/EOT.
- Wymagania dekodowania: `do_sample=false`, `num_beams=1`, `seed=0`, `max_new_tokens=96`, `use_cache=true`. W llama.cpp dobrać odpowiedniki bez ukrytych zmian penalizacji, top-k, temperature, stop words i kontekstu; zapisać rzeczywiste ustawienia, nawet gdy nie mają dokładnego odpowiednika.
- **Jeżeli tokenizacja lub chat template nie zgadzają się**, oznaczyć `PROMPT_PARITY_FAIL`; wykazać, na czym polega różnica, skorygować konfigurację i dopiero potem rozpocząć porównanie. Nie zamieniać merytorycznie różnych promptów w „te same zadania”.
- Historyczny, jednopunktowy wynik `2+2=4` miał inne otoczenie wiadomości systemowej, więc **nie zalicza** automatycznie przypadku `M01` z nowego zbioru.

## III. Instrukcja dla drugiego komputera — RunPod BF16

1. Pobrać **dokładnie ten sam plik JSONL z GitHuba**, policzyć SHA-256 i porównać z wartością powyżej. Nie uruchamiać płatnego zasobu przed potwierdzeniem budżetu i dostępności wymaganych GPU.
2. Przed uruchomieniem zasobu zapisać zaakceptowany **maksymalny koszt całej kampanii**, realną stawkę dwóch GPU, typ i stawkę dysku/volume oraz sposób zachowania wyników. Ceny muszą pochodzić z panelu i rozliczenia konkretnego uruchomienia, nie z szacunków.
3. Na dwóch A100 80 GB przypiąć **tę samą rewizję HF modelu i tokenizera**. Zapis modelu użyty w poprzednim teście miał 30 plików wag i 141,107 GB łącznie; to nie znaczy, że należy automatycznie pobierać te wagi ponownie bez decyzji operatora.
4. Przed płatnym przebiegiem wykonać wyłącznie test parsera zestawu i suche sprawdzenie konfiguracji. Po zatwierdzeniu limitu kosztu — mały pilot na `M01, W03, E01, G04, S03`. W trakcie faktycznej sesji zbierać łączny czas rozliczeniowy od startu do zatrzymania wraz z pobieraniem, inicjalizacją, ładowaniem i przerwami.
5. Dopiero po pilocie wykonać pełne `32` zadań w **3 powtórzeniach** w tej samej serii, bez zmieniania promptów. Dla każdego pytania zapisać surową odpowiedź i metryki prywatnie; do publicznego GitHuba trafi zestaw ocen i zagregowanych pomiarów.
6. Monitorować każdą GPU oddzielnie (VRAM, wykorzystanie, moc jeśli dostępna). Parametry typu `nvidia-smi --query-gpu=...` można zbierać w krótkich odstępach; próbkowanie co 1 s jest zbyt rzadkie, aby niezawodnie mierzyć szczyt bardzo krótkich zapytań, więc także raportować peak allocatora PyTorch.
7. Po zakończeniu zapisać odpowiedzi, manifest środowiska i sumy SHA na MSI, zweryfikować odczyt; wyłączyć zasób i niezależnie sprawdzić naliczanie compute i storage w panelu. Stwierdzenie „GPU wyłączone” nie wystarcza do orzekania braku kosztu trwałego storage.

## IV. Instrukcja dla CORE24 — CPU IQ2_XXS

1. Użyć *identycznego* pliku 32 pytań i tej samej kolejności; przed startem porównać jego SHA-256.
2. Utrwalić rzeczywistą wersję llama.cpp, hash GGUF, ustawienia konwersacji i rzeczywisty limit cgroup. Historyczne wartości `MemoryMax=8 GiB`, `MemorySwapMax=8 GiB` można uznać za **punkt odniesienia**, ale trzeba pokazać aktywne limity badanego procesu, nie tylko parametr dawnych testów.
3. Osobno zmierzyć czasy załadowania modelu, przygotowania promptu i generacji; nie zestawiać czasu całego procesu CPU z samym `generate` na już załadowanym GPU.
4. Rejestrować `memory.peak`/peak RSS, CPU-seconds, major page faults, cgroup `io.stat` w przedziale próby, swap i PSI oraz zram (jeśli aktywny). Zram jest aktualnie pilotem z priorytetem 100; **nie wyłączać go globalnie i nie wykonywać swapoff/drop_caches na współdzielonym VPS w celu zrobienia „uczciwego testu”**. Gdy nie da się wyrównać warunków, opisać je zamiast ukrywać.
5. Pilot `M01,W03,E01,G04,S03` i oszacowanie czasu. Pełny test `32×3` tylko gdy mieści się w zatwierdzonym czasie, koszcie i limitach bezpieczeństwa; timeout/OOM/błąd są rejestrowane, nie usuwane z próby.
6. Dla testu modułów B ↔ C wymagany jest **ten sam GGUF**, identyczny backend i rzeczywiste uruchomienie funkcji MultiQuant; zachować kontrolę cache, dysku, pory oraz pozostałego obciążenia. Jeżeli adapter nie jest gotowy, wynik `MODULE_ABLATION: NOT_RUN`, a nie domniemana przewaga.

## V. Przebieg etapowy, kolejność i punkt STOP

**P0 / przygotowanie bez kosztu GPU:** weryfikacja 32 JSONL, hashy, schematu metryk, wersji modeli, dostępnej pamięci i zaakceptowanego budżetu.  
**P1 / 5 pytań:** mały pilot z każdego z pięciu obszarów. Tylko po PASS infrastruktury i akceptacji dalszego kosztu.  
**P2 / 32×3:** pełny zbiór; identyczny porządek zadań, 3 niezależne powtórzenia, bez strojenia modelu na wynikach; zachować także niepowodzenia i przerwane przebiegi. Jeżeli budżet wymaga przerwania, status `PARTIAL_NOT_COMPARABLE_AS_FULL_SUITE`.  
**P3 / B kontra C:** prawdziwy test modułów MultiQuant na tym samym CPU i GGUF, osobno od A/B.  
**P4 / większy ślepy zestaw:** po analizie 32 jawnych pytań, walidacja na nieużywanym do strojenia zbiorze, trudniejszych zadaniach i długim kontekście, z nowym ID zestawu. W 32 prostych pytaniach nie wolno dowodzić ogólnej wyższości 70B lub gotowości produkcyjnej.

**STOP natychmiast**, gdy: hash zestawu się nie zgadza, prompt parity nie zachowano, źródłowej rewizji GGUF nie da się potwierdzić dla rygorystycznej atrybucji kwantyzacji, obciążenie zagraża produkcyjnemu SSI, koszt zbliża się do zatwierdzonego limitu, pojawia się OOM/długotrwały timeout wymagający interwencji, albo moduły deklarowane jako aktywne nie są faktycznie wykonywane.

## VI. Co zapisujemy dla KAŻDEGO zadania i powtórzenia

| Obszar | Minimalne dane |
| --- | --- |
| **Tożsamość** | `run_id`, `arm_id`, `task_id`, `repeat_no`, SHA zestawu, model ID+revision/GGUF hash, backend commit, parametry dekodowania |
| **Kontrola wejścia/wyjścia** | role/messages, SHA wyrenderowanego promptu i token IDs, surowa odpowiedź (prywatnie), znormalizowana odpowiedź, wzorzec, status i błąd |
| **Jakość** | poprawna/niepoprawna/timeout/OOM/format/prompt-parity; wynik kategorii i łączny, liczba odmów i halucynacji |
| **Czas** | UTC start/koniec, `wall_s`, `ttft_s` jeżeli mierzony, `prefill_s`, `decode_s`, `tokens_output`, `tokens_per_second`, koszty download/load/cold start oddzielnie |
| **CPU / pamięć** | CPU-seconds, peak RSS, cgroup peak RAM, peak swap, major page faults, odczyt/zapis dysku, PSI, liczniki zram |
| **GPU / pamięć** | GPU model/ilość, wykorzystanie w czasie, VRAM peak **na każdej GPU**, opcjonalnie zużycie mocy, czas realnie rozliczony |
| **Koszt** | waluta, rzeczywista stawka compute i storage, przedział naliczania, opłaty dodatkowe według dostawcy, metoda alokacji stałego abonamentu VPS, koszt całej sesji i jednostkowy |
| **Warunki** | cache cold/warm, obciążenie innych usług, wersja kernela/sterowników, zegary/pomiary i granica dokładności próbników |

**Agregaty:** per ramie i kategoriach 32 pytań — poprawność (n/32), p50/p95 czasu odpowiedzi, mediana tok./s, max RAM/VRAM/swap, liczba OOM/timeout, łączny czas pracy serwera, pełny koszt, koszt na **poprawną** odpowiedź i koszt na 1000 wygenerowanych tokenów (gdy sensowny). Nie mieszać p95 odpowiedzi z czasem pobrania modelu. Przy n=32 i 3 powtórzeniach pokazać niepewność/statystykę parowaną; wyniki są badaniem wstępnym.

**Reguła oceny `normalized_exact.r1`:** Unicode NFC → obcięcie białych znaków na brzegach → sprowadzenie wewnętrznych wielokrotnych odstępów do jednej spacji → `casefold` tekstu. Dla liczb i kodów nie ma tolerancji matematycznej: np. `4.0` nie równa się `4`, a `INV-707` nie równa się `707`. Oprócz wyniku automatycznego przechować wyjście surowe, by dało się skorygować błędy formatu w oddzielnej analizie; pierwotnych wyników nie nadpisywać.

## VII. Koszt, czas, obciążenie — uczciwe wzory

**Koszt całego BF16 GPU**: faktyczna stawka za zasoby GPU × **naliczony czas** + faktycznie naliczony dysk/volume + inne występujące opłaty. Osobno: koszt przy zimnym starcie (wraz z pobieraniem, ładowaniem, instalacją i przerwami), koszt kolejnej odpowiedzi po załadowaniu, oraz koszt zamortyzowany przez 32/96 zapytań. **Zapisana wcześniej latencja 0.718 s nie obejmuje uruchomienia i pobrania 141 GB modelu.**

**Koszt CPU VPS**: dwie jawne perspektywy — koszt *przyrostowy* (jeśli zasób już opłacony, czas wykonywania i ewentualne dopłaty) oraz udział *pełnego abonamentu i zasobów* przypisany do zadania według opisanej metody. Nie pisać „$0” jako uniwersalnej ceny pracy CPU. Pokazać użyte CPU-seconds, RAM-residency i I/O, a następnie koszt pełnej kampanii.

**Zadanie / poprawna odpowiedź**:
- `unit_cost = campaign_total_cost / liczba_wykonanych_zadań`
- `cost_per_correct = campaign_total_cost / liczba_poprawnych_odpowiedzi` (nieokreślony, gdy brak poprawnych)
- `quality = poprawne / wszystkie_32` dla kompletnej próby, z rozbiciem na kategorie
- `observed_latency_difference = median_wall_A - median_wall_B`, ale tylko jako **opis dwóch środowisk** dla A/B
- `module_time_gain = (median_wall_B - median_wall_C) / median_wall_B` dla kontrolowanej próby na tym samym sprzęcie; jednocześnie raportować `module_quality_delta`, różnicę kosztu i pamięci.

RunPod deklaruje naliczanie compute/storage według zużycia, a **storage może kosztować także po zatrzymaniu GPU**; konkretne stawki zależą od typu i konfiguracji. Wartość kosztową należy sprawdzić w panelu danego przebiegu i rozliczeniu, a nie wpisywać do raportu z pamięci. [Dokumentacja rozliczeń RunPod](https://github.com/runpod/docs/blob/main/accounts-billing/billing.mdx). Parametry monitoringu GPU i rozdzielczość próbek należy jawnie opisać, zgodnie z [dokumentacją NVIDIA](https://docs.nvidia.com/deploy/nvidia-smi/index.html).

## VIII. Jak uczciwie stwierdzimy przewagę MultiQuant

**Nie oceniamy mechanizmów MultiQuant na podstawie samego faktu, że 70B IQ2 mieści się w 8 GiB cgroup.** Zweryfikowane wcześniej eksperymenty używały standardowego llama.cpp oraz innych środowisk sprzętowych; ich poprawne zakończenie to ważny wynik wykonalności, a nie dowód przyspieszenia autorskich modułów.

Po uzyskaniu rzeczywistego ramienia C raportujemy oddzielnie:
1. **Jakość:** co najmniej brak pogorszenia na powtarzalnych zadaniach, a dla krytycznych obszarów zero nowych błędów. 32 proste pytania są zbyt małe na szerokie roszczenia.
2. **Czas:** mediana i p95, powtórzenia i zakres niepewności. Odnotować każdą zmianę cache i timeout.
3. **Obciążenie:** RAM, swap, CPU-seconds, I/O i wykorzystanie dysku; wskazać efekt każdej włączonej funkcji, nie całego niezweryfikowanego pakietu.
4. **Koszt:** rzeczywisty dodatkowy koszt, koszt wykonania całego zestawu i koszt na poprawną odpowiedź.
5. **Misje SSI (osobny test po integracji):** trwale weryfikowane checkpointy, ACL, wznowienie, konflikty planu i evidence na **natywnym SCC**, a nie tylko na syntetycznym JSON. Nie łączyć tego wyniku z oceną modelu na 32 pytaniach.

O wyniku „przewaga MultiQuant” można mówić **dla konkretnej mierzonej metryki i konfiguracji**, dopiero po porównaniu B/C z niepogorszoną jakością i po kontrolowanych powtórzeniach. Dopóki to nie nastąpi, status: `MODULE_ADVANTAGE_NOT_ESTABLISHED`.

## IX. Polityka publikacji i statusy

Raw answers, pliki dowodowe, cennik/koszt przypisany do konta, logi hostów, pełne identyfikatory zasobów i wewnętrzne skrypty pozostają prywatne. GitHub publiczny publikuje **ustalony, syntetyczny zbiór pytań** (nie klienta), protokół pomiarów, metryki zagregowane, sumy kontrolne, ograniczenia i wyniki. Nie publikować kluczy API, kodu autorskiego, wag modeli, danych klientów ani ścieżek operacyjnych.

**Aktualne statusy:**
- `SUITE_32_FROZEN: YES`
- `RUNPOD_BF16_32_CASES: NOT_RUN`
- `CORE24_IQ2_32_CASES: NOT_RUN`
- `CORE24_MULTIQ_ABLATION: NOT_QUALIFIED_NOT_RUN`
- `SCC_NATIVE_INTEGRATION: PENDING`
- `PUBLIC_ADVANTAGE_CLAIM: NONE`

**Najbliższa decyzja:** zweryfikować lokalny wynik B1 (archiwum i hash zadań), potwierdzić SHA/pochodzenie GGUF, przygotować rejestr rzeczywistych stawek i limit wydatku dla BF16, sprawdzić zgodność tokenizera, a następnie wykonać mały pilot i pełną kampanię — dopiero po zgodzie operatora na koszt i ryzyko obciążenia.

## X. Aktualizacja wykonania — 2026-10-25, po zamrożeniu protokołu

Powyższe statusy z chwili przyjęcia protokołu pozostają zapisem historycznym. **Tor A BF16 został zakończony i zweryfikowany:** 5 prób pilotażowych, następnie 32×3, wynik 32/32 w każdym przebiegu (96/96). Operator przed sesją jawnie zniósł wcześniejszy globalny limit kosztu i czasu; zachowano ustalone pytania, kolejność, parametry generacji i ocenę. Powtórzenia greedy dotyczą tych samych 32 zadań i nie są niezależnymi zadaniami. Archiwum zapisano na NOUT1, przekazano do weryfikacji, a panel potwierdził zatrzymanie compute i tymczasowego storage oraz $0.00/h. Oryginalnych danych nie zmieniano.

[Raport BF16 B1](SSI_MULTIQ_B1_BF16_RESULTS_20261025.md) · [Metryki, oceny i hashe 32 promptów/tokenów](SSI_MULTIQ_B1_BF16_PUBLIC_EVIDENCE_20261025.json).

Aktualny status toru A: `BF16_ARM_VERIFIED_COMPLETE_POD_STOPPED_PAIRING_PENDING`. Zgodność tokenów CPU, pochodzenie GGUF, koszt według szczegółowego rachunku i wyniki B/C pozostają do udokumentowania. Referencja jest dostępna bez ponownego uruchamiania GPU; brak podstaw do twierdzenia o przewadze MultiQuant lub kwalifikacji produkcyjnej.
