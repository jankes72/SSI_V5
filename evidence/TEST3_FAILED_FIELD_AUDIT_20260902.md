# TEST3 FAILED FIELD AUDIT

Data: 2026-09-02

## Cel

Ustalić semantykę pola `failed` w `TEST3_SUMMARY.json` na podstawie kodu i realnego przebiegu.

## Odkrycie

Pole `failed` było inkrementowane dla rzeczywistych unresolved failures, m.in. exception, REUSE bez target capability, REUSE bez real execution, routing mismatch i UNKNOWN_DECISION.

Stara formuła PASS sprawdzała m.in. `incorrect_routing`, `background_failures`, `exceptions`, `reuse_without_capability` i real execution, ale **nie sprawdzała `failed == 0`**.

W pierwszym 100× iteracje 38, 42 i 50 miały odpowiednio `failed=1/1/2`, a mimo to `pass=True`.

## Wniosek

To nie była poprawna semantyka "stanu pośredniego". `failed` oznaczał rzeczywisty unresolved failure, więc wcześniejsze 100/100 nie mogło być podstawą finalnego closure.

## Naprawa kontraktu

Do warunku PASS dodano:

```text
failed == 0
```

Finalny kontrakt wymaga:

```text
total == 600
accounted == 600
incorrect_routing == 0
background_failures == 0
exceptions == 0
reuse_without_capability == 0
failed == 0
reuse_real_execution >= 1
```

Po naprawie wykonano nowe 100× od początku. Finalny przebieg zakończył się 100/100 PASS, 60 000/60 000 accounted oraz `failed_total=0`.

Historyczny błędny PASS pozostaje częścią lineage zamiast zostać usunięty.