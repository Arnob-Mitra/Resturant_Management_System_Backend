from beanie import Document, Link
from pydantic import BaseModel, Field
from base.model import Measurement, Discount
from typing import Optional
from enum import Enum
from restaurant.model import Restaurant
from floorPlan.model import FloorPlan
from user.model import User
from uuid import UUID, uuid4
from datetime import datetime

class FoodItem(BaseModel):
    name: str
    price: Measurement
    offer: Optional[Discount]

class OrderStatusEnum(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    UNPAID = "unpaid"
    PAID = "paid"

class Order(Document):
    id: UUID = Field(default_factory=uuid4)
    status: OrderStatusEnum
    food_items: FoodItem
    restaurant: Link[Restaurant]
    floor_plan: Link[FloorPlan]
    table_number: str
    total_price: Measurement
    discounted_price: Measurement
    created_by: Link[User]
    served_by: Link[User]
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()