# SSI — wynik manifestu rdzenia R1 i budżet 80 GB

Data: 25 października 2026 r.  
Status: **pomiar szerokiego zakresu zakończony; wybór i odbiór minimalnego rdzenia oczekują**.  
[Wersja JSON](SSI_CORE_MANIFEST_R1_REVIEW_PUBLIC_20261025.json) · [Decyzja ACTIVE/ARCHIVE i połączenia MultiQuant](SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025.md).

## Potwierdzony pomiar

Sprawdzono CRC archiwum operatora, trzy sumy SHA-256 jego plików raportowych oraz zgodność obu modułów narzędzia z dostarczoną paczką. Skan metadanych zakończył się w wybranych lokalizacjach bez zgłoszonych błędów: **904 568 wpisów, 771 261 lokalizacji zwykłych plików, 110 dowiązań nieśledzonych**. Nie jest to potwierdzenie wszystkich źródeł SSI ani spójnego punktu w czasie dla zmieniających się baz.

| Wariant | Zwykłe pliki, logiczne GB dziesiętne | Interpretacja |
| --- | ---: | --- |
| Cały zmierzony zakres | 146,18 | Zawiera stare instalacje i środowiska |
| Kandydaci do archiwum | 59,83 | Klasyfikacja; niczego nie przeniesiono |
| Pozostały szeroki zestaw | 86,35 | Nadal przekracza 80 GB |
| Dalszy kandydat: historia Git | 8,05 | Zachować poza pakietem uruchomieniowym, po sprawdzeniu odwołań runtime |
| Warunkowo po obu wydzieleniach | 78,30 | Nie jest jeszcze domkniętym rdzeniem |
| Ten wariant + rezerwa 10 GB | 88,30 | Przed doliczeniem narzutów systemu i innych brakujących zależności |

Dokładne wartości w bajtach są w JSON. To sumy rozmiarów logicznych lokalizacji plików, **nie zmierzone odzyskane miejsce** ani rozmiar odtworzonego pakietu. Dowiązania, twarde linki, zajęte bloki i narzut systemu wymagają osobnego rozliczenia. Wydzielenie historii Git nie oznacza usuwania repozytorium źródłowego.

W pozostałym zestawie są **trzy środowiska Python o łącznym rozmiarze 20,20 GB**. Ich ewentualna konsolidacja jest kierunkiem oszczędności, nie odebraną zgodnością. Nie można odjąć całej tej wartości i twierdzić, że silnik dalej działa. Moduły domenowe, dane potrzebne aktywnym funkcjom i pamięci aktorów pozostają w zakresie wymaganym przez ich zależności.

## Co oznacza wskazany zestaw aktywny

Narzędzie odczytało **26 plików Python jako AST**, zarejestrowało **334 krawędzie zależności** i wskazało **27 zwykłych plików ACTIVE_CANDIDATE, razem 891 241 B**. Ta mała liczba jest wyłącznie listą rozpoznanych referencji. **Nie jest rozmiarem całego SSI** i nie dowodzi ukończenia wyboru głównych kompetencji.

Rejestr Czary zachowuje **520 deklarowanych wpisów QUALIFIED**. Status kwalifikacji nie został zmieniony ani ponownie nadany. Historyczne dowody treningowe opisane we wcześniejszym raporcie nie zastępują odbioru bieżącego kodu.

## Konkretne brakujące powiązania

- Plik startowy Dyrektora importuje `importlib`; R1 nie wskazał jego dynamicznego celu uruchomienia.
- Dla usługi interfejsu R1 znalazł Uvicorn, ale nie rozpoznał właściwej aplikacji.
- Wyszukiwanie modułu Luny wymaga uwzględnienia jej katalogu aplikacji.
- Zależności danych i zgodność środowisk pozostają do potwierdzenia.
- Aktualny autorytatywny parser SCC oraz pełna ścieżka kompetencja → wykonawca → Evidence nadal wymagają odbioru.

Następna paczka sprawdza **613 konkretnych plików silnika, łącznie około 4 MB**, deklaracje startowe i metadane trzech środowisk. Nie wymaga ponownego skanowania całej instalacji. Przeszła **7 lokalnych testów syntetycznych**; wynik wykonania na MSI jeszcze nie dotarł. Nie uruchamia silnika, modeli ani misji.

## Synchronizacja z MultiQuant

Sprawdzono main `94c730b8e18ee8c7b2f8c7f9adf17d7026c8d998`. [Opublikowana referencja BF16 B1](../PUBLIC_MODELS/BENCHMARKS/SSI_MULTIQ_B1_BF16_RESULTS_20261025.md) raportuje **32 zadania × 3 powtórzenia = 96/96**. Są to powtórzenia tych samych prostych zadań, nie 96 niezależnych pytań. Syntetyczne teksty przypominające SCC nie potwierdzają natywnego wykonania misji.

Nowszy [start produktu FSE-01](../PUBLIC_MODELS/SSI_MULTIQ_FSE01_FIRST_PRODUCT_REAL_HARDWARE_KICKOFF_R1_20261025.md) zachowuje integrację przez natywny SCC, Router, Research Memory, adapter, kolejkę i Evidence jako cel do odbioru. CPU B1 i działanie modułów nadal oczekują na walidację. Nie przenosimy statusu BF16 na migrację, kwalifikację skilli ani produkcyjne SCC.

Wagi modeli na wspólnej roli CORE24/MultiQuant nie są domyślnym składnikiem dysku Dyrektora. Adapter, jego kontrakty i wymagany stan muszą zostać uwzględnione w pakiecie. Nie kopiujemy dużego GGUF na Dyrektora wyłącznie dlatego, że model bierze udział w równoległym eksperymencie.

## Warunek dalszej migracji

**Nie ma jeszcze dowodu, że kompletny aktywny rdzeń mieści się w 80 GB ani że działa bez NOUT1.** Potrzebny jest domknięty manifest, pomiar przygotowanego pakietu ze środowiskiem, danymi i rezerwą, a następnie staging: start, natywna misja i recovery bez archiwalnego komputera.

Nie usunięto źródeł ani plików SQLite WAL, nie wyzerowano stanu aktorów, nie zmieniono rejestrów i nie wykonano migracji produkcyjnej. Checkpointy, aktywny stan i ciągłość dowodów zachowujemy; duża objętość danych nie stanowi zgody na ich reset.

Źródło prywatnego raportu operatora, SHA-256: `d810ac2998722581802f64997dd419c335b89330536afcce82b0c98c2f7e648b`. Publikacja obejmuje wyniki i ograniczenia; surowy manifest, kod, bazy, adresy i prywatne ścieżki nie są publikowane.
