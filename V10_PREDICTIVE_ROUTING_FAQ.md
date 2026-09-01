# V10 Predictive Routing — Reviewer FAQ

## Czy V10 jest tylko routerem lub cache'em?

Nie. V10 zawiera warstwę predykcyjnego dopasowania, która ocenia, czy bieżące wejście odpowiada wcześniej zwalidowanej kompetencji oraz z jakim poziomem confidence system powinien ją wykorzystać.

```text
INPUT
-> PREDICTIVE MATCH / ROUTE ESTIMATION
-> CONFIDENCE
   -> HIGH   -> REUSE_TOP1
   -> MEDIUM -> VERIFY_TOPK
   -> LOW / UNKNOWN / CONFLICT -> FULL_FLOW
```

Exact-cache jest tylko jedną z możliwych ścieżek. W Test 3 zanotowano 100 exact hits, ale również 434 similarity hits oraz 133 route compilations.

## Co dokładnie przewiduje V10?

Na poziomie architektonicznym V10 przewiduje, czy istniejąca zwalidowana kompetencja jest odpowiednim kandydatem dla aktualnego problemu i jak bezpiecznie ją wykorzystać. Wynikiem nie musi być bezpośredni reuse — system może wybrać dodatkową weryfikację albo pełny flow.

## Dlaczego prediction jest ważne dla mikrosieci?

Mikrosieć odpowiada za persistent competence i jej lifecycle. V10 odpowiada za dostęp do tej kompetencji.

```text
MICRONETWORK
= validated evolving competence

V10
= predictive competence access
+ confidence gate
+ route selection
+ feedback / route update
```

Bez warstwy predykcyjnej system musiałby albo wykonywać pełny flow dla każdego problemu, albo ryzykować ślepe ponowne użycie wcześniejszych rezultatów.

## Czy V10 chroni przed false reuse?

Takie jest jego założenie architektoniczne: confidence gate ma ograniczać użycie wcześniejszej kompetencji wtedy, gdy dopasowanie jest niewystarczające lub konfliktowe.

To jednak nie oznacza, że problem false reuse został już uniwersalnie rozwiązany. Obecny publiczny Test 3 pokazał poprawne zachowanie dla badanego zakresu, ale nie zawierał dostatecznie szerokiej populacji przypadków unknown/conflicting/adversarial wymuszających FULL_FLOW.

## Jakie evidence jest już publiczne?

Test 3 zarejestrował:

```text
lookups:             600
cache_exact_hits:    100
similarity_hits:     434
route_compilations:  133
REUSE_TOP1:          534
VERIFY_TOPK:          66
fallback_count:        0
errors:                0
known correctness: 100/100
```

Interpretacja jest ograniczona do badanego przebiegu. Liczby pokazują, że V10 korzystał nie tylko z exact lookup, lecz także z similarity-based routing i selektywnej weryfikacji.

## Jaki test jest teraz najważniejszy?

Najważniejsza jest walidacja jakości predykcji, nie kolejny sam rekord czasu:

```text
KNOWN -> REUSE_TOP1
AMBIGUOUS -> VERIFY_TOPK
UNKNOWN -> FULL_FLOW
DECEPTIVELY SIMILAR / CONFLICTING -> NO FALSE REUSE -> FULL_FLOW
```

Należy mierzyć m.in. false-reuse rate, false-escalation rate, routing precision/recall i calibration confidence.

## Czy ta dokumentacja ujawnia kod V10?

Nie. Publiczna dokumentacja opisuje kontrakt, zachowanie, wyniki i granice twierdzeń. Wewnętrzna implementacja predyktora oraz prywatny silnik mikrosieci nie muszą być publikowane, aby recenzent mógł ocenić hipotezę badawczą i evidence.
