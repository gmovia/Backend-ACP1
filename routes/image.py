from fastapi import APIRouter, Depends
from schemas.imageSchema import ImageSchema
from sqlalchemy.orm import Session
from controller import imageController
from config.db import engine, get_db
from models import image

image.Base.metadata.create_all(bind=engine)

image = APIRouter()


@image.post('/fetchAllPropertyImages/')
def fetch_all_propery_images(property_id: int, db: Session = Depends(get_db)):
    return imageController.fetch_by_property_id(property_id, db)

