from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from app.schemas.receipts import ReceiptResponse
from app.repositories.receipts import receipt_repo

router = APIRouter(prefix="/receipts", tags=["Receipts"])


@router.get("/", response_model=List[ReceiptResponse])
def get_receipts(db: Session = Depends(get_db)):
    return receipt_repo.get_multi(db)


@router.get("/{receipt_id}", response_model=ReceiptResponse)
def get_receipt(receipt_id: int, db: Session = Depends(get_db)):
    receipt = receipt_repo.get(db, receipt_id, "receipt_id")
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt document not found")
    return receipt
