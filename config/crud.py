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

