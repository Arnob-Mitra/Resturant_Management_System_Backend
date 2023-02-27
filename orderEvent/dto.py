from pydantic import BaseModel
from typing import Optional
from order.model import FoodItem
from user.model import User
from uuid import UUID

class CreateDTO(BaseModel):
    event: str
    created_by: User

class UpdateDTO(BaseModel):
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    
class ResponseDTO(BaseModel):
    id: UUID
    event: str
    added: Optional[FoodItem]
    #removed: Optional[]
        