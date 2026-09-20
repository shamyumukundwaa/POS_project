from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from typing import Optional


class SaleItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class SaleItemCreate(SaleItemBase):
    pass


class SaleItemResponse(SaleItemBase):
    sale_item_id: int
    sale_id: int
    unit_price: Decimal
    subtotal: Optional[Decimal] = None

    model_config = ConfigDict(from_attributes=True)
    
    