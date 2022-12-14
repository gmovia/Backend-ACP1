from fastapi import APIRouter, Depends
from schemas.publicationSchema import PublicationSchema, PublicationFilter
from sqlalchemy.orm import Session
from controller import publicationController, questionController
from config.db import engine, get_db
from models import publication
from schemas.questionSchema import QuestionSchema, AnswerSchema

publication.Base.metadata.create_all(bind=engine)

publication = APIRouter()


@publication.post('/createPublication/', status_code=200)
def create_publication(publicationSchema: PublicationSchema, db: Session = Depends(get_db)):
    return publicationController.create(publicationSchema, db)


@publication.put('/updatePublication/', status_code=200)
def update_publication(publication_id: int, publicationSchema: PublicationSchema, db: Session = Depends(get_db)):
    return publicationController.update(publication_id, publicationSchema, db)


@publication.delete('/deletePublication/', status_code=200)
def delete_publication(publication_id: int, email_user: str, db: Session = Depends(get_db)):
    return publicationController.delete(publication_id, email_user, db)


@publication.post('/fetchAllUserPublications/', status_code=200)
def fetch_all_user_publications(email_user: str, db: Session = Depends(get_db)):
    return publicationController.fetch_by_user(email_user, db)


@publication.post('/publications/', status_code=200)
def fetch_all_publications(filter: PublicationFilter, offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return publicationController.fetch_all(filter, offset, limit, db)


@publication.post('/getPublicationById/', status_code=200)
def get_publication_by_id(publication_id: int, db: Session = Depends(get_db)):
    return publicationController.fetch_publication_by_id(publication_id, db)


@publication.post('/question/', status_code=200)
def add_question(question: QuestionSchema, db: Session = Depends(get_db)):
    return questionController.add_question(db, question)


@publication.post('/answer/', status_code=200)
def add_answer(answer: AnswerSchema, db: Session = Depends(get_db)):
    return questionController.add_answer(db, answer)


@publication.get('/question/{publication_id}', status_code=200)
def get_questions(publication_id: int, db: Session = Depends(get_db)):
    return questionController.get_questions(db, publication_id)
