# Tripma — Flight Reservation System

A FastAPI REST API for managing flights, bookings, and users. Built with **FastAPI + SQLModel + MySQL**.

## Tech Stack

| Layer        | Technology                                                        |
| ------------ | ----------------------------------------------------------------- |
| Framework    | [FastAPI](https://fastapi.tiangolo.com/)                           |
| ORM / Schema | [SQLModel](https://sqlmodel.tiangolo.com/) (SQLAlchemy + Pydantic) |
| Database     | MySQL 8+ via`pymysql`                                           |
| Server       | [Uvicorn](https://www.uvicorn.org/) (ASGI)                         |
| Runtime      | Python 3.10+                                                      |

---

## Prerequisites

- Python **3.10+**
- A running **MySQL** instance (or use SQLite for quick local dev — see below)

---

## Quick Start

### 1. Clone & create virtual environment

```bash
git clone <repo-url>
cd Flight-Reservation-System-V2

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -e .
```

> This reads `pyproject.toml` and installs all required packages automatically.

Or install manually:

```bash
pip install fastapi "uvicorn[standard]" sqlmodel pymysql cryptography python-dotenv pydantic-settings
```

### 3. Configure environment

Copy the example env file and fill in your credentials:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Then edit `.env`:

```env
# MySQL (production / local MySQL)
DATABASE_URL=mysql+pymysql://root:<your-password>@localhost:3307/tripma_db

# SQLite (quick local dev — no MySQL needed)
# DATABASE_URL=sqlite:///./dev.db
```

| Variable         | Description                                      |
| ---------------- | ------------------------------------------------ |
| `DATABASE_URL` | SQLAlchemy connection string for MySQL or SQLite |

### 4. Create the MySQL database (if using MySQL)

**Option A — Docker (recommended):**

```bash
docker run -d --name mysql \
  -e MYSQL_ROOT_PASSWORD=<your-password> \
  -p 3307:3306 \
  mysql:latest

docker exec mysql mysql -uroot -p<your-password> \
  -e "CREATE DATABASE tripma_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

**Option B — Local MySQL:**

```sql
CREATE DATABASE tripma_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Tables are created **automatically on startup** via `SQLModel.metadata.create_all(engine)` — no manual migration needed for local dev.

### 5. Run the server

```bash
# Development (with auto-reload)
uvicorn app.main:app --reload

# Production-ready (single worker, no reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Custom port
uvicorn app.main:app --reload --port 8080
```

The API starts on **http://localhost:8000**

---

## API Documentation

| Interface                          | URL                                |
| ---------------------------------- | ---------------------------------- |
| **Swagger UI** (interactive) | http://localhost:8000/docs         |
| **ReDoc**                    | http://localhost:8000/redoc        |
| **OpenAPI JSON spec**        | http://localhost:8000/openapi.json |

---

## API Endpoints

### Flights — `/api/v1/flights`

| Method     | Path                            | Description                                        |
| ---------- | ------------------------------- | -------------------------------------------------- |
| `POST`   | `/api/v1/flights/`            | Create a new flight                                |
| `GET`    | `/api/v1/flights/`            | List all flights (supports`?offset=0&limit=100`) |
| `GET`    | `/api/v1/flights/{flight_id}` | Get a single flight by ID                          |
| `PATCH`  | `/api/v1/flights/{flight_id}` | Partially update a flight                          |
| `DELETE` | `/api/v1/flights/{flight_id}` | Delete a flight                                    |

**Example — create a flight:**

```bash
curl -X POST http://localhost:8000/api/v1/flights/ \
  -H "Content-Type: application/json" \
  -d '{
    "flight_number": "VN123",
    "airline_id": 1,
    "departure_airport_id": 10,
    "arrival_airport_id": 20,
    "base_price": 150.50,
    "aircraft_id": 5
  }'
```

### Users — `/api/v1/users`

| Method  | Path                        | Description      |
| ------- | --------------------------- | ---------------- |
| `GET` | `/api/v1/users/{user_id}` | Get a user by ID |

---

## Project Structure

```
Flight-Reservation-System-V2/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── api/
│   │   └── v1/
│   │       ├── api.py          # Router aggregator
│   │       └── routes/         # (future route files)
│   ├── core/
│   │   ├── settings.py         # Environment / config loading
│   │   ├── security.py         # JWT & password hashing helpers
│   │   └── logging.py          # Logging configuration
│   ├── db/
│   │   ├── session.py          # SQLAlchemy engine & session factory
│   │   └── base.py             # Central model registry for create_all()
│   ├── features/
│   │   ├── flights/
│   │   │   ├── router.py       # FastAPI router (endpoints)
│   │   │   ├── service.py      # Business logic
│   │   │   ├── repository.py   # Database queries
│   │   │   ├── models.py       # SQLModel DB table
│   │   │   └── schemas.py      # Pydantic request/response schemas
│   │   ├── users/              # Same structure as flights/
│   │   ├── billing/            # Placeholder
│   │   └── reports/            # Placeholder
│   ├── shared/                 # Shared utilities & exceptions
│   └── workers/                # Background tasks
├── tests/                      # Pytest test suite
├── alembic/                    # Database migrations
├── pyproject.toml              # Project metadata & dependencies
├── .env.example                # Environment variable template
└── README.md
```

---

## Running Tests

```bash
# Install dev dependencies
pip install pytest httpx pytest-asyncio

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_flights.py
```

---

## References

- UI Figma: https://www.figma.com/community/file/911320742349428744/tripma-flight-booking-web-app
- FastAPI Docs: https://fastapi.tiangolo.com/
- SQLModel Docs: https://sqlmodel.tiangolo.com/
