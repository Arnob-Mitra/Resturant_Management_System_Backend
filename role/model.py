from beanie import Document
from typing import Optional
from uuid import UUID
from base.model import Base

class Role(Base, Document):
    name: str
    permission: dict[str, int]
    restaurant: Optional[UUID]
    admin: bool