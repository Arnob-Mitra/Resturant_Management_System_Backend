from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreateDTO(BaseModel):
    phone: str
    password: str
    user_type: str

class UpdateUserDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    last_login: Optional[datetime]