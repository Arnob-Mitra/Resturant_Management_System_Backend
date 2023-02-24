from beanie import Document 
from restaurant.model import Restaurant
from pydantic import BaseModel

class Table(BaseModel):
    table_number: str
    location_x: float
    location_y: float

class FloorPlan(Document):
    restaurant: Restaurant
    floor_number: str 
    tables: Table