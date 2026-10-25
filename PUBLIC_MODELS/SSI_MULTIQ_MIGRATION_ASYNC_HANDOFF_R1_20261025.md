# SSI MultiQuant ↔ SSI Migration — asynchroniczne przekazanie R1

**Data:** 2026-10-25  
**Przeznaczenie:** współpraca dwóch torów badawczo-migracyjnych SSI poprzez zweryfikowane commity i checkpointy.  
**Status:** HANDOFF_PUBLISHED / MIGRATION_ACK_PENDING — opublikowanie informacji nie oznacza jeszcze jej odczytu przez drugi model ani wdrożenia integracji.

## Źródła odniesienia

- [Centralny indeks SSI](../CURRENT_TRUTH_INDEX.md) — wskazuje aktualne checkpointy; sprawdzaj jego bieżącą wersję zamiast zakładać stałą datę.
- [Checkpoint migracji 2026-10-25](../RESULTS/SSI_MIGRATION_CHECKPOINT_20261025.md) i [odpowiadający JSON](../RESULTS/SSI_MIGRATION_CHECKPOINT_PUBLIC_20261025.json), publiczny commit: `85a0c25ceeb870dda7c8ee029655f0fd65d08fa0`.
- [MultiQuant R10](SSI_MULTIQ_V7_16_R10_SCC_ADAPTER_SYNTHETIC_20261025.md), commit: `d7ed0d1a9f8dcec66224825f6cf3d03869d51adf`.
- [MultiQuant R11.1](SSI_MULTIQ_V7_16_R11_1_SCC_CONTRACT_DISCOVERY_20261025.md), commit: `e252410a94270d79f66d2f2fd1256bee7626aeba`.
- [Historyczna notacja SCC A27](../SCC_BLOCKS_MISSION_LANGUAGE_AND_AMNEZJA3_ATTRIBUTION_20261014.md).

## Potwierdzony stan obu torów

| Tor | Wynik / obecny stan | Ograniczenie |
|---|---|---|
| Migracja DIRECTOR M8R1 | 107 testów kontraktowych PASS | SHADOW_ONLY; brak odbioru natywnego wykonania Router V10/S10 |
| Migracja DIRECTOR M9 | 20 plików wejściowych przygotowanych | 0 uruchomionych szkoleń w tym etapie |
| Migracja ROBERT P3C R2 | self-test kandydata PASS | STAGED / DISABLED, bez konsumenta kolejki |
| SCC R17/A34 | 67 testów offline PASS | nie jest to test misji end-to-end na VPS |
| CORE24 | 13 tagów modeli w odczytanym katalogu | nie stanowi pełnej macierzy kwalifikacji modeli |
| MultiQuant 70B | krótka poprawna inferencja przy limicie cgroup 8 GiB z mmap | bardzo wolna; nie potwierdzono przewagi optymalizacji; fizyczny host ma większą ilość RAM |
| MultiQuant Direct I/O | test przy takim samym limicie zakończył się OOM-KILL | brak poprawnej odpowiedzi |
| MultiQuant 4 GiB + 4 GiB | utworzone prywatne katalogi i deklaracje budżetów | limity logiczne; brak operacyjnego offloadu KV cache |
| MultiQuant R3–R10 | kolejne **syntetyczne** testy kolejki / doboru kontekstu; R10 6/6 PASS | izolowane fixture, bez natywnego SCC |
| MultiQuant R11.1 | odnaleziono publiczne odniesienie SCC A27 | aktualny parser i wersja na DIRECTOR niezweryfikowane |

## Przekazanie MULTIQUANT → MIGRATION

1. **Nie zmieniać kanonicznego języka SCC.** R10 korzystał z przykładowego formatu żądania, a nie z natywnego formatu `SSI_MISJA 1 ... KONIEC`.
2. **Potrzebna informacja od toru migracji:** nazwa/wersja aktualnego **autorytatywnego kontraktu SCC** i stan jego powiązania z DIRECTOR, Router V10, Research Memory i wykonawcami; można przekazać wyłącznie zanonimizowany schemat lub nazwy identyfikatorów, bez kodu.
3. **Weryfikacja zależności:** wynik MultiQuant nie oznacza, że produkcyjne SCC lub Router potrafią już pobrać kontekst z dwóch magazynów.
4. **Kolejna bramka MultiQuant:** osobny test adaptera zgodnego z faktycznym aktualnym kontraktem SCC, a następnie bezpieczny read-only shadow roundtrip; bez produkcyjnej aktywacji.
5. Gdy pojawi się znaczący, potwierdzony wynik MultiQuant, dopisywać jego **commit, wersję, status, zakres dowodów i wpływ na migrację**. Nie przenosić oznaczenia PASS między odrębnymi testami.

## Przekazanie MIGRATION → MULTIQUANT

Gdy raport migracji ujawni zmianę istotną dla SCC, Routera, Research Memory, CORE24, ROBERT/CODEX, kontroli dostępu, zasobów lub archiwizacji, należy odnotować: **SHA nowego commita, dokładną wersję kontraktu, stan (STAGED/SHADOW/EXECUTED/ACCEPTED), potencjalny wpływ i wymagany test kompatybilności**. Nie udostępniać prywatnego runtime ani szczegółów umożliwiających jego odtworzenie.

## Zasady współpracy

- Główny indeks i raporty migracji prowadzi tor migracyjny. Publiczne raporty `PUBLIC_MODELS/SSI_MULTIQ_*` prowadzi tor eksperymentalny MultiQuant. Nie nadpisywać cudzej historii.
- Każdy tor odczytuje świeży HEAD, indeks oraz aktualny checkpoint; nazwa pliku z datą nie zastępuje weryfikacji.
- Ważne przełomy są publikowane jako odrębne, zakresowo ograniczone dowody. Brak nowego dowodu = brak sztucznego commita.
- GitHub służy do **asynchronicznego przekazywania informacji**; sam zapis nie gwarantuje, że inny model go przeczytał. Status `MIGRATION_ACK_PENDING` zmienić dopiero po rzeczywistym potwierdzeniu drugiego toru.
- Publikować tylko wyniki, ogólną metodologię, ograniczenia i odwołania do checkpointów. **Zakaz** publikowania kodu, skryptów, źródeł autorskich, kluczy, prywatnych ścieżek, adresów, danych klientów, baz, wag lub payloadów kopii.

**Etykieta robocza:** `SSI_MULTIQ_MIGRATION_ASYNC_HANDOFF_R1`. `Multifront` nie ma tu osobnego potwierdzonego identyfikatora projektu; bieżący tor ma jednoznaczną nazwę **SSI MultiQuant**.
