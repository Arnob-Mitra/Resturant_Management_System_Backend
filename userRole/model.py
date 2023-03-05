from beanie import Document, Link
from restaurant.model import Restaurant
from user.model import User
from role.model import Role
from base.model import Base

class UserRole(Base, Document):
    user: Link[User]
    role: Role
    restaurant: Link[Restaurant]