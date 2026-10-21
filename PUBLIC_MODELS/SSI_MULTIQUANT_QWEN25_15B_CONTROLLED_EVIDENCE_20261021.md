# SSI MultiQuant — Qwen2.5-Coder 1.5B: wyniki porównawcze i granice dowodowe (21.10.2026)

**Status:** opublikowany raport z ograniczonych eksperymentów CPU; **kandydat badawczy / SHADOW-HOLD**, bez kwalifikacji produkcyjnej.  
**Podstawa:** logi i raporty z uruchomień przeprowadzonych przez operatora SSI V5, odczytane 21 października 2026. To nie jest niezależna replikacja.  
**Polityka ujawniania:** wyłącznie wyniki liczbowe, kontekst i ograniczenia. Prywatne pozostają implementacja, skrypty, receptury tensorów, dane misji, prompty, infrastruktura, wagi i materiały pozwalające odtworzyć know-how SSI.

## Wynik w skrócie

Przetestowano warianty **Qwen2.5-Coder 1.5B**: źródłowy F16, standardowy **Q4_K_M** utworzony narzędziem `llama.cpp` z kontrolowanego F16 oraz eksperymentalny **SSI MultiQuant Q4KM**. Model SSI ma plik **o 3,14% mniejszy** od standardowego Q4_K_M i w krótkiej, kontrolowanej serii wykazał **około 1,82% niższy zmierzony szczyt RSS procesu**. W tej samej serii oba warianty miały **praktycznie identyczny czas**.

To **nie jest** dowód przewagi szybkości, jakości programowania, większej inteligencji, wykonania destylacji ani gotowości do produkcji. Dokumentacja wcześniejszego QA odnotowuje jeden dodatkowy przypadek niezaliczony przez SSI względem F16; **zgodność checkpointów źródłowych nadal nie została niezależnie potwierdzona**.

## 1. Artefakty i zasady porównania

| Wariant | Wielkość pliku (bajty) | MB dziesiętne | Status testów |
| --- | ---: | ---: | --- |
| F16, punkt odniesienia | 3 093 669 568 | 3 093,67 | Uruchomiony natywnie w ograniczonych próbach |
| Zwykły Q4_K_M z kontrolowanego F16 | 986 048 704 | 986,05 | Utworzony, zweryfikowany i uruchomiony natywnie |
| Eksperymentalny SSI MultiQuant Q4KM | 955 053 760 | 955,05 | Zweryfikowany i uruchomiony natywnie; niezakwalifikowany |

Różnica SSI względem zwykłego Q4_K_M: **30 994 944 bajty** (około **29,56 MiB**, **3,14%** wielkości standardowego pliku). Porównano **rozmiar całych plików GGUF**, nie wyłącznie rozmiar tensorów.

Standardowy Q4_K_M również stosuje różne precyzje zależnie od typu tensora. Sama nazwa „mixed” ani samo mieszanie precyzji nie dowodzą nowości metody SSI.

**Pochodzenie:** manifest SSI wskazuje otwarty model `Qwen/Qwen2.5-Coder-1.5B-Instruct`; identyfikatory i rozmiary lokalnych artefaktów sprawdzano na serwerze. W przypadku nowego standardowego Q4_K_M potwierdzono zgodność wejściowego F16 przed konwersją. **Pełny dowód, że autorski plik SSI i oba warianty kontrolne pochodzą z identycznych wag, pozostaje otwartym zadaniem.**

## 2. Native CPU inference — kontrolowane testy krótkiej odpowiedzi

Ustawienia wybranej serii: jeden wątek CPU, kontekst **1 024 tokeny**, limit generowania **16 tokenów**, ograniczenie pamięci procesu przez cgroup **6 GiB**, bez płatnego GPU. Każda próba uruchamiała pełny model natywnym silnikiem; testowana odpowiedź to tylko elementarne działanie arytmetyczne.

### Seria ABBA, dwa powtórzenia na wariant

