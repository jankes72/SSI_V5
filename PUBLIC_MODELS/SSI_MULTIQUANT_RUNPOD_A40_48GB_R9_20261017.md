# SSI MultiQuant R9 — A40 48 GB: warsztat 13 kandydatów dla VPS MODELS 16 GB RAM

**17.10.2026. Status: tylko audyt REST API; Pod nie został uruchomiony, żadnej kwantyzacji ani migracji jeszcze nie wykonano.**

## Zweryfikowane przez operatora

- Z dostępnego lokalnie klucza RunPod API (wartość nie ujawniona) możliwy był odczyt własnych zasobów.
- Jeden istniejący Pod w stanie **EXITED**, z jednym GPU **NVIDIA A40**. NVIDIA potwierdza nominalną pojemność **48 GB VRAM** tego modelu GPU: https://www.nvidia.com/en-us/data-center/a40/.
- REST API podało **30 GB dysku kontenera**, nie wcześniej deklarowane 40 GB.
- Poprzedni skrypt diagnostyczny nie wykazał osobnego trwałego wolumenu — **NIE POTWIERDZA to jego braku**, ponieważ zależy od mapowania pól odpowiedzi REST. Wymagany odczyt właściwych pól i weryfikacja w konsoli.
- Pamięć RAM i liczba vCPU maszyny nie były dostępne w polach wydrukowanych przez skrypt; nadal **nieznane**.
- Odczyt pola kosztu dał wartość **0.59**, jednak jednostka i obejmowane składniki nie zostały zweryfikowane — **nie przyjmować tego za końcowy rachunek**.
- W odrębnym audycie produkcyjnego VPS MODELS potwierdzono: działająca Ollama i 13 oryginalnych modeli, ~15 GiB RAM, 12 GiB SWAP, ~59 GB wolnego dysku, skompilowane **CPU-only** `llama-quantize` i `llama-imatrix`. Narzędzia tam pozostają do diagnostyki, nie do produkcyjnego budowania 13 modeli.

## Rozdział obliczeń i odpowiedzialności

- **RunPod A40 48 GB** — warsztat na żądanie: legalne oryginały wag o dopasowanej rewizji, weryfikacja architektury i licencji, kalibracja `imatrix` z przyspieszeniem GPU tam, gdzie możliwe, selektywne kwantyzacje i — tylko jako **odrębnie zaplanowana praca** — dostrajanie/destylacja decyzji.
- **VPS MODELS 24/7** — serwer inferencji CPU, bez pobierania źródłowych BF16/FP16 i bez ciężkich prac nad wagami. Otrzymuje tylko gotowe warianty w stagingu z sumą SHA256 i manifestem pochodzenia, a po oddzielnym dopuszczeniu oferuje je Routerowi.
- **Director / Robert / CODEX** — działają dalej autonomicznie. Posiadane modele produkcyjne bez zmian. Cele: **13 oryginalnych + do 13 nowo zweryfikowanych wariantów** (bez automatycznego równoległego ładowania wszystkich). **5 przyszłych modeli Roberta wyłącznie w planie.**
- **Klasa jakości 48 GB GPU nie jest przenoszona samym kwantyzowaniem**: rozmiar VRAM karty to pojemność sprzętowa, nie cecha inteligencji. Kompresja pojedynczego małego modelu nie zapewni zdolności większego; możliwa jest osobna destylacja wybranych umiejętności na bazie autoryzowanych danych i praw do modeli.

## Blokery przed uruchomieniem płatnego GPU

