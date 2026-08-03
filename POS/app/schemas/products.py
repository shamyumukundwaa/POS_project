from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: Decimal = Field(..., gt=0)
    sku: str
    stock_quantity: int = Field(..., ge=0)
    category_id: int
    supplier_id: Optional[int] = None


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    product_id: int

    class Config:
        from_attributes = True
