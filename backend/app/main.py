from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to VidTalk"}

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
