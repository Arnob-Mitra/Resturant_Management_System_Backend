from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class CreateDTO(BaseModel):
    phone: str
    password: str
    user_type: str

class UpdateUserDTO(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    last_login: Optional[datetime]
    
class ResponseDTO(BaseModel):
    id: UUID
    name: Optional[str]
    phone: str
    email: Optional[str]
    password: str
    user_type: str
    is_active: bool    
    
class LoginDTO(BaseModel):
    phone: str
    password: str