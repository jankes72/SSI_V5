> **AKTUALNY ZAKRES R11 — 17.10.2026:** pierwsza seria **7 modeli <= 4B** na istniejacym SSI MODELS VPS (4 vCPU, ~15 GiB RAM), **bez RunPod i bez kolejnych platnych GPU**. Produkcja etapami i tylko wtedy, gdy nie koliduje z Ollama; **6 modeli 6.7–8B odlozonych** do czasu integracji Director, Robert, SSI CODEX, Charlie, Iskier i szkolen. Tev1/D1: wymagaja ustalenia pochodzenia/formatu i zgodnosci vision; Qwen2.5 Coder 3B: licencja badawcza, brak wykorzystania komercyjnego bez osobnej licencji. 13 oryginalow zachowane. **Nie potwierdzono wykonania nowych wag.** [Dokumentacja R11](SSI_MULTIQUANT_CPU7_VPS_MODELS_R11_20261017.md).

# SSI MultiQuant R10 — kontrolowana produkcja na infrastrukturze 24/7 (NOWY PLAN GŁÓWNY)

**Data:** 2026-10-17  
**Właściciel decyzji:** użytkownik / SSI DIRECTOR  
**Status:** PLAN I POLITYKA WDROŻENIOWA — żadne nowe wagi, trening, kwantyzacja ani zmiany produkcyjne nie są potwierdzone w ramach R10.

> **R10 zastępuje wcześniejsze założenie R8/R9, że płatny RunPod GPU ma być standardowym warsztatem wszystkich 13 modeli.** Celem jest ciągła, kontrolowana i tania produkcja wariantów SSI na już utrzymywanych zasobach 24/7, z pomocą lokalnych komputerów i zewnętrznych LLM w granicach istniejących budżetów. RunPod tylko wyjątkowo i po osobnej akceptacji.

## 1. Cel i granice

1. **Zachować 13 działających oryginalnych tagów Ollama** na niezależnym SSI MODELS VPS 24/7; planowane jest **do 13 nowych** sprawdzonych wariantów SSI MultiQuant jako odrębne tagi, nie automatycznie 13 jednoczesnych procesów w RAM.
2. Nowe warianty projektować tak, aby można je było uruchamiać **na VPS z ok. 15 GiB RAM** (dodatkowe 12 GiB swap jest zabezpieczeniem, nie szybkim RAM), z osobno określonym oknem kontekstowym i kosztami CPU.
3. Docelowa jakość oznacza **trafność konkretnych decyzji SSI**, mierzona z Notariuszem w prawdziwych misjach. **Kwantyzacja nie zamienia modelu małego w większy**; przenoszenie kompetencji wymaga odrębnej, zgodnej z prawami destylacji/dostrajania i oceny.
4. Brak automatycznego płatnego GPU, dodatkowych abonamentów lub masowej generacji danych przez API. Nie publikować prywatnych mikrosieci, reguł Routera, kodu, danych klientów ani sekretów.

## 2. Stałe zasoby i role

| Zasób | Rola | Granica |
|---|---|---|
| **SSI DIRECTOR VPS 24/7** | Kontroler pipeline, kolejka, wybór zadań, limity, checkpointy, notary, delegacja | Priorytet misji Dyrektora ponad produkcją |
| **SSI ROBERT VPS 24/7** | Opcjonalny low-priority worker: inspekcja plików, preprocessing, lekka ewaluacja, liczenie statystyk; ewentualnie CPU build jeśli preflight potwierdza wolne zasoby | Nie może opóźniać misji Roberta, Playwright, memory, queues |
| **SSI MODELS VPS 24/7** | Normalna inferencja 13 oryginałów; katalog nowych kandydatów, staging, integracja i finalne testy zgodności | Bez dużych konwersji i utraty RAM, bez przerw usługi |
| **MSI / NODE-01 / Lenovo** | Offline/batch workery gdy dostępne, backup i archiwa, narzędzia i sanitizacja danych | Brak zależności krytycznej od ich obecności online |
| **Luna, Together AI, OpenRouter, Groq i inne doładowane konta** | Opcjonalne konsultacje decyzji przy **prawdziwych misjach**; dokumentacja porównań, selektywne oznaczanie przykładowych decyzji | Osobne liczniki budżetu, polityka prywatności/licencji, brak automatycznego korzystania ze wszystkich |
| **RunPod A40 48 GB GPU / 55 GB RAM / 10 vCPU / 30 GB disk** | **ESCALATION_ONLY**, przy blokadzie technicznej i pozytywnym rachunku koszt/zysk, manualna aprobata | Status w ostatnim audycie EXITED; stawka GPU 0.59 USD/h; brak wolumenu trwałego |
| **RunPod 24/48 lub inne płatne GPU** | Nie należy do normalnej ścieżki | Żadnego uruchomienia bez decyzji użytkownika |

