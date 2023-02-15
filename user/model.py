from beanie import Document 
from uuid import UUID, uuid4

class User(Document):
    _id:UUID = uuid4()
    name:str
    phone:str
    email:str
    password:str
    userType:str
    isActive:bool 