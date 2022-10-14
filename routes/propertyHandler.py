from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from sqlalchemy.orm import Session
from config import crud
from routes import access

propertyHandler = APIRouter()

@propertyHandler.post('/createProperty/')
def create_property(propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):
   db_user = crud.get_user(db, propertySchema.email_user)
    
   if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = crud.create_property(
                                        db, 
                                        propertySchema.direction, 
                                        propertySchema.province, 
                                        propertySchema.location, 
                                        propertySchema.country,
                                        propertySchema.toilets, 
                                        propertySchema.rooms,
                                        propertySchema.people,
                                        propertySchema.description,
                                        db_user.id
                                     )
   return db_property