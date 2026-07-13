from pydantic import BaseModel, Field
from typing import Optional


class ItemCreate(BaseModel):
    # name must be greater than 3 and less than 10 characters
    name: str = Field(..., min_length=4, max_length=9)
    description: Optional[str] = None


class Item(ItemCreate):
    id: int


class ItemUpdate(BaseModel):
    # For updates, fields are optional but keep same validation for `name` when provided
    name: Optional[str] = Field(None, min_length=4, max_length=9)
    description: Optional[str] = None
