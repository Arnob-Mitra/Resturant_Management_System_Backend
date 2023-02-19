from pydantic import BaseModel
from uuid import UUID
from .model import Price, Discount

class FoodItemDTO(BaseModel):
    restaurant:UUID 
    name:str
    description:str
    category:str
    cuisine:str
    price:Price
    currency: str
    recipe:dict[str, Discount]
     