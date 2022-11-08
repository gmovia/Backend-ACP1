from fastapi import HTTPException
from schemas.publicationSchema import PublicationSchema, PublicationFilter
from config.userCrud import *
from config.propertyCrud import *
from config.publicationCrud import *
from sqlalchemy.orm import Session

def create(publicationSchema: PublicationSchema, db: Session):
    db_user = get_user(db, publicationSchema.email_user)
    
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")
    
    db_property = get_property(db, publicationSchema.property_id)

    if (db_property is None) or (db_property.user_id != db_user.id) or (get_publications_by_property_id(db, publicationSchema.property_id) is not None):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return create_publication(db, publicationSchema)

def delete(publication_id: int, email_user: str, db: Session):
    db_user = get_user(db, email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    db_publication = get_publication(db, publication_id)
    db_property = get_property(db, db_publication.property_id)

    if (db_publication is None) or (db_property.user_id != db_user.id):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return delete_publication(db, db_publication)

def update(publication_id, publicationSchema: PublicationSchema, db: Session):
    db_user = get_user(db, publicationSchema.email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    db_publication = get_publication(db, publication_id)
    db_property = get_property(db, db_publication.property_id)

    if (db_publication is None) or (db_property.user_id != db_user.id):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return update_publication(db, db_publication, publicationSchema)

def fetch_by_user(email_user: str, db: Session):
   db_user = get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="User not exist.")

   return get_publications_by_user_id(db, db_user.id)


def fetch_all(filter: PublicationFilter, offset: int, limit: int, db: Session):
   return get_publications(db, filter, offset, limit)

def fetch_publication_by_id(email_user: str, publication_id: int, db: Session):
   db_user = get_user(db, email_user)

   if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")

   db_publication = get_publication(db, publication_id)

   if db_publication is None:
        raise HTTPException(status_code=400, detail="Publication not exist.")

   return get_publication_and_property(db, publication_id) 
    