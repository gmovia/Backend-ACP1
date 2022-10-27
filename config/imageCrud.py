from sqlalchemy.orm import Session

from models.image import Image


def get_images_by_property_id(db: Session, property_id: int):
    return db.query(Image).filter(Image.property_id == property_id).all()
