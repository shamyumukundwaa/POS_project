from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional


class CustomerBase(BaseModel):
    name: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    email: EmailStr | None = None
    address: str | None = None

class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    phone: str | None = Field(default=None, min_length=1)
    email: EmailStr | None = None
    address: str | None = None


class CustomerResponse(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
