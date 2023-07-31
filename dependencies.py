from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from domain.users.repositories import UserRepository
from domain.users.services import UserService
from infrastructure.dependencies import get_db

ALGORITHM = "HS256"
SECRET_KEY = "your-secret-key"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        #token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user = user_service.get_user_by_email(username)
    if user is None:
        raise credentials_exception
    return user
