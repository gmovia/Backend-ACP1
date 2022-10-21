from fastapi import APIRouter, Depends, HTTPException
from schemas import schemas
from sqlalchemy.orm import Session
from routes import access

publicationHandler = APIRouter()

@publicationHandler.post('/createPublication/')
def create_publication(publicationSchema: schemas.PublicationSchema, db: Session = Depends(access.get_db)):
    return "Implementar"

