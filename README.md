# Recruitment-task

Moje rozwiązanie zadania rekrutacyjnego na stanowisko stażysty Python Developer

## Instalacja

Do uruchomienia programu należy wykorzystać zewnętrzne biblioteki [Click](https://click.palletsprojects.com/en/7.x/),  [requests](https://realpython.com/python-requests/) oraz do uruchomienia testów [pytest](https://docs.pytest.org/en/stable/getting-started.html). Metody ich instalacji znajdują się na oficjalnych stronach internetowych. W zależności od systemu operacyjnego, uruchamianie programów może zaczynać się od `py`, `python`, lub `python3`.

### Pobranie projektu

Do pobrania tego repozytorium można wykorzystać komendę 
```
git clone https://github.com/mateuszgrzelak/recruitment-task.git
```

### Uruchomienie 

Aby skorzystać z komend dostępnych w programie nalezy w interpreterze poleceń przejść do pobranego projektu oraz utworzyć bazę danych za pomocą komendy `py script.py -ltdb [number]`, gdzie argument *number* odpowiada za ilość danych pobranych z API https://randomuser.me/. Po wykonaniu wyżej wymienionej komendy w folderze pojawi się plik o nazwie *data.db*, na którym można wykonać poniższe operacje.

## Dostępne komendy:

Przed wywołaniem każdej komendy należy dodac na początku `py script.py`

<table>
 <th>Komenda</th>
 <th>Skrócona wersja</th>
 <th>Parametr</th>
 <th>Opis</th>
 <tr>
  <td>--load-random-users</td>
  <td>-lru</td>
  <td>Integer</td>
  <td>Pobiera dane z API i zapisuje do bazy danych o nazwie<i> data.db</i></td>
 <tr>
 <tr>
  <td>--gender-percentage</td>
  <td>-gp</td>
  <td>[male|female]</td>
  <td>Wyświetla procent mężczyzn lub kobiet</td>
 <tr>
 <tr>
  <td>--average-age</td>
  <td>-aa</td>
  <td>[male|female|all]</td>
  <td>Wyświetla średni wiek mężczyzn, kobiet lub kobiet+mężczyzn</td>
 <tr>
 <tr>
  <td>--most-common-cities</td>
  <td>-mcc</td>
  <td>Integer</td>
  <td>Wyświetla [liczba] najczęściej pojawiających się miast</td>
 <tr>
 <tr>
  <td>--most-common-pass</td>
  <td>-mcp</td>
  <td>Integer</td>
  <td>Wyświetla [liczba] najczęściej pojawiających się haseł</td>
 <tr>
 <tr>
  <td>--users-born-between-dates</td>
  <td>-ubbd</td>
  <td>Text Text</td>
  <td>Przyjmuje dwa argumenty w formacie YYYY-MM-DD i zwraca ilość osób urodzonych w podanym przedziale</td>
 <tr>
 <tr>
  <td>--most-secure-pass</td>
  <td>-msp</td>
  <td></td>
  <td>Zwraca najbezpieczniejsze hasło wyliczone na podstawie określonego rankingu </td>
 <tr>
</table>

## Testy

W celu uruchomienia testów jednostkowych należy przejść w interpreterze poleceń do podkatalogu *test* i uruchomić komendę 
```
py -m pytest test_unit_operations_db.py
```
Aby uruchomić testy integracyjne należy w podkatalogu *test* uruchomić komendę
```
py -m pytest test_integration_operations_db.py
```
Testy te wykorzystują testową bazę danych o nazwie *data_test.db*

## Zalożenia

W trakcie pisania programu pojawiły się następujące pytania, jednak ze względu, że jest to "tylko" zadanie rekrutacyjne postanowiłem nie zabierać czasu rekruterom:

- W jakim języku powinien być interfejs poleceń. Wybrałem język angielski
- Czy osoba urodzona 29 lutego w roku przestępnym obchodzi urodziny w roku, który nie jest przestępny 28 lutego czy 1 marca, czy może obchodzi urodziny co 4 lata. Obliczając ilość dni do urodzin założyłem że obchodzi je 28 lutego.
- W przypadku gdy ilośc wystąpień najbardziej popularnych miast lub haseł jest większa niż podany argument ograniczający ich ilość, jaką formę sortowania zastosować.