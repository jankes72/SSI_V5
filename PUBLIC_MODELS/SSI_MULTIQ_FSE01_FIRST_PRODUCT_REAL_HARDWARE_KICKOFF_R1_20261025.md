# SSI MultiQuant FSE-01 — pierwszy produkt: etap sprzętowy R1

**Data:** 2026-10-25  
**Typ:** rozpoczęcie produktu / zakres i bramki wdrożenia, nie ogłoszenie produkcji  
**Identyfikator:** `SSI_MULTIQ_FSE01_REAL_HARDWARE_KICKOFF_R1_20261025`  
**Nazwa:** `FSE-01` — robocza etykieta właściciela. Nie rozwijamy skrótu bez definicji autora.  
**Status:** `PRODUCT_KICKOFF_ACCEPTED / BF16_REFERENCE_VERIFIED / CPU_AND_MODULE_VALIDATION_PENDING`  
**Granica publikacji:** wyłącznie architektura logiczna, metodologie i wyniki; implementacja, modele, wewnętrzne ścieżki, sekrety i surowe logi pozostają prywatne.

## 1. Produkt, który faktycznie rozpoczynamy

**SSI MultiQuant FSE-01: kontrolowane, kolejkowane zadania modelu klasy 70B na ograniczonym zasobie CPU**, z raportowaniem jakości, czasu, RAM/zram/swapu, I/O i kosztu. Jest to **prototyp badawczo-wdrożeniowy**, a nie gotowa usługa przedsiębiorstwa.

Wyjściowy scenariusz: krótka, ograniczona czasowo misja/batch. Nie obiecujemy rozmowy interaktywnej, ponieważ istniejące pojedyncze próby 70B IQ2_XXS zajmowały 116–127 sekund, a raportowane tempo CLI wynosiło około 0,1 tokena/s.

Docelowy przepływ integracji: **zweryfikowany natywny SCC → Router V10/S10 → uprawnienia Research Memory → wersjonowany adapter MultiQuant → kolejkowany wykonawca → Evidence/Notariusz → checkpoint/recovery**. To **cel integracyjny**, nie obecny potwierdzony stan. Nie budujemy konkurencyjnego parsera SCC. Zewnętrzne płatne modele są opcją routingu wyłącznie z osobną autoryzacją kosztu.

## 2. Potwierdzona baza naukowa — nie mylić z przewagą produktu

### A. BF16 GPU — badanie zakończone

- Zestaw: **32 różne syntetyczne zadania × 3 powtórzenia**, dodatkowo 5 pytań pilota.
- Ocenianie: **32/32** w każdym powtórzeniu, **96/96** wszystkich prób, pilot 5/5. Powtórzenia greedy nie są 96 niezależnymi zadaniami.
- Model: `meta-llama/Llama-3.1-70B-Instruct`, pinned revision `1605565b47bb9346c5515c34102e054115b4f98b`, BF16, 2 × A100 80GB.
- Rozmiar wag: **141,107,497,872 B**.
- Pobieranie wag **460,853 s**; ładowanie **16,125 s**; pełny skrypt pobranie/załadowanie/testy **508,477 s**; launcher do żądania stop **535,457 s**.
- 96 prób po pilocie **28,472 s**; mediana jednej odpowiedzi **0,244743 s**, p95 **0,447384 s**; model już w pamięci.
- Szczyt alokacji PyTorch GPU0/GPU1 **70,601,726,976 / 70,599,641,600 B**; proces RSS **11,556,020,224 B**, swap cgroup **0 B**, OOM **0**.
- Zabezpieczenie dowodu: ZIP CRC i 11 sum kontrolnych SHA-256 PASS, ponowna ocena surowych odpowiedzi i zgodność promptów/token ID.
- Stop: niezależnie potwierdzone compute/storage not running i bieżące **$0.00/hr**, co **nie** oznacza, że sesja była darmowa.
- **Dokładny koszt zakończonej sesji:** `PENDING_PROVIDER_ITEMIZED_BILL`. Szacunku 3 USD **nie przedstawiać jako faktu**.

Źródła: [raport BF16](BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md), [dowody publikowane](BENCHMARKS/SSI_MULTIQ_B1_BF16_PUBLIC_EVIDENCE_20261025.json), [32 zadania](BENCHMARKS/SSI_MULTIQ_B1_SUITE_32_20261025.jsonl).

### B. CPU IQ2_XXS — wykonalność, a nie full-suite

