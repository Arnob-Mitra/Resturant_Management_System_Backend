from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from base.model import Address, Discount
from .model import Restaurant, ModeEnum

class CreateDTO(BaseModel):
    name: str
    cuisine_types: str
    categories: str
    address: Address

class UpdateDTO(BaseModel):
    chain_of: Optional[Restaurant]
    image:Optional[str]    
    discounts: Optional[Discount]

class ResponseDTO(BaseModel):
    id: UUID 
    name: str
    mode: ModeEnum
    chain_of: Optional[Restaurant]
    cuisine_type: str
    categories: str
    address:Address
    images:Optional[str]
    discounts: Optional[Discount]      