# SSI ROBERT — migracja środowiska wykonawczego: stan na 24.10.2026

## Podsumowanie

Przygotowano i zweryfikowano kolejne etapy migracji SSI ROBERT na docelowy VPS 24/7, wraz z kandydackim środowiskiem SSI CODEX oraz połączeniem metadanych z SSI CORE24.

**Ostatni potwierdzony wynik operatora: P3C_REVIEW_REQUIRED.**

Oznacza to, że etapy przygotowania źródeł, izolowanego runtime i testu integracyjnego zostały wykonane, ale kandydacki worker P3C **nie został jeszcze zaakceptowany ani aktywowany**.

**Pełna migracja Roberta nie jest zakończona.** W szczególności nie podłączono jeszcze kanonicznej pamięci aktora, historycznej kolejki, checkpointów ani ciągłości Notariusza. Nie uruchomiono produkcyjnego konsumenta kolejki.

## Architektura docelowa

Aktualny podział trzech VPS:

- **SSI DIRECTOR** — Dyrektor, Universal Lab, orkiestracja, planowanie i delegacja;
- **SSI ROBERT** — Robert jako wykonawca techniczny 24/7, współlokowany SSI CODEX i MultiQuant;
- **SSI CORE24 / MODELS** — wspólna usługa modeli Ollama dostępna przez kontrolowane API.

Urządzenia lokalne pozostają rozszerzeniami i źródłami historycznych danych. Ich niedostępność nie może blokować zadań SERVER_NATIVE.

## Co wykonano

| Etap | Udokumentowany rezultat |
| --- | --- |
| P0 / P0R1 | Zebrano ograniczone metadane trzech VPS. Każdy host miał około 16 GiB RAM i 4 vCPU. Potwierdzono spójność katalogu 13 tagów modeli w zakresie metadanych. Nie wykonywano inferencji ani kwalifikacji modeli. |
| P1 | Zbudowano lokalny manifest bieżących usług, portów i kandydackich katalogów bez zmian na VPS. Potwierdzono aktywne usługi CORE24 oraz istniejące dane MultiQuant na roli Roberta. |
| P2A | Na VPS Roberta zapisano wersjonowany, prywatny zestaw źródeł migracyjnych. 5 oryginalnych archiwów, 62 pliki kandydatów i 45 plików Python przeszło kontrolę składni. Nie uruchomiono żadnego kandydata. |
| P2B | Próby wskazania pełnego historycznego stanu Roberta zakończyły się częściowo. Nie potwierdzono jeszcze pełnej kanonicznej pamięci, kolejki i checkpointów. Nie utworzono pustego zamiennika. |
| P3A | Przygotowano izolowany runtime-prep na VPS Roberta. Skopiowano 22 pliki źródłowe, 20 plików Python przeszło kontrolę AST, a connector CORE24 odczytał 13 tagów modeli. Brak aktywacji usług i brak migracji stanu. |
| P3B | Izolowany test runtime zakończył się wynikiem **P3B_ISOLATED_RUNTIME_TEST_PASS_NOT_ACTIVATED**. Kontrola AST: 20/20; metadane CORE24: 13 tagów. State binding: NOT_PERFORMED, queue consumer: NOT_STARTED, systemd changes: 0. |
| P3C | Pierwsza próba przygotowania kandydata workera zakończyła się **P3C_REVIEW_REQUIRED**. Wynik nie został zamieniony na PASS i worker nie został aktywowany. |

## Ważne poprawki narzędzi migracyjnych

Podczas P3A wykryto dwa błędy w samych paczkach migracyjnych:

1. brak utworzenia katalogu dla jednego z pokwitowań;
2. nieaktualny wewnętrzny manifest po poprawce.

Oba problemy zostały poprawione bez aktywowania usług Roberta. Poprawiona paczka P3AR2 przeszła self-check, a następnie P3A zakończyło się poprawnie.

Te błędy dotyczyły narzędzia wdrożeniowego, nie stanu Roberta, MultiQuant ani SSI CORE24.

## Stan SSI CORE24

