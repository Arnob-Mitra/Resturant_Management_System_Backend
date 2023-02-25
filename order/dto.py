from pydantic import BaseModel
from .model import FoodItem
from uuid import UUID
from datetime import datetime
from restaurant.model import Restaurant
from floorPlan.model import FloorPlan 
from base.model import Measurement
from user.model import User

class CreateDTO(BaseModel):
    food_items: FoodItem
    table_number: str
    
class UpdateDTO(BaseModel):
    status: str
    table_number: str
    
class ResponseDTO(BaseModel):
    id: UUID
    status: str
    food_items: FoodItem
    restaurant: Restaurant
    floor_plan: FloorPlan
    table_number: str
    total_price: Measurement
    discounted_price: Measurement
    created_by: User
    served_by: User
    
           