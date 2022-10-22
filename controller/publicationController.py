from fastapi import HTTPException
from schemas.publicationSchema import PublicationSchema
from config.userCrud import *
from config.propertyCrud import *
from config.publicationCrud import *
from sqlalchemy.orm import Session


def create(publicationSchema: PublicationSchema, db: Session):
    db_user = get_user(db, publicationSchema.email_user)
    
    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")
    
    db_property = get_property(db, publicationSchema.property_id)

    if (db_property is None) or (db_property.user_id != db_user.id) or (get_publications_by_property_id(db, publicationSchema.property_id) is not None):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return create_publication(db, publicationSchema)

def delete(publication_id: int, email_user: str, db: Session):
    db_user = get_user(db, email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

    db_publication = get_publication(db, publication_id)
    db_property = get_property(db, db_publication.property_id)

    if (db_publication is None) or (db_property.user_id != db_user.id):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return delete_publication(db, db_publication)
