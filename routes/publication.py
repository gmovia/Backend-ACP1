from fastapi import APIRouter, Depends
from schemas.publicationSchema import PublicationSchema
from sqlalchemy.orm import Session
from controller import publicationController
from config.db import engine, get_db
from models import publication

publication.Base.metadata.create_all(bind=engine)

publication = APIRouter()

@publication.post('/createPublication/')
def create_publication(publicationSchema: PublicationSchema, db: Session = Depends(get_db)):
    return publicationController.create(publicationSchema, db)

@publication.put('/updatePublication/')
def update_publication(publication_id: int, publicationSchema: PublicationSchema, db: Session = Depends(get_db)):
    return publicationController.update(publication_id, publicationSchema, db)

@publication.delete('/deletePublication/')
def delete_publication(publication_id: int, email_user: str, db: Session = Depends(get_db)):
    return publicationController.delete(publication_id, email_user, db)

@publication.post('/fetchAllUserPublications/')
def fetch_all_user_publications(email_user: str, db: Session = Depends(get_db)):
    return publicationController.fetch_by_user(email_user, db)
