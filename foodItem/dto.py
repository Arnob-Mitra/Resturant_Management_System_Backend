from pydantic import BaseModel
from .model import Measurement, Discount
from typing import Optional
from restaurant.model import Restaurant

class CreateDTO(BaseModel):
    name: str
    description: str
    category: str
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]

class UpdateDTO(BaseModel):
    image: Optional[str]
    price: Measurement
    offer: Optional[Discount]

class ResponseDTO(BaseModel):
    name: str
    description: str
    category: str
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    image: Optional[str]
    restaurant: Restaurant
    offer: Optional[Measurement]  