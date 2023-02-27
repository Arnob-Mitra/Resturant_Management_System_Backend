from pydantic import BaseModel
from typing import Optional
from order.model import FoodItem
from user.model import User
from uuid import UUID

class CreateDTO(BaseModel):
    created_by: User

class UpdateDTO(BaseModel):
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    
class ResponseDTO(BaseModel):
    id: UUID
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
        