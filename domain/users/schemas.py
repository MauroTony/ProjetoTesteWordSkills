from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    password: str
    celular: str
    nome: str
    img_perfil_base64: Optional[str] = None

class Userlogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