- Model GGUF **19,097,389,632 B**; silnik historycznych prób: CPU llama.cpp `9d1878a`.
- Wcześniejsze krótkie próby 70B na maszynie **4 vCPU/16 GB RAM** z cgroup **MemoryMax=8 GiB + MemorySwapMax=8 GiB** zwróciły poprawnie `4` w **116,920–127,310 s**. Jest to ograniczenie cgroup, **nie** fizyczna maszyna 8 GiB.
- Historyczne intensywne I/O (m.in. cgroup ~75,66 GB odczytu w V7.14) i znaczące page faults wskazują obszar badań. Rozbieżne liczniki I/O wymagają zachowania źródeł i nie uprawniają do przypisywania bajtów konkretnym tensorom.
- R5 odczyt jednego katalogu MultiQuant: 299 wpisów, **19,098,148,698 B**, 29 kandydatów DB, brak błędów; zram logiczne 2 GiB priorytet 100, zachowany swap dyskowy i ~33,70 GB wolnego dysku w chwili audytu. R5 nie identyfikuje aktywnego rdzenia całego SSI.
- **Stan**: nie wykonano jeszcze pełnego CPU B1 32×3 ani dowodu zgodności tokenów/promptów i pochodzenia GGUF.

Źródła: [historyczne CPU + BF16](SSI_MULTIQ_V7_70B_8G_PUBLIC_RESULTS_20261025.md), [R5](SSI_MULTIQ_ACTIVE_ARCHIVE_R5_CORE24_INVENTORY_20261025.md).

## 3. Granice pierwszej wersji

**W zakresie FSE-01 R1:** wersjonowany kontrakt wejścia/wyjścia batch, pojedyncza kolejka i timeout, limit współbieżności 1 przy presji pamięci, dozwolone źródła modeli, jawne cgroup i stan swap/zram, oddzielne cold/warm, zapis wyników/metryk bez prywatnych treści w publicznym repo, przerwanie i recovery, reprodukowalny benchmark 32 przypadków.

**Poza odbiorem R1:** nieograniczone narzędzia/misje, samodzielne wykonanie operacji na klientach, deklaracja 70B „na fizycznym 8 GB RAM”, automatyczne uruchamianie płatnych GPU, usuwanie plików modeli/archiwów, 4+4 GiB faktycznych kwot ACTIVE/LONGTERM, migracja/backup całego SSI, gotowy natywny SCC w produkcji, gwarancja jakości lub przyspieszenia.

## 4. Plan egzekucji — etapami i z mierzalnymi bramkami

| Etap | Działanie | Wymagany wynik | Status |
|---|---|---|---|
| **FSE-P0** | Przypięcie referencji BF16 32×3, kontrola archiwum, modeli i SHA | `BF16_REFERENCE_VERIFIED`; koszt szczegółowy nadal osobno | **PASS / COST PENDING** |
| **FSE-P1** | **Read-only preflight CORE24:** identyfikacja prawdziwego GGUF i sumy SHA, wersji llama.cpp, aktywnej jednostki cgroup i swapu, wolnego miejsca, usług obciążających host, zgodność 32 zadań | Prywatny manifest sprzętu i limitów; jawne ograniczenia, 0 zmian w usługach | **NOT RUN** |
| **FSE-P2** | **Pilot CPU plain IQ2**: najpierw pojedynczy przypadek M01; następnie najwyżej 5 uzgodnionych przypadków jeśli bezpiecznie. Strumieniowy zapis metryk per zadanie | Wynik, limit czasu/pamięci, CPU/RAM/swap/zram/PSI/I/O, prompt/token hashes, poprawność i koszt szacunkowy | **NOT RUN** |
| **FSE-P3** | Pełne CPU 32×3 dopiero po estymacji czasu i zatwierdzonym oknie; checkpoint po każdym przypadku, wynik `PARTIAL` zamiast cichego usuwania timeoutów | Zbiór porównywalny BF16 A, kompletne mianowniki, no-OOM albo jawna klasyfikacja błędów | **NOT RUN** |
| **FSE-P4** | Realna ablacją **B=IQ2 plain versus C=IQ2 + działające MultiQuant**, ten sam GGUF/backend/host/cgroup/cache | Potwierdzone wykonanie modułu, latencje, I/O, RAM, jakość, powtarzalność | **NOT QUALIFIED** |
| **FSE-P5** | Jedna nieprodukcyjna **natywna** misja SCC→Router→Research Memory→MultiQuant→Evidence, ACL deny, checkpoint/restart/idempotencja, NOUT1 nieobowiązkowy | Evidence, sign-off staging, brak wtórnych skutków ubocznych, jawne braki | **NOT RUN** |

