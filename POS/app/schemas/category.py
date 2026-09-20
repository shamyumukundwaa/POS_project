from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class CategoryBase(BaseModel):
    name: str = Field(min_length=1)
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(validation_alias="category_id")

    model_config = ConfigDict(from_attributes=True)
