from beanie import Document, Link
from pydantic import BaseModel
from base.model import Base, Measurement
from restaurant.model import Restaurant

class Quantity(Measurement, BaseModel):
    restock_alert: int

class Inventory(Base, Document):
    name: str
    price: Measurement
    quantity: Quantity
    restaurant: Link[Restaurant]