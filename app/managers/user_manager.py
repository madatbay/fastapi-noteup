

from app.managers.base_manager import BaseManager
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate

class UserManager(BaseManager[UserModel, UserCreate, UserUpdate]):
    ...

user_manager = UserManager(UserModel)