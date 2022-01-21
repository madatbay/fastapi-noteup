from fastapi import APIRouter, status
from schemas.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    """
    Create a new user
    """
    return user
