# fastapi_contacts/app/models.py

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from fastapi_contacts.app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class UserCreate(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}  # Add this line
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
