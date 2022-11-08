from sqlalchemy.orm import Session
from schemas.publicationSchema import PublicationFilter, PublicationSchema
from models.publication import Publication
from models.propertie import Property
from models.user import User

def get_publication(db: Session, publication_id: int):
    return db.query(Publication).filter(Publication.id == publication_id).first()

def get_publication_and_property(db: Session, publication_id: int):
    return db.query(Publication, Property).filter(Publication.id == publication_id).filter(Publication.property_id == Property.id).first()

def get_publications_by_property_id(db: Session, property_id: int):
    return db.query(Publication).filter(Publication.property_id == property_id).first()

def get_publications_by_user_id(db: Session, user_id: int):
    return db.query(Publication, Property).filter(Publication.property_id == Property.id).filter(Property.user_id == user_id).all()

def get_publications(db: Session, filter: PublicationFilter, offset: int, limit: int):
    query = db.query(Publication, Property).filter(Publication.property_id == Property.id)
    if filter.email_user is not None:
        query = query.join(User).filter(User.email != filter.email_user)
    if filter.price_min is not None:
        query = query.filter(Publication.price >= filter.price_min)
    if filter.price_max is not None:
        query = query.filter(Publication.price <= filter.price_max)
    if filter.rating is not None:
        query = query.filter(Publication.rating >= filter.rating)
    if filter.people is not None:
        query = query.filter(Property.people == filter.people)
    if filter.country is not None:
        query = query.filter(Property.country.ilike(f'%{filter.country}%'))
    if filter.province is not None:
        query = query.filter(Property.province.ilike(f'%{filter.province}%'))
    if filter.location is not None:
        query = query.filter(Property.location.ilike(f'%{filter.location}%'))

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


    