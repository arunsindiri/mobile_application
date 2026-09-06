from pydantic import BaseModel


class UserCreate(BaseModel):
    google_id: str 
    display_name: str

class UserResponse(BaseModel):
    id: int
    google_id: str
    display_name: str

class UserUpdate(BaseModel):
    display_name: str
