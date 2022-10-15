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

   db_property = crud.create_property(db, propertySchema, db_user.id)

   return db_property

@propertyHandler.post('/deleteProperty/')
def delete_property(property_id: int, email_user: str, db: Session = Depends(access.get_db)):
   db_user = crud.get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = crud.delete_property(db, property_id, db_user.id)

   if db_property is None:
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return db_property

@propertyHandler.post('/updateProperty/')
def update_property(property_id: int, propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):
   db_user = crud.get_user(db, propertySchema.email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = crud.update_property(db, property_id, db_user.id, propertySchema)

   if db_property is None:
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return db_property