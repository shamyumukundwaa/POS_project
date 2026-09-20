from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class SupplierBase(BaseModel):
    company_name: str = Field(min_length=1)
    contact_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    supplier_id: int


    
    model_config = ConfigDict(from_attributes=True)
    
