from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.products import ProductCreate, ProductUpdate, ProductResponse
from app.repositories.products import product_repo
from app.services.product import product_service

router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=False,
)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create(db, product)


@router.get("", response_model=List[ProductResponse])
@router.get("/", response_model=List[ProductResponse], include_in_schema=False)
def get_all_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return product_repo.get_all(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_one_product(product_id: int, db: Session = Depends(get_db)):
    product = product_repo.get_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, update_data: ProductUpdate, db: Session = Depends(get_db)
):
    product = product_repo.get_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product_service.update(db, product, update_data)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_repo.get_by_id(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    product_repo.delete(db, product)
    return None
