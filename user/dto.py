from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name:Optional[str]
    phone:str
    email:Optional[str]
    password:str
    userType:str
    isActive:bool 