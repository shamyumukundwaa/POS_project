from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.category import CategoryCreate, CategoryResponse
from app.services.category import category_service

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create(db, payload.model_dump())

@router.get("/", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return category_service.get_all(db)

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category record not found")
    return category

@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, payload: CategoryCreate, db: Session = Depends(get_db)):
    category = category_service.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category record not found")
    return category_service.update(db, category, payload.model_dump())

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = category_service.get_by_id(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category record not found")
    category_service.delete(db, category)
    return None
