from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String

from app.database.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), nullable=False)
    name = Column(String(256), index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
