from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from base.model import Address, Discount
from restaurant.model import ModeEnum

class CreateDTO(BaseModel):
    name: str
    mode: ModeEnum
    cuisine_types: list[str]
    categories: list[str]
    address: Address

class UpdateDTO(BaseModel):
    chain_of: Optional[UUID]
    name: str
    mode: ModeEnum
    cuisine_types: list[str]
    categories: list[str]
    address: Address
    image: Optional[list[str]]    
    discounts: Optional[list[Discount]]

class ResponseDTO(BaseModel):
    id: UUID 
    name: str
    mode: ModeEnum
    chain_of: Optional[UUID]
    cuisine_types: list[str]
    categories: list[str]
    address:Address
    images:Optional[list[str]]
    discounts: Optional[list[Discount]]      