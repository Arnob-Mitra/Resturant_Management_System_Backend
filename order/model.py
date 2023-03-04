from beanie import Document, Link
from pydantic import BaseModel
from base.model import Base, Measurement, Discount
from typing import Optional
from enum import Enum
from restaurant.model import Restaurant
from floorPlan.model import FloorPlan
from user.model import User

class FoodItem(BaseModel):
    name: str
    price: Measurement
    offer: Optional[Discount]

class OrderStatusEnum(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    UNPAID = "unpaid"
    PAID = "paid"

class Order(Base, Document):
    status: OrderStatusEnum = OrderStatusEnum.CREATED
    food_items: list[FoodItem]
    restaurant: Link[Restaurant]
    floor_plan: Link[FloorPlan]
    table_number: str
    total_price: Measurement
    discounted_price: Measurement
    created_by: Link[User]
    served_by: Link[User]