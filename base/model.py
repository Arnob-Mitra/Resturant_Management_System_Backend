from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class DateFrequencyEnum(str, Enum):
    DAILY = "daily"
    WEEKLY_SUNDAY = "weekly sunday"
    WEEKLY_MONDAY = "weekly monday"
    WEEKLY_TUESDAY = "weekly tuesday"
    WEEKLY_WEDNESDAY = "weekly wednesday"
    WEEKLY_THURSDAY = "weekly thursday"
    WEEKLY_FRIDAY = "weekly friday"
    WEEKLY_SATURDAY = "weekly saturday"
    BIWEEKLY_SUNDAY = "biweekly- sunday"
    BIWEEKLY_MONDAY = "biweekly monday"
    BIWEEKLY_TUESDAY = "biweekly tuesday"
    BIWEEKLY_WEDNESDAY = "biweekly wednesday"
    BIWEEKLY_THURSDAY = "biweekly thursday"
    BIWEEKLY_FRIDAY = "biweekly friday"
    BIWEEKLY_SATURDAY = "biweekly saturday"
    MONTHLY_FIRST_SUNDAY = "monthly first sunday"
    MONTHLY_FIRST_MONDAY = "monthly first monday"
    MONTHLY_FIRST_TUESDAY = "monthly first tuesday"
    MONTHLY_FIRST_WEDNESDAY = "monthly first wednesday"
    MONTHLY_FIRST_THURSDAY = "monthly first thursday"
    MONTHLY_FIRST_FRIDAY = "monthly first friday"
    MONTHLY_FIRST_SATURDAY = "monthly first saturday"
    MONTHLY_LAST_SUNDAY = "monthly last sunday"
    MONTHLY_LAST_MONDAY = "monthly last monday"
    MONTHLY_LAST_TUESDAY = "monthly last tuesday"
    MONTHLY_LAST_WEDNESDAY = "monthly last wednesday"
    MONTHLY_LAST_THURSDAY = "monthly last thursday"
    MONTH_LAST_FRIDAY = "monthly last friday"
    MONTH_LAST_SATURDAY = "monthly last saturday"

class DiscountTypeEnum(str, Enum):
    COUPON = "coupon"
    DISCOUNT = "discount"
    
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
    discount_type: DiscountTypeEnum
    code: Optional[str]
    validation_date_range: Optional[RangeString]
    validation_time_range: Optional[RangeString]
    discounted_amount: Optional[Measurement]
    date_frequency: Optional[DateFrequencyEnum]
    price_limit: Optional[float]           