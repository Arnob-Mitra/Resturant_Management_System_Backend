from beanie import Document 
from typing import Optional
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4
from pydantic import Field

from base.model import Base

class UserTypeEnum(str, Enum):
    ADMIN = 'admin'
    RESTAURANT = 'restaurant'
    USER = 'user'

class User(Base, Document):
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: Optional[str]
    user_type: UserTypeEnum
    is_active: bool = True
    last_login: datetime = datetime.now()