from pydantic import BaseModel
from rating.model import RatingEnum
from uuid import UUID
from restaurant.model import Restaurant

class CreateDTO(BaseModel):
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum
    
class UpdateDTO(BaseModel):
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum    
    
class ResponseDTO(BaseModel):
    id: UUID
    restaurant: Restaurant
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum