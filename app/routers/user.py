from typing import Any

from app.core.auth import authenticate, create_access_token
from app.dependencies import get_current_user, get_db
from app.managers.user_manager import user_manager
from app.models.user import User as UserModel
from app.schemas.user import User, UserCreate
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/all", response_model=list[User], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    return user_manager.all(db)


@router.post("/login")
def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    Get the JWT token for user with OAuth2
    """
    user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrent username or password")

    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer",
    }


@router.get("/initial/")
def get_initial(current_user: UserModel = Depends(get_current_user)):
    """
    Fetch the current logged in user.
    """
    return current_user


@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
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
        detail="The user with this email already exists",
    )
