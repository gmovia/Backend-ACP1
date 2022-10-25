from fastapi import APIRouter, Depends
from schemas.propertySchema import PropertySchema, PropertySchemaOut
from sqlalchemy.orm import Session
from controller import propertyController
from models import propertie
from config.db import engine, get_db

propertie.Base.metadata.create_all(bind=engine)

propertie = APIRouter()

@propertie.post('/createProperty/', status_code=200, response_model=PropertySchemaOut)
def create_property(propertySchema: PropertySchema, db: Session = Depends(get_db)):
   return propertyController.create(propertySchema, db)

@propertie.delete('/deleteProperty/', status_code=200, response_model=PropertySchemaOut)
def delete_property(property_id: int, email_user: str, db: Session = Depends(get_db)):
   return propertyController.delete(property_id, email_user, db)

@propertie.put('/updateProperty/', status_code=200, response_model=PropertySchemaOut)
def update_property(property_id: int, propertySchema: PropertySchema, db: Session = Depends(get_db)):
   return propertyController.update(property_id, propertySchema, db)

@propertie.post('/fetchAllUserProperties/', status_code=200, response_model=PropertySchemaOut)
def fetch_all_user_properties(email_user: str, db: Session = Depends(get_db)):
   return propertyController.fetch_by_user(email_user, db)
