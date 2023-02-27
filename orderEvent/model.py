from typing import Optional
from beanie import Document
from user.model import User
from order.model import FoodItem
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime
from enum import Enum

class OrderEventEnum(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    UNPAID = "unpaid"
    PAID = "paid"
 
class OrderEvent(Document):
    id: UUID = Field(default_factory=uuid4)
    event: OrderEventEnum
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: User
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
