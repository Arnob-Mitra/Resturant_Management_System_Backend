from pydantic import BaseModel
from typing import Optional
from order.model import FoodItem
from user.model import User
from uuid import UUID
from beanie import Link

class CreateDTO(BaseModel):
    created_by: Link[User]

class UpdateDTO(BaseModel):
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: Optional[Link[User]]
    
class ResponseDTO(BaseModel):
    id: UUID
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    created_by: Link[User]
        