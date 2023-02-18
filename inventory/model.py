from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field, BaseModel


class Price(BaseModel):
    value:float
    currency:str

class Quantity(BaseModel):
    value:float
    restockAlert:float
    unit:str

class Inventory(Document):
    id:UUID = Field(default_factory= uuid4())
    entity:UUID 
    name:str
    price:Price
    quantity:int 
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()