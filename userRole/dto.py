from pydantic import BaseModel
from uuid import UUID
from restaurant.model import Restaurant
from user.model import User
from role.model import Role
from typing import Optional

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
    user: User
    role: Role
    restaurant: Restaurant