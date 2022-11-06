from sqlalchemy.orm import Session
from schemas.publicationSchema import PublicationFilter, PublicationSchema
from models.publication import Publication
from models.propertie import Property
from models.user import User

def get_publication(db: Session, publication_id: int):
    return db.query(Publication).filter(Publication.id == publication_id).first()

def get_publications_by_property_id(db: Session, property_id: int):
    return db.query(Publication).filter(Publication.property_id == property_id).first()

def get_publications_by_user_id(db: Session, user_id: int):
    return db.query(Publication, Property).filter(Publication.property_id == Property.id).filter(Property.user_id == user_id).all()

def get_publications(db: Session, filter: PublicationFilter, offset: int, limit: int):
    user_db = db.query(User).filter(User.email == filter.email_user).first() 
    query = db.query(Publication, Property).filter(Publication.property_id == Property.id).filter(Property.user_id != user_db.id)
    if filter.email_user is not None:
        query = query.join(User).filter(User.email != filter.email_user)
    return query.limit(limit).offset(limit * offset).all()

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

def update_publication(db: Session, db_publication, publicationSchema: PublicationSchema):
    db_publication.title = publicationSchema.title
    db_publication.description = publicationSchema.description
    db_publication.price = publicationSchema.price                         
    db.add(db_publication)
    db.commit()
    return db_publication


    