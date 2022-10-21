from models.users import User
from config.db import db
from schemas.user_login_schema import UserLoginSchema


def get_user(email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(user: UserLoginSchema):
    db_user = User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