Kolejność: **standardowy Q4 → SSI → SSI → standardowy Q4**.

| Próba | Model | Całkowity czas, s | Próbkowany szczyt RSS procesu, MiB | Odpowiedź |
| --- | --- | ---: | ---: | --- |
| 1 | Zwykły Q4_K_M | 4,061 | 1 623,78 | Prawidłowa |
| 2 | SSI MultiQuant Q4KM | 4,062 | 1 594,21 | Prawidłowa |
| 3 | SSI MultiQuant Q4KM | 3,460 | 1 594,12 | Prawidłowa |
| 4 | Zwykły Q4_K_M | 3,460 | 1 623,73 | Prawidłowa |
| **Średnia Q4_K_M** | | **3,7605** | **1 623,755** | **2/2** |
| **Średnia SSI** | | **3,7610** | **1 594,165** | **2/2** |

SSI uzyskał w tej serii o około **29,59 MiB (1,82%) niższy próbkowany szczyt RSS**. Różnica średniego czasu wyniosła **0,0005 s na niekorzyść SSI**, czyli wynik jest praktycznie **remisowy**. Zmiany czasu w kolejnych pozycjach serii są znacznie większe od tej różnicy; nie wolno przypisywać jej skuteczności konkretnej metody.

Dodatkowe wcześniejsze próby krótkiej inferencji: **F16 2/2**, **standard Q4 1/1**, **SSI 2/2** prawidłowych odpowiedzi. Razem z ABBA daje to **9 poprawnie zakończonych natywnych prób**, lecz wszystkie opierają się na tej samej banalnej klasie zadania i **nie mierzą zdolności programistycznych**.

RSS to obserwowana pamięć rezydentna próbkowanego procesu, **nie** pełne zużycie pamięci hosta. Istniejące metryki cgroup wymagają osobnego ujednolicenia przed użyciem w porównaniach.

## 3. Wcześniejsze kontrole jakości kandydata (R12–R15)

Wyniki pochodzą z wcześniejszych lokalnych raportów SSI i nie stanowią testu standardowego Q4_K_M na poniższym zestawie.

| Kontrola | F16 / oryginał | SSI MultiQuant | Granica interpretacji |
| --- | ---: | ---: | --- |
| R12: deterministyczne formaty AST/JSON | — | **3/4** | Kontrola formatu, nie pełna jakość programowania |
| R13: cztery przypadki | **3/4** | **3/4** | Wyniki SSI **ponownie wykorzystano**, bez nowej inferencji kandydata w R13 |
| R14: 24 przypadki | **17/24** | **16/24** | Różnica jednego przypadku, brak izolacji wpływu kwantyzacji |
| R15 | — | — | Zmiana parametrów batch/ubatch; brak nowej kwalifikacji |

Rozkład R14:

| Grupa | F16 / oryginał | SSI |
| --- | ---: | ---: |
| Python AST | 8/8 | 8/8 |
| Typed Routing | 5/8 | 5/8 |
| SCC Context | 4/8 | 3/8 |
| **Razem** | **17/24** | **16/24** |

Jedyna niezgodność ocen w R14 występuje w **przypadku nr 19** (indeks 18), kategorii **SCC Context**: oryginał PASS, SSI FAIL. Pozostałe 23 przypadki mają zgodne rozstrzygnięcia. Nie opublikowano treści prywatnych zadań ani odpowiedzi.

**Ograniczenie krytyczne:** raporty R13–R15 oznaczają pochodzenie porównywanych checkpointów jako **niepotwierdzone**, a wpływ kwantyzacji jako **niewyizolowany**. Nie wolno twierdzić, że stwierdzony jeden dodatkowy błąd został spowodowany wyłącznie przez metodę SSI. W R14 nie wykonywano wygenerowanego przez model kodu.

## 4. Oddzielne doświadczenia R8/R9 — bez łączenia miar

