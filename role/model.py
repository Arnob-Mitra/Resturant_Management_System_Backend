from beanie import Document
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from base.model import Base

class RolePermission(BaseModel):
    name: str
    permission: int

class Role(Base, Document):
    name: str
    permission: list[RolePermission]
    restaurant: Optional[UUID]
    admin: bool