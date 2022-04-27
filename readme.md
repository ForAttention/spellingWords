## Opis pierwszego repozytorium
* [Poprawianie błędów](#Poprawianie-błędów)
* [O Programie](#O-programie)
* [Setup](#setup)

## Poprawianie błędów
Program poprawia błędy ortograficzne jak i literówki, można by napisać, że program nam zwraca wszystko co podkreśla Microsoft Word na czerwono.


## O programie
W programie na początku napisałem fragment kodu, który pobiera cały tekst z ```<p></p>```.
W ten sposób mogłem sprawdzić tekst bezpośrednio ze strony, wczesniej jeszcze pobierałem wszystkie podstrony w taki sposób:
```python
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

"""trzeba pobrać i tak bibliotekę lxml ale:
    - jeśli nie wybraliśmy opcji (PyCharm) ładowania zewnętrznych bibliotek to trzeba pobrać przez File > Settings.. > Project:MyProject > Python Interpreter > +
    - jeśli wybraliśmy opcję żeby jednak importowało to można z poziomu terminala pobrać ją za pomocą 'pip'
"""
all_site = []
url= "Strona do testowania"

req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
find = soup.find_all('a')

for slash_link in find:
    full_link = urljoin(url, slash_link.get('href'))
    all_site.append(full_link)

"""Teraz iterujemy wszystkie strony z listy all_site i z każdej pobieramy tekst
    Nie jest to oczywiście pełny kod, wykonuje się on raz dla podanej strony
    Nie ma usalonych wyjątków, żeby nie zbierało facebooka oraz mailto:xyz
    I wykonywania tak długo aż nie znajdzie wszystkich
    Mam nadzieję że ten kod mi się przyda jeszcze w pracy ;)"""

for x in all_site:
    "I tutaj zaczynamy kod z początku main.py gdzie w url podajemy x"
```

Tekst zapisałem w pliku o formacie .txt, nie od razu w pliku docx, na różnych maszynach występują czasem problemy ze zgodnością wersji więc jest to indywidualna sprawa każdego programisty.
Dalsza część programu działa dość niestabilnie, klient COM od win32 wymaga sporo czasu na proces.
Zauważyłem, że małe ilośći wyrazów (tak po 100) nie wywala programu, kiedy jednak jest ich ponad 700 tysięcy to program nie działał prawidłowo



## Setup
Aby zainstalować potrzebne biblioteki wykonaj polecenie w folderze projektu:
```shell
pip install -r requires
```