Etykiety R8/R9 obejmują także **odrębne eksperymenty inżynierskie**, których pomiarów nie można dodawać do wyników jakości R12–R15.

- **R8, dostęp do fragmentów rzeczywistych wag GGUF**: mediana w ograniczonym mikroteście `eco` **0,100699 s**, `fast` **0,045704 s**, `adaptive` **0,069745 s**. To **czasy odczytu/obsługi fragmentów**, a nie generowania tokenów pełnego LLM. Tryb `fast` zużywał więcej pamięci podręcznej; `adaptive` nie był najszybszy w tym teście.
- **R9, router laboratoryjny SHADOW**: osiem sprawdzonych planów; wszystkie pozostawiono w HOLD ze względu na brak kwalifikacji modelu lub fizyczny charakter żądania. To **nie** jest aktywacja produkcyjnego Routera SSI V10.
- **R9, trzy krótkie uruchomienia przez Ollama**: **3/3** odpowiedzi zgodnych z prostymi oczekiwaniami, bez dowodu jakości na realistycznych misjach.

Te rezultaty nie dowodzą działania fragmentowego cache wewnątrz pełnej natywnej inferencji ani kwalifikacji do autonomicznego wykonywania misji.

## 5. Decyzja i następne bramki

**Decyzja na 21.10.2026:** wariant SSI pozostaje **eksperymentalnym kandydatem HOLD/SHADOW**. Nie ma potwierdzenia promocji do produkcyjnego routingu ani treningu/destylacji nowego modelu. W przedstawionych eksperymentach nie zmieniano produkcyjnych tagów Ollama i nie uruchamiano płatnych zasobów GPU.

Przed rozszerzeniem twierdzeń wymagane są:
1. Potwierdzenie wspólnego pochodzenia wag i zgodności tokenizera we wszystkich trzech wariantach.
2. Porównanie zwykłego Q4_K_M z SSI na tym **samym**, reprezentatywnym zestawie zadań programistycznych i SCC, w tym na jednym przypadku rozbieżnym z R14.
3. Więcej powtórzeń ze zmienną kolejnością, weryfikacja poprawności, pomiar prefill/decode, pamięci procesu i cgroup.
4. Dopiero potem niezależna recenzja, kontrola bezpieczeństwa oraz osobna decyzja o ewentualnym wdrożeniu.

**Zakres roszczenia publicznego:** dla jednego badanego checkpointu SSI MultiQuant otrzymał *mniejszy plik* i *niższy próbkowany szczyt RSS* w ograniczonej serii niż zwykłe Q4_K_M, **bez wykazanej przewagi szybkości** i **bez zweryfikowanej równoważności jakości**. Wynik nie jest uogólnieniem na inne rozmiary modeli ani parametry sprzętowe.

Powiązane wcześniejsze materiały:
- [Pierwszy pilotaż i granice audytu z 17–18.10](../RESULTS/SSI_V5_PUBLIC_PROGRESS_CPU7_SCC_AWARENESS_20261018.md)
- [Plan kontrolowanej serii kandydatów CPU-7](SSI_MULTIQUANT_CPU7_VPS_MODELS_R11_20261017.md)
- [Odrębne eksperymenty pamięciowe R1–R7](SSI_MEMORY_R1_R7_RESULTS_20261019.md)

---

### Short English summary

**21 October 2026, operator-reported bounded evidence.** For Qwen2.5-Coder 1.5B, the SSI mixed-precision GGUF was **3.14% smaller** than a standard llama.cpp Q4_K_M control. A four-run ABBA CPU-only arithmetic smoke test measured **1.82% lower sampled process peak RSS** and **indistinguishable wall-clock timing**. Historical quality checks found **16/24** passing cases for SSI versus **17/24** for the F16 reference, with one SCC Context discordance; exact source checkpoint parity was **not established** and a vanilla-Q4 control was **not** evaluated on that quality suite. No training, production promotion, independent replication, or broad quality improvement is claimed. Private implementation and operational data are intentionally withheld.
