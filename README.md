# Orbitron Backend

Бэкенд сервиса астрологии с ИИ, построенный на FastAPI, Stellium и Pydantic-AI.

## Функции

- **Натальные карты**: Генерация красивых SVG-карт с помощью библиотеки Stellium
- **Интерпретация ИИ**: Персонализированные астрологические insights с GPT-4
- **Управление пользователями**: JWT аутентификация с уровнями подписок
- **Безопасность**: Ограничение скорости, CORS, валидация ввода, структурированное логирование

## Быстрый старт

### Предварительные требования

- Docker и Docker Compose
- Python 3.12+

### Установка

1. Клонируйте репозиторий:
```bash
git clone <repo-url>
cd backend
```

2. Скопируйте файл окружения:
```bash
cp .env.example .env
```

3. Отредактируйте `.env` с вашими секретами:
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/astrology
JWT_SECRET_KEY=your-super-secret-key-change-in-production
AI_API_KEY=your-api-key
AI_BASE_URL=https://your-custom-provider.com/v1  # опционально
AI_MODEL=gpt-4  # или другое
REDIS_URL=redis://redis:6379
LOG_LEVEL=INFO  # DEBUG для разработки, INFO для продакшена
```

4. Запустите с Docker Compose:
```bash
docker-compose up --build
```

API будет доступен по адресу `http://localhost:8000` (или через Traefik по адресу `api.orbitron.pro`).

## Конфигурация ИИ

Сервис поддерживает кастомных ИИ-агентов. Настройте через переменные окружения:

- `AI_API_KEY`: Ваш API ключ (OpenAI или кастомный провайдер)
- `AI_BASE_URL`: Base URL для кастомных провайдеров (опционально, по умолчанию OpenAI)
- `AI_MODEL`: Название модели (например, "gpt-4", "local-model")

Пример для OpenAI:
```env
AI_API_KEY=sk-your-openai-key
AI_MODEL=gpt-4
```

Пример для кастомного провайдера:
```env
AI_API_KEY=your-custom-key
AI_BASE_URL=https://your-llm-server.com/v1
AI_MODEL=your-model-name
```

## Документация API

После запуска посетите `/docs` для интерактивной документации API.

### Основные эндпоинты

- `POST /api/v1/auth/register` - Регистрация пользователя
- `POST /api/v1/auth/login` - Вход пользователя
- `POST /api/v1/charts/natal` - Создание натальной карты
- `POST /api/v1/ai/{chart_id}/interpret` - Интерпретация ИИ

## Разработка

### Локальная настройка (с SQLite)

Для быстрой разработки без Docker:
```bash
poetry install
export DATABASE_URL=sqlite:///./dev.db
export LOG_LEVEL=DEBUG
poetry run uvicorn app.main:app --reload
```

### Разработка в Docker

Используйте compose для разработки для полной среды:
```bash
docker-compose -f compose.dev.yaml up --build
```

Это использует базу данных SQLite и hot reload для более быстрой разработки.

### Продакшн

Используйте основной compose.yaml для развертывания в продакшене с PostgreSQL и Traefik.

### Тестирование

```bash
poetry run pytest
```

### Линтинг

```bash
poetry run ruff check .
poetry run ruff format .
```

## Развертывание

Приложение контейнеризовано и готово к развертыванию с Traefik reverse proxy.

1. Убедитесь, что Traefik настроен для `api.orbitron.pro`
2. Установите переменные окружения в вашей среде развертывания
3. Запустите `docker-compose up -d`

## Безопасность

- JWT токены с настраиваемым сроком действия
- Ограничение скорости (100 запросов/минуту глобально)
- Контроль доступа на основе подписок
- Валидация ввода с Pydantic
- Структурированное логирование с контекстом
- SSL сертификат: SHA256:9qwcljntHiyelg4PrIGoRXxY1NA5Mdxxxkbj+TqePLc

## Лицензия

AGPL-3.0