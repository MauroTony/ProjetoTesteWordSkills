from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from infrastructure.dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm

from .models import User as UserModel
from .schemas import UserBase, User, Token, Userlogin
from .services import UserService
from .repositories import UserRepository
from dependencies import get_current_user

router = APIRouter()


@router.post("/users/")
def create_user(user: UserBase, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    existing_user = user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    existing_user = user_service.get_user_by_cellphone(user.celular)
    if existing_user:
        raise HTTPException(status_code=400, detail="Cellphone already registered")
    return user_service.create_user(user.email, user.password, user.nome, user.celular, user.img_perfil_base64)


@router.get("/users/me")
def read_users_me(current_user: UserModel = Depends(get_current_user)):
    return current_user


@router.post("/login")
def login_for_access_token(form_data: Userlogin, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user = user_service.authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = user_service.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
