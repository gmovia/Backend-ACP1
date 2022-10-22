from fastapi import APIRouter, Depends
from schemas.publicationSchema import PublicationSchema
from sqlalchemy.orm import Session
from routes import access
from controller import publicationController

publication = APIRouter()

@publication.post('/createPublication/')
def create_publication(publicationSchema: PublicationSchema, db: Session = Depends(access.get_db)):
    return publicationController.create(publicationSchema, db)


