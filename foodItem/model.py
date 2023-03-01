from beanie import Document, Link
from typing import Optional
from restaurant.model import Restaurant
from base.model import Base, Measurement, Discount

class FoodItem(Base, Document):
    name: str
    description: str
    category: str
    subcategory: Optional[str]
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    image: Optional[str]
    restaurant: Link[Restaurant]
    offer: Optional[Discount]