# Odpowiedź SSI MultiQuant na uzgodnienie migracyjne ACTIVE / ARCHIVE R1

**Data:** 2026-10-25  
**Handoff ID:** `SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025`  
**Przeczytany commit migracji:** `e1f41fc9fce673d087144088e1c30e546a602ad3`  
**Przeczytany stan MultiQuant / RAM Guard przed handoff:** `00f7287230cce6999b5c938e792ad084420b7819`  
**Status odpowiedzi:** `MULTIQ_HANDOFF_RESPONSE_R1 / RESEARCH_RESULTS_CONFIRMED / INTEGRATION_PENDING`

## 1. Potwierdzone wyniki i rozdzielenie zakresów

- MultiQuant R15: **10/10 PASS**; izolowany guard i dwa syntetyczne poziomy po **96 bajtów**. Wartości **4 GiB ACTIVE + 4 GiB LONGTERM** są deklaracjami, a nie potwierdzonymi produkcyjnymi limitami dysku.
- R16/R17: izolowane wykrywanie uszkodzeń, kwarantanna i odzyskiwanie z poprawnej kopii. Nie wykazano recovery całego SSI.
- R18/R19: odczyt pamięci przez nowe procesy i wznowienie syntetycznej pięcioetapowej misji **od kroku 3 po dwóch zapisanych checkpointach**; R19 **10/10 PASS**.
- R20/R21: izolacja zapisów, konkurujące claims i fencing, pięć niezależnych syntetycznych misji; R21 **10/10 PASS**. Brak gwarancji exactly-once dla efektów poza SQLite, szczególnie po awarii między wykonaniem zewnętrznej operacji a zapisem potwierdzenia.
- RAM Guard R2: testowo aktywny, **nietrwały po restarcie** zram o logicznej pojemności **2 GiB**, priorytecie **100**, z zachowanym swapem dyskowym i `swappiness=10`. Brak udowodnionego przyspieszenia; zram nie jest backupem.
- RAM Guard R4: potwierdzona kopia **dwóch małych syntetycznych magazynów**, **12 plików i 24 960 B**, na MSI poza CORE24; ponowny odczyt SQLite i SHA-256 PASS. **Nie zabezpieczono w ten sposób wszystkich magazynów SSI**.
- R22 konkurencji wykonawców oraz BASELINE BRIDGE B1 pozostają poza powyższym zakresem potwierdzonych wyników: nie przedstawiono tu ukończonego wykonania na CORE24/MSI.

## 2. Co MultiQuant potrzebuje w rdzeniu ACTIVE

**Wymagane klasy danych i zależności do integracji (projekt interfejsu, nie potwierdzona instalacja):**

1. Wersjonowany interfejs adaptera oraz minimalny runtime i jego środowisko wykonawcze; zależności należy ustalić na podstawie właściwej, prywatnej implementacji, nie na podstawie samych fixture.
2. Natywny kontrakt misji i identyfikatory projektu/aktora/domeny, kontekst z SHA-256, wersje planów, reguły uprawnień, limity odczytu oraz odwołania do źródeł Research Memory.
3. Indeks aktywnego magazynu i metadata ACTIVE/LONGTERM, integralność obiektów, kontrola zajętości, polityka retencji oraz możliwość wycofania błędnych zapisów. **Pojemności 4+4 GiB nie wolno deklarować jako wdrożonego limitu.**
4. Trwałe potwierdzenia misji i kroków, statusy przed i po wykonaniu, lease/claim z generacją fencing, kontrola replay, błędy oraz dowody odtworzenia.
5. Odwołania do notariusza/evidence, identyfikatorów i korzeni łańcuchów, a nie samodzielny drugi rejestr prawdy.
6. Konfiguracja usługi modeli współdzielonej na CORE24. **Nie należy duplikować wag modeli na serwerze Dyrektora** w celu spełnienia handoffu.

Wersje archiwalne, historyczne treningi, powielone środowiska, surowe logi benchmarków oraz testowe fixture powinny pozostawać poza ACTIVE, z zachowaniem ich pochodzenia i wymaganych odwołań. Archiwizacja wymaga dowodu odtwarzalności, nie kasowania. Nie scalać mutowalnego stanu aktorów na podstawie identycznych bajtów.

## 3. Kontrakt SCC i brakujące połączenia

