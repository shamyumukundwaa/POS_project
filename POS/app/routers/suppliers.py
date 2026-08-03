from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.suppliers import SupplierCreate, SupplierResponse
from app.repositories.suppliers import supplier_repo

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.post("/", response_model=SupplierResponse, status_code=status.HTTP_201_CREATED)
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db)):
    return supplier_repo.create(db, payload.model_dump())


@router.get("/", response_model=List[SupplierResponse])
def get_suppliers(db: Session = Depends(get_db)):
    return supplier_repo.get_multi(db)


@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = supplier_repo.get(db, supplier_id, "supplier_id")
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.put("/{supplier_id}", response_model=SupplierResponse)
def update_supplier(
    supplier_id: int, payload: SupplierCreate, db: Session = Depends(get_db)
):
    supplier = supplier_repo.get(db, supplier_id, "supplier_id")
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier_repo.update(db, supplier, payload.model_dump())


@router.delete("/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = supplier_repo.get(db, supplier_id, "supplier_id")
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    supplier_repo.delete(db, supplier)
    return None
