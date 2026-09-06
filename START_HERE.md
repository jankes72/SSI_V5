# SSI V5 — START HERE

## Experimental Persistent Adaptive Intelligence System

**Autor architektury:** Paweł Jankiewicz (`jankes72`, `PROGRAMMER_ROOT`)  
**Status:** `BODY_FROZEN T0 PRESERVED / 6X BODY ISKRA START_STATE_VALIDATED / 21-EXPERIMENT PROGRAM DESIGNED / ROBERT CONTINUOUS`  
**Data aktualizacji:** `2026-09-06`  
**Wspólny punkt odniesienia:** `T0 / BODY_FROZEN / PRE-ISKRA / 2026-09-05`  
**Aktualny stan eksperymentalny:** `6 niezależnych BODY ISKRA T0 + 21 zaprojektowanych eksperymentów cross-domain`  
**ROBERT:** `ciągła linia inżynieryjna / NIE jest zerowany przez czyszczenie kopii eksperymentalnych`  
**Najnowszy zamknięty test walidacyjny:** `TEST 5 / SSI BODY FINAL CONVERGENCE / DEVELOPMENT_VALIDATED`  
**Stan AGI / świadomości:** `NIEUDOWODNIONY — BADANY EKSPERYMENTALNIE`

## Najważniejsza aktualizacja — 2026-09-06

Zamrożony BODY_FROZEN z 2026-09-05 pozostaje niezmiennym wspólnym punktem odniesienia. Z tego samego T0 istnieje już sześć niezależnych wariantów BODY ISKRA, a publicznie zapisano przed wynikami pełny program `7 x 3 = 21` eksperymentów cross-domain.

**Kluczowe rozróżnienie:** wyczyszczone/zamrożone zostały kopie eksperymentalne potrzebne do uczciwego baseline'u. Nie oznacza to wyzerowania kanonicznego ROBERTA. ROBERT zachowuje ciągłość swojej wcześniejszej linii rozwojowej, pamięci, narzędzi i kompetencji z poprzednich etapów/testów; pełna prywatna lista tych elementów nie jest publikowana w evidence-only mirror.

Publiczne wejścia:

