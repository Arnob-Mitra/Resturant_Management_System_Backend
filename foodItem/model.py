from beanie import Document
from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from typing import Optional
from restaurant.model import Restaurant
from enum import Enum 

#class allCurrency (Enum):
#    BDT:str ="BDT"
class DateFrequencyEnum(Enum):
    daily: str = "daily"

class RangeString(BaseModel):
    value_from: str
    value_to: str

class Measurement(BaseModel):
    value:float
    unit:str

class Discount(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    discount_type: str
    code: Optional[str]
    validation_date_range: Optional[RangeString]
    validation_time_range: Optional[RangeString]
    discounted_amount: Optional[Measurement] 
    data_frequency: Optional[DateFrequencyEnum] 
    price_limit: Optional[float] 

class FoodItem(Document):
    restaurant: Restaurant 
    name: str
    description: str
    category: str
    cuisine: str
    price: Measurement
    recipe: dict[str, Measurement]
    image: Optional[str]
    offers: Optional[Discount]    