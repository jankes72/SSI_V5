# SSI MultiQuant — MICRO-13 zorientowane na decyzje (R7)

**Data ustalenia:** 2026-10-17  
**Status:** PLAN TECHNICZNY ZATWIERDZONEGO KIERUNKU, **nie raport konwersji ani wdrożenia**. Na moment publikacji: **13 źródłowych pozycji według historycznego raportu, 13 nowych wariantów zaplanowanych, 0 nowych plików GGUF potwierdzonych, 0 nowych aktywacji bramki**. Pięć dodatkowych modeli dla Roberta jest osobnym przyszłym planem.

> **NAJNOWSZA DECYZJA O MIEJSCU PRAC — zastępuje starszy plan R5/R6 o budowaniu wyłącznie na Robercie:** Pierwsze trzynaście wariantów SSI MultiQuant będzie przygotowywanych **na tym samym serwerze SSI MODELS 24/7**, gdzie działają obecne modele Ollama, **pod warunkiem rzeczywiście potwierdzonej dostępności RAM/CPU/dysku oraz możliwości pracy bez zatrzymania zwykłych misji**. Dyrektor ma osobny VPS; Robert i NODE-01 pozostają osobnymi agentami i odbiorcami wyników. RunPod 24/48 GB nie jest potrzebny do tego pierwszego projektu. **Jeśli źródłowe wagi lub proces kwantyzacji nie mieszczą się bezpiecznie na MODELS VPS, oznaczamy zadanie BLOCKED_RESOURCE zamiast ryzykować stabilność serwera, udawać sukces lub automatycznie zamawiać GPU.**

## Co znaczy „kwantyzujemy po naszemu”?

W R7 **SSI MultiQuant to nasza własna, odtwarzalna polityka selekcji i walidacji kwantyzacji**, z narzędziami konwersji dobranymi do rodzaju modelu; nie jest to jeszcze autorski format wag ani deklaracja, że napisano nowy algorytm kodowania. Profil ma odzwierciedlać misje SSI: **wybór dopuszczalnych działań, delegowanie, routing, sprawdzanie warunków, recovery i współpracę z mikrosieciami**. Dążymy do niskiego RAM i czasu CPU **bez fałszywej obietnicy, że więcej kompresji zwiększa jakość**.

1. **Provenance:** z lokalnej Ollamy odczytać rzeczywisty model/tag/digest/architekturę i odpowiadający mu upstream; dla dobrych wyników preferować legalne, dokładnie zgodne wagi źródłowe BF16/F16/F32, nie kolejną kwantyzację istniejącego Q3/Q4.
2. **Model-aware:** dobrać wspierany konwerter oraz format wag dla faktycznej architektury, nie wymuszać jednego kodeka dla Tev1, D1, LFM2.5 MoE i zwykłych generatorów.
3. **Decision-aware:** gdy zasoby pozwalają, przygotować dopuszczony, zanonimizowany zbiór **prawdziwych, wcześniej wykonanych misji SSI** opisujących sensowne wybory i trudne przypadki. Może on służyć do obliczenia `imatrix` **w osobnej lokalnej operacji CPU**, bez dodatkowych płatnych wywołań nauczyciela. Nie pobierać haseł, wizerunków ani prywatnych rekordów klientów; nie publikować surowych danych.
4. **Mixed precision:** niektóre tensory, np. `output.weight`, `token_embd.weight` lub zidentyfikowane wagi wrażliwe, zachować w wyższej precyzji, a odpowiednio kompatybilne pozostałe używać w Q3/IQ3, ostrożnie w Q2/IQ2. **Dokładna mapa tensorów jest zależna od modelu**; dostępność parametru `--tensor-type` nie oznacza, że zawsze poprawi jakość.
5. **Decision interface:** modele `D1` i `Tev1` zachowują interfejs pytań typowanych **System One/Jev**; modele generatywne korzystają z osobnego SSI adaptera proponującego wybór spośród jawnie dozwolonych opcji i uzasadnienie. Żaden wynik typu `confidence` nie staje się automatycznie skalibrowanym prawdopodobieństwem poprawności.
6. **Native competence boundary:** SCC, Research Memory, mikrosieci i Router pozostają odrębnymi, prywatnymi modułami SSI. Model nie otrzymuje prawa bezpośrednio wykonywać dowolnych działań. Router waliduje dozwolone opcje, budżet, uprawnienia i możliwość przejścia do fallbacku.
7. **Real-mission comparison only:** nowy wariant, gdy przejdzie kwalifikację statyczną i zostanie osobno dopuszczony, obsługuje autentyczne misje SSI. Notariusz zbiera model/digest, kwantyzację, rodzaj zadania, anonimowy identyfikator mikrosieci, faktyczny wynik, opóźnienie, RAM, błędy i przyczynę fallbacku. **Nie uruchamiać drugiej kopii zadania tylko po to, by testować model**. Porównywać próbki z zastrzeżeniem nierównej trudności i selekcji misji.
8. **Publication:** wyłącznie oryginalne źródła modeli/licencje, metody deklaratywne, statystyki rzeczywistych działań i anonimizowane wyniki. **Brak publikacji kodu Routera, mikrosieci, pamięci operacyjnej i pełnych treści misji.**

