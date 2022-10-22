from sqlalchemy.orm import Session
from models import models
from schemas.publicationSchema import PublicationSchema

def get_publication(db: Session, publication_id: int):
    return db.query(models.Publication).filter(models.Publication.id == publication_id).first()

def create_publication(db: Session, publicationSchema: PublicationSchema):
    db_publication = models.Publication(
                                        title=publicationSchema.title,
                                        description=publicationSchema.description,
                                        price=publicationSchema.price,
                                        property_id=publicationSchema.property_id
                                    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication




    