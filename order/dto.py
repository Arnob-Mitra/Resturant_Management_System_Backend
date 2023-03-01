from pydantic import BaseModel
from order.model import FoodItem
from order.model import OrderStatusEnum
from uuid import UUID
from restaurant.model import Restaurant
from floorPlan.model import FloorPlan 
from base.model import Measurement
from user.model import User
from beanie import Link
from typing import Optional

class CreateDTO(BaseModel):
    status: OrderStatusEnum 
    food_items: FoodItem
    restaurant: Link[Restaurant]
    floor_plan: Link[FloorPlan]
    table_number: str
    total_price: Measurement
    discounted_price: Measurement
    created_by: Link[User]
    served_by: Link[User]
    
class UpdateDTO(BaseModel):
    status: Optional[OrderStatusEnum]
    food_items: Optional[FoodItem]
    restaurant: Optional[Link[Restaurant]]
    floor_plan: Optional[Link[FloorPlan]]
    table_number: Optional[str]
    total_price: Optional[Measurement]
    discounted_price: Optional[Measurement]
    created_by: Optional[Link[User]]
    served_by: Optional[Link[User]]
    
class ResponseDTO(BaseModel):
    id: UUID
    status: OrderStatusEnum 
    food_items: FoodItem
    restaurant: Link[Restaurant]
    floor_plan: Link[FloorPlan]
    table_number: str
    total_price: Measurement
    discounted_price: Measurement
    created_by: Link[User]
    served_by: Link[User] 