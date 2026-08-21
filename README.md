# Tripma — Flight Reservation System

A FastAPI REST API for managing flights, backed by MySQL.

## Tech Stack

- Python 3
- FastAPI
- SQLModel (SQLAlchemy + Pydantic)
- MySQL 8+ (via `pymysql`)
- Uvicorn

## Prerequisites

- Python 3.8+
- A running MySQL instance

## Setup

### 1. Database

Create a MySQL database for the app to use. For local development, a Docker container works well:

```bash
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=<your-password> \
  -p 3307:3306 \
  mysql:latest

docker exec mysql mysql -uroot -p<your-password> \
  -e "CREATE DATABASE tripma_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

### 2. Environment variables

Copy the example env file and fill in your credentials:

```bash
cp .env.example .env
```

`.env` (git-ignored) is loaded automatically in `app/core/config.py` using `python-dotenv`:

| Variable | Description |
|---|---|
| `DATABASE_URL` | Database connection string, e.g. `mysql+pymysql://user:password@localhost:3306/tripma_db` |

### 3. Schema

`SQLModel.metadata.create_all(engine)` is executed on startup, so tables are created automatically from the models — no manual schema migration needed for local dev.

### 4. Run

Activate your virtual environment (if using one), install dependencies, and run the app:

```bash
pip install fastapi sqlmodel pymysql uvicorn python-dotenv
uvicorn app.main:app --reload
```

The app starts on **http://localhost:8000**.

## API Documentation

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
OpenAPI spec: http://localhost:8000/openapi.json

## Project Structure

```
app/
├── api/          FastAPI routers (endpoints)
├── core/         Core configurations (e.g., database engine)
├── models/       SQLModel entities and Pydantic schemas
├── crud.py       Reusable CRUD operations
└── main.py       FastAPI application entry point
```

## CI

Pull requests are automatically reviewed by Claude via GitHub Actions ([.github/workflows/claude_pr_review.yml](.github/workflows/claude_pr_review.yml)). Comment `@claude` on a PR to trigger a re-review.

## References

UI Figma: https://www.figma.com/community/file/911320742349428744/tripma-flight-booking-web-app
