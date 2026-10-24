# office.py — SoFa 0 (2022)

> **Archiwum.** To repozytorium jest zamknięte i tylko do odczytu.
> Program, który z niego wyrósł, rozwija się dziś jako **SoFa3**.

## Co to jest

Pierwsza wersja programu **SoFa**: księgi intencji mszalnych i rozliczeń
księży w parafii. Powstała jesienią 2022 roku (26.10–23.11.2022, 143 commity).

To tutaj pierwszy raz zapisano w kodzie zasady, którymi SoFa liczy do dziś:

- **stypendia** (intencje mszalne) i ich średnia,
- **KOZI**, czyli potrącenia od posług (kuria, organista, zakrystian, intencja),
- **pars**, czyli podział tego, co zostaje z kancelarii,
- **kuchnia** i **obciążenia**,
- zestawienia miesięczne i ogólne.

## Co jest w środku

| Folder | Zawartość |
|---|---|
| `buisness/Computing` | obliczenia: `pars_computer`, `kozi_computer`, `statements_computer`, `tax_computer` |
| `buisness/Database` | budowa i obsługa bazy SQLite |
| `buisness/Employee`, `buisness/Income`, `buisness/Input` | księża, wpływy (stypendia, kancelaria), wprowadzanie danych |
| `gui` | zakładki okna: wpis intencji, KOZI, kancelaria, zestawienia, filtr, ustawienia |
| `tests` | pierwsze testy (pars, obliczenia, baza) |

Stan zatrzymany w trakcie pracy: `main.py` jest pusty, więc programu
w tej postaci nie da się uruchomić. Wartość tego repozytorium jest historyczna.

## Co było dalej

| Wersja | Lata | Uwagi |
|---|---|---|
| **SoFa 0** (to repozytorium) | 2022 | pierwszy kod, testy, struktura katalogów |
| **SoFa 1 / 2** | 2023–2024 | nowa historia gita, ten sam układ katalogów; program używany w parafiach (Windows) |
| **SoFa3** | od 2026 | napisana od zera na podstawie doświadczeń z SoFa 1 i 2: pieniądze jako `Decimal`, stawki z datą obowiązywania, zamykanie miesięcy, wersja webowa |

Błędy wykryte w starych wersjach (np. dzielenie przez zero w średniej,
kwoty jako `float`, rekurencja przy stawce gościa 0 zł) mają w SoFa3 testy,
które je wykluczają.

## Dane

Repozytorium nie zawiera danych parafii. Baza testowa z historii
(`tests/test.db`) miała wyłącznie dane fikcyjne.

---

*Autor: ks. Maciej Słyż.*
