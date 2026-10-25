# SSI FSE-01 — kontrola trzech VPS i usługi MultiPort / webshop

**Data:** 2026-10-25  
**Wymóg właściciela:** **SSI DIRECTOR**, pierwszy serwer z **MultiQuant/modułami**, i trzeci serwer związany z **MultiPort/webshopem** muszą być dostępne i połączone w jeden bezpieczny obieg misji SSI.  
**Status:** `THREE_NODE_CONNECTIVITY_PARTIALLY_VERIFIED / WEBSHOP_LOCATION_UNVERIFIED / END_TO_END_MISSION_PENDING`.  
**Zmiany na hostach:** **nie wykonano** w tym etapie; dokument definiuje zakres kontroli, nie wdrożenie.

## Role weryfikowane w aktualnej architekturze

| Rola | Ustalenie | Potwierdzenie |
| --- | --- | --- |
| **SSI DIRECTOR** | Nadzór misji, natywny SCC, Router V10/S10, Research Memory, Universal Lab, dostęp do serwerów modeli i MultiQuant. | Rola architektoniczna jest udokumentowana. Pełny runtime natywny SCC ↔ MultiQuant i dostęp do każdego hosta wymagają aktualnego testu. |
| **VPS MultiQuant** (historycznie alias ROBERT VPS) | Ma być właściwym punktem wejścia autorskich modułów FSE; nie omijać go przez bezpośrednie `llama-cli`. | Log z 25.10: obecne skrypty R20/R21 i Offline MICRO; jednostka tunelu modelowego aktywna, HTTP 200 przez tunel. Aktualny kanoniczny engine/adapter jeszcze niezweryfikowany. |
| **VPS CORE24 / MODELS** | 13 zarejestrowanych tagów Ollama oraz osobny GGUF 70B IQ2_XXS i backend CPU `llama.cpp`. | Log z 25.10 potwierdza model 19 097 389 632 B, binarkę w drzewie MultiQuant, API Ollama, usługi CORE24 API i worker. Nie oznacza to, że 70B obsługuje publiczne API Ollama lub że działa autorski engine. |
| **MultiPort / webshop** | Wskazany przez właściciela komponent/aplikacja do połączenia w tej samej infrastrukturze. | **Brak ustalonego z aktualnego odczytu położenia, jednostki, domeny i endpointu webshopu**. Nie przypisywać automatycznie na CORE24 ani innym VPS, dopóki nie ma audytu usługi. |

Zapis roli CORE24 jako serwera modeli wynika z wcześniejszej dokumentacji; właściciel wspomniał teraz „MultiPort, tam gdzie jest webshop”. To powiązanie **wymaga rozpoznania** i nie jest bez dowodu przypisaniem lokalizacji produktu na konkretny węzeł.

## Macierz połączeń i poziom dowodu

| Łącze | Ostatni znany stan | Co jeszcze weryfikujemy |
| --- | --- | --- |
| **MultiQuant → CORE24 / Ollama** | **PASS transport/katalog:** aktywny SSH forward, `GET /api/tags` HTTP 200; 25.10 właściciel potwierdził identyczny SHA-256 uporządkowanych list tagów i digestów z obu końców. | Uwierzytelniony tor właściwej misji; identyfikacja kanonicznego engine, adaptera i wybranego modelu 70B. |
| **DIRECTOR → CORE24 / Ollama** | Wcześniejszy historyczny raport z 20.10 opisywał aktywny tunel do lokalnego API modeli i odpowiedź o wersji. | **Ponowny odczyt aktualnego stanu 25.10**, sprawdzenie zgodności katalogu i autoryzacji. |
| **DIRECTOR → MultiQuant** | **NOT VERIFIED w tej kampanii**. | Dostępność z obu stron, istniejący kontrakt SCC/Router, auth/ACL, przekazanie misji i receipt. |
| **MultiPort/webshop ↔ DIRECTOR/MultiQuant/MODELS** | **NOT VERIFIED** — brak zidentyfikowanej usługi sklepu i jej lokalizacji. | Proces/port, health, granice bezpieczeństwa, droga zamówienie→misja i wynik→webshop. |

