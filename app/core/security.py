from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(raw_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(raw_password, hashed_password)

def hash_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)