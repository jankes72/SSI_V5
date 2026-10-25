# SSI MultiQuant FSE-01 — P1R10: odkrycie źródeł V7.16 na MSI i ograniczony przegląd pierwszego VPS

**Data:** 2026-10-25  
**Dowód:** wynik read-only skryptu P1R10 wykonany przez operatora na MSI i historycznym pierwszym VPS (MultiQuant/Robert). Nie przeprowadzono niezależnego SSH ani inferencji.  
**Status:** `P1R10_MSI_SOURCE_CANDIDATES_IDENTIFIED / FIRST_VPS_SOURCE_MANAGERS_CONFIRMED / CANONICAL_MULTIQ_ENGINE_UNVERIFIED / FSE70B_NOT_RUN`.  
**Zmiany wg logu:** `MODEL_EXECUTION=NO`, `PRODUCTION_CHANGES=NONE`.

## Ustalenia — MSI

Skrypt przeszukał wybrane katalogi lokalne **maksymalnie do głębokości 5**, filtrował nazwy plików według `multiq`, `quant`, `fragment`, `distill`, `composite`, `compress`, pomijał wskazane duże drzewa i zatrzymywał wyniki po 50 trafieniach lub limicie czasu. Z tego powodu **nie jest to pełny skan źródeł SSI**.

- W katalogu pobranych występują lokalne skrypty `SSI_MULTIQ_V7_16_R19.py`, `SSI_MULTIQ_V7_16_R20.py`, `SSI_MULTIQ_V7_16_R21.py`. Są to **ważni kandydaci do analizy AST i porównania z raportami eksperymentów R19–R21**.
- Dodatkowo znaleziono m.in. `SSI_MULTIQ_BASELINE_BRIDGE_B1.py`, `SSI_MULTIQ_ACTIVE_ARCHIVE_R5.py`, `SSI_MULTIQ_RAMGUARD_R1/R2/R3/R4.py` i pomocniczy odczytowy skrypt łączący SCC/LEGO/MultiQuant R9.113.
- W badanym drzewie `SSI_V5` filtr nazw wskazał kilka materiałów LEGO Pocket związanych z kompresją i fragmentowanymi odpowiedziami; nie zweryfikowano ich związku z kanonicznym engine.
- Lokalny katalog `SSI_V5_Body` nie został wypisany przez skrypt, więc jego obecność i zakres nie są potwierdzone tym logiem.

**Nie utożsamiać tytułów R19/R20/R21 z gotową implementacją ani aktywną usługą.** W publicznych raportach V7.16 R19/R21 istnieją ograniczone, izolowane PASS testów checkpointów/claims, a nie automatyczny dowód produkcyjnego adaptera SCC lub faktycznego obiegu FSE-01.

## Ustalenia — pierwszy VPS

- W dwóch **oddzielnych** lokalizacjach są pliki o nazwie `01_R20_SOURCE_MANAGER.py` (podobna lista funkcji top-level, nie ustalono tożsamości treści). Znaleziono także `01_R21_MANAGER.py`.
- Funkcje managerów odpowiadają z wcześniejszych audytów m.in. za `request`, `get_source_metadata`, `remote_plan`, `sha256_file`, `preflight`, `install_deps`, `prepare`, `convert`, `verify_artifact`; mogą stanowić tooling przygotowania źródeł i wag.
- W wybranym katalogu `r21` pod drzewem offline MICRO skrypt nie znalazł w badanym zakresie plików Python. To **nie jest** dowód braku innych artefaktów w ~11GB drzewie.
- Znacznik `HAS_MAIN_GUARD=True` w oryginalnym skrypcie oznaczał tylko obecność **jakiegokolwiek `ast.If` z warunkiem `ast.Compare` na top-level**; **nie stanowi prawidłowego wykrycia dokładnego `if __name__ == '__main__'`**. Nie używamy tego pola do akceptacji entrypointu.

## Rozstrzygnięte / otwarte

| Bramka | Stan |
| --- | --- |
| MSI: pliki nazwane V7.16 R19/R20/R21 | `FOUND` w ograniczonym skanie |
| Pierwszy VPS: source manager R20/R21 | `FOUND`; nie zidentyfikowano aktywnego engine |
| CORE24: API→Worker domyślnie `ollama_chat` | `STATIC_PASS` w P1R9 |
| Kanoniczny program MultiQuant, jego źródło, wersja i deploy na pierwszym VPS | `UNVERIFIED` |
| Natywny SCC→MultiQuant→70B IQ2→Evidence | `NOT_EXECUTED` |
| FSE-01 jako produkt | `HOLD` |

## Weryfikacja następna — P1R11

1. **Najpierw lokalnie na MSI** statycznie przeczytać wyłącznie znalezione, konkretne skrypty V7.16 R19/R20/R21 i `BASELINE_BRIDGE_B1`: rozmiar, SHA-256, rzeczywisty `__main__` guard, nazwy top-level `ClassDef/FunctionDef`, jawne importy i obecność argumentów CLI; bez wykonywania.
2. **Nie mieszać** tych plików V7.16 z odrębnymi managerami `01_R20_SOURCE_MANAGER.py` i `01_R21_MANAGER.py` na VPS. Weryfikować zgodność dopiero przez jawne metadane i hashe.
3. Po zidentyfikowaniu kandydata na **rzeczywisty engine**, sprawdzić implementację w zabezpieczonym prywatnym repo/paczce i możliwość kontrolowanego wdrożenia, bez nadpisywania aktywnych procesów.
4. Jeżeli R19–R21 są wyłącznie syntetycznymi fixture/testami, szukać osobno **kanonicznego runtime MultiQuant** w zachowanych źródłach MSI/CORE24, nie promować testowego skryptu na produkcję.
5. Finalnie wykonać tylko po odpowiedniej bramce staging pojedynczy obieg `DIRECTOR (SCC/Router) → MultiQuant → CORE24 70B → Evidence`.

**Ochrona:** brak zmian produkcyjnych, kopiowania 19GB GGUF, uruchamiania modelu lub płatnych GPU. W raporcie publicznym nie umieszczono prywatnych logów, kodu, kluczy, IP ani poufnych danych.

## Powiązania

- [P1R9: wybór domyślnego callbacku Ollama](SSI_MULTIQ_FSE01_P1R9_CORE24_DEFAULT_OLLAMA_CALLBACK_RESOLVED_20261025.md)
- [R19: izolowane checkpointy](SSI_MULTIQ_V7_16_R19_STEP_RESUMPTION_20261025.md)
- [R21: izolowane równoległe misje](SSI_MULTIQ_V7_16_R21_MULTI_MISSION_CONCURRENCY_20261025.md)
- [Koordynacja migracji](../RESULTS/SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md)
