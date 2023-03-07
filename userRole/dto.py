from pydantic import BaseModel
from uuid import UUID
from restaurant.model import Restaurant
from user.model import User
from role.model import Role
from typing import Optional
from beanie import Link

class CreateDTO(BaseModel):
    user: UUID
    role: UUID
    restaurant: UUID

class UpdateDTO(BaseModel):
    user: Optional[UUID]
    role: Optional[UUID]
    restaurant: Optional[UUID]

class ResponseDTO(BaseModel):
    id: UUID
    user: Link[User]
    role: Role
    restaurant: Link[Restaurant]