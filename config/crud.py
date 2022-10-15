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

def get_property(db: Session, property_id: int):
    return db.query(models.Property).filter(models.Property.id == property_id).first()

def create_property(db: Session, direction: str, province: str, location: str, country: str, toilets: int, rooms: int, people: int, description: str, user_id: int):
    db_property = models.Property(
                                    direction=direction, 
                                    province=province, 
                                    location=location, 
                                    country=country, 
                                    toilets=toilets, 
                                    rooms=rooms,
                                    people=people, 
                                    description=description, 
                                    user_id=user_id)
    db.add(db_property)
    db.commit() 
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int):
    db_property = get_property(db, property_id)
    if db_property is not None:
        db.delete(db_property)
        db.commit()
    return db_property