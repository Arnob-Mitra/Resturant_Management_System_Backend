from beanie import Document
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional
from enum import Enum
from base.model import Address, Discount
#from .model import Restaurant

class ModeEnum(str, Enum):
    dine_in = "dine in"
    take_away = "take away"
    delivery = "delivery"
    dine_in_take_away = "dine in and take away"
    dine_in_delivery = "dine in and delivery"
    take_away_delivery = "take away and delivery"
    all = "all options"  

class Restaurant(Document):
    id:UUID = Field(default_factory=uuid4)
    name: str
    mode: ModeEnum
    chain_of: Optional[str]
    cuisine_types: list[str] = []
    categories: list[str] = []
    address: Address
    images: Optional[str]
    discounts: Optional[Discount]
    created_at:datetime = datetime.now()
    updated_at:datetime = datetime.now()