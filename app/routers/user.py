from app.dependencies import get_db
from app.managers.user_manager import user_manager
from app.schemas.user import User
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/users", response_model=list[User], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return user_manager.all(db)


@router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    _user = user_manager.create(db, user)
    return _user
