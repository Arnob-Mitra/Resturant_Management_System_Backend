from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from role.model import RolePermission

class CreateDTO(BaseModel):
    name: str
    permission: list[RolePermission]
    restaurant: Optional[UUID]
    admin: bool 
    
class UpdateDTO(BaseModel):
    name: Optional[str]
    permission: Optional[list[RolePermission]]
    
class ResponseDTO(BaseModel):
    id: UUID
    name: str
    permission: list[RolePermission]
    restaurant: Optional[UUID]
    admin: bool