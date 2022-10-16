from sqlalchemy.orm import Session
from models import models
from schemas import schemas

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

def get_properties_by_user_id(db: Session, user_id: int):
    return db.query(models.Property).filter(models.Property.user_id == user_id).all()

def create_property(db: Session, propertySchema: schemas.PropertySchema, user_id: int):
    db_property = models.Property(
                                    direction=propertySchema.direction, 
                                    province=propertySchema.province, 
                                    location=propertySchema.location, 
                                    country=propertySchema.country, 
                                    toilets=propertySchema.toilets, 
                                    rooms=propertySchema.rooms,
                                    people=propertySchema.people, 
                                    description=propertySchema.description, 
                                    user_id=user_id
                                 )
    db.add(db_property)
    db.commit() 
    db.refresh(db_property)
    return db_property

def delete_property(db: Session, property_id: int, user_id: int):
    db_property = get_property(db, property_id)
    
    if (db_property is None) or (db_property.user_id != user_id):
        return None
    
    db.delete(db_property)
    db.commit()
    return db_property

def update_property(db: Session, property_id: int, user_id: int, propertySchema: schemas.PropertySchema):
    db_property = get_property(db, property_id)
    
    if (db_property is None) or (db_property.user_id != user_id):
        return None
    
    db_property.direction = propertySchema.direction
    db_property.province = propertySchema.province 
    db_property.location = propertySchema.location 
    db_property.country = propertySchema.country 
    db_property.toilets = propertySchema.toilets 
    db_property.rooms = propertySchema.rooms
    db_property.people = propertySchema.people 
    db_property.description = propertySchema.description 
                                 
    db.add(db_property)
    db.commit()
    return db_property
