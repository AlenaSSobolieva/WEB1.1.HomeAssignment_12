from sqlalchemy.orm import Session
from fastapi_contacts.app.models import User
from fastapi_contacts.app import models

def create_user(db: Session, user: models.UserCreate):
    db_user = User(email=user.email, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
