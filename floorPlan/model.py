from beanie import Document 
from restaurant.model import Restaurant
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class Table(BaseModel):
    table_number: str
    location_x: float
    location_y: float

class FloorPlan(Document):
    id:UUID = Field(default_factory=uuid4)
    restaurant: Restaurant
    floor_number: str 
    tables: Table
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()