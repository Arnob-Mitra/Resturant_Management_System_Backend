from pydantic import BaseModel
from .model import Quantity
from base.model import Measurement
from restaurant.model import Restaurant


class CreateDTO(BaseModel):
    name: str
    quantity: Quantity
    
class UpdateDTO(BaseModel):
    name: str
    quantity: Quantity
    restaurant: Restaurant
        
class ResponseDTO(BaseModel):
    name: str
    price: Measurement
    quantity: Quantity
    restaurant: Restaurant    