from sqlalchemy.orm import Session
from schemas.propertySchema import PropertySchema
from models.propertie import Property
from models.image import Image


def get_property(db: Session, property_id: int):
    return db.query(Property).filter(Property.id == property_id).first()


def get_properties_by_user_id(db: Session, user_id: int):
    return db.query(Property).filter(Property.user_id == user_id).all()


def create_property(db: Session, propertySchema: PropertySchema, user_id: int):
    db_property = Property(**propertySchema.dict(exclude={'images', 'email_user'}), user_id=user_id)
    for img in propertySchema.images:
        db_property.images.append(Image(link=img.link, property_id=db_property.id))
    db.add(db_property)
    db.commit()
    db.refresh(db_property)
    return db_property


def delete_property(db: Session, db_property):
    db.delete(db_property)
    db.commit()
    return db_property


def update_property(db: Session, db_property, propertySchema: PropertySchema):
    for attr, value in propertySchema.dict(exclude={'images', 'email_user'}).items():
        setattr(db_property, attr, value)
    db.query(Image).filter(Image.property_id == db_property.id).delete()
    for img in propertySchema.images:
        db_property.images.append(Image(link=img.link, property_id=db_property.id))
    db.add(db_property)
    db.commit()
    return db_property