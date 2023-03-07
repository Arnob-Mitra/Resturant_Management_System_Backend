from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from .model import UserTypeEnum, GenderEnum
from uuid import UUID
from datetime import datetime

class CreateDTO(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: constr(regex=r'^(?=.*[A-Za-z])(?=.*\d)[@$!%*#?&A-Za-z\d]{8,}$')
    phone: Optional[str]
    gender: Optional[GenderEnum]
    date_of_birth: Optional[datetime]
    user_type: UserTypeEnum

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
    password: constr(regex=r'^(?=.*[A-Za-z])(?=.*\d)[@$!%*#?&A-Za-z\d]{8,}$')
    
class ChangePasswordDTO(BaseModel):
    old_password: constr(regex=r'^(?=.*[A-Za-z])(?=.*\d)[@$!%*#?&A-Za-z\d]{8,}$')
    new_password: constr(regex=r'^(?=.*[A-Za-z])(?=.*\d)[@$!%*#?&A-Za-z\d]{8,}$')