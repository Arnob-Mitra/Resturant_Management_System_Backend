from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field

class InventoryEvents(Document):
    id:UUID = Field(default_factory=uuid4)
    inventory:UUID 
    event:str
    value_from:int
    value_to:int
    createdAt:datetime = datetime.now()