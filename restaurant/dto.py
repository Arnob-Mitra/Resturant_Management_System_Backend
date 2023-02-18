from pydantic import BaseModel
from uuid import UUID

class RestaurantDTO(BaseModel):
    managedBy:UUID 
    name:str
    chainOf:UUID 
    ratings:str
    images:str
    cuisineType:str