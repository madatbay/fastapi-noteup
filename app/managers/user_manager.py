from typing import Optional
from app.core.security import hash_password
from app.managers.base_manager import BaseManager
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate
from sqlalchemy.orm import Session

class UserManager(BaseManager[UserModel, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[UserModel]:
        return db.query(UserModel).filter(UserModel.email == email).first()
    
    def create(self, db: Session, *, obj_in: UserCreate) -> UserModel:
        obj_in.password = hash_password(obj_in.password)
        return super().create(db, obj_in=obj_in)

user_manager = UserManager(UserModel)