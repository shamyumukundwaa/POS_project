from pydantic import BaseModel
from datetime import datetime


class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str


class ReceiptCreate(ReceiptBase):
    pass


class ReceiptResponse(ReceiptBase):
    receipt_id: int
    issued_date: datetime

    class Config:
        from_attributes = True
