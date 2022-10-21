from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from sqlalchemy.orm import Session
from config import userCrud, publicationCrud, propertyCrud
from routes import access
from models import models
from config.db import engine
from sqlalchemy import text

publicationHandler = APIRouter()

@publicationHandler.post('/createPublication/')
def create_publication(publicationSchema: schemas.PublicationSchema, db: Session = Depends(access.get_db)):
    db_user = userCrud.get_user(db, publicationSchema.email_user)
    
    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")
    
    db_property = propertyCrud.get_property(db, publicationSchema.property_id)

    if (db_property is None) or (db_property.user_id != db_user.id):
        raise HTTPException(status_code=400, detail="Permission denied.")

    return publicationCrud.create_publication(db, publicationSchema)