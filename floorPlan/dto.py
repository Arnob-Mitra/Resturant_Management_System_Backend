from pydantic import BaseModel
from uuid import UUID

class FloorPlan(BaseModel):
    restaurant:UUID 
    floorNumber:int 
    detail:str