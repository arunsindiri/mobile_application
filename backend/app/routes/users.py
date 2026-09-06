from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, UserUpdate

from sqlalchemy import select


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        google_id=user.google_id,
        display_name=user.display_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    result = db.scalars(select(User))
    users = result.all()

    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    result = db.scalars(
        select(User).where(User.id == user_id)
    ).first()

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    result = db.scalars(
        select(User).where(User.id == user_id)
    ).first()

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    result.display_name = user.display_name

    db.commit()
    db.refresh(result)

    return result


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    result = db.scalars(
        select(User).where(User.id == user_id)
    ).first()

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(result)
    db.commit()

    return {"message": "User deleted successfully"}
