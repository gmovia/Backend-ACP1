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

    if (db_property is None) or (db_property.user_id != db_user.id):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return create_publication(db, publicationSchema)


