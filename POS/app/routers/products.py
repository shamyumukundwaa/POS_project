from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.products import ProductCreate, ProductResponse
from app.services.product import product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create(db, payload.model_dump())


@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_service.get_all(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = product_service.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product record not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, payload: ProductCreate, db: Session = Depends(get_db)
):
    product = product_service.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product record not found")
    return product_service.update(db, product, payload.model_dump())


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_service.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product record not found")
    product_service.delete(db, product)
    return None
