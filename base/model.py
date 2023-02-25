from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class DateFrequencyEnum(str, Enum):
    daily = "daily"
    weekly_sunday = "weekly sunday"
    weekly_monday = "weekly monday"
    weekly_tuesday = "weekly tuesday"
    weekly_wednesday = "weekly wednesday"
    weekly_thursday = "weekly thursday"
    weekly_friday = "weekly friday"
    weekly_saturday = "weekly saturday"
    biweekly_sunday = "biweekly- sunday"
    biweekly_monday = "biweekly monday"
    biweekly_tuesday = "biweekly tuesday"
    biweekly_wednesday = "biweekly wednesday"
    biweekly_thursday = "biweekly thursday"
    biweekly_friday = "biweekly friday"
    biweekly_saturday = "biweekly saturday"
    monthly_first_sunday = "monthly first sunday"
    monthly_first_monday = "monthly first monday"
    monthly_first_tuesday = "monthly first tuesday"
    monthly_first_wednesday = "monthly first wednesday"
    monthly_first_thursday = "monthly first thursday"
    monthly_first_friday = "monthly first friday"
    monthly_first_saturday = "monthly first saturday"
    monthly_last_sunday = "monthly last sunday"
    monthly_last_monday = "monthly last monday"
    monthly_last_tuesday = "monthly last tuesday"
    monthly_last_wednesday = "monthly last wednesday"
    monthly_last_thursday = "monthly last thursday"
    month_last_friday = "monthly last friday"
    month_last_saturday = "monthly last saturday"

#class DiscountTypeEnum(str, Enum):
    

class Base(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    create_at:datetime = datetime.now()
    update_at:datetime = datetime.now()
    
class Address(BaseModel):
    home_info: Optional[str]
    street: str
    administrative_locality3: str
    administrative_locality2: str
    administrative_locality1: str
    country: str
    post_code: str    
    
class RangeString(BaseModel):
    value_from: str
    value_to: str
    
class Measurement(BaseModel):
    value: float
    unit: str
    
class Discount(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    discount_type: str
    code: Optional[str]
    validation_date_range: Optional[RangeString]
    validation_time_range: Optional[RangeString]
    discounted_amount: Optional[Measurement]
    date_frequency: Optional[DateFrequencyEnum]
    price_limit: Optional[float]           