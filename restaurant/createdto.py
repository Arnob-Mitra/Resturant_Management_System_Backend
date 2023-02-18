from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from .model import Address

class RestaurantCreateDTO(BaseModel):
    managedBy:UUID 
    name:str
    address:Address
    chainOf:UUID 
    cuisineType:str