from pydantic import BaseModel
from restaurant.model import Restaurant
from .model import Table
from uuid import UUID
from datetime import datetime

class CreateDTO(BaseModel): 
    floor_number: str
    tables: Table

class UpdateDTO(BaseModel):
    restaurant: Restaurant
    floor_number: str
    tables: Table

class ResponseDTO(BaseModel):
    id:UUID
    restaurant: Restaurant
    floor_number: str
    tables: Table   
    