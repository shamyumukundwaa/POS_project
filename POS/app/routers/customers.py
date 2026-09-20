from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.customers import CustomerCreate, CustomerResponse, CustomerUpdate
from app.repositories.customers import customer_repo

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    return customer_repo.create(db, payload.model_dump())


@router.get("/", response_model=List[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return customer_repo.get_multi(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_repo.get(db, customer_id, "id")
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int, payload: CustomerUpdate, db: Session = Depends(get_db)
):
    customer = customer_repo.get(db, customer_id, "id")
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer_repo.update(db, customer, payload.model_dump(exclude_unset=True))


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_repo.get(db, customer_id, "id")
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    customer_repo.delete(db, customer)
    return None
