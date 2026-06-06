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

Po zainicjowaniu aplikacji zaleca się przeprowadzenie podstawowej weryfikacji funkcjonalnej:

1. **Moduł tożsamości:** Rejestracja nowego użytkownika, logowanie do systemu oraz poprawne wylogowanie.
2. **Operacje na zadaniach:** Dodanie zadania testowego, modyfikacja jego atrybutów (np. zmiana nazwy, kategorii) oraz jego usunięcie.
3. **Nawigacja:** Przetestowanie mechanizmów wyszukiwania słownikowego oraz filtrowania wyników za pomocą dostępnych kryteriów.
4. **Integracja:** Weryfikacja poprawności generowania pliku CSV wraz z kontrolą struktury wyeksportowanych danych.
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