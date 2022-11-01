from fastapi import APIRouter, Depends
from schemas.reviewSchema import ReviewSchema, ReviewSchemaOut
from sqlalchemy.orm import Session
from controller import reviewController
from config.db import engine, get_db
from models import review

review.Base.metadata.create_all(bind=engine)

review = APIRouter()


@review.put('/newReview/{publication_id}', status_code=201, response_model=ReviewSchemaOut)
def add_review(publication_id: int, review: ReviewSchema, db: Session = Depends(get_db)):
    return reviewController.add_review(publication_id, review, db)


@review.get('/reviews/{publication_id}', status_code=200)
def get_reviews(publication_id: int, db: Session = Depends(get_db)):
    return reviewController.get_reviews(publication_id, db)