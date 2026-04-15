# Orbitron Backend

AI-powered astrology service backend built with FastAPI, Stellium, and Pydantic-AI.

## Features

- **Natal Charts**: Generate beautiful SVG charts using Stellium library
- **AI Interpretation**: Get personalized astrological insights with GPT-4
- **User Management**: JWT authentication with subscription tiers
- **Security**: Rate limiting, CORS, input validation, structured logging

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.12+

### Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd backend
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Edit `.env` with your secrets:
```env
DATABASE_URL=postgresql://user:pass@localhost:5432/astrology
JWT_SECRET_KEY=your-super-secret-key-change-in-production
AI_API_KEY=your-api-key
AI_BASE_URL=https://your-custom-provider.com/v1  # опционально
AI_MODEL=gpt-4  # или другое
REDIS_URL=redis://redis:6379
LOG_LEVEL=INFO  # DEBUG for development, INFO for production
```

4. Run with Docker Compose:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000` (or via Traefik at `api.orbitron.pro`).

## AI Configuration

The service supports custom AI agents. Configure via environment variables:

- `AI_API_KEY`: Your API key (OpenAI or custom provider)
- `AI_BASE_URL`: Base URL for custom providers (optional, defaults to OpenAI)
- `AI_MODEL`: Model name (e.g., "gpt-4", "local-model")

Example for OpenAI:
```env
AI_API_KEY=sk-your-openai-key
AI_MODEL=gpt-4
```

Example for custom provider:
```env
AI_API_KEY=your-custom-key
AI_BASE_URL=https://your-llm-server.com/v1
AI_MODEL=your-model-name
```

## API Documentation

Once running, visit `/docs` for interactive API documentation.

### Key Endpoints

- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/charts/natal` - Create natal chart
- `POST /api/v1/ai/{chart_id}/interpret` - AI interpretation

## Development

### Local Setup (with SQLite)

For quick development without Docker:
```bash
poetry install
export DATABASE_URL=sqlite:///./dev.db
export LOG_LEVEL=DEBUG
poetry run uvicorn app.main:app --reload
```

### Docker Development

Use the development compose for full environment:
```bash
docker-compose -f compose.dev.yaml up --build
```

This uses SQLite database and hot reload for faster development.

### Production

Use the main compose.yaml for production deployment with PostgreSQL and Traefik.

### Testing

```bash
poetry run pytest
```

### Linting

```bash
poetry run ruff check .
poetry run ruff format .
```

## Deployment

The application is containerized and ready for deployment with Traefik reverse proxy.

1. Ensure Traefik is configured for `api.orbitron.pro`
2. Set environment variables in your deployment environment
3. Run `docker-compose up -d`

## Security

- JWT tokens with configurable expiration
- Rate limiting (100 requests/minute globally)
- Subscription-based access control
- Input validation with Pydantic
- Structured logging with context

## License

AGPL-3.0