from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional
from enum import Enum
from base.model import Address, Discount

class ModeEnum(str, Enum):
    DINE_IN = "dine in"
    TAKE_AWAY = "take away"
    DELIVERY = "delivery"
    DINE_IN_TAKE_AWAY = "dine in and take away"
    DINE_IN_DELIVERY = "dine in and delivery"
    TAKE_AWAY_DELIVERY = "take away and delivery"
    ALL = "all options"  

class Restaurant(Document):
    id:UUID = Field(default_factory=uuid4)
    name: str
    mode: ModeEnum
    #chain_of: Optional[Restaurant]
    cuisine_types: str
    categories: str
    address: Address
    images: Optional[str]
    discounts: Optional[Discount]
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()