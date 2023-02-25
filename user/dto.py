from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from .model import UserTypeEnum
from uuid import UUID

class CreateDTO(BaseModel):
    phone: str
    password: str
    user_type: UserTypeEnum

class UpdateUserDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    
class ResponseDTO(BaseModel):
    id:UUID
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: str
    user_type: UserTypeEnum
    is_active: bool    
    
class LoginDTO(BaseModel):
    phone: str
    password: str
    
class ChangePasswordDTO(BaseModel):
    old_password: str
    new_password: str