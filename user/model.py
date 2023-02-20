from beanie import Document 
from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional
from datetime import datetime

class User(Document):
    id: UUID = Field(default_factory= uuid4)
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: str
    user_type: str
    is_active: bool = True
    last_login: datetime = datetime.now()
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()