## Generator wartości na laboratoria z Baz Danych:

- Program generuje tabele w formacie .csv.
- Wartości są:
    - zgodne z wytycznymi
    - zawierają polskie znaki
    - zgodne z rzeczywistością
    - pozbawione błędów ortograficznych

## Instalacja

```bash
pip install factory-boy==3.2.1  
```

### Uruchomienie

```bash
python3 main.py
```
## Importowanie do Access
W otwartej bazie danych Access w menu wybieramy:

`Dane Zewnętrzne` -> `Nowe żródło danych` -> `Z pliku` -> `Plik tekstowy`
Wybieramy plik .csv i klikamy `Dalej`. Teraz możemy wybrać separator kolumn np. `Tabulacja` i szczegóły pól.

W przypadku źle zaimportowanych polskich znaków w menu wybieramy:
`Zaawansowane` -> `Kodowanie znaków` -> `Unicode (UTF-8)` 
