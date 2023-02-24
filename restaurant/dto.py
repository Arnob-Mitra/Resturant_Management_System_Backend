from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from .model import Address, Coupons, Ratings

class CreateDTO(BaseModel):
    managed_by:UUID 
    name:str
    address:Address
    chain_of:UUID 
    cuisine_type:str

class UpdateDTO(BaseModel):
    coupons:Optional[Coupons]
    ratings:Optional[Ratings]
    image:Optional[str]    

class ResponseDTO(BaseModel):
    id:UUID 
    managed_by:UUID 
    name:str
    address:Address
    chain_of:UUID 
    coupons:Optional[Coupons]
    ratings:Optional[Ratings]
    images:Optional[str]
    cuisine_type:str         