from beanie import Document
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import Field

class FoodItemEvents(Document):
    id:UUID = Field(default_factory=uuid4)
    foodItem:UUID
    event:str
    value_from:int
    value_to:int
    createdAt:datetime = datetime.now()