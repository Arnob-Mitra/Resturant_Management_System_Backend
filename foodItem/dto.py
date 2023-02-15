from pydantic import BaseModel
from uuid import UUID

class FoodItemDTO(BaseModel):
    restaurant:UUID
    name:str
    description:str
    foodType:str
    price:float
    currency:str