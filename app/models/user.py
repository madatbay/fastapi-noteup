from app.database.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), nullable=False)
    name = Column(String(256), index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    password = Column(String, nullable=False)
