from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class CreateDTO(BaseModel):
    name: str
    permission: dict[str, int]
    admin: bool
    
class UpdateDTO(BaseModel):
    restaurant: Optional[UUID]
    
class ResponseDTO(BaseModel):
    id: UUID
    name: str
    permission: dict[str, int]
    restaurant: Optional[UUID]
    admin: bool