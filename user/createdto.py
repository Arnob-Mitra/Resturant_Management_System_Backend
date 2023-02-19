from pydantic import BaseModel

class UserDTO(BaseModel):
    phone:str
    password:str
    userType:str
    isActive:bool 