from fastapi import FastAPI

from app.routes.users import router as users_router

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to VidTalk"}


app.include_router(users_router)


@app.get("/videos")
def get_videos():
    videos = [
        {
            "id": 1,
            "title": "Python Tutorial",
            "description": "Learn Python basics"
        },
        {
            "id": 2,
            "title": "FastAPI Tutorial",
            "description": "Build APIs with FastAPI"
        }
    ]

    return videos
