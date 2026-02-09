# YourHub - Aplikacja do zarządzania czasem i zadaniami

**Autor:** Tomasz Falkiewicz  
**Przedmiot:** Wstęp do Programowania  
**Temat:** Aplikacja typu "To-Do List" z panelem webowym i CLI.

---

## 📋 Opis Projektu
YourHub to hybrydowa aplikacja do zarządzania zadaniami (Task Manager), zaprojektowana zgodnie z nowoczesnymi standardami inżynierii oprogramowania. Projekt łączy logikę biznesową napisaną w języku Python z interfejsem webowym opartym na frameworku Flask.

Głównym celem projektu było stworzenie skalowalnej architektury, która oddziela warstwę danych (Backend) od warstwy prezentacji (Frontend/CLI).

## 🚀 Kluczowe Funkcjonalności
* **Zarządzanie Zadaniami (CRUD):** Dodawanie, usuwanie, oraz oznaczanie zadań jako ukończone/nieukończone.
* **State-Based UI:** Interfejs dynamicznie reaguje na stan zadania (ukrywanie przycisku "Done", pokazywanie "Undo").
* **Dwa Interfejsy:**
    * **Web Dashboard:** Responsywny panel w przeglądarce (HTML/CSS/Jinja2).
    * **CLI (Command Line Interface):** Możliwość zarządzania zadaniami bezpośrednio z terminala.
* **Konteneryzacja:** Aplikacja jest w pełni "zdockeryzowana" i gotowa do uruchomienia na dowolnej maszynie.

## 🛠️ Stack Technologiczny
* **Język:** Python 3.11
* **Framework Web:** Flask (Blueprints, Routing)
* **Frontend:** HTML5, CSS3 (Custom Flexbox Design), Jinja2 Templating
* **Baza Danych:** SQLite / JSON (Architektura modułowa `storage_manager`)
* **DevOps:** Docker (Multi-stage build)

## 🏗️ Architektura
Projekt wykorzystuje wzorzec **MVC (Model-View-Controller)**:
1.  **Models:** Definicja obiektu `Task` i jego zachowań.
2.  **Views (Templates):** Pliki HTML renderujące widok dla użytkownika.
3.  **Controllers (Routes):** Logika w `tasks.py` łącząca żądania HTTP z bazą danych.

## 📦 Jak uruchomić projekt?

### Opcja 1: Docker (Zalecane)
Aplikacja została spakowana do kontenera, aby zapewnić powtarzalność środowiska.
Wymagane: Docker Desktop.

1. **Pobierz obraz:**
   ```bash
   docker run -p 5000:5000 tomfal2234/yourhub-app

### Opcja 2: Localhost
uruchom wirtualne środowisko, a następnie ->
1. Aplikacje uruchamiamy za pomocą:
    ```bash
    python run.py