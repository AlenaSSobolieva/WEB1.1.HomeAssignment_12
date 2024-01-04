from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi_contacts.app import crud, models, database, authentication

router = APIRouter()

@router.post("/register", response_model=models.User)  # Use User as response model
async def register_user(user: models.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already registered with this email")
    created_user = crud.create_user(db=db, user=user)
    return models.User(**created_user.dict())

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordBearer = Depends()):
    return {"access_token": form_data, "token_type": "bearer"}

@router.get("/users/me", response_model=models.User)
def read_users_me(current_user: models.User = Depends(authentication.get_current_user)):
    return current_user

@router.get("/items/")
def read_item(token: str = Depends(authentication.oauth2_scheme)):
    return {"token": token}

