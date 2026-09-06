# 🎬 VidTalk Development Checklist

## ✅ Completed

1. **Project setup**
   - Created vidtalk project
   - Created Python virtual environment
   - Installed FastAPI
   - Created basic FastAPI server
   - Tested `/` endpoint

2. **FastAPI structure**
   - Created `app/` package
   - Created `main.py`
   - Learned FastAPI routes
   - Created `/videos` test API

3. **PostgreSQL**
   - Installed PostgreSQL
   - Created vidtalk database
   - Tested PostgreSQL connection

4. **SQLAlchemy**
   - Installed SQLAlchemy
   - Installed PostgreSQL driver
   - Created database connection
   - Created SQLAlchemy Base
   - Learned how Python models connect to database tables

5. **Environment configuration**
   - Created `.env`
   - Stored database URL in `.env`
   - Created `.gitignore`
   - Prevented `.env` and venv from Git

6. **User database**
   - Created User model
   - Added:
     - `id`
     - `google_id`
     - `display_name`
   - Created users table

7. **Alembic**
   - Installed Alembic
   - Configured migrations
   - Generated users migration
   - Applied migration
   - Verified table in PostgreSQL

8. **Database sessions**
   - Created `SessionLocal`
   - Created `get_db()`
   - Learned database session lifecycle
   - Learned `yield`, `try`, `finally`

9. **Pydantic schemas**
   - Created `UserCreate` schema
   - Created `UserResponse` schema
   - Created `UserUpdate` schema
   - Learned difference between:
     - Schema → API data
     - Model → Database data

10. **User API**
    - Created `/users` router
    - Created `POST /users`
    - Created `GET /users` (list all)
    - Created `GET /users/{user_id}` (get by ID)
    - Created `PUT /users/{user_id}` (update display name)
    - Created `DELETE /users/{user_id}` (delete user)
    - Connected API → SQLAlchemy → PostgreSQL
    - Tested using Swagger
    - Verified data in PostgreSQL

## 🚧 What We Need To Do Next

We'll build the application gradually.

### 👤 Users

- ~~`GET /users`~~ ✅
- ~~`GET /users/{id}`~~ ✅
- ~~Response schemas~~ ✅
- Handle duplicate `google_id`
- Google OAuth login
- User authentication/session handling

## 🔐 Google Cloud Setup — Step 20

**Authentication approach:** Google's current Android documentation deprecates the older `GoogleSignInOptions` APIs and recommends **Credential Manager** for authentication. We'll use the current Android authentication approach, not an outdated tutorial.

### Google Cloud setup (no code yet)

We need to create/configure:

```
Google Cloud
│
├── Google Cloud Project
│
├── OAuth configuration
│
├── Android Client ID
│   ├── Package name
│   └── SHA-1
│
└── Web Client ID
    └── Used as the server/client ID for the ID token
```

Google's documentation specifically requires an **Android client** and a **server/web client** for the backend ID-token flow.

The Android app will eventually request an ID token, send it to FastAPI, and our backend will verify it. Google identifies the account using the token's `sub` value, which is the stable unique identifier.

### 🔁 Our flow (eventually)

```
Android
   │
   │ Sign in with Google
   ▼
Google
   │
   │ ID Token
   ▼
FastAPI
   │
   │ Verify token
   ▼
Google identity (sub)
   │
   ▼
PostgreSQL
   │
   ▼
VidTalk User
```

### 📱 One thing we need from Android

The Android OAuth client requires the app's **package name** and **SHA-1 signing certificate** (Google confirms SHA-1 is required for services such as Google Sign-In).

Since we haven't created the Android project yet, **we will not create the Android OAuth credentials yet.**

### ✅ Our adjusted order

```
Backend CRUD                 ✅
       ↓
Create Android project       ⬅️ next
       ↓
Get package name + SHA-1
       ↓
Google Cloud OAuth setup
       ↓
Android Google login
       ↓
FastAPI token verification
       ↓
Create/find user
```

**Next step — Step 20A:** Create the VidTalk Android project in Android Studio. 📱

### 🎥 Videos

- Create Video model
- Database migration
- Video API
- YouTube video information
- Video listing
- Video details

### 💬 Comments

- Comment model
- Text comments
- Timestamp comments
- Threaded replies
- Like/dislike
- Blue timestamp markers

### 🎥 Video comments

- Record video using Android CameraX
- Maximum 3-minute validation
- Upload to Cloudinary
- Save Cloudinary URL
- Play video comments

### 📱 Android application

- Create Kotlin Android project
- Jetpack Compose UI
- Login screen
- Google login
- Home/video screen
- Video player
- Comments UI
- Record comment screen
- Reply/thread UI
- Like/dislike UI

### 🔌 Android ↔ Backend

- Retrofit
- API models
- Repository
- ViewModels
- Coroutines/Flow
- Authentication flow

### 🚀 Final

- Testing
- Error handling
- Security
- Backend deployment
- Database deployment
- Android release build
- Google Play preparation