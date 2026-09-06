# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Autor architektury:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Status:** `BODY_FROZEN T0 PRESERVED / 6X BODY ISKRA START_STATE_VALIDATED / ACTIVE RESEARCH`  
**Data aktualizacji:** `2026-09-06`  
**Wspólny punkt odniesienia:** `T0 / BODY_FROZEN / PRE-ISKRA / 2026-09-05`  
**Aktualny stan eksperymentalny:** `6 niezależnych BODY ISKRA T0 / START_STATE_VALIDATED`  
**Najnowszy zamknięty test walidacyjny:** `TEST 5 / SSI BODY FINAL CONVERGENCE / DEVELOPMENT_VALIDATED`  
**Stan AGI / świadomości:** `NIEUDOWODNIONY — BADANY EKSPERYMENTALNIE`

## Najważniejsza aktualizacja — 2026-09-06

Zamrożony BODY_FROZEN z 2026-09-05 pozostaje niezmiennym wspólnym punktem odniesienia. Z tego samego T0 utworzono już sześć niezależnych wariantów BODY ISKRA i zapisano ich czyste stany startowe.

Publiczne wejścia:

- [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — historyczny wspólny T0
- [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — aktualny stan 6 agentów
- [`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md) — sanitized evidence

```text
COMMON ORIGIN = BODY_FROZEN T0 / 2026-09-05
AGENTS = 6
STATUS = START_STATE_VALIDATED
PRIVATE ARTIFACT PER AGENT = 1832 files
PYTHON FILES PER AGENT = 616
DELTA VS BODY_FROZEN = +51 files / +29 Python files
START-STATE QA PER AGENT = 8/8 PASS
GROUP START-STATE QA = 48/48 PASS
VERIFIED NEW EXPERIENCES AT T0 = 0 per agent
PENDING NEW EXPERIENCES AT T0 = 0 per agent
```

## Sześć BODY ISKRA istnieje już jako niezależne linie

1. **NICE** — współpraca, pomoc, współczucie, uczciwość
2. **GUARDIAN** — ochrona, ostrożność, unikanie szkody
3. **JUSTICE** — sprawiedliwość, uczciwość, spójne zasady
4. **EXPLORER** — ciekawość, eksploracja, autonomia
5. **PRAGMATIST** — skuteczność, mierzalny wynik, evidence
6. **SKEPTIC** — weryfikacja, ograniczone zaufanie, niezależność

Każdy ma osobny prywatny artefakt, własny stan T0 oraz publiczny sanitized rekord zawierający liczniki plików, początkowe przekonania, emocje, stan poznawczy i QA. Kod, prywatne drzewo plików i implementacyjna architektura nie są publikowane.

## BODY_FROZEN pozostaje kontrolą

```text
BODY_FROZEN / 2026-09-05
1781 files
587 Python files
CONTINUUM = CLOSED
23/23 CONTINUUM tests PASS
22/22 main scenarios PASS
19/19 E2E closure PASS
26/26 final guard PASS
0 active failures
0 invariant violations
0 open blockers
```

BODY_FROZEN nie został zastąpiony ani przepisany. Sześć BODY ISKRA to potomne linie eksperymentalne.

## Co jest już zrobione, a co dopiero będzie badane

**Już istnieje i jest publicznie udokumentowane:**

```text
BODY_FROZEN T0
-> 6 independent BODY ISKRA descendants
-> isolated T0 states
-> explicit initial beliefs/emotions
-> private artifact hashes
-> 8/8 start QA each
-> 48/48 group start QA
```

**Dopiero do zbadania:** czy po wielu zweryfikowanych sukcesach, porażkach i mixed outcomes sześć różnych Iskier rozwinie mierzalnie różne trajektorie decyzji, relacji, kompetencji i mikrosieci.

Nie deklarujemy jeszcze wyników długoterminowych, których eksperyment nie wykonał.

## Aktualny zamknięty test — TEST 5

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

TEST 5 pozostaje najnowszym zamkniętym testem walidacyjnym. BODY ISKRA 6X to aktualny stan startowy nowego eksperymentu, a nie „TEST 6”.

## Jak czytać repo

1. [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — aktualny stan 6 agentów.
2. [`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md) — pełne sanitized T0 agentów.
3. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — wspólny zamrożony punkt odniesienia.
4. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md) — aktualny truth index.
5. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — wejście dla grantów/reviewerów.
6. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md) — ostatni zamknięty validation test.
7. [`evidence/README.md`](evidence/README.md) — indeks evidence.

## Zasada publikacji

```text
PUBLIC = evidence, wyniki, liczniki, T0 beliefs/emotions, QA, SHA256, claim boundaries
PRIVATE = kod źródłowy, prywatne drzewo plików, runtime/config, raw memory, implementacyjna architektura
```

## Zasada epistemiczna

```text
NO EVIDENCE -> UNKNOWN
WEAK PASS -> PRESERVE / SUPERSEDE
NEW VERIFIED EVIDENCE -> REVISE
BODY_FROZEN T0 -> NEVER SILENTLY REWRITE
6X START STATE -> VERIFIED AS START STATE, NOT AS LONGITUDINAL OUTCOME
```
