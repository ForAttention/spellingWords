import win32com.client # pywin32
# import docx
import requests
from bs4 import BeautifulSoup

"""Nie sporządzam żadnej klasy pod to

Kod jest bardzo niestabilny 
Jak go testowałem to często się wysypywał 
Być może dlateo że testowałem 450 stron (tematyka - czasopisma)
i miałem z każdej średnio po 70 tyś stron A4 tekstu

Chciałbym pokazać, jak program z pliku docx sprawdza błędy, oraz jak można pobrać cały tekst ze strony 
"""


# pobieranie tekstu ze strony, celujemy głównie w paragrafy
url = "https://polonistyka.amu.edu.pl/kandydaci/slowniczek-kandydata"
file = open("stuff1.txt", "w")
requests = requests.get(url)
data = BeautifulSoup(requests.text, "lxml")
syntax = data.html.find_all("p")
# tutaj możemy dodaćj już coś co nam oddzieil część tekstu od pozostałych części (podstron)
file.write(45*"=" + "\n" + url + "\n" + 45*"=")
print("Zaczynamy wyciąganie tekstu")
for text in syntax[:]:
    try:
        file.write("\n")
        file.write(text.text)
    except Exception as error:
        print(error)
        # jest to zabezpieczenie przed zapisem jakiś nieznanych znaków
print("koniec")
file.close()


# teraz będziemy sprawdzali poprawność w pisowni wyrazów

# trzeba by plik stuf1 przepisać do stuf2.docx, ale nie piszę tego jak na razie

spelling = []
# ten path_to_file_doc jest po prostu ścieżką do naszego pliku z dokumentem Microsoft
path_to_file_doc = r"C:\sciezka\asd"
num = 0
wordapp = win32com.client.Dispatch("Word.Application")
worddoc = wordapp.Documents.Open(path_to_file_doc)
if worddoc.SpellingErrors.Cout:
    for giveme in worddoc.SpellingErrors:
        spelling.append(str(giveme))
        spelling.append("\n")
        num += 1
        print(f"Znaleziono błąd numer {num}")
    num += 1
    worddoc.ActiveWindow.Close()

"""
Na ten moment nie mam nazędzi by napisać to dalej
Myślę, że nie długo zrobię update gitaz kodem który mam przetestowany
"""
