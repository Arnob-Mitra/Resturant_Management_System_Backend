from pydantic import BaseModel
from uuid import UUID

class Inventory(BaseModel):
    entity:UUID 
    name:str
    quantity:int 