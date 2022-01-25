from typing import Optional

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.core.auth import oauth2_scheme
from app.core.config import settings
from app.database.session import SessionLocal
from app.models.user import User


class TokenData(BaseModel):
    username: Optional[str] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    CredentialsException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException
        token_data = TokenData(username=username)
    except JWTError as error:
        raise HTTPException(status_code=400, detail=f"{error}")

    user = db.query(User).filter(User.id == token_data.username).first()
    if user is None:
        raise CredentialsException
    return user