CPU, RAM i dyski dwóch VPS **nie sumują się** jak zasoby jednego serwera. Można rozdzielić zadania i wymieniać bezpieczne artefakty przez sieć, ale duża operacja wymaga wystarczającego RAM na jednym hoście.

## 3. Rozdzielenie działań, którego nie wolno mylić

- **Wariant wag (QUANT):** kwantyzacja wag właściwego checkpointu BF16/FP16/F32 → GGUF, ewentualnie `imatrix` i regulacje precyzji per tensor. Nie oznacza treningu i nie zmienia liczby parametrów.
- **Specjalizacja umiejętności (TUNE/DISTILL):** wybrany model „uczeń” dostrajany na zgodnych licencyjnie i zatwierdzonych przykładach decyzji. Osobny etap, opłacalność i wymagania RAM/GPU analizowane osobno. Nie obiecywać 48 GB GPU / większej inteligencji na 16 GB CPU przez sam QUANT.
- **Routing mikrosieci:** skuteczność końcowa SSI to model + Router + memory + tools + polityka decyzji. Zmiany routingu wymagają autoryzacji i rollbacku.

Oficjalne informacje: https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md oraz https://github.com/ggml-org/llama.cpp/blob/master/tools/imatrix/README.md.

## 4. Misjami zasilana kontrolowana kolejka

`SOURCE_CHECK → LICENSE_AND_ARCH_CHECK → RESOURCE_PREFLIGHT → SOURCE_READY → CALIBRATION_READY → BUILD_PENDING → BUILDING → ARTIFACT_VERIFIED → CANDIDATE_DISABLED → LIMITED_LIVE_MISSIONS → PROMOTED`

Stany wyjątków: `WAITING_FOR_RESOURCES`, `WAITING_FOR_INPUT`, `WAITING_FOR_NODE01`, `BLOCKED_MEMORY`, `BLOCKED_STORAGE`, `BLOCKED_LICENSE`, `COST_APPROVAL_REQUIRED`, `FAILED`, `ROLLED_BACK`.

**Algorytm kontrolera:** pojedynczy „director-owned” scheduler i kolejka z tokenem lease/idempotency. Każda próba ma manifest źródłowy modelu, oryginalny digest, wersję narzędzia, rozmiary plików, wejście, wynik, limit czasu/CPU/RAM/dysku, checkpoint, SHA256 wynikowego modelu i wpis notarialny.

**Priorytety:**
- P0: produkcyjne misje i komunikacja agentów;
- P1: użycie aktualnych modeli przez Router;
- P2: statystyki i walidacja kandydatów;
- P3: budowanie wariantów i prace z datasetami (tylko wolne okna).
  
Przykładowe PROPOZYCJE początkowych limitów (nie już aktywna konfiguracja): maks. **jeden** worker build na raz w całym SSI, na współdzielonym VPS nie więcej niż 20–25% CPU na proces budowania i nie więcej niż 2 GiB zaplanowanej pamięci, ale tylko gdy wystarcza do operacji; gdy wymagania są większe, przesunąć ciężki etap na lokalny komputer/odrębną maszynę lub status `WAITING_FOR_RESOURCES`, zamiast przekroczyć limit. Zachować dynamiczny zapas pamięci produkcyjnej. Automatyczna pauza gdy zwiększa się czas odpowiedzi usług lub maleje wolny RAM/dysk; nie restartować usług krytycznych. *Bardziej szczegółowe limity dopiero po odczycie rzeczywistego obciążenia Director/Robert VPS.*

