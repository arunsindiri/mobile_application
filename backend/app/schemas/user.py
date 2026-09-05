from pydantic import BaseModel


class UserCreate(BaseModel):
    google_id: str 
    display_name: str
