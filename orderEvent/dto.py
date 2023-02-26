from pydantic import BaseModel
from typing import Optional
from order.model import FoodItem
from uuid import UUID

class UpdateDTO(BaseModel):
    added: Optional[FoodItem]
    removed: Optional[FoodItem]
    
class ResponseDTO(BaseModel):
    id: UUID
    event: str
    added: Optional[FoodItem]
    #removed: Optional[]
        