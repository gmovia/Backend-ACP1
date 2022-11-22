from sqlalchemy.orm import Session
from schemas.queryPublicationSchema import QueryPublicationSchema
from models.queryPublication import QueryPublication
from models.publication import Publication
from models.propertie import Property
from sqlalchemy import func

def add_query(query: QueryPublicationSchema, db: Session):
    db_query = QueryPublication(user_email=query.user_email, publication_id=query.publication_id)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

def get_propertys_by_more_frequent_location(user_email: str, db: Session):
    location = db.query(Property.location, func.count(Property.location).label("count")).filter(QueryPublication.publication_id == Publication.id).filter(Publication.property_id == Property.id).group_by(Property.location).order_by(func.count(Property.location).desc()).first()
    return db.query(Publication, Property).filter(Publication.property_id == Property.id).filter(Property.location == location.location).all()