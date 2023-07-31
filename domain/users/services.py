from .repositories import UserRepository
from .models import User
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: int):
        return self.user_repository.get_user(user_id)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def get_user_by_cellphone(self, cellphone: str):
        return self.user_repository.get_user_by_cellphone(cellphone)

    def create_user(self, email: str, password: str, nome: str, celular: str, img_perfil: str):
        hashed_password = self.get_password_hash(password)
        user = User(email=email, hashed_password=hashed_password, nome=nome, celular=celular, img_perfil_base64=img_perfil)
        return self.user_repository.create_user(user)

    def authenticate_user(self, email: str, password: str):
        user = self.get_user_by_email(email)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def get_password_hash(self, password):
        return pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)