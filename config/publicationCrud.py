from sqlalchemy.orm import Session
from schemas.publicationSchema import PublicationSchema
from models.publication import Publication

def get_publication(db: Session, publication_id: int):
    return db.query(Publication).filter(Publication.id == publication_id).first()

def get_publications_by_property_id(db: Session, property_id: int):
    return db.query(Publication).filter(Publication.property_id == property_id).first()

def create_publication(db: Session, publicationSchema: PublicationSchema):
    db_publication = Publication(
                                    title=publicationSchema.title,
                                    description=publicationSchema.description,
                                    price=publicationSchema.price,
                                    property_id=publicationSchema.property_id
                                )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication

def delete_publication(db: Session, db_publication):
    db.delete(db_publication)
    db.commit()
    return db_publication    




    