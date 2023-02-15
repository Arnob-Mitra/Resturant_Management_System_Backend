from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4

class Inventory(Document):
    _id:UUID = uuid4()
    entity:UUID = uuid4()
    name = str
    quantity = int 
    restockQuantity = int 
    quantityType = str
    cost = float
    currency = str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()