from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from app.schemas.sale_items import SaleItemCreate, SaleItemResponse


class SaleBase(BaseModel):
    user_id: int
    customer_id: Optional[int] = None


class SaleCreate(SaleBase):
    items: List[SaleItemCreate]


class SaleResponse(SaleBase):
    sale_id: int
    sale_date: datetime
    total_amount: Decimal
    sale_items: List[SaleItemResponse]

    class Config:
        from_attributes = True
