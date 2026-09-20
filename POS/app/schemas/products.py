from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    category_id: int
    sku: str = Field(min_length=1)
    supplier_id: Optional[int] = None



class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    price: Optional[float] = Field(default=None, gt=0)
    quantity: Optional[int] = Field(default=None, ge=0)
    category_id: Optional[int] = None
    sku: Optional[str] = Field(default=None, min_length=1)
    supplier_id: Optional[int] = None


class ProductResponse(ProductBase):
    id: int = Field(validation_alias="product_id")
    model_config = ConfigDict(from_attributes=True)
