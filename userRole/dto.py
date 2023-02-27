from pydantic import BaseModel
from uuid import UUID
from restaurant.model import Restaurant
from user.model import User
from role.model import Role

class CreateDTO(BaseModel):
    user: User
    role: Role

class UpdateDTO(BaseModel):
    user: User
    role: Role

class ResponseDTO(BaseModel):
    id: UUID
    user: User
    role: Role
    restaurant: Restaurant