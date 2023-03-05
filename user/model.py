from beanie import Document, Indexed
from pydantic import EmailStr, constr, root_validator
from typing import Optional
from datetime import datetime
from enum import Enum

from base.model import Base

class UserTypeEnum(str, Enum):
    ADMIN = 'admin'
    RESTAURANT = 'restaurant'
    USER = 'user'
    
class GenderEnum(str, Enum):
    MALE ='male'
    FEMALE = 'female'
    OTHER = 'other'

class User(Base, Document):
    name: Optional[str]
    email : Optional[Indexed(EmailStr, unique=True, partialFilterExpression={'email': {'$type': 'string'}})]
    phone : Optional[Indexed(constr(regex=r'^([+]{1}[8]{2}(01){1}[3-9]{1}\d{8})$'), unique=True, partialFilterExpression={'phone': {'$type': 'string'}})]
    password: Optional[str]
    user_type: UserTypeEnum
    gender: Optional[GenderEnum]
    date_of_birth: Optional[datetime]
    last_login: datetime = datetime.now()
    
    @root_validator
    def validate_credentials(cls, values):
        if (values.get('user_type') == UserTypeEnum.ADMIN or values.get('user_type') == UserTypeEnum.RESTAURANT) and\
        (values.get('password') is None or values.get('email') is None):
            raise ValueError('Please provide email and password')
        
        if values.get('user_type') == UserTypeEnum.USER and values.get('phone') is None:
            raise ValueError('Please provide phone number')