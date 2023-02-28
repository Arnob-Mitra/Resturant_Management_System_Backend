from pydantic import BaseModel
from .model import Quantity
from base.model import Measurement
from restaurant.model import Restaurant
from beanie import Link
from typing import Optional
from uuid import UUID

class CreateDTO(BaseModel):
    name: str
    price: Measurement
    quantity: Quantity
    restaurant: Link[Restaurant]
    
class UpdateDTO(BaseModel):
    name: Optional[str]
    price: Optional[Measurement]
    quantity: Optional[Quantity]
    restaurant: Optional[Link[Restaurant]]
        
class ResponseDTO(BaseModel):
    id: UUID
    name: str
    price: Measurement
    quantity: Quantity
    restaurant: Link[Restaurant]    