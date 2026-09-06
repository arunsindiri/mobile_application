# VidTalk Backend Cheat Sheet

## Folder / File Reference

| Folder / File | What it does |
|---|---|
| `backend/` | Root folder of the Python backend |
| `app/` | Contains the actual application code |
| `app/__init__.py` | Makes `app` a Python package |
| `app/main.py` | Starts FastAPI and registers routes |
| `app/database/` | Everything related to database connection/session |
| `app/database/__init__.py` | Makes `database` a Python package |
| `app/database/connection.py` | Creates PostgreSQL connection (engine) and SQLAlchemy Base |
| `app/database/session.py` | Creates/manages database sessions |
| `app/models/` | Contains database table definitions |
| `app/models/__init__.py` | Makes `models` a Python package |
| `app/models/user.py` | Defines the `users` database table |
| `app/schemas/` | Contains API input/output data definitions |
| `app/schemas/__init__.py` | Makes `schemas` a Python package |
| `app/schemas/user.py` | Defines user API data, currently `UserCreate` |
| `app/routes/` | Contains API endpoints |
| `app/routes/__init__.py` | Makes `routes` a Python package |
| `app/routes/users.py` | Contains user APIs like `POST /users` and `GET /users` |
| `migrations/` | Alembic database migration system |
| `migrations/versions/` | Stores individual database migration files |
| `migrations/env.py` | Connects Alembic to our models/database |
| `migrations/script.py.mako` | Template used to create migration files |
| `migrations/README` | Alembic migration information |
| `alembic.ini` | Alembic configuration |
| `.env` | Stores environment variables such as database URL |
| `.gitignore` | Tells Git what not to track |
| `venv/` | Python virtual environment and installed packages |

## Remember These 4

- `routes/` → API endpoints
- `schemas/` → API data
- `models/` → Database tables
- `database/` → Database connection/session

## Basic Flow

```
Android
   ↓
routes
   ↓
schemas
   ↓
database/session
   ↓
models
   ↓
PostgreSQL
```