Autorytetem pozostają oryginalny parser Dyrektora i istniejące kontrakty **`ssi.mission.goal.r1`** oraz **`ssi.mission.intent.r1`**. Adapter MultiQuant może odbierać wyłącznie **zwalidowaną, autoryzowaną reprezentację misji**, nie zastępuje składni natywnego SCC syntetycznym JSON-em.

Docelowy przepływ: **parser SCC → zwalidowany kontrakt misji → Router V10/S10 → autoryzacja Research Memory → adapter MultiQuant / store → właściwy wykonawca → Evidence/Notariusz → checkpoint**.

**Brakuje dowodu:** obecnego autorytatywnego parsera i natywnego bindingu na VPS Dyrektora, trasowania Router V10/S10 do adaptera, rzeczywistego ACL i odwołań Research Memory, podłączenia wykonawcy/Notariusza, rekwalifikacji skilli, odzyskiwania na wielu hostach, restartu stagingu i działania bez NOUT1. Syntetyczny PASS nie promuje kompetencji ani produkcji.

## 4. Wymagania checkpointów i wykonawców

Klucz logiczny checkpointu: **misja + krok + wersja planu + hash kontekstu + identyfikator aktora**, z zachowaniem autorytatywnego ACL. Żądanie powtórne o tym samym kontrakcie powinno być idempotentne; inne parametry powinny kończyć się konfliktem, nie nadpisaniem. Przejęcie kroku wymaga jednoznacznej generacji fencing, odmowy spóźnionego wykonawcy i zapisu rozstrzygnięcia do evidence. Osierocone i uszkodzone dane: **STOP + dowód + kwarantanna**, odzyskiwanie tylko ze zweryfikowanej kopii. Dla realnych efektów zewnętrznych potrzebne są osobne idempotency keys, potwierdzenia wykonawcy i procedura reconcilation po niejednoznacznym błędzie; sama transakcja SQLite nie gwarantuje exactly-once.

## 5. Zmierzone wielkości i brakujące dane

| Wielkość | Zakres dowodu |
| --- | --- |
| Dwa testowe magazyny R15 | 96 B ACTIVE + 96 B LONGTERM; nie rzeczywiste kwoty 4+4 GiB |
| Testowe magazyny R15 i R18 badane w RAM Guard | po 5 rekordów i 192 B danych |
| Kopia MSI R4 | 12 plików, 24 960 B; wyłącznie fixture |
| CORE24 R1 preflight | 15,62 GiB RAM fizycznego, 15,05 GiB dostępne w chwili pomiaru |
| Zram R2 | 2 GiB logicznego swapu, nietrwałe po restarcie, priorytet 100 |
| Dyskowy swap CORE24 | ok. 12 GiB zapasowego swapu zachowane |
| Wielkość faktycznego runtime MultiQuant, baz danych i pełnego ACTIVE | **NIE ZMIERZONO** |
| Nowy minimalny rdzeń migracji / zgodność z 80 GB | **NIE ZMIERZONO / NIE POTWIERDZONO** |

Osobny eksperyment modelu bazowego BF16 70B: RunPod 2×A100 80GB, wagi 141,107 GB, jedno pytanie zakończone PASS; GPU zatrzymany. To **zewnętrzna referencja benchmarkowa**, nie element minimalnego rdzenia Dyrektora ani dowód przyspieszenia MultiQuant. Wariant CPU IQ2_XXS (~19,10 GB pliku) badano na innym sprzęcie; nie porównywać bezpośrednio jego czasu z ciepłym zapytaniem BF16 na GPU.

## 6. Najbliższa ograniczona bramka odbiorcza

**STAGING_ONLY**: zidentyfikować aktualny parser i registry Dyrektora; ustalić wersjonowany, minimalny adapter MultiQuant; uruchomić *jedną* natywną misję testową **SCC → Router → Research Memory (autoryzacja) → MultiQuant → Evidence**. Zweryfikować hash kontekstu, odmowę nieautoryzowanego dostępu, unikatowe checkpointy, przerwanie i wznowienie, dowód działania Notariusza oraz zależności bez NOUT1. Następnie zmierzyć rozpakowany runtime, faktyczne zajęte miejsce i RAM oraz powtórzyć próbę na stagingu bez NOUT1. **Żadnego przenoszenia, kasowania, nadpisywania skilli, automatycznej promocji do produkcji ani płatnych GPU** w ramach tego dokumentu.

**Odpowiedź dotyczy zakresu i dowodów, nie potwierdza pełnej integracji.** Kod, pełne manifesty i ścieżki operacyjne pozostają prywatne.
