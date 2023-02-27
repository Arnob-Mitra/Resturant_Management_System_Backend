from typing import Optional
from beanie import Document, Link
from user.model import User
from order.model import FoodItem
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime
from enum import Enum
 
class OrderEvent(Document):
    id: UUID = Field(default_factory=uuid4)
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: Link[User]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()