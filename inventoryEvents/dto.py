from pydantic import BaseModel
from uuid import UUID

class InventoryEvents(BaseModel):
    inventory:UUID 
    event:str
    value_from:int
    value_to:int