W aktualnym przepływie migracyjnym potwierdzono dostęp do metadanych **13 tagów modeli** z roli Roberta.

Nie oznacza to, że wszystkie modele:
- były jednocześnie załadowane;
- zostały ponownie przetestowane inferencyjnie;
- mają aktualną kwalifikację jakości do wszystkich zadań;
- są kopiowane na każdy VPS.

Docelowy model pracy pozostaje wspólny: uprawnione komponenty korzystają z CORE24 przez kontrolowane API, zamiast duplikować wszystkie wagi.

## SSI CODEX na Robercie

Źródła SSI CODEX R4/R5 są zachowane jako materiał migracyjny. Przygotowanie P3A/P3B służy uruchomieniu CODEX-a jako odrębnej roli wykonawczej na VPS Roberta.

Nie uznajemy:
- samej obecności kodu za działającą usługę;
- historycznego HUB R5 za gotowe produkcyjne SSO;
- starego układu Lenovo za wymaganą zależność runtime;
- testowego stanu za prawdziwą pamięć Roberta.

CODEX ma docelowo korzystać z CPU/RAM Roberta do pracy projektowej, testów i budowy artefaktów, a z modeli CORE24 korzystać przez API.

## MultiQuant

Istniejące dane MultiQuant na VPS Roberta zostały zachowane bez nadpisywania.

W tej części migracji:
- nie uruchamiano kwantyzacji;
- nie uruchamiano destylacji;
- nie uruchamiano płatnych GPU;
- nie wykonywano automatycznej promocji modelu.

Docelowo MultiQuant ma obsługiwać oddzielne ścieżki:
- **Q** — rzeczywista kwantyzacja z pełnym pochodzeniem artefaktu;
- **D** — rzeczywisty trening/destylacja ucznia z osobnym backendem i dowodami.

## Czego jeszcze brakuje

Do uznania Roberta za rzeczywiście zmigrowanego wymagane są nadal:

1. powiązanie kanonicznego stanu Roberta: pamięci, kolejki, checkpointów i historii;
2. zachowanie ciągłości Evidence/Notariusza bez tworzenia nowej pustej tożsamości;
3. sprawdzony backup i niezależna próba odtworzenia;
4. odbiór workera ROBERT/CODEX po wyniku P3C_REVIEW_REQUIRED;
5. jedna kontrolowana misja SERVER_NATIVE przez pełny cykl request → execution → receipt → evidence;
6. restart/recovery bez zdublowania skutków;
7. późniejsze spięcie delegacji z Universal Lab / Operations i właściwymi ACL;
8. dopiero później uruchomienie szkoleń oraz rzeczywistych ścieżek D/Q MultiQuant.

## Punkt wznowienia

Nie powtarzamy P0, P1, P2A, P3A ani P3B.

Aktualny punkt wznowienia to analiza wyniku **P3C_REVIEW_REQUIRED** i poprawienie wyłącznie kandydata workera P3C. Nie należy w tym celu:
- uruchamiać pustej bazy Roberta;
- podmieniać istniejących danych MultiQuant;
- kopiować wszystkich modeli na serwer Roberta;
- przywracać starszych instalatorów bez zgodności z bieżącą architekturą;
- uruchamiać produkcyjnego konsumenta kolejki przed związaniem stanu.

## Granica publikacji

Ten dokument jest publicznym raportem technicznym.

Nie zawiera:
- prywatnego kodu SSI;
- baz i pamięci agentów;
- kluczy, tokenów lub haseł;
- adresów infrastruktury;
- prywatnych ścieżek i pełnych inwentarzy operacyjnych.

Wyniki opisują wyłącznie zakres potwierdzony przez raporty migracyjne i terminal operatora. PASS jednego etapu nie jest rozszerzany na obszary, których dany test nie obejmował.

## Powiązane dokumenty

- [Migracja środowiska Dyrektora M1–M8R1](./SSI_DIRECTOR_MIGRATION_M1_M8R1_20261023.md)
- [BLOKS — plan i punkt wznowienia](../docs/SSI_BLOKS_ROADMAP_HANDOFF_20261018.md)
