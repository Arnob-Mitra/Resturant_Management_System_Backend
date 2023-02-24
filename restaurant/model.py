from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field, BaseModel
from typing import Optional

class Coupons(BaseModel):
    id:UUID = Field(default_factory=uuid4) 
    code:str
    valid_til:datetime = datetime.now()
    max_use:int 
        
class Ratings(BaseModel):
    ambience:str
    taste:str
    cleanliness:str
    staff:str
    budget_friendly:str
    
class Address(BaseModel):
    country:str    

class Restaurant(Document):
    id:UUID = Field(default_factory=uuid4)
    managed_by:UUID 
    name:str
    address:Address
    chain_of:UUID 
    coupons:Optional[Coupons]
    ratings:Optional[Ratings]
    images:Optional[str]
    cuisine_type:str
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()