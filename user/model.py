from beanie import Document 
from typing import Optional
from datetime import datetime
from enum import Enum

class UserTypeEnum(str, Enum):
    admin = "admin"
    restaurant = "restaurant"
    user = "user"

class User(Document):
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: Optional[str]
    user_type: UserTypeEnum
    is_active: bool = True
    last_login: datetime = datetime.now()