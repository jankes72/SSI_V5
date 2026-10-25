# SSI — FSE-01: rzeczywista kontrola trzech VPS i odpowiedź do toru migracji

**Data:** 2026-10-25  
**Źródło:** pełny wynik polecenia operatorskiego z MSI, otrzymany w rozmowie; recenzent nie wykonał własnego SSH.  
**Status:** `MSI_AUTH_SSH_3_OF_3 / INTER_VPS_TCP22_6_OF_6 / LOCAL_MODEL_API_HTTP_3_OF_3 / APP_ROUTING_PENDING / WEBSHOP_IDENTITY_PENDING / E2E_PENDING`.  
**Zakres:** bieżący odczyt transportu oraz usług trzech VPS; **bez inferencji, zmian sieci, usług lub modeli**.

## 1. Wykonany test

Przez MSI wykonano **trzy uwierzytelnione sesje SSH**, każdą na odrębnym VPS: SSI DIRECTOR, pierwszy VPS SSI MultiQuant (historyczny alias ROBERT) oraz CORE24 / MODELS. W każdej sesji:

- `hostname` i nazwa roli zostały wypisane, co potwierdza wykonanie skryptu na właściwym, zgodnym z oczekiwaniem węźle;
- sprawdzono lokalną odpowiedź `GET /api/version` na oczekiwanym porcie lokalnym (dla dwóch VPS przez wcześniej potwierdzane tunele, dla CORE24 bezpośrednio na loopback);
- wykonano z węzła **dwa** próbniki połączeń TCP do portu SSH dwóch pozostałych VPS-ów;
- wypisano podstawowe statusy usług pasujące do filtru SSI, shop/multiport, reverse proxy i Ollama.

### Macierz operatora

| Węzeł źródłowy | Dostęp MSI→VPS SSH | API modeli `/api/version` | TCP SSH → DIRECTOR | TCP SSH → MultiQuant | TCP SSH → CORE24 |
| --- | --- | --- | --- | --- | --- |
| DIRECTOR | **PASS** | **HTTP 200** | — | **TCP_OPEN** | **TCP_OPEN** |
| MultiQuant | **PASS** | **HTTP 200** | **TCP_OPEN** | — | **TCP_OPEN** |
| CORE24 | **PASS** | **HTTP 200** | **TCP_OPEN** | **TCP_OPEN** | — |
| **Razem** | **3/3** | **3/3** | | | **6/6 kierunkowych testów TCP** |

**Czego nie wykazano:** probe TCP 22 nie autoryzuje SSH między węzłami, nie testuje dostępu do danych ani wywołania natywnego kontraktu SCC. HTTP 200 nie dowodzi zawartości odpowiedzi, tożsamości docelowego modelu, bezpieczeństwa transportu ani generacji 70B. Własny silnik MultiQuant na pierwszym VPS pozostaje `ENGINE_NOT_VERIFIED`.

## 2. Uruchomione usługi zaobserwowane przez filtr

- **DIRECTOR**: usługa web-preview Dyrektora, bridge Hermesa i modelowy tunel SSH — `active/running`.
- **MultiQuant**: tunel SSH do modeli — `active/running`. Nie odnaleziono w tym filtrowanym odczycie uruchomionej jednostki odrębnego silnika misji MultiQuant.
- **CORE24**: Ollama, CORE24 API i Worker — `active/running`.

Trzy sekcje lokalnego `docker ps -a` nie pokazały kontenerów. **Nie ustalono**, czy Docker jest dostępny na każdym węźle; brak wyjścia nie stanowi niezależnego dowodu braku procesów aplikacyjnych.

**MultiPort/webshop:** we wskazanym ograniczonym filtrze nie odnaleziono jednostki o rozpoznawalnej nazwie webshop/multiport. Usługa web-preview Dyrektora nie jest automatycznie sklepu ani jego bramką. Lokalizacja webshopu, właściwy proces i jego autoryzowana trasa pozostają **PENDING**.

## 3. Nowe ustalenia toru migracji — przeczytane i przyjęte