**Dostęp do HTTP 200 nie oznacza wykonania misji.** Odniesienie do „wszystkie serwery połączone” może być odbierane dopiero po aktualnym teście każdej wymaganej ścieżki z właściwą identyfikacją usług.

## Przyjęty przepływ produktu

`webshop / MultiPort → uwierzytelniona bramka SSI → DIRECTOR (SCC/Router) → MultiQuant (kanoniczny autorski engine) → wykonawca modelu na CORE24 → Evidence/Notariusz → DIRECTOR → odpowiedź do webshopu`.

Ruch sieciowy powinien korzystać z istniejących tuneli lub sieci prywatnej oraz uprawnień per usługa, nie z nieograniczonego otwierania API modeli w Internecie. Webshop nie powinien bezpośrednio wykonywać operacji modelowych z dostępem do wewnętrznych plików MultiQuant. Utrzymać jeden rzeczywisty punkt logowania użytkownika tam, gdzie przewiduje go projekt Universal Lab.

## Weryfikacja P1R4 — bez zmian

1. **Inwentarz trzech VPS:** SSH do każdego, tożsamość hosta i usługi systemd/kontenery; listę usług związaną z webshopem, proxy, SSI/Router/MultiQuant i Ollama; stany i porty (bez wypisywania konfiguracji, sekretów, pełnych `ExecStart` i prywatnych URL).
2. **DIRECTOR i VPS MultiQuant → CORE24:** lokalny odczyt `/api/version` oraz `/api/tags` przez istniejące tunele. Żadnego generowania w tym etapie.
3. **DIRECTOR ↔ MultiQuant:** sprawdzić łączność TCP do konkretnego, dopuszczonego portu API lub 22/tcp tylko jako test transportu. Sam TCP PASS nie stanowi akceptacji aplikacji.
4. **Webshop/MultiPort:** ustalić konkretną instalację i sprawdzić lokalny health oraz autoryzowaną trasę przez Dyrektora. Nie przyjmować, że proces typu nginx sam z siebie jest webshopem.
5. **FSE-01 mission:** po bezpiecznym preflight i rozpoznaniu engine — jeden nieprodukcyjny obieg z request ID, checkpointem, audytem użytego modelu i dowodem odpalenia MultiQuant. Dopiero potem próby wydajności 70B.

## Bramka końcowa

`NETWORK_BASIC_PASS`: wszystkie wymagane tunele i autoryzowane kanały odpowiadają.

`APP_ROUTING_PASS`: endpointy właściwych usług rozpoznane, handshake/auth, jednoznaczny routing zadania.

`E2E_SCC_MULTIQ_WEBSHOP_PASS`: prawdziwy testowy request webshopu przechodzi przez właściwy SCC/Router, autorski MultiQuant i model, a odpowiedź jest odnotowana w Evidence; nie modyfikuje rzeczywistych danych klienta.

Bez spełnienia trzech poziomów pełny system pozostaje `INTEGRATION_IN_PROGRESS`. Wcześniejszy BF16 B1 96/96 potwierdza tylko bazę modelu, nie łączność trzech serwerów ani działanie webshopu.

## Referencje

- [FSE-01 Issue #5](https://github.com/jankes72/SSI_V5/issues/5).
- [P1R2 tunel](SSI_MULTIQ_FSE01_P1R2_TUNNEL_MANAGER_INTERFACE_20261025.md).
- [P1R3 zgodność katalogu Ollama](SSI_MULTIQ_FSE01_P1R3_MODEL_INVENTORY_PARITY_OPERATOR_20261025.md).
- [Korekta routingu przez silnik MultiQuant](SSI_MULTIQ_FSE01_SERVER_ROUTING_CORRECTION_R1_20261025.md).
- [Migracja i niezamknięte bramki](../RESULTS/SSI_MIGRATION_MULTIQ_CORE_ARCHIVE_HANDOFF_R1_20261025.md).

**Granica publikacji:** bez IP/hostname rzeczywistych maszyn, tunelowych portów, kluczy, URL i sekretów, nazw kont, prywatnego kodu, surowych logów ani danych sklepu.
