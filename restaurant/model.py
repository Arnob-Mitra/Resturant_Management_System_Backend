from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field, BaseModel
from typing import Optional

class Coupons(BaseModel):
    id:UUID = Field(default_factory=uuid4) 
    code:str
    validTil:datetime = datetime.now()
    maxUse:int 
        
class Ratings(BaseModel):
    ambience:str
    taste:str
    cleanliness:str
    staff:str
    budgetFriendly:str
    
class Address(BaseModel):
    country:str    

class Restaurant(Document):
    id:UUID = Field(default_factory=uuid4)
    managedBy:UUID 
    name:str
    address:Address
    chainOf:UUID 
    coupons:Optional[Coupons]
    ratings:Optional[Ratings]
    images:str
    cuisineType:str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()