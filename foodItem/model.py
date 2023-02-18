from beanie import Document
from pydantic import Field, BaseModel
from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
#from enum import Enum 

#class allCurrency (Enum):
#    BDT:str ="BDT"

class Price(BaseModel):
    value:float
    currency:str

class Discount(BaseModel):
    value:float
    unit:str

class Offers(BaseModel):
    discount:Discount 
    limit:Optional[float]
    
    

class FoodItem(Document):
    id:UUID = Field(default_factory=uuid4)
    restaurant:UUID 
    name:str
    description:str
    category:str
    cuisine:str
    foodType:str
    price:float
    currency: str
    recipe:dict[str, Discount]
    image: str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()
    offers:Optional[Offers]
    
    