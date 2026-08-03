from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.repositories.users import user_repo

router = APIRouter(prefix="/users", tags=["Users (Staff)"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    return user_repo.create(db, payload.model_dump())


@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_repo.get_multi(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get(db, user_id, "user_id")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = user_repo.get(db, user_id, "user_id")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = payload.model_dump(exclude_unset=True, exclude_none=True)
    if not update_data:
        return user

    return user_repo.update(db, user, update_data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_repo.get(db, user_id, "user_id")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_repo.delete(db, user)
    return None
