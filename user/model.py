from beanie import Document 
from typing import Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
from pydantic import Field

class UserTypeEnum(str, Enum):
    ADMIN = 'admin'
    RESTAURANT = 'restaurant'
    USER = 'user'

class User(Document):
    id:UUID = Field(default_factory = uuid4)
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: Optional[str]
    user_type: UserTypeEnum
    is_active: bool = True
    last_login: datetime = datetime.now()
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()