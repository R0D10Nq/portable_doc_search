# 🔍 Portable DocSearch - Продвинутая поисковая система документов

> **Статус:** ✅ MVP готов  
> **Тип:** Full-Stack поисковая платформа  
> **Технологии:** FastAPI + SQLite FTS5 + Vue.js  

Современная система полнотекстового поиска для PDF и Markdown документов. Построена на FastAPI бэкенде, SQLite FTS5 для молниеносного поиска и Vue.js фронтенде. Разработана для автономного использования с веб-интерфейсом и инструментами командной строки.

## ✨ Ключевые особенности

- **📄 Обработка документов** - Индексация PDF и Markdown файлов с извлечением текста
- **🔍 Полнотекстовый поиск** - SQLite FTS5 с алгоритмом ранжирования BM25
- **💡 Умные сниппеты** - Контекстно-зависимые результаты поиска с подсветкой
- **🌐 Веб-интерфейс** - Современный Vue.js фронтенд (на основе CDN, без сборки)
- **🔐 Аутентификация** - JWT-аутентификация с HTTP-only куками
- **⚡ CLI инструменты** - Интерфейс командной строки для управления базой данных
- **📱 Адаптивный дизайн** - Работает на десктопе и мобильных устройствах
- **🔒 Автономность** - Полная функциональность без подключения к интернету

## 🛠 Технологический стек

**Бэкенд:**
- Python 3.12+
- FastAPI + Uvicorn
- SQLAlchemy 2.x
- SQLite FTS5
- Pydantic v2

**Фронтенд:**
- Vue.js 3 (CDN)
- Jinja2 шаблоны
- Современные CSS/JavaScript

**Разработка:**
- Typer (CLI)
- Ruff (линтинг)
- mypy (проверка типов)
- pytest (тестирование)

## 🚀 Быстрый старт

### Требования
- Python 3.12+
- Git

### Установка

```bash
# Клонируем репозиторий
git clone <repository-url>
cd Pet_project_in_Python

# Создаем виртуальное окружение
python -m venv .venv

# Активируем виртуальное окружение
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Устанавливаем зависимости
pip install -U pip
pip install -e .[develop]

# Настраиваем окружение
cp .env.example .env
# Редактируем .env файл с вашими настройками (SECRET_KEY, пути к БД)

# Инициализируем базу данных
python -m docsearch.cli init-db

# Запускаем сервер
python -m docsearch.cli run
```

### Доступ к приложению
- **Веб-интерфейс:** http://127.0.0.1:8000
- **Документация API:** http://127.0.0.1:8000/docs
- **Проверка здоровья:** http://127.0.0.1:8000/healthz

## 📁 Структура проекта

```
Pet_project_in_Python/
├── src/
│   └── docsearch/
│       ├── api/              # FastAPI routes and endpoints
│       ├── core/             # Core configuration and settings
│       ├── db/               # Database models and migrations
│       ├── services/         # Business logic and services
│       ├── web/              # Web interface
│       │   ├── templates/    # Jinja2 templates
│       │   └── static/       # CSS, JS, assets
│       ├── cli.py           # Command-line interface
│       └── main.py          # Application entry point
├── var/
│   ├── db/                  # SQLite database files
│   └── storage/             # Uploaded documents
├── tests/                   # Test suite
├── pyproject.toml          # Project configuration
├── .env.example           # Environment variables template
├── .pre-commit-config.yaml # Pre-commit hooks
├── .github/workflows/     # CI/CD pipelines
└── README.md             # Project documentation
```

## 🎯 Примеры использования

### Web интерфейс
1. **Загрузка документов:** Перейдите в административную панель и загрузите PDF/MD файлы
2. **Поиск:** Используйте интерфейс поиска для поиска содержимого везде
3. **Просмотр результатов:** Просмотрите результаты поиска с подсветкой фрагментов

### CLI команды
```bash
# Initialize database
python -m docsearch.cli init-db

# Start web server
python -m docsearch.cli run

# Index documents (planned)
python -m docsearch.cli index /path/to/documents

# Rebuild search index (planned)
python -m docsearch.cli rebuild

# Show statistics (planned)
python -m docsearch.cli stats
```

## 🧪 Тестирование

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src

# Type checking
mypy src/

# Linting
ruff check src/
```

## 🚀 Деплой

### Docker (скоро будет)
Поддержка Docker будет добавлена в будущих версиях с `Dockerfile` и `docker-compose.yml`.

### Ручной деплой
```bash
# Прод окружение
pip install -e .
export ENVIRONMENT=production
python -m docsearch.cli run --host 0.0.0.0 --port 8000
```

## 📈 Roadmap

### Текущий MVP
- [x] Backend часть FastAPI с SQLite FTS5
- [x] Vue.js frontend (CDN)
- [x] Базовая загрузка документов и поиск
- [x] JWT authentication foundation
- [x] CLI interface

### Планируемые функции
- [ ] Полный конвейер индексации PDF/MD
- [ ] Полная аутентификация JWT с ролями (администратор/пользователь)
- [ ] Расширенные команды CLI (индексация, перестройка, статистика, создание-администратор)
- [ ] Улучшенные HTML-фрагменты с подсветкой FTS5
- [ ] Полный набор тестов и CI / CD
- [ ] Дополнительный модуль встраивания для семантического поиска
- [ ] версия 2: Поддержка распознавания текста для отсканированных документов

## 🎯 Зачем нужен этот проект?

**Для разработчиков:**
- Демонстрирует современную веб-разработку на Python
- Демонстрирует интеграцию FastAPI + SQLite FTS5
- Демонстрирует чистые архитектурные шаблоны
- Включает как веб-, так и CLI-интерфейсы

**Для пользователей:**
- Быстрый автономный поиск документов
- Отсутствие внешних зависимостей или облачных сервисов
- Простота настройки и обслуживания
- Расширяемая архитектура для индивидуальных нужд

## ✅ Особенности производительности

- **✅ Быстрый поиск:** SQLite FTS5 с рейтингом BM25
- **✅ Эффективное хранение:** Оптимизированная индексация документов
- **✅ Асинхронная обработка:** Поддержка FastAPI async/await
- **📱 Адаптивный пользовательский интерфейс: ** Работает на устройствах всех размеров

---