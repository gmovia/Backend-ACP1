from sqlalchemy.orm import Session
from models import models

def create_user(db: Session, email: str, password: str):
    db_user = models.User(email=email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
    
def create_property(db: Session, title: str, direction: str, province: str, country: str, price: int, user_id: int):
    db_property = models.Property(title=title, direction=direction, province=province, country=country, price=price, user_id=user_id)
    db.add(db_property)
    db.commit() 
    db.refresh(db_property)
    return db_property