**Pipeline pobierania modeli:** źródła dozwolone, konkretny upstream revision/digest i licencja, pobierać maks. jedną bazę na raz, bufor na lokalnym storage gdy VPS nie mieści, nie ingerować w magazyn modeli Ollama. **Nie requantyzować już stratnych Q3/Q4 tak, jakby były pierwotnym FP16.**

## 5. Reguły dostawców modeli/finansów

- Domyślny **przyrost wydatków na dodatkowe GPU: 0 USD/dzień**. Start płatnego GPU = wyłącznie `COST_APPROVAL_REQUIRED`; nigdy autonomiczne uruchamianie pod pretekstem wygody.
- Luna, Together AI, OpenRouter i pozostali: wykorzystywać przy rzeczywistych misjach wtedy, gdy istnieje decyzja wymagająca mocniejszego modelu; nie generować masowo „sztucznego treningu” bez rachunku kosztu.
- Zachować istniejące odrębne liczniki dostawców/kredytów; historyczne 3 USD/dzień na MSI i 3 USD/dzień na NODE-01 **nie są nową pulą ani potwierdzeniem salda**. OpenRouter — osobny licznik. Każdy płatny request ma model/provider/est_cost/approval/mission_id, i lokalną kwalifikację danych do wysłania.
- W procesie uczenia wykorzystać tylko dane użytkownika, do których SSI ma prawo i które zostały oczyszczone z sekretów oraz danych partnerów. Ograniczenia licencji/model terms mogą zabronić wykorzystania odpowiedzi niektórych usług do treningu; wówczas tylko konsultacja podczas misji.
- W pierwszej kolejności korzystać ze zweryfikowanych decyzji już zapisanych przez notariusza, nie dokupywać identycznych odpowiedzi u kilku nauczycieli.

## 6. Realizacja 13 wariantów: etapy

1. **0 — audyt bez zmian:** maszyny Director i Robert (CPU, RAM, dysk, obciążenie, usługowe P0/P1), stan SSI MODELS, lokalne storage i już istniejące checkpointy, lista modeli i uprawnienia.
2. **1 — rozruch mały:** Qwen2.5-Coder 1.5B jako kandydat QUANT. Nie pobierać ciężkich źródłowych wag na SSI MODELS; gdy nie ma zgodnych źródeł zasobów, wstrzymać.
3. **2 — warianty 0.8B–4B:** dobrać priorytet rzeczywistych zastosowań, Tev1/D1 tylko po weryfikacji architektury, multimodalności i zachowania System One.
4. **3 — modele 6–8B:** planowane tylko przy wykazanej wystarczającej pojedynczej maszynie / lokalnym storage. Przenoszenie fragmentów zadania między VPS nie zastąpi pamięci potrzebnej dla monolitycznej konwersji.
5. **4 — praca misyjna:** notariusz obserwuje wyniki realnych zadań i stopniowo zatwierdza candidate → canary → promoted. Porażka = rollback bez utraty oryginałów.
6. **5 — escalacja GPU:** tylko gdy powtarzalny `BLOCKED_RESOURCE` i udokumentowana oszczędność wyraźnie uzasadnia osobną akceptację. Korzystać z A40 jako pojedynczego, ograniczonego czasowo burstu — nie zasobu stałego.
  
**Nie obiecujemy, że wszystkie 13 wariantów da się uzyskać na 16 GiB pamięci bez płatnego GPU**. Celem R10 jest minimalizacja kosztu przy realnych ograniczeniach, a nie pozorny stan „zrobione”.

## 7. Oczekiwane dowody

Na każdy kandydat wymagane: `source_model_id`, `source_revision`, `source_license`, `build_host_role`, `llama_cpp_revision`, `quant_method`, `imatrix_dataset_hash_or_none`, `artifact_sha256`, `artifact_size_bytes`, `memory_peak`, `cpu_time`, `wall_time`, `api_cost_usd`, `gpu_cost_usd`, `validation_status`, `routing_status`, `rollback_tag` oraz potwierdzenie braku zmian oryginalnych 13 modeli.

**Dostarczenie R10 oznacza zmianę planu na GitHubie, nie instalację produkcyjną ani rozpoczęcie nowego modelu.**
