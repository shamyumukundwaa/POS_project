from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.payments import PaymentCreate, PaymentResponse
from app.repositories.payments import payment_repo

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payload: PaymentCreate, db: Session = Depends(get_db)):
    return payment_repo.create(db, payload.model_dump())


@router.get("/", response_model=List[PaymentResponse])
def get_payments(db: Session = Depends(get_db)):
    return payment_repo.get_multi(db)


@router.get("/{payment_id}", response_model=PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = payment_repo.get(db, payment_id, "payment_id")
    if not payment:
        raise HTTPException(status_code=404, detail="Payment record not found")
    return payment
