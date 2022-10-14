from fastapi import APIRouter, Depends
from schemas import schemas
from sqlalchemy.orm import Session
from config import crud
from routes import access

propertyHandler = APIRouter()

@propertyHandler.post('/registerProperty/')
def register_property(propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):
    db_user = crud.get_user(db, propertySchema.email_user)
    db_property = crud.create_property(db, propertySchema.title, propertySchema.direction, 
                                     propertySchema.province, propertySchema.country,
                                     propertySchema.price, db_user.id)
    return db_property