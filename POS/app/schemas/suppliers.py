from pydantic import BaseModel, EmailStr
from typing import Optional


class SupplierBase(BaseModel):
    company_name: str
    contact_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    supplier_id: int

    class Config:
        from_attributes = True
