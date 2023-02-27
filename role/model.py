from beanie import Document
from typing import Optional
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime

class Role(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    permission: dict[str, int]
    restaurant: Optional[UUID]
    admin: bool
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    