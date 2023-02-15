from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4

class Restaurant(Document):
    _id:UUID = uuid4()
    managedBy:UUID = uuid4()
    name:str
    address:str
    chainOf:UUID = uuid4()
    rating:str
    offers:str
    cuisineType:str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()