# SSI V5 — Public Evidence Index

Ten katalog zawiera publiczne artefakty evidence dla najważniejszych etapów przed T0.

Zasada: README opisuje hipotezy, architekturę i interpretację; pliki w `evidence/` mają pokazywać surowe lub możliwie bezpośrednie wyniki maszynowe, root cause, hashe, snapshoty oraz instrukcje reprodukcji.

## Dostępne zestawy

### `robert_600x/`
Evidence dla naprawy i stress-testu idempotency/replay/restart ROBERTA przed migracją do neutralnego core.

Zawiera:
- finalny wynik 600X;
- root cause duplikacji i `NoneType.get`;
- raw torture results dla promotion/replay/retry/restart/null/concurrency;
- snapshoty stanu BEFORE/AFTER;
- jawnie zachowaną rozbieżność `5 vs 6 challengers`.

### `organism_core_m00_micronetworks/`
Evidence pierwszej kontrolowanej migracji Micronetwork Engine z ROBERTA do neutralnego `SSI ORGANISM CORE`.

Zawiera:
- final verdict;
- state hashes BEFORE/AFTER;
- state separation proof;
- rollback proof;
- zasady reprodukcji/parity.

### `PRE_T0_LAYERED_SELF_DEVELOPMENT_AND_INFRASTRUCTURE_PROTOCOL_20260830.md`
Protokół porządkujący aktualny eksperyment warstwowy ROBERTA i kolejne porównania PRE-T0.

Opisuje:
- baseline uproszczonego ROBERTA;
- pomiar czasu, błędów, retry, model switching, LEGO rebuilds i checkpoint returns;
- śledzenie skilli, mikrosieci oraz `candidate -> challenger -> champion`;
- porównania `baseline -> kolejna capability layer -> ponowny pomiar`;
- Hello World i Tetris jako kontrolowane zadania wykonawcze;
- Eyes/Hands jako osobny eksperyment wymagający własnego machine evidence;
- Technology Memory / External Technology Knowledge Store;
- uczenie wzorców samorozwoju przez LEGO i champion lifecycle;
- rolę Tailscale jako warstwy przenośności między lokalnymi węzłami i przyszłymi serwerami;
- drogę `single execution -> multi-worker -> multi-CONTINUUM -> distributed infrastructure`;
- ekonomiczny wzrost realnych capability SSI poprzez compute, storage i infrastrukturę;
- granicę między publicznym evidence a prywatną implementacją.

## Ograniczenia

Publiczny evidence mirror nie zawiera sekretów, API keys, tokenów, prywatnych danych ani pełnego prywatnego runtime. Publikowane artefakty mają umożliwiać kontrolę twierdzeń bez ujawniania wrażliwych danych.

## Reguła metodologiczna

```text
CLAIM
-> PUBLIC EVIDENCE POINTER
-> REPRODUCTION / CHECK
-> RESULT
```

Jeżeli evidence jest niepełne albo zawiera niespójność, jest to zapisywane jawnie zamiast wygładzane retrospektywnie.
