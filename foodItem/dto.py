from pydantic import BaseModel
from base.model import Measurement, Discount
from typing import Optional
from restaurant.model import Restaurant
from uuid import UUID
from beanie import Link

class CreateDTO(BaseModel):
    name: str
    description: str
    category: str
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    restaurant: Link[Restaurant]

class UpdateDTO(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    subcategory: Optional[str]
    cuisine: Optional[str]
    image: Optional[str]
    price: Optional[Measurement]
    recipe: Optional[dict[str, Measurement]]
    restaurant: Optional[Link[Restaurant]]
    offer: Optional[Discount]

class ResponseDTO(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    subcategory: Optional[str]
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    image: Optional[str]
    restaurant: Link[Restaurant]
    offer: Optional[Discount]  