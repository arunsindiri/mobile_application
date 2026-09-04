# VidTalk Development Progress

## Project Overview

VidTalk is a native Android video-watching and commenting application. Its main feature is interactive video comments, including timestamp-pinned comments, short video comments, threaded replies, and comment reactions.

The Android app communicates with FastAPI through a REST API. FastAPI communicates with PostgreSQL through SQLAlchemy and with Cloudinary for video storage; the Android app must not connect directly to PostgreSQL.

## Technology Stack

- Android: Kotlin, Android Studio, Jetpack Compose, MVVM, Retrofit, OkHttp, Coroutines, Flow, Hilt, Room, Media3/ExoPlayer, and CameraX.
- Backend: Python, FastAPI, REST API, SQLAlchemy 2.x, Alembic, and PostgreSQL.
- Authentication: Google OAuth / Google Sign-In.
- Video: Media3/ExoPlayer for playback, CameraX for recording, and Cloudinary for storage.
- Version control: Git and GitHub.

## Current Backend Structure

```text
vidtalk/
└── backend/
    ├── venv/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── database/
    │   │   ├── __init__.py
    │   │   └── connection.py
    │   └── models/
    │       ├── __init__.py
    │       └── user.py
    ├── migrations/
    │   ├── versions/
    │   ├── env.py
    │   ├── README
    │   └── script.py.mako
    ├── .env
    ├── .gitignore
    └── alembic.ini
```

## Completed Work

1. **Project and backend setup — COMPLETE**
   - Created the VidTalk project and `backend/` directory.
   - Created the Python virtual environment at `backend/venv/`.

2. **FastAPI setup — COMPLETE**
   - Installed FastAPI and Uvicorn.
   - Created `app/main.py`.
   - Added `GET /`, returning `{"message": "Welcome to VidTalk"}`.
   - The backend runs with `uvicorn app.main:app --reload`; Swagger documentation is available at `/docs`.

3. **Temporary videos API — COMPLETE**
   - Added `GET /videos` with temporary sample video data.
   - This endpoint will later retrieve videos from PostgreSQL.

4. **PostgreSQL setup — COMPLETE**
   - Installed PostgreSQL and created the local `vidtalk` database.
   - Confirmed PostgreSQL is running locally.

5. **SQLAlchemy and database connection — COMPLETE**
   - Installed SQLAlchemy and `psycopg2-binary`.
   - Created `app/database/connection.py`.
   - Confirmed SQLAlchemy connects successfully to PostgreSQL.

6. **Environment configuration — COMPLETE**
   - Installed `python-dotenv`.
   - Created `.env` and configured `DATABASE_URL` for the local PostgreSQL connection.
   - `.env` must never be committed to GitHub.

7. **Git ignore configuration — COMPLETE**
   - Created `.gitignore` to ignore `venv/`, `.env`, and `__pycache__/`.

8. **SQLAlchemy Base — COMPLETE**
   - Created the SQLAlchemy `Base` using `DeclarativeBase`.
   - Future database models will inherit from `Base`.

9. **User model — COMPLETE**
   - Created `app/models/user.py`.
   - Added the `users` model with `id`, `google_id`, and `display_name`.
   - `id` is an integer primary key; `google_id` is a unique, non-null `varchar(255)`; `display_name` is a non-null `varchar(100)`.

10. **Alembic setup — COMPLETE**
    - Installed and initialized Alembic in `migrations/`.
    - Configured Alembic to load `DATABASE_URL` from `.env`, use `Base.metadata`, detect SQLAlchemy models, and generate migrations.

11. **Users table migration — COMPLETE**
    - Created the Alembic migration for the `users` table.
    - Successfully applied the migration.
    - Verified the `users` table exists directly in PostgreSQL.

## Current Database

Database: `vidtalk`

Current tables:

- `alembic_version`
- `users`

Current `users` table:

```text
users
├── id
├── google_id
└── display_name
```

No real users have been created yet.

## Current Position

The FastAPI backend foundation, PostgreSQL connection, SQLAlchemy setup, Alembic configuration, and `users` table are working.

## Exact Next Step

Create and understand the SQLAlchemy database session in `app/database/session.py`.

After that, build `POST /users` using this flow:

```text
Android / API Client → FastAPI → Request Schema → Database Session → SQLAlchemy → PostgreSQL → users table
```

## Backend Roadmap

1. FastAPI setup — COMPLETE
2. `GET /` endpoint — COMPLETE
3. `GET /videos` endpoint — COMPLETE
4. PostgreSQL setup — COMPLETE
5. SQLAlchemy setup — COMPLETE
6. Environment variables — COMPLETE
7. `.gitignore` — COMPLETE
8. SQLAlchemy Base — COMPLETE
9. User model — COMPLETE
10. Alembic setup — COMPLETE
11. Users table migration — COMPLETE
12. Database session
13. `POST /users`
14. `GET /users`
15. `GET /users/{id}`
16. Improve User model
17. Video model
18. Video APIs
19. Comment model
20. Comment APIs
21. Nested replies
22. Timestamp comments
23. Like/dislike system
24. Google authentication
25. Cloudinary integration
26. Video comment upload
27. Video comment validation
28. Backend testing
29. Deployment

## Android Roadmap

1. Create Android Studio project
2. Kotlin setup
3. Jetpack Compose setup
4. MVVM architecture
5. Navigation
6. Network layer
7. Retrofit
8. Connect Android to FastAPI
9. Google Sign-In
10. Login screen
11. Display-name screen
12. Home/video feed
13. Video screen
14. Media3 / ExoPlayer
15. Comments UI
16. Replies UI
17. Nested comment tree
18. Timestamp markers
19. Like/dislike
20. CameraX
21. Record video comment
22. Select video from device
23. Three-minute duration restriction
24. Cloudinary upload
25. Video comment display
26. Error handling
27. Loading states
28. Offline/local data where appropriate
29. Testing
30. Release APK/AAB

## Database Roadmap

Expected future tables:

- `users`
- `videos`
- `comments`
- `comment_reactions`

Comments will use a parent-child relationship for nested replies, likely through a `parent_id` field. Timestamp comments will store their position in seconds; for example, `timestamp = 97` represents `01:37` and will appear as a marker on the Android video progress bar.

## Documentation Workflow

After every major completed step, plan, implement, explain, and test the feature; commit it to Git; then update this file while preserving previous history. This tracker should always show completed work, current structure, database state, technologies and files added, testing, the current position, exact next step, and the future roadmap.
