from pydantic import BaseModel
from restaurant.model import Restaurant
from .model import Table
from uuid import UUID
from beanie import Link
from typing import Optional

class CreateDTO(BaseModel): 
    restaurant: Link[Restaurant]
    floor_number: str
    tables: Table

class UpdateDTO(BaseModel):
    restaurant: Optional[Link[Restaurant]]
    floor_number: Optional[str]
    tables: Optional[Table]

class ResponseDTO(BaseModel):
    id:UUID
    restaurant: Link[Restaurant]
    floor_number: str
    tables: Table   