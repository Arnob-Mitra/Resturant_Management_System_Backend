from pydantic import BaseModel
from uuid import UUID

class FoodItemEventsDTO(BaseModel):
    foodItem:UUID
    event:str
    value_from:int
    value_to:int