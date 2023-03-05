from pydantic import BaseModel, EmailStr
from typing import Optional
from .model import UserTypeEnum, GenderEnum
from uuid import UUID
from datetime import datetime

class CreateDTO(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str
    phone: Optional[str]
    gender: Optional[GenderEnum]
    date_of_birth: Optional[datetime]
    user_type: Optional[UserTypeEnum]

class UpdateDTO(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    gender: Optional[GenderEnum]
    date_of_birth: Optional[datetime]
    
class ResponseDTO(BaseModel):
    id:UUID
    name: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    user_type: UserTypeEnum
    is_active: bool    
    
class LoginDTO(BaseModel):
    email: EmailStr
    password: str
    
class ChangePasswordDTO(BaseModel):
    old_password: str
    new_password: str