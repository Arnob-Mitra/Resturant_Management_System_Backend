from typing import Optional
from beanie import Document
from user.model import User
from order.model import FoodItem
from enum import Enum
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime

#class OrderEventEnum(str, Enum):
    

class OrderEvent(Document):
    id: UUID = Field(default_factory=uuid4)
    event: str
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: User
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
