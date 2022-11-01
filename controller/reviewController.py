from fastapi import HTTPException
from config.userCrud import get_user
from config.publicationCrud import get_publication
from config.reviewCrud import put_review
from schemas.reviewSchema import ReviewSchema
from sqlalchemy.orm import Session

def add_review(publication_id: int, review: ReviewSchema, db: Session):
   db_publication = get_publication(db, publication_id)
   
   if db_publication is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   user = get_user(db, review.email_user)

   if user is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   return put_review(db, db_publication, review, user.id)

def get_reviews(publication_id: int, db: Session):
   db_publication = get_publication(db, publication_id)

   if db_publication is None:
      raise HTTPException(status_code=400, detail="Permission denied.")

   return db_publication.reviews
