from beanie import Document 
from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional
from datetime import datetime

class User(Document):
    id:UUID = Field(default_factory= uuid4)
    name:Optional[str]
    phone:str
    email:Optional[str]
    password:str
    userType:str
    isActive:bool 
    lastLogin:datetime = datetime.now()
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()