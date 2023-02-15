from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4


class InventoryEvents(Document):
    _id:UUID = uuid4()
    inventory:UUID = uuid4()
    event:str
    value_from:int
    value_to:int
    createdAt:datetime = datetime.now()