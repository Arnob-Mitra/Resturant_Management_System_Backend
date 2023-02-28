from beanie import Document, Link
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import Field
from restaurant.model import Restaurant
from enum import Enum
from base.model import Base

class RatingEnum(str, Enum):
    VERY_GOOD = "very good"
    GOOD = "good"
    AVERAGE = "average"
    BAD = "bad"
    VERY_BAD = "very bad"

class Rating(Base, Document):
    restaurant: Link[Restaurant]
    ambience: RatingEnum
    taste: RatingEnum
    cleanliness: RatingEnum
    staff: RatingEnum
    budget_friendly: RatingEnum