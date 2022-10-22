from fastapi import HTTPException
from schemas.propertySchema import PropertySchema
from config.userCrud import *
from config.propertyCrud import *
from sqlalchemy.orm import Session

def create(propertySchema: PropertySchema, db: Session):
   db_user = get_user(db, propertySchema.email_user)
    
   if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

   return create_property(db, propertySchema, db_user.id)


def delete(property_id: int, email_user: str, db: Session):
   db_user = get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = get_property(db, property_id)

   if (db_property is None) or (db_property.user_id != db_user.id): 
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return delete_property(db, db_property)


def update(property_id: int, propertySchema: PropertySchema, db: Session):
   db_user = get_user(db, propertySchema.email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   db_property = get_property(db, property_id)

   if (db_property is None) or (db_property.user_id != db_user.id):
      raise HTTPException(status_code=400, detail="Permission denied.")
   
   return update_property(db, db_property, propertySchema)


def fetch_by_user(email_user: str, db: Session):
   db_user = get_user(db, email_user)

   if db_user is None:
      raise HTTPException(status_code=400, detail="User not exist.")

   return get_properties_by_user_id(db, db_user.id)