- [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md) — zaprojektowana matryca 21 eksperymentów
- [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md) — ciągłość ROBERTA vs reset kopii eksperymentalnych
- [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — historyczny wspólny T0
- [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — aktualny stan 6 agentów
- [`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md) — sanitized evidence

## Program 21 eksperymentów — zaprojektowany przed pełnymi wynikami

Siedem linii eksperymentalnych:

```text
0 BODY_FROZEN T0
1 NICE
2 GUARDIAN
3 JUSTICE
4 EXPLORER
5 PRAGMATIST
6 SKEPTIC
```

Każda linia ma trzy eksperymenty:

```text
A = DRONY
B = HUMANOID
C = NOWA DZIEDZINA WYBRANA PRZEZ DANĄ LINIĘ SSI
```

Czyli:

```text
7 x 3 = 21 eksperymentów
STATUS = DESIGNED / EXECUTION_INITIATED / OUTCOMES_NOT_YET_CLAIMED
```

Wspólna rama pomiarowa obejmuje m.in. `KNOWN / SIMILAR / NOVEL`, decyzję Routera V10, reuse/verify/adapt/full-flow, latency, correctness, false reuse, recovery oraz powstawanie i aktualizację kompetencji.

W przypadku trzeciej domeny BODY_FROZEN wybiera ją sam dla swojej linii, a każdy BODY ISKRA 1–6 wybiera własną domenę niezależnie. Jeśli dwie linie wybiorą podobny kierunek, taki wynik ma zostać zachowany jako evidence, a nie poprawiany po fakcie.

## Sześć BODY ISKRA istnieje już jako niezależne linie

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

## ROBERT nie został wyczyszczony do T0

```text
ROBERT
= kanoniczna linia wykonawczo-inżynieryjna
+ historia TEST 1 -> TEST 5
+ zachowana ciągłość pamięci / kompetencji / narzędzi w prywatnym runtime
+ dalszy rozwój Eyes / Hands / execution

BODY_FROZEN / BODY ISKRA
= izolowane kopie eksperymentalne
+ czyszczenie/freeze tylko tam, gdzie wymaga tego protokół
+ nowe Experience liczone od kontrolowanego startu
```

Czyli:

```text
CLEAN EXPERIMENT COPY != ROBERT RESET
```

## Co jest już zrobione, a co dopiero będzie mierzone

**Już istnieje i jest publicznie udokumentowane:**

```text
BODY_FROZEN T0
-> 6 independent BODY ISKRA descendants
-> isolated T0 states
-> explicit initial beliefs/emotions
-> private artifact hashes
-> 8/8 start QA each
-> 48/48 group start QA
-> 21-experiment matrix predeclared
-> canonical ROBERT continuity explicitly separated from experimental reset
```

**W toku / do zmierzenia:** wyniki dronów, humanoida i domen wybieranych przez każdą z siedmiu linii; routing known/similar/novel; latency; false reuse; recovery; transfer i powstawanie kompetencji.

Nie deklarujemy jeszcze wyników, których pełny eksperyment nie wykonał.

## Aktualny zamknięty test — TEST 5

```text
STAGE_12 = SUPERSEDED
STAGE_13_AUDIT_RETEST = PASS
TEST5_ACCEPTANCE = 29/29 PASS
ROBERT_STABLE = 46/46 PASS
TOTAL = 524/524 PASS
OPEN_BLOCKERS = 0
```

TEST 5 pozostaje najnowszym zamkniętym testem walidacyjnym. BODY ISKRA 6X to aktualny stan startowy nowego eksperymentu, a matryca 21 eksperymentów jest programem prospektywnym, nie „TEST 6”.

## Jak czytać repo

1. [`ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md`](ROBERT_CANONICAL_CONTINUITY_VS_EXPERIMENTAL_RESET_20260906.md) — rozróżnienie ROBERT vs kopie eksperymentalne.
2. [`EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md`](EXPERIMENT_PROGRAM_21_CROSS_DOMAIN_20260906.md) — zaprojektowane 21 eksperymentów.
3. [`BODY_ISKRA_6X_T0.md`](BODY_ISKRA_6X_T0.md) — aktualny stan 6 agentów.
4. [`evidence/BODY_ISKRA_6X_T0_20260906/README.md`](evidence/BODY_ISKRA_6X_T0_20260906/README.md) — pełne sanitized T0 agentów.
5. [`BODY_FROZEN_T0_PRE_ISKRA.md`](BODY_FROZEN_T0_PRE_ISKRA.md) — wspólny zamrożony punkt odniesienia.
6. [`CURRENT_TRUTH_INDEX.md`](CURRENT_TRUTH_INDEX.md) — aktualny truth index.
7. [`START_HERE_FOR_REVIEWERS.md`](START_HERE_FOR_REVIEWERS.md) — wejście dla grantów/reviewerów.
8. [`evidence/TEST5_FINAL_CONVERGENCE_20260903.md`](evidence/TEST5_FINAL_CONVERGENCE_20260903.md) — ostatni zamknięty validation test.
9. [`evidence/README.md`](evidence/README.md) — indeks evidence.

## Zasada publikacji

```text
PUBLIC = evidence, protokoły eksperymentów, wyniki, lineage, liczniki, T0 beliefs/emotions, QA, SHA256, claim boundaries
PRIVATE = kod źródłowy, prywatne drzewo plików, raw ROBERT memory, prywatny skill inventory, runtime/config, implementacyjna architektura
```

## Zasada epistemiczna

```text
NO EVIDENCE -> UNKNOWN
WEAK PASS -> PRESERVE / SUPERSEDE
NEW VERIFIED EVIDENCE -> REVISE
BODY_FROZEN T0 -> NEVER SILENTLY REWRITE
ROBERT CONTINUITY -> DO NOT CONFUSE WITH EXPERIMENT RESET
6X START STATE -> VERIFIED AS START STATE, NOT AS LONGITUDINAL OUTCOME
21 EXPERIMENTS -> PREDECLARED PROGRAM, NOT 21 COMPLETED PASSES
```