1. Potwierdzić RAM, vCPU, realny koszt za godzinę, rozmiar i trwałość magazynu oraz to, czy zatrzymany Pod można wznowić na dostępnej karcie A40.
2. **30 GB dysku kontenera jest tymczasowe** (RunPod: usuwane po zatrzymaniu Poda). Ustalona i sprawdzona strategia eksportu wyników i checkpointów jest obowiązkowa, zanim zacznie się konwersja. Potwierdzić stan wolumenów, nie zakładać ich braku ani obecności. Dokumentacja: https://docs.runpod.io/pods/storage/types.
3. Uwaga na 7B–8B: FP16/BF16 + GGUF wejściowy + wynik + biblioteki/cache mogą przekroczyć 30 GB. Nie uruchamiać takiego przetwarzania bez planu wolnego miejsca (np. powiększony tymczasowy dysk + natychmiastowy eksport lub trwały wolumen) i osobnej wyceny. Miejsce powiększać dopiero świadomie i bez niszczenia danych.
4. Zaczynać od jednego małego pilota Qwen2.5-Coder 1.5B, dopiero potem skalować serię. Zgodność i docelową jakość decyzji oceniać w prawdziwych misjach z Notariuszem i fallbackiem.
5. Zero ujawniania API keys, haseł, wewnętrznych adresów, surowych danych misji, prywatnego kodu czy niepublicznych mikrosieci.

**Źródła publiczne:** https://www.nvidia.com/en-us/data-center/a40/ ; https://docs.runpod.io/pods/storage/types ; https://docs.runpod.io/pods/pricing .

## Pelna konfiguracja potwierdzona przez operatora — audyt GraphQL

**17.10.2026 (kolejny odczyt lokalnego API RunPod; nadal 0 mutacji):**

| Parametr | Potwierdzony wynik |
|---|---|
| GPU | 1 × NVIDIA A40, 48 GB VRAM wg specyfikacji producenta |
| RAM hosta Poda | 55 GB (wedlug pola `memoryInGb`) |
| vCPU | 10 |
| Container disk | 30 GB |
| Volume disk | 0 GB |
| Network volume | nie |
| Status | EXITED |
| `costPerHr`, `adjustedCostPerHr` | 0.59 USD/h każda wartość; dodatkowe opłaty sprawdzać osobno |

**Wniosek:** GPU i host RAM są wystarczającym punktem wyjścia dla etapowego eksperymentu 1.5B i obliczeń kwantyzacji, lecz 30 GB dysku to ograniczenie dla 7–8B i kompletu wag pośrednich. Kontener nie ma wolumenu zachowującego wyniki po stop/restart, wiec wynik **eksportować na zewnątrz po każdej ukończonej pracy**. Dokumentacja RunPod (zaktualizowana 15.10.2026) potwierdza utratę danych `container disk` po stop/restart, oddzielną trwałość `volume disk`, i pozwala edytować dysk kontenera: https://docs.runpod.io/pods/storage/types.

**Najbliższy etap**: (1) nie uruchamiać GPU bez świadomej decyzji i limitu kosztowego; (2) pierwszy pilot Qwen2.5-Coder 1.5B może zmieścić się na 30 GB, po kontroli zajętości obrazu, brakującej pojemności, wersji CUDA i dostępności dopasowanego źródła; (3) przed 7–8B zapewnić ok. 80 GB roboczego kontenera **lub** inaczej wykazane wystarczające miejsce; (4) 55 GB RAM hosta nie jest 55 GB wolnego RAM, monitorować `free -h` i `df -h`; (5) przed każdym stopem eksportować wszystkie niezbędne wyniki, manifesty i dane.

**Budżet orientacyjny samego GPU przy 0.59 USD/h:** 2 h = 1.18 USD, 4 h = 2.36 USD, 8 h = 4.72 USD, 12 h = 7.08 USD; nie gwarantuje to wykonania pełnych 13 wariantów i nie obejmuje innych kosztów.

**Rozróżnienie możliwości:** ten Pod A40 48 GB VRAM jest warsztatem, a nie gwarancją odtworzenia przez modele 1–8B na 16 GB CPU zachowania większego modelu. Aby przenieść umiejętności, potrzebna jest osobna destylacja/finetuning i niezależne metryki jakości na zadaniach docelowych.
