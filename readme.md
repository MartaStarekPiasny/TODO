# ToDo App (Django + Docker)

## 📖 Spis treści
- [Opis projektu](#opis-projektu)
- [Architektura i stos technologiczny](#architektura-i-stos-technologiczny)
- [Uruchomienie aplikacji](#uruchomienie-aplikacji)
- [Zarządzanie i Panel Administratora](#zarządzanie-i-panel-administratora)
- [Struktura projektu](#struktura-projektu)
- [Funkcjonalności](#funkcjonalności)
- [Testowanie i weryfikacja](#testowanie-i-weryfikacja)
- [Metodyka pracy i Zespół](#metodyka-pracy-i-zespół)

---

## 📝 Opis projektu

Aplikacja webowa typu ToDo stworzona przy użyciu frameworka Django, oparta na wzorcu architektonicznym **MTV (Model-Template-View)**. Narzędzie umożliwia kompleksowe zarządzanie zadaniami (CRUD), ich kategoryzację, zaawansowane filtrowanie oraz generowanie raportów do formatu CSV. Aplikacja została wyposażona w interaktywny system powiadomień informujących użytkownika o statusie realizowanych operacji.

Całość środowiska deweloperskiego i produkcyjnego została skonteneryzowana przy użyciu platformy Docker, co gwarantuje spójność działania aplikacji niezależnie od maszyny hosta, izolację zależności oraz łatwość wdrażania (Deployment).

---

## 🛠 Architektura i stos technologiczny

Projekt wykorzystuje nowoczesny stos technologiczny, zapewniający skalowalność i bezpieczeństwo:
- **Język programowania:** Python 3
- **Framework Backendowy:** Django (architektura MTV, wbudowany system ORM)
- **Baza danych:** SQLite3 (lekka relacyjna baza danych, idealna do środowiska deweloperskiego)
- **Infrastruktura i konteneryzacja:** Docker, Docker Compose
- **Frontend:** Szablony Django (Django Templates), HTML5, CSS3

---

## 🚀 Uruchomienie aplikacji

### Wymagania

- System operacyjny: Windows / macOS / Linux
- Docker  
- Docker Compose  

---

### Uruchomienie

Aby uruchomić aplikację, należy wykonać polecenie:

docker compose up --build

Aby zatrzymać działającą aplikację (kontenery), w innym oknie terminala wykonaj polecenie:

docker compose down

*Wskazówka: W pliku `docker-compose.yml` skonfigurowano mapowanie wolumenów (`- .:/app`). Oznacza to, że modyfikacje kodu wykonywane lokalnie na Twoim komputerze są natychmiast odzwierciedlane w kontenerze, bez konieczności ponownego budowania obrazu.*

---

## Dostęp do aplikacji

Po uruchomieniu aplikacja dostępna jest pod adresem:

http://127.0.0.1:8000/

---

## Działanie kontenera

Podczas uruchamiania kontenera wykonywane są następujące operacje:

- budowanie obrazu aplikacji Django  
- instalacja zależności z pliku requirements.txt  
- wykonanie migracji bazy danych  
- uruchomienie serwera aplikacji  

---

## Baza danych

W projekcie wykorzystano bazę danych SQLite.

- plik bazy danych: db.sqlite3  
- przechowywana lokalnie w projekcie  
- migracje wykonywane automatycznie przy starcie aplikacji  

---

## Struktura projektu (skrót)

todo/
│
├── tasks/                # aplikacja Django
├── todo/                 # konfiguracja projektu
├── templates/            # szablony HTML
├── static/               # pliki statyczne (CSS)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── db.sqlite3

---

## Funkcjonalności

- **Autentykacja i autoryzacja:** Bezpieczny system rejestracji, logowania oraz zarządzania sesją użytkownika.
- **Moduł zarządzania zadaniami (CRUD):** Kompleksowa obsługa cyklu życia zadań (tworzenie, odczyt, aktualizacja, usuwanie).
- **Kategoryzacja:** Możliwość elastycznego przypisywania i zarządzania kategoriami zadań, ułatwiająca organizację pracy.
- **Zaawansowane wyszukiwanie:** Mechanizmy filtrowania po atrybutach oraz wyszukiwania tekstowego na liście zadań.
- **Eksport danych:** Wbudowany generator raportów umożliwiający zrzut aktualnego zestawienia zadań do formatu CSV.
- **Powiadomienia systemowe:** Interaktywny system komunikatów (flash messages) informujący użytkownika o wynikach podjętych akcji (np. pomyślny zapis, błędy walidacji).

---

## Testowanie i weryfikacja

### Scenariusze testów manualnych (UAT)

Testowanie i weryfikacja aplikacji
1. Cel testów
Celem testów było sprawdzenie poprawności działania aplikacji internetowej służącej do zarządzania zadaniami. Weryfikacja objęła podstawowe funkcjonalności systemu, takie jak rejestracja i logowanie użytkownika, zarządzanie zadaniami, obsługa kategorii, wyszukiwanie, filtrowanie, eksport danych do pliku CSV oraz działanie komunikatów systemowych.
Testy miały charakter manualny i zostały przeprowadzone z perspektywy użytkownika końcowego. Ich zadaniem było potwierdzenie, że aplikacja działa zgodnie z założeniami funkcjonalnymi oraz że interfejs jest czytelny i możliwy do obsługi w typowych scenariuszach użycia.

2. Zakres testów
Zakres testów obejmował następujące obszary aplikacji:
1.	Moduł tożsamości użytkownika
o	rejestracja nowego użytkownika,
o	logowanie do systemu,
o	wylogowanie z systemu,
o	kontrola dostępu do funkcji dostępnych tylko dla zalogowanego użytkownika.
2.	Moduł zarządzania zadaniami
o	dodawanie nowego zadania,
o	wyświetlanie listy zadań,
o	edycja istniejącego zadania,
o	zmiana nazwy, kategorii i innych atrybutów zadania,
o	usuwanie zadania.
3.	Kategoryzacja zadań
o	przypisanie zadania do kategorii,
o	filtrowanie zadań według kategorii,
o	sprawdzenie poprawnego prezentowania kategorii na liście zadań.
4.	Wyszukiwanie i filtrowanie
o	wyszukiwanie zadań po nazwie lub fragmencie tekstu,
o	filtrowanie wyników według dostępnych kryteriów,
o	sprawdzenie zachowania aplikacji w przypadku braku wyników.
5.	Eksport danych do CSV
o	wygenerowanie pliku CSV,
o	kontrola struktury pliku,
o	sprawdzenie zgodności danych w pliku z danymi widocznymi w aplikacji.
6.	Interfejs użytkownika
o	czytelność formularzy,
o	poprawność komunikatów systemowych,
o	responsywność widoku na różnych szerokościach ekranu,
o	ogólna wygoda obsługi aplikacji.

3. Środowisko testowe
Testy zostały przeprowadzone lokalnie po uruchomieniu aplikacji Django. Struktura projektu obejmowała między innymi:
•	katalog tasks zawierający główną aplikację Django,
•	katalog todo zawierający konfigurację projektu,
•	katalog templates zawierający szablony HTML,
•	katalog static zawierający pliki statyczne, w tym style CSS,
•	plik Dockerfile,
•	plik docker-compose.yml,
•	plik requirements.txt,
•	bazę danych db.sqlite3.
Aplikacja została uruchomiona w środowisku lokalnym. Do testów wykorzystano przeglądarkę internetową oraz przykładowe dane testowe wprowadzane ręcznie przez użytkownika.

4. Dane testowe
Na potrzeby testów wykorzystano przykładowe dane:
Użytkownik testowy:
•	nazwa użytkownika: testuser
•	hasło: Test12345
•	adres e-mail: testuser@example.com
Przykładowe zadanie testowe:
•	nazwa zadania: Przygotować dokumentację projektu
•	opis: Opis zadania testowego do weryfikacji działania aplikacji
•	kategoria: Studia
•	status: Do wykonania
Zmodyfikowane dane zadania:
•	nowa nazwa zadania: Przygotować dokumentację końcową projektu
•	nowa kategoria: Projekt
•	status: W trakcie

5. Scenariusze testów manualnych UAT
Scenariusz 1: Rejestracja nowego użytkownika
Cel testu:
Sprawdzenie, czy użytkownik może poprawnie utworzyć nowe konto w aplikacji.
Warunki początkowe:
Użytkownik nie jest zalogowany. Aplikacja jest uruchomiona.
Kroki testowe:
1.	Otworzyć stronę aplikacji w przeglądarce.
2.	Przejść do formularza rejestracji.
3.	Wprowadzić nazwę użytkownika, adres e-mail oraz hasło.
4.	Potwierdzić rejestrację.
5.	Sprawdzić, czy aplikacja przekierowuje użytkownika do właściwego widoku.
6.	Zweryfikować, czy pojawia się komunikat o poprawnej rejestracji.
Oczekiwany rezultat:
Konto użytkownika zostaje utworzone. System informuje użytkownika o poprawnej rejestracji i umożliwia dalsze korzystanie z aplikacji.
Status testu:
Pozytywny, jeżeli konto zostanie utworzone, a użytkownik może się zalogować.

Scenariusz 2: Logowanie użytkownika
Cel testu:
Sprawdzenie, czy zarejestrowany użytkownik może zalogować się do systemu.
Warunki początkowe:
Użytkownik posiada aktywne konto w aplikacji.
Kroki testowe:
1.	Otworzyć stronę logowania.
2.	Wprowadzić poprawną nazwę użytkownika i hasło.
3.	Kliknąć przycisk logowania.
4.	Sprawdzić, czy użytkownik zostaje przekierowany do listy zadań lub panelu głównego.
5.	Zweryfikować, czy dostępne są funkcje przeznaczone dla zalogowanego użytkownika.
Oczekiwany rezultat:
Użytkownik zostaje poprawnie zalogowany. Aplikacja udostępnia funkcje zarządzania zadaniami.
Status testu:
Pozytywny, jeżeli logowanie przebiega bez błędów, a użytkownik widzi swoje zadania.

Scenariusz 3: Próba logowania błędnymi danymi
Cel testu:
Sprawdzenie, czy aplikacja prawidłowo reaguje na niepoprawne dane logowania.
Warunki początkowe:
Użytkownik znajduje się na stronie logowania.
Kroki testowe:
1.	Wprowadzić niepoprawną nazwę użytkownika lub błędne hasło.
2.	Kliknąć przycisk logowania.
3.	Sprawdzić, czy użytkownik nie zostaje zalogowany.
4.	Zweryfikować, czy pojawia się komunikat o błędnych danych.
Oczekiwany rezultat:
System nie powinien dopuścić do logowania. Powinien wyświetlić komunikat informujący o niepoprawnych danych logowania.
Status testu:
Pozytywny, jeżeli aplikacja blokuje niepoprawne logowanie.

Scenariusz 4: Wylogowanie użytkownika
Cel testu:
Sprawdzenie, czy użytkownik może poprawnie zakończyć sesję.
Warunki początkowe:
Użytkownik jest zalogowany.
Kroki testowe:
1.	Kliknąć przycisk lub link wylogowania.
2.	Sprawdzić, czy użytkownik zostaje przekierowany do strony logowania lub strony głównej.
3.	Spróbować wejść bezpośrednio na adres listy zadań.
4.	Zweryfikować, czy dostęp do chronionych zasobów jest zablokowany.
Oczekiwany rezultat:
Użytkownik zostaje wylogowany, a dostęp do funkcji wymagających autoryzacji zostaje zablokowany.
Status testu:
Pozytywny, jeżeli po wylogowaniu użytkownik nie ma dostępu do prywatnych danych.

Scenariusz 5: Dodanie nowego zadania
Cel testu:
Sprawdzenie, czy użytkownik może utworzyć nowe zadanie.
Warunki początkowe:
Użytkownik jest zalogowany.
Kroki testowe:
1.	Przejść do widoku dodawania zadania.
2.	Wprowadzić nazwę zadania.
3.	Uzupełnić opis zadania.
4.	Wybrać kategorię.
5.	Ustawić status zadania.
6.	Zapisać formularz.
7.	Sprawdzić, czy nowe zadanie pojawiło się na liście zadań.
Oczekiwany rezultat:
Nowe zadanie zostaje zapisane w bazie danych i wyświetlone na liście zadań użytkownika.
Status testu:
Pozytywny, jeżeli zadanie pojawia się na liście i zawiera poprawnie zapisane dane.

Scenariusz 6: Walidacja formularza dodawania zadania
Cel testu:
Sprawdzenie, czy aplikacja poprawnie obsługuje brak wymaganych danych.
Warunki początkowe:
Użytkownik jest zalogowany i znajduje się w formularzu dodawania zadania.
Kroki testowe:
1.	Pozostawić wymagane pole, np. nazwę zadania, puste.
2.	Kliknąć przycisk zapisu.
3.	Sprawdzić, czy zadanie nie zostaje zapisane.
4.	Zweryfikować, czy pojawia się komunikat walidacyjny.
Oczekiwany rezultat:
System nie powinien zapisać niekompletnego formularza. Użytkownik powinien otrzymać informację o konieczności uzupełnienia wymaganych danych.
Status testu:
Pozytywny, jeżeli aplikacja blokuje zapis niepoprawnych danych.

Scenariusz 7: Edycja istniejącego zadania
Cel testu:
Sprawdzenie, czy użytkownik może zmienić dane istniejącego zadania.
Warunki początkowe:
Użytkownik jest zalogowany i posiada co najmniej jedno zadanie na liście.
Kroki testowe:
1.	Otworzyć listę zadań.
2.	Wybrać zadanie do edycji.
3.	Kliknąć opcję edycji.
4.	Zmienić nazwę zadania.
5.	Zmienić kategorię zadania.
6.	Zmienić status zadania.
7.	Zapisać formularz.
8.	Sprawdzić, czy lista zadań prezentuje zaktualizowane dane.
Oczekiwany rezultat:
Zmiany zostają zapisane i są widoczne na liście zadań oraz w szczegółach zadania.
Status testu:
Pozytywny, jeżeli edycja zadania działa poprawnie.

Scenariusz 8: Usunięcie zadania
Cel testu:
Sprawdzenie, czy użytkownik może usunąć zadanie.
Warunki początkowe:
Użytkownik jest zalogowany i posiada przynajmniej jedno zadanie.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Wybrać zadanie przeznaczone do usunięcia.
3.	Kliknąć opcję usunięcia.
4.	Potwierdzić operację, jeżeli aplikacja wymaga potwierdzenia.
5.	Sprawdzić, czy zadanie zostało usunięte z listy.
Oczekiwany rezultat:
Zadanie zostaje usunięte i nie jest już widoczne na liście zadań.
Status testu:
Pozytywny, jeżeli zadanie znika z listy po wykonaniu operacji.

Scenariusz 9: Filtrowanie zadań według kategorii
Cel testu:
Sprawdzenie, czy aplikacja poprawnie filtruje zadania na podstawie wybranej kategorii.
Warunki początkowe:
Użytkownik jest zalogowany i posiada zadania przypisane do różnych kategorii.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Wybrać jedną z dostępnych kategorii.
3.	Uruchomić filtrowanie.
4.	Sprawdzić, czy na liście widoczne są tylko zadania należące do wybranej kategorii.
5.	Zmienić kategorię i ponownie sprawdzić wyniki.
Oczekiwany rezultat:
Lista zadań powinna zostać ograniczona do pozycji spełniających wybrane kryterium kategorii.
Status testu:
Pozytywny, jeżeli filtrowanie działa zgodnie z wybraną kategorią.

Scenariusz 10: Wyszukiwanie tekstowe zadań
Cel testu:
Sprawdzenie działania mechanizmu wyszukiwania zadań po nazwie lub fragmencie tekstu.
Warunki początkowe:
Użytkownik jest zalogowany i posiada kilka zadań o różnych nazwach.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Wpisać w pole wyszukiwania fragment nazwy istniejącego zadania.
3.	Uruchomić wyszukiwanie.
4.	Sprawdzić, czy aplikacja wyświetla pasujące wyniki.
5.	Wpisać frazę, która nie występuje w żadnym zadaniu.
6.	Sprawdzić reakcję systemu.
Oczekiwany rezultat:
System powinien wyświetlać zadania zgodne z wpisaną frazą. W przypadku braku wyników powinien pokazać pustą listę lub odpowiedni komunikat.
Status testu:
Pozytywny, jeżeli wyniki wyszukiwania są zgodne z wpisaną frazą.

Scenariusz 11: Jednoczesne wyszukiwanie i filtrowanie
Cel testu:
Sprawdzenie, czy aplikacja poprawnie obsługuje jednoczesne użycie kilku kryteriów.
Warunki początkowe:
Użytkownik jest zalogowany i posiada zadania różniące się nazwą, kategorią oraz statusem.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Wpisać fragment nazwy zadania.
3.	Wybrać kategorię.
4.	Uruchomić filtrowanie.
5.	Sprawdzić, czy wyniki spełniają oba kryteria.
6.	Zmienić jedno z kryteriów i ponownie sprawdzić wyniki.
Oczekiwany rezultat:
Aplikacja powinna wyświetlić tylko te zadania, które spełniają wszystkie wskazane kryteria.
Status testu:
Pozytywny, jeżeli mechanizm wyszukiwania i filtrowania działa łącznie.

Scenariusz 12: Eksport listy zadań do pliku CSV
Cel testu:
Sprawdzenie poprawności generowania pliku CSV z listą zadań.
Warunki początkowe:
Użytkownik jest zalogowany i posiada co najmniej jedno zadanie.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Kliknąć opcję eksportu danych do CSV.
3.	Pobrać wygenerowany plik.
4.	Otworzyć plik w edytorze tekstowym lub arkuszu kalkulacyjnym.
5.	Sprawdzić, czy plik zawiera nagłówki kolumn.
6.	Sprawdzić, czy dane w pliku odpowiadają danym widocznym w aplikacji.
Oczekiwany rezultat:
Aplikacja generuje plik CSV zawierający aktualną listę zadań. Struktura pliku jest poprawna, a dane są zgodne z danymi zapisanymi w systemie.
Przykładowa oczekiwana struktura pliku CSV:
Nazwa zadania,Opis,Kategoria,Status,Data utworzenia
Przygotować dokumentację końcową projektu,Opis zadania testowego,Projekt,W trakcie,2026-06-06
Status testu:
Pozytywny, jeżeli plik CSV zostaje poprawnie pobrany i zawiera kompletne dane.

Scenariusz 13: Eksport przefiltrowanych danych do CSV
Cel testu:
Sprawdzenie, czy eksport CSV uwzględnia aktualnie zastosowane filtry.
Warunki początkowe:
Użytkownik jest zalogowany i posiada zadania w kilku kategoriach.
Kroki testowe:
1.	Przejść do listy zadań.
2.	Zastosować filtr, np. kategorię Projekt.
3.	Sprawdzić, czy lista pokazuje tylko wybrane zadania.
4.	Kliknąć eksport do CSV.
5.	Otworzyć pobrany plik.
6.	Sprawdzić, czy plik zawiera tylko dane zgodne z zastosowanym filtrem.
Oczekiwany rezultat:
Plik CSV powinien zawierać wyłącznie dane odpowiadające aktualnie wyświetlanej liście zadań, jeżeli taka logika została przewidziana w aplikacji.
Status testu:
Pozytywny, jeżeli eksport jest zgodny z aktualnym widokiem danych.

Scenariusz 14: Komunikaty systemowe
Cel testu:
Sprawdzenie, czy aplikacja wyświetla czytelne komunikaty po wykonaniu akcji użytkownika.
Warunki początkowe:
Użytkownik jest zalogowany.
Kroki testowe:
1.	Dodać nowe zadanie.
2.	Sprawdzić, czy pojawia się komunikat o pomyślnym dodaniu.
3.	Edytować zadanie.
4.	Sprawdzić, czy pojawia się komunikat o zapisaniu zmian.
5.	Usunąć zadanie.
6.	Sprawdzić, czy pojawia się komunikat o usunięciu.
7.	Wykonać błędną akcję, np. wysłać pusty formularz.
8.	Sprawdzić, czy pojawia się komunikat błędu.
Oczekiwany rezultat:
Aplikacja powinna informować użytkownika o rezultacie wykonanych działań. Komunikaty powinny być widoczne, zrozumiałe i jednoznaczne.
Status testu:
Pozytywny, jeżeli komunikaty pojawiają się po najważniejszych akcjach i są czytelne.

Scenariusz 15: Responsywność interfejsu użytkownika
Cel testu:
Sprawdzenie, czy aplikacja poprawnie wyświetla się na różnych rozdzielczościach ekranu.
Warunki początkowe:
Aplikacja jest uruchomiona w przeglądarce.
Kroki testowe:
1.	Otworzyć aplikację na ekranie komputera.
2.	Sprawdzić widok listy zadań, formularzy i przycisków.
3.	Zmniejszyć szerokość okna przeglądarki.
4.	Sprawdzić, czy elementy interfejsu pozostają czytelne.
5.	Uruchomić tryb podglądu mobilnego w narzędziach deweloperskich przeglądarki.
6.	Zweryfikować, czy formularze, przyciski i lista zadań są nadal możliwe do obsługi.
Oczekiwany rezultat:
Interfejs powinien być czytelny, a najważniejsze funkcje powinny pozostać dostępne na różnych szerokościach ekranu.
Status testu:
Pozytywny, jeżeli aplikacja zachowuje podstawową użyteczność na widoku desktopowym i mobilnym.

Scenariusz 16: Kontrola dostępu do danych użytkownika
Cel testu:
Sprawdzenie, czy użytkownik widzi tylko własne zadania.
Warunki początkowe:
W systemie istnieją co najmniej dwa konta użytkowników.
Kroki testowe:
1.	Zalogować się jako pierwszy użytkownik.
2.	Dodać kilka zadań.
3.	Wylogować się.
4.	Zalogować się jako drugi użytkownik.
5.	Sprawdzić listę zadań.
6.	Zweryfikować, czy zadania pierwszego użytkownika nie są widoczne.
Oczekiwany rezultat:
Każdy użytkownik powinien mieć dostęp wyłącznie do własnych zadań. Dane innych użytkowników nie powinny być widoczne.
Status testu:
Pozytywny, jeżeli aplikacja poprawnie separuje dane użytkowników.

6. Tabela przypadków testowych
ID testu	Obszar	Opis testu	Oczekiwany rezultat	Status
T01	Rejestracja	Utworzenie nowego konta użytkownika	Konto zostaje poprawnie utworzone	Pozytywny
T02	Logowanie	Logowanie poprawnymi danymi	Użytkownik uzyskuje dostęp do aplikacji	Pozytywny
T03	Logowanie	Logowanie błędnymi danymi	System blokuje dostęp	Pozytywny
T04	Sesja	Wylogowanie użytkownika	Sesja zostaje zakończona	Pozytywny
T05	Zadania	Dodanie nowego zadania	Zadanie pojawia się na liście	Pozytywny
T06	Zadania	Walidacja pustego formularza	System wyświetla komunikat błędu	Pozytywny
T07	Zadania	Edycja zadania	Dane zadania zostają zaktualizowane	Pozytywny
T08	Zadania	Usunięcie zadania	Zadanie zostaje usunięte z listy	Pozytywny
T09	Kategorie	Filtrowanie po kategorii	Lista pokazuje zadania z wybranej kategorii	Pozytywny
T10	Wyszukiwanie	Wyszukiwanie po fragmencie nazwy	System pokazuje pasujące zadania	Pozytywny
T11	Wyszukiwanie	Brak wyników dla frazy	System pokazuje pustą listę lub komunikat	Pozytywny
T12	Eksport CSV	Pobranie pliku CSV	Plik zostaje wygenerowany	Pozytywny
T13	Eksport CSV	Kontrola struktury pliku CSV	Plik zawiera poprawne kolumny i dane	Pozytywny
T14	UI	Sprawdzenie komunikatów systemowych	Komunikaty są widoczne i czytelne	Pozytywny
T15	UI	Sprawdzenie responsywności	Interfejs działa na różnych szerokościach ekranu	Pozytywny
T16	Bezpieczeństwo	Separacja danych użytkowników	Użytkownik widzi tylko swoje zadania	Pozytywny

7. Kryteria akceptacji
Aplikację można uznać za poprawnie działającą, jeżeli spełnia następujące kryteria:
1.	Użytkownik może utworzyć konto, zalogować się i wylogować.
2.	Dostęp do listy zadań wymaga zalogowania.
3.	Użytkownik może dodawać, edytować i usuwać zadania.
4.	Zadania są poprawnie zapisywane w bazie danych.
5.	Użytkownik może przypisywać zadania do kategorii.
6.	Mechanizmy wyszukiwania i filtrowania zwracają poprawne wyniki.
7.	Eksport CSV generuje plik o poprawnej strukturze.
8.	Dane w pliku CSV są zgodne z danymi widocznymi w aplikacji.
9.	Komunikaty systemowe są widoczne i zrozumiałe.
10.	Interfejs pozostaje czytelny na różnych rozdzielczościach ekranu.
11.	Użytkownik nie ma dostępu do danych innych użytkowników.

8. Wyniki testów
Przeprowadzone testy manualne potwierdziły poprawne działanie podstawowych funkcjonalności aplikacji. Rejestracja, logowanie oraz wylogowanie użytkownika działały zgodnie z oczekiwaniami. Moduł zarządzania zadaniami umożliwiał tworzenie, edycję oraz usuwanie zadań. Mechanizmy wyszukiwania i filtrowania pozwalały na zawężenie listy zadań według wskazanych kryteriów.
Poprawnie działał również eksport danych do pliku CSV. Wygenerowany plik zawierał dane zgodne z informacjami prezentowanymi w aplikacji. Komunikaty systemowe informowały użytkownika o rezultatach wykonanych operacji, takich jak zapisanie zadania, edycja, usunięcie lub wystąpienie błędu walidacji.
Weryfikacja interfejsu użytkownika wykazała, że aplikacja jest czytelna i możliwa do obsługi. Formularze oraz przyciski były rozmieszczone w sposób zrozumiały, a podstawowe funkcje były dostępne z poziomu widoku użytkownika.

9. Wnioski z testów
Na podstawie przeprowadzonych testów można stwierdzić, że aplikacja spełnia podstawowe wymagania funkcjonalne określone dla systemu zarządzania zadaniami. Najważniejsze procesy użytkownika, takie jak rejestracja, logowanie, obsługa zadań, filtrowanie, wyszukiwanie oraz eksport danych, działają poprawnie.
Testy manualne UAT pozwoliły potwierdzić, że aplikacja jest gotowa do podstawowego wykorzystania przez użytkownika końcowego. Jednocześnie w przyszłości możliwe byłoby rozszerzenie procesu testowania o testy automatyczne, testy jednostkowe oraz testy integracyjne, które pozwoliłyby na szybsze wykrywanie błędów podczas dalszego rozwoju aplikacji.

5. **Interfejs:** Sprawdzenie responsywności interfejsu (UI) oraz widoczności i czytelności powiadomień systemowych.

---

## Autor

Projekt wykonany w ramach nauki pracy z metodyką Scrum. 

1. Uladzislau Beliakou
2. Patryk Bieniaszek
3. Mirosław Kitowski
4. Daria Panchenko
5. Łukasz Rosicki
6. Marta Starek-Piasny
7. Ryszard Wasilewski

## 11. Dokumentacja graficzna (UML)

### Diagram klas
![Diagram klas](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/lukaszrosicki/TODO/blob/main/diagram_klas.puml)

### Diagram przypadków użycia
![Diagram przypadków użycia](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/lukaszrosicki/TODO/blob/main/diagram_przypadkow_uzycia.puml)

### Schemat bazy danych
![Schemat bazy danych](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/lukaszrosicki/TODO/blob/main/schemat_bazy.puml)
