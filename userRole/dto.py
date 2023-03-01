from pydantic import BaseModel
from uuid import UUID
from restaurant.model import Restaurant
from user.model import User
from role.model import Role
from beanie import Link
from typing import Optional

class CreateDTO(BaseModel):
    user: Link[User]
    role: Link[Role]
    restaurant: Link[Restaurant]

class UpdateDTO(BaseModel):
    user: Optional[Link[User]]
    role: Optional[Link[Role]]
    restaurant: Optional[Link[Restaurant]]

class ResponseDTO(BaseModel):
    id: UUID
    user: Link[User]
    role: Link[Role]
    restaurant: Link[Restaurant]