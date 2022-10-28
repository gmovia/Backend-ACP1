from fastapi import HTTPException
from schemas.imageSchema import ImageSchema
from config.imageCrud import *
from config.propertyCrud import *
from sqlalchemy.orm import Session

def fetch_by_property_id(property_id: int, db: Session):
   return get_images_by_property_id(db, property_id)

