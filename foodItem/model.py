from beanie import Document
from pydantic import Field
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum 

#class allCurrency (Enum):
#    BDT:str ="BDT"



class FoodItem(Document):
    id:UUID = Field(default_factory=uuid4)
    restaurant:UUID 
    name:str
    description:str
    foodType:str
    price:float
    currency: str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()