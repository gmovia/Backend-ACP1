from fastapi import APIRouter, Depends
from schemas.propertySchema import PropertySchema
from sqlalchemy.orm import Session
from routes import access
from controller import propertyController

propertie = APIRouter()

@propertie.post('/createProperty/', status_code=200)
def create_property(propertySchema: PropertySchema, db: Session = Depends(access.get_db)):
   return propertyController.create(propertySchema, db)

@propertie.delete('/deleteProperty/', status_code=200)
def delete_property(property_id: int, email_user: str, db: Session = Depends(access.get_db)):
   return propertyController.delete(property_id, email_user, db)

@propertie.put('/updateProperty/', status_code=200)
def update_property(property_id: int, propertySchema: PropertySchema, db: Session = Depends(access.get_db)):
   return propertyController.update(property_id, propertySchema, db)

@propertie.post('/fetchAllUserProperties/', status_code=200)
def fetch_all_user_properties(email_user: str, db: Session = Depends(access.get_db)):
   return propertyController.fetch_by_user(email_user, db)
