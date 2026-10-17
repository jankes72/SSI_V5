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