**Istotne ryzyko P3:** przy historycznych 116–127 s nawet na proste pytanie, pełne 96 prób może trwać **ponad 3 godziny**, nie licząc nowych promptów, timeoutów i obciążenia I/O. Nie uruchamiać automatycznie całej serii, gdy współdzielony VPS obsługuje inne zadania. P2 stanowi twardą bramkę bezpieczeństwa.

## 5. Instrumentacja: dowód produktu, nie deklaracja

Każda próba: `run_id, case_id, arm, repetition, suite_sha256, gguf_sha256, engine_commit, prompt_sha256, input_token_ids_sha256, answer/status, output_tokens, wall_s, ttft/prefill/decode if available, memory_peak, swap_peak, CPU_seconds, major_faults, read/write delta, disk/memory PSI, zram before-after, cache_regime, cgroup limits`.

Wyniki dla CPU porównywać z [referencją BF16](BENCHMARKS/SSI_MULTIQ_B1_BF16_PUBLIC_EVIDENCE_20261025.json). **Gdy tokeny wejściowe/szablony różnią się, zachować jawne `PROMPT_PARITY_FAIL`**, a nie uznawać zadań automatycznie za bezpośrednio sparowane. Zgodność wag źródłowych GGUF pozostaje osobną bramką.

**A kontra B (GPU BF16 vs CPU IQ2):** wyłącznie obserwacja jakości i czasu/kosztu rozwiązań na różnych maszynach. **B kontra C (ten sam CPU + GGUF):** jedyna grupa mogąca wykazać korzyść z autorskich modułów. Proponowany eksperymentalny cel ≥20% mniej czasu i ≥20% mniej I/O przy jakości nie gorszej to **hipoteza do zmierzenia**, nie obecny fakt ani gotowa cecha marketingowa.

## 6. Bezpieczeństwo hosta i danych

- Nie wyłączać produkcyjnego swapu, nie zmieniać globalnej `vm.swappiness`, nie wykonywać `drop_caches`, `swapoff`, `systemctl stop` lub masowych operacji na katalogach bez osobnego przeglądu.
- Zram 2 GiB jest **testowy/nietrwały po restarcie**. Nie udaje backupu, dodatkowego fizycznego RAM ani potwierdzonego przyspieszenia.
- Nie kopiować 19 GB GGUF tylko dla duplikatu benchmarku; przed przeliczeniem SHA dużego pliku ustalić dopuszczalną presję I/O.
- Materiały źródłowe, skrypty, jawne hostnames/ścieżki i prywatne testy przechowywać prywatnie; GitHub publiczny wyłącznie raport/sanitized metrics/checksum.
- Dane trwałe FSE muszą mieć niezależny backup i sprawdzony restore zanim będą przyjmować prawdziwe misje klientów. Dotychczasowy R4 dotyczy wyłącznie dwóch maleńkich magazynów syntetycznych.
- Płatny RunPod uruchamiać wyłącznie po akceptacji aktualnego limitu kosztów i stawki. BF16 już zakończony: **brak potrzeby kolejnego startu GPU** do samego sparowania wyników.
- P0–P4 nie oznacza kwalifikacji produkcyjnej; FSE-P5 jest nieprodukcyjną integracją i również wymaga osobnego odbioru.

## 7. Odbiór pierwszej funkcji

**Pierwszy realny krok:** FSE-P1 — sprawdzenie prawdziwego węzła CORE24 wyłącznie do odczytu, spisanie sprzętu/runtime, zapis odrębnej prywatnej paczki dowodowej i zgłoszenie `P1_READ_ONLY_PREFLIGHT_PASS` albo `BLOCKED`. Po nim pojedyncza inferencja P2 w zatwierdzonym oknie.

**Pierwszy mierzalny produkt:** po P2–P4 działający, izolowany, odtwarzalny tryb `SSI MultiQuant 70B BATCH / LOW-RAM` z raportem kosztu i jakości. Nie ogłaszać przewagi ani gotowości dla klientów bez dalszego audytu.

**Odnośniki:** [Issue #4 — pomiary BF16/IQ2](https://github.com/jankes72/SSI_V5/issues/4) · [Handoff migracji i SCC](../RESULTS/SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025.md) · [Odpowiedź MultiQuant na handoff](SSI_MULTIQ_TO_MIGRATION_ACTIVE_ARCHIVE_HANDOFF_RESPONSE_R1_20261025.md).
