from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.sales import SaleCreate, SaleResponse
from app.services.sale import sale_service

router = APIRouter(prefix="/sales", tags=["Sales Transaction Ledger"])


@router.post("/", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def checkout_transaction(payload: SaleCreate, db: Session = Depends(get_db)):
    return sale_service.process_checkout(db, payload)
