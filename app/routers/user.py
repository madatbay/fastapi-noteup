from app.dependencies import get_db
from app.managers.user_manager import user_manager
from app.schemas.user import User, UserCreate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all", response_model=list[User], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return user_manager.all(db)

@router.get('/{user_id}', response_model=User, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_manager.get(db=db, id=user_id)

@router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    if not user_manager.get_by_email(db=db, email=user.email):
        return user_manager.create(db=db, obj_in=user)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="The user with this email already exists"
    )
