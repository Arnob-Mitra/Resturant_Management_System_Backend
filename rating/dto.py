from pydantic import BaseModel
from rating.model import RatingEnum
from uuid import UUID
from restaurant.model import Restaurant
from beanie import Link
from typing import Optional

class CreateDTO(BaseModel):
    restaurant: Link[Restaurant]
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum
    
class UpdateDTO(BaseModel):
    restaurant: Optional[Link[Restaurant]]
    ambience: Optional[RatingEnum]
    taste: Optional[RatingEnum]
    cleanliness: Optional[RatingEnum]
    staff: Optional[RatingEnum]
    budget_friendly: Optional[RatingEnum]  
    
class ResponseDTO(BaseModel):
    id: UUID
    restaurant: Link[Restaurant]
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum