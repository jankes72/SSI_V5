# M00 Micronetwork Migration — Reproduction / Verification

## Cel

Sprawdzić, czy wydzielony Micronetwork Engine zachowuje parity ze źródłowym modułem ROBERTA oraz czy migracja nie zmieniła persistent state.

## Minimalna kontrola hashy stanu

```bash
sha256sum /home/jankes72/Pulpit/ROBERT/data/micronetwork_state.json
sha256sum /home/jankes72/Pulpit/ROBERT/data/micronetwork_inventory.json
```

Oczekiwane hashe zapisane w `STATE_HASHES.txt`:

```text
445f826dc3bfa1b384d64bd05f2d122801f812b4a9f290abc9caf68b2da06e73
3d9e38391d68a153b3d779f81f40bad35bc454b2ad5ac88e7b4ae2cd64cbda12
```

## Kontrole migracji

W oryginalnym bundle wykonano:

- shadow parity starego i nowego mechanizmu;
- adapter ROBERTA do core;
- restart/resume;
- replay/reuse 100x;
- same-case duplicate replay;
- evidence duplicate guard 100x;
- promotion idempotency 100x;
- null/stale-reference regression;
- mechanical probe;
- NO_MATCH -> candidate smoke;
- rollback proof;
- state separation proof.

Finalny wynik znajduje się w `FINAL_VERDICT.txt`.

## Ważne ograniczenie

Pierwotny bundle M00 zawierał `SHA256SUMS.txt` w niestandardowym formacie, dlatego od kolejnych modułów wymagany jest standardowy format kompatybilny z:

```bash
sha256sum -c SHA256SUMS.txt
```

Ta wada evidence została zachowana jawnie i nie jest ukrywana.
