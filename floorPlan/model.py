from beanie import Document 
from datetime import datetime 
from uuid import UUID, uuid4

class FloorPlan(Document):
    _id:UUID = uuid4()
    restaurant:UUID = uuid4()
    floorNumber:int 
    detail:str
    createdAt:datetime = datetime.now()
    updatedAt:datetime = datetime.now()