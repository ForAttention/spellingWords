## Opis pierwszego repozytorium
* [Poprawianie błędów](#Poprawianie-błędów)
* [O Programie](#O-programie)
* [Setup](#setup)

## Poprawianie błędów
Program wykonuje sprawdzanie blędów w pliku spell.docx.  Błędy są z domyślnego języka nadanego w programie Microsoft Word.

Wykorzystuje wirtualny port COM (jako klient) systemu Windows i za pomocą jego API dokonuje otwrcia aplikacji 'Word' oraz pliku .docx.

Dzięki wykonaniu wszystkie przez API systemu Windows (win21com.client) mogę jednocześnie (tzn. za pomocą paru linijek kodu) wyciągać wyrazy, które są podkreśline przec dokument Word, przypominam tylko, że musi być ustawiony odpowiedni język w domyślnym dokumencie Word.Application


## O programie
Aby zacząć działanie, najpierw trzeba mieć pakiet Office od Microsoft na komputerze, to jest banalne ale ja akurat nie mam ;_;
Żeby korzystać z win32com trzeba najpierw pobrać odpowiednią paczkę, sporo jest 'złych' lub po prostu podstawionych, które prawodpobnie mają w sobie złośliwe oprogramowanie dlatego podam link do mojego źródła: https://github.com/mhammond/pywin32
I tak stworzę plik z requires do pobrania wszystkiego od razu z pewnymi źródłami.
Myślę, ża te metoda to dość duża i fajna sprawa, wrzucę kod który uważam, że jest poprawny. Przy najbliżeszej okazji sprawdzę go na jakiś komputerze z pakietem office.


## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```