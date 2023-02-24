from pydantic import BaseModel
from restaurant.model import Restaurant
from .model import Table

class CreateDTO(BaseModel): 
    floor_number: str
    tables: Table

class UpdateDTO(BaseModel):
    restaurant: Restaurant
    floor_number: str
    tables: Table

class ResponseDTO(BaseModel):
    restaurant: Restaurant
    floor_number: str
    tables: Table    