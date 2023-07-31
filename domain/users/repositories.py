from sqlalchemy.orm import Session
from .models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_cellphone(self, cellphone: str):
        return self.db.query(User).filter(User.celular == cellphone).first()

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
