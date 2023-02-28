from typing import Optional
from beanie import Document, Link
from user.model import User
from order.model import FoodItem
from base.model import Base
 
class OrderEvent(Base, Document):
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: Link[User]