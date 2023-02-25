from beanie import Document
from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from typing import Optional
from restaurant.model import Restaurant
from datetime import datetime
from base.model import Measurement, Discount

class FoodItem(Document):
    id:UUID = Field(default_factory=uuid4)
    name: str
    description: str
    category: str
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    image: Optional[str]
    restaurant: Restaurant
    offer: Optional[Discount]
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()