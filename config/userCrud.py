from sqlalchemy.orm import Session
from models.user import User

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str):
    db_user = User(email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: User, new_attributes: dict()):
    for attr, value in new_attributes.items():
        setattr(db_user, attr, value)
    db.commit()
    db.refresh(db_user)
    return db_user