## Pierwszy dobór — 13 par oryginał → wariant kandydacki

**Wszystkie propozycje wymagają potwierdzenia live digesta, zgodnej wersji źródłowej oraz obsługi w narzędziu.** Nie należy generować całej trzynastki jedną operacją bez kontroli zasobów.

| # | Wariant bazowy zgłoszony jako obecny na MODELS VPS | Kandydat SSI MultiQuant | Priorytet / kryterium |
|---|---|---|---|
| 1 | Qwen2.5-Coder 1.5B Q4 | **SSI-CODER15-DEC-MICRO**: Q3_K_M z wag źródłowych | Pilot. Diagnostyka kodu i wybór poprawki; czy faktycznie mniej RAM przy zachowanej trafności? |
| 2 | Qwen3 1.7B Q4 | **SSI-QWEN17-DEC-MICRO**: Q3_K_M / zgodny IQ3 | Decyzje ogólne, eskalacja, delegowanie |
| 3 | Hermes3 3B Q4 | **SSI-HERMES3-DEC-MICRO**: Q3_K_M | Planowanie krótkich sekwencji i zgodność poleceń |
| 4 | Qwen2.5-Coder 3B Q4 | **SSI-CODER3-DEC-MICRO**: Q3_K_M | Kontrakty kodu, analiza błędów i recovery |
| 5 | Tev1 0.8B, dokładna precyzja niezweryfikowana lokalnie | **SSI-TEV08-DEC-MICRO**: cel Q4_K_M tylko jeśli kompatybilny z natywnym `System One` | **HOLD_RUNTIME:** porównać typowane odpowiedzi, nie chat; nie zmieniać upstreamowego interfejsu |
| 6 | Liquid D1 3B, dokładna precyzja niezweryfikowana lokalnie | **SSI-D1-DEC-MICRO**: cel Q4_K_M dla kompatybilnych wag + zachowanie modelu wizyjnego/projektora | **HOLD_RUNTIME:** decyzje typowane i pytania obrazowe muszą pozostać wspierane; obsługa części wizyjnej krytyczna |
| 7 | Qwen3.5 4B Q4 | **SSI-QWEN35-DEC-MICRO**: Q3_K_M przy kompatybilności architektury | Wielojęzyczne misje; poprawność lokalnego JSON |
| 8 | DeepSeek-Coder 6.7B Q4 | **SSI-DSCODER67-DEC-MICRO**: Q3_K_M | **HOLD_RESOURCE** przed pobieraniem lub konwersją pełnych wag; zadania programistyczne |
| 9 | Qwen2.5-Coder 7B Q4 | **SSI-CODER7-DEC-MICRO-A**: zgodne Q3_K_S / IQ3, nie duplikować istniejącego Q3 | **HOLD_RESOURCE**, porównanie ze znanym Q3 baseline |
| 10 | Hermes3 8B Q4 | **SSI-HERMES8-DEC-MICRO-A**: zgodne Q3_K_S / IQ3 | **HOLD_RESOURCE**, decyzje agenta i strukturalne delegacje |
| 11 | LFM2.5 8B-A1B Q4 | **SSI-LFM8-DEC-MICRO**: Q3_K_M tylko przy dowiedzionej obsłudze architektury MoE | **HOLD_ARCH+RESOURCE**, licencja i silnik |
| 12 | Qwen2.5-Coder 7B Q3 | **SSI-CODER7-DEC-NANO-B**: kompatybilne mieszane Q2/IQ2 tylko jeśli uzasadnione wynikami | **EXPERIMENTAL/HOLD_RESOURCE**, duże ryzyko degradacji; nie kwantyzować starego Q3 |
| 13 | Hermes3 8B Q3 | **SSI-HERMES8-DEC-NANO-B**: kompatybilne mieszane Q2/IQ2 tylko jeśli uzasadnione wynikami | **EXPERIMENTAL/HOLD_RESOURCE**, nie kwantyzować starego Q3 |

