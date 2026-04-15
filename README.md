# Orbitron Backend

Бэкенд астрологического сервиса с ИИ на FastAPI.

## Быстрый старт

### Требования
- Docker и Docker Compose
- Python 3.12+

### Установка
```bash
git clone https://github.com/ibeercan/orbitron.git
cd backend
cp .env.example .env
# Отредактируйте .env
docker-compose up --build
```

API доступен на `http://localhost:8000` или `api.orbitron.pro`.

## API эндпоинты
- `POST /api/v1/auth/register` - Регистрация
- `POST /api/v1/auth/login` - Авторизация
- `POST /api/v1/charts/natal` - Создание натальной карты
- `POST /api/v1/ai/{chart_id}/interpret` - ИИ интерпретация

Документация: `/docs`

## Конфигурация
Настройте в `.env`:
- `DATABASE_URL` - База данных
- `JWT_SECRET_KEY` - Секрет для JWT
- `AI_API_KEY` - Ключ ИИ (OpenAI или кастомный)
- `AI_MODEL` - Модель (gpt-4)
- `LOG_LEVEL` - Уровень логирования

## Разработка
```bash
# Локально с SQLite
poetry install
poetry run uvicorn app.main:app --reload

# В Docker
docker-compose -f compose.dev.yaml up --build
```

## Продакшн
```bash
docker-compose up -d
```

## Лицензия
AGPL-3.0