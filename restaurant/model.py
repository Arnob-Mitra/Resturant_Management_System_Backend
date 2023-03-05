from beanie import Document, Link
from uuid import UUID
from typing import Optional
from enum import Enum
from base.model import Address, Base, Discount

class ModeEnum(str, Enum):
    DINE_IN = "dine in"
    TAKE_AWAY = "take away"
    DELIVERY = "delivery"
    DINE_IN_TAKE_AWAY = "dine in and take away"
    DINE_IN_DELIVERY = "dine in and delivery"
    TAKE_AWAY_DELIVERY = "take away and delivery"
    ALL = "all options"  

class Restaurant(Base, Document):
    name: str
    mode: ModeEnum
    chain_of: Optional[UUID] 
    cuisine_types: list[str] = []
    categories: list[str] = []
    address: Address
    images: Optional[list[str]]
    discounts: Optional[list[Discount]]