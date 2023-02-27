from beanie import Document, Link
from restaurant.model import Restaurant
from user.model import User
from role.model import Role
from uuid import UUID, uuid4
from pydantic import Field
from datetime import datetime

class UserRole(Document):
    id: UUID = Field(default_factory=uuid4)
    user: Link[User]
    role: Link[Role]
    restaurant: Link[Restaurant]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()