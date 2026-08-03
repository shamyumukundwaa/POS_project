from dataclasses import field

from pydantic import BaseModel, EmailStr
from typing import Optional


class CustomerBase(BaseModel):
    full_name: str
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    loyalty_points: Optional[int] = field(default=0)


class CustomerCreate(CustomerBase):
    pass


class CustomerResponse(CustomerBase):
    customer_id: int

    class Config:
        from_attributes = True
