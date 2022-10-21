from sqlalchemy.orm import Session
from models import models
from schemas import schemas

def get_publication(db: Session, publication_id: int):
    return db.query(models.Publication).filter(models.Publication.id == publication_id).first()

def get_publication_by_property_id(db: Session, property_id: int):
    return db.query(models.Publication).filter(models.Publication.property_id == property_id).first()

def create_publication(db: Session, publicationSchema: schemas.PropertySchema):
    db_publication = models.Publication(
                                        title=publicationSchema.title,
                                        description=publicationSchema.description,
                                        property_id=publicationSchema.property_id
                                    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    create_price_by_publication(db, publicationSchema)
    return db_publication

def create_price_by_publication(db: Session, publicationSchema: schemas.PropertySchema):
    db_publication = get_publication_by_property_id(db, publicationSchema.property_id)
    db_price = models.Price(
                            start_date=publicationSchema.start_date,
                            end_date=publicationSchema.end_date,
                            price_per_day=publicationSchema.price_per_day,
                            publication_id=db_publication.id
                        )
    db.commit()
    db.refresh(db_price)
    return db_price



    