from beanie import Document, Link
from restaurant.model import Restaurant
from pydantic import BaseModel
from base.model import Base

class Table(BaseModel):
    table_number: str
    location_x: float
    location_y: float

class FloorPlan(Base, Document):
    restaurant: Link[Restaurant]
    floor_number: str 
    tables: Table