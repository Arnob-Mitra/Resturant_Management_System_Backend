from beanie import Document
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import Field
from restaurant.model import Restaurant
from enum import Enum

class RatingEnum(str, Enum):
    very_good = "very good"
    good = "good"
    average = "average"
    bad = "bad"
    very_bad = "very bad"

class Rating(Document):
    id: UUID = Field(default_factory=uuid4)
    restaurant: Restaurant
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()