Dwie pary modeli bazowych mają już na serwerze Q4 i Q3: Qwen2.5-Coder 7B i Hermes 8B. Nie produkować kopii tego samego digesta jako nowego wariantu. Może się okazać, że **mniej niż 13 nowych plików ma techniczny sens**, mimo że rezerwujemy 13 par do badań; raport musi oddzielać przypadki `READY`, `SOURCE_NOT_AVAILABLE`, `DUPLICATE`, `UNSUPPORTED` i `RESOURCE_BLOCKED`.

**Przybliżenie docelowego rozmiaru** ma wynikać z rzeczywistej zmiany wag GGUF i runtime RAM; nie podajemy fałszywie precyzyjnych MB. Mniejszy plik na dysku nie przesądza o mniejszym opóźnieniu na 4 vCPU.

## Umowa decyzyjna dla Roberta i Dyrektora

Rozdzielić **jakość modelu** od **skuteczności całej kompozycji SSI**. Dla prawdziwej misji do porównania wystarczą bezpieczne pola:
- stabilny ID misji i modelowy `digest` / rewizja / kwant;
- klasa celu SCC; publicznie tylko kategoria;
- anonimowy ID klasy mikrosieci / kompetencji; **bez jej implementacji**;
- typowany wybór lub zweryfikowana sugestia spośród jawnych opcji;
- `PASS` / `FAIL` / `INCONCLUSIVE`, źródło sprawdzenia, przyczyna fallbacku;
- pomiary czasu końca misji/etapu, RAM, CPU, zasoby i rzeczywiste koszty;
- odrębnie `model_only` (jeśli da się uczciwie wyodrębnić z naturalnego przebiegu) i `SSI_with_micro_networks`. Nie przypisywać sukcesu całej misji tylko LLM-owi.

Natywne **Tev1/D1** mogą dostarczyć decyzję według własnego System One; generatory służą do propozycji przechodzących walidator. Zewnętrzny JEV, jeśli był używany w *tej samej realnej klasie misji*, jest **historycznym wzorcem**, nie powodem do kupowania wywołań do testów. **Robert jest odbiorcą katalogu i dowodów, nie wymaganym miejscem kompresji pierwszej trzynastki.**

## Sposób wdrożenia bez ryzyka dla serwera produkcyjnego

1. **Read-only preflight na MODELS VPS:** rzeczywiste `ollama list`, `ollama ps`, `/api/show`, `df -h`, `free -h`, procesy CPU i deklarowany budżet. Bez zmian.
2. **Dokładna selekcja źródeł:** na podstawie tagu/digest, licencji i typu checkpointu; nie przyjmować przypadkowego „oryginału” z tej samej rodziny.
3. **Pilot #1 tylko wtedy, gdy preflight zaakceptowany:** mała paczka źródłowa Qwen2.5-Coder 1.5B i kompatybilny `llama-quantize`; nowa nazwa/tag, żadnego nadpisywania.
4. **Lokalne okna zasobowe:** jeden proces na raz, z ograniczeniami CPU/RAM/I/O i stopem przy presji pamięci. Kontenery/modelowe usługi mają pierwszeństwo; kwantyzacja ma się wycofać.
5. **Weryfikacja artefaktu:** suma, plik GGUF, typy tensorów, licencja, zgodność wczytania / API, rozmiar i zapotrzebowanie na RAM. Minimalne sprawdzenie kompatybilności to kontrola uruchomienia, **nie sztuczny konkurs benchmarkowy**.
6. **Kontrolowane dodanie modelu:** wpis `CANDIDATE_OFF`, odrębny niekolizyjny tag, jawna zgoda przed udostępnieniem; brak naruszenia 13 oryginałów.
7. **Rzeczywiste misje i Notariusz:** dopiero wtedy tryb dopuszczenia do zwykłej pracy; routing z fallbackiem, wyniki porównania z obserwacji, nie z dublowania misji.
8. **Rzeczywiste następne 12:** po pierwszym sukcesie i potwierdzeniu źródeł, jedna konwersja naraz; hold dla zbyt dużych modeli, specjalnych architektur i wagi wizyjnej D1.

