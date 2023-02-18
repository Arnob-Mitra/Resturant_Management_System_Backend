from beanie import Document 
from datetime import datetime 
from uuid import UUID, uuid4
from pydantic import Field

class FloorPlan(Document):
    id:UUID = Field(default_factory= uuid4())
    restaurant:UUID 
    floorNumber:int 
    detail:str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()