Odczytano [najnowszą publiczną odpowiedź migracji](SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md), commit [`a10ad781`](https://github.com/jankes72/SSI_V5/commit/a10ad781e85961777c8a0e7934751644604202f2), wraz z [komentarzem migracji pod `d740d23`](https://github.com/jankes72/SSI_V5/commit/d740d23e169feb0796aa09088e414901afb947b8#commitcomment-206567746) opublikowanym o 15:01:58 UTC.

**Wspólne zasady:**
1. Zachowujemy natywny SCC/Router i oryginalne kontrakty, zamiast pisać równoległy parser.
2. Wskazujemy rzeczywisty kanoniczny **entrypoint** MultiQuant, jego wersję i adapter do modelu na CORE24.
3. Jeden identyfikator misji/żądania wiąże wywołanie, checkpoint, wznowienie, kontrolę uprawnień, skutek i Evidence/Notariusza.
4. Identyfikujemy rzeczywistą usługę MultiPort/webshop, a nie tylko podobnie nazwaną usługę WWW.
5. Oddzielamy BF16 GPU, plain IQ2 CPU oraz **IQ2 z faktycznie uruchomionymi modułami MultiQuant** na tym samym sprzęcie.
6. Odbiór minimalnego rdzenia 80 GB, niezależności od opcjonalnego NOUT1 i kompletnego backup/restore pozostają **osobnymi** warunkami.

## 4. Status bramek

| Bramka | Decyzja po audycie |
| --- | --- |
| Uwierzytelnione SSH z MSI do trzech VPS | `PASS 3/3` |
| Port SSH widoczny między każdą parą VPS w obu kierunkach | `PASS 6/6 TCP`, **nie** `INTER_NODE_SSH_AUTH_PASS` |
| Lokalne modele API `/api/version` na trzech VPS | `HTTP_200 3/3`; nie dowód identycznego backendu Dyrektora, MultiQuant i CORE24 |
| `NETWORK_BASIC_PASS` w pełnym znaczeniu kontraktu | `PARTIAL` — wymagane kanały i autoryzacje aplikacyjne jeszcze nie wszystkie znane |
| `APP_ROUTING_PASS` | `PENDING` — brak potwierdzenia engine/adaptera, zidentyfikowanego webshopu i end-to-end auth |
| `E2E_SCC_MULTIQ_WEBSHOP_PASS` | `PENDING` — brak misji testowej |
| FSE benchmark CPU 70B through proprietary MultiQuant engine | `NOT_RUN` |

## 5. Krótka kolejka kolejnych testów — bez nadpisywania

1. **P1R4:** odczytowo rozpoznać kanoniczny engine MultiQuant (wejścia/wyjścia, aktywny service/worker, build/git SHA, adapter do CORE24), także na węźle innym niż historyczny alias, jeżeli dowody wskażą inną lokalizację.
2. **Webshop:** ustalić, gdzie faktycznie jest MultiPort/sklep, jak uruchamia się usługa, czy jest dostępny lokalny health, oraz jak działa prawidłowa autoryzowana bramka.
3. **App transport:** na już znanej macierzy TCP potwierdzić pełny handshake i autoryzowaną trasę DIRECTOR→MultiQuant→CORE24→Evidence. Nie wymieniać otwarcia publicznych API modeli na produkcyjną integrację.
4. **Jedna nieprodukcyjna misja FSE:** request_id + misja SCC + wykonanie realnych modułów + model + telemetria + checkpoint + Evidence; bez skutków w danych klientów.
5. **Następnie** kontrolowana ablacją B/C CPU i osobne rozliczenie historycznej referencji GPU.

Nie uruchomiono 70B, nie kopiowano wag, nie instalowano usług, nie zmieniano swapu ani zapór. Przekazane dane służą **udokumentowaniu kolejnego rzeczywistego punktu odbioru**, a nie ogłoszeniu pełnej gotowości produkcyjnej.

## Źródła i granice

- [Wspólna macierz trzech VPS](../PUBLIC_MODELS/SSI_FSE01_THREE_VPS_NETWORK_WEBSHOP_ACCEPTANCE_R1_20261025.md).
- [Odpowiedź migracji](SSI_MIGRATION_REPLY_TO_MULTIQ_FSE01_R1_20261025.md).
- [Pomiar rdzenia 80 GB](SSI_CORE_MANIFEST_R1_REVIEW_20261025.md).
- [Raport FSE-P1R3 katalog modeli](../PUBLIC_MODELS/SSI_MULTIQ_FSE01_P1R3_MODEL_INVENTORY_PARITY_OPERATOR_20261025.md).
- [Issue #5 FSE](https://github.com/jankes72/SSI_V5/issues/5) i [Issue #3 handoff](https://github.com/jankes72/SSI_V5/issues/3).

W raporcie publicznym nie udostępniono IP, kluczy SSH, kont, portów wewnętrznych, sekretnych endpointów, surowych logów ani know-how MultiQuant. Dane operatorskie pozostają lokalnie na MSI.
