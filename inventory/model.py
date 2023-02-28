from beanie import Document, Link
from pydantic import BaseModel, Field
from base.model import Base, Measurement
from restaurant.model import Restaurant
from uuid import UUID, uuid4
from datetime import datetime

class Quantity(Measurement, BaseModel):
    restock_alert: int

class Inventory(Base, Document):
    id: UUID = Field(default_factory = uuid4)
    name: str
    price: Measurement
    quantity: Quantity
    restaurant: Link[Restaurant]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()