**Dysk 24/7 VPS nie jest gwarantowanym magazynem wszystkich pełnych wag FP16**. Należy zawczasu sprawdzić koszt miejsca źródło + plik tymczasowy + wynik + zachowany aktualny model oraz zużycie RAM. Jeśli brakuje miejsca lub wolnej pamięci: `RESOURCE_BLOCKED`, a nie przełączenie na Roberta lub RunPod.

## Pięć modeli Roberta — wyłącznie rezerwacja

`ROBERT_FUTURE_01` – `ROBERT_FUTURE_05`: pięć **pustych slotów na przyszłość**, bez modeli, plików, wyników i aktywnej dystrybucji. Przyszłe NODE-01, GUI, sterowanie myszą/klawiaturą, Vision, Luna i GPU 24/48 GB to **osobne plany**, nie zakres tej pierwszej realizacji.

## Źródła techniczne (bez publikacji prywatnego kodu SSI)

- [llama.cpp — dokumentacja kwantyzacji i ostrzeżenie przed rekwantyzacją](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md)
- [llama.cpp — importance matrix](https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md)
- [Tev1 w Ollama: System One](https://ollama.com/library/tev1)
- [Liquid D1 w Ollama: decyzje tekstowe/obrazowe, System One, projektor wizji](https://ollama.com/library/d1)
- [Kanoniczna architektura SSI](../SSI_V5_C4_ARCHITECTURE.md)
- [Poprzedni dokument o planie MICRO-13](SSI_MICRO13_BASELINE_TO_CANDIDATES_R6_20261017.md)

**Zasada dowodu:** Fakt istnienia dokumentu R7 nie oznacza, że pliki wag zostały pobrane, skwantyzowane czy wdrożone. Każdy taki stan wymaga odrębnego raportu hosta i checksumy. Autorska implementacja Routera/Micronetworks/SCC pozostaje poza repozytorium.


## Aktualizacja po audycie MODELS VPS — 17.10.2026

Operator uruchomil audyt tylko do odczytu na VPS MODELS (Debian 12, Ollama 0.40.5) i przekazal rzeczywisty wynik `ollama list` oraz `/api/tags` i `/api/show`. **13 wariantow obecnych**: 9 x Q4_K_M, 2 x Q3_K_M, 2 x Q8_0, reprezentujacych 11 roznych konfiguracji bazowych. W chwili odczytu: 4 vCPU, 15 GiB RAM, ~15 GiB pamieci dostepnej z uwzglednieniem cache, 72 GiB wolnego dysku, **zero swapu**, 0 uruchomionych runnerow, CPU load 0.00. Przy braku swapu proces kwantyzacji musi miec twarde limity zasobow i moze zostac zablokowany; bezpieczne zasoby nie sa gwarantowane podczas normalnej pracy SSI.

**Potwierdzone tagi decyzyjne:** `tev1:0.8b-q8_0` (Q8_0, ~0.776 GiB) i `d1:3b` (Q8_0, ~3.474 GiB). D1 uzywa modelu wizyjnego z projektorem, wiec kwantyzacja samego LLM nie moze byc podawana jako pelne zachowanie modelu. Naturalne pary Q3/Q4 to `qwen2.5-coder:7b-instruct` i `hermes3:8b-llama3.1`. Audyt potwierdza rzeczywiste tagi i kwantyzacje raportowane przez operatora, lecz nie ustala jeszcze autentycznych zrodel BF16/FP16 ani kompatybilnosci konwertera. **0 nowych wag SSI MultiQuant potwierdzonych.** Piec przyszlych modeli Roberta pozostaje wyłącznie planem.

Nastepny krok to tylko do-odczytowy audyt dostepnosci narzedzi kwantyzacji i wysokoprecyzyjnych zrodel. Pierwszy maly pilot: Qwen2.5-Coder 1.5B, jezeli pasujaca rewizja i zasoby to umozliwia. Kwantyzacje decyzjne Tev1/D1 rozpatrywac po sprawdzeniu interfejsu System One. **Nie rekwantyzowac slepo obecnych Q3/Q4.**
