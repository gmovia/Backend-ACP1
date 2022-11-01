from sqlalchemy.orm import Session
from models.publication import Publication
from models.review import Review
from schemas.reviewSchema import ReviewSchema


def get_review_by_user(db: Session, db_publication: Publication, user_id: int):
    return db.query(Review).filter(
        Review.publication_id == db_publication.id).filter(
            Review.user_id == user_id).first()


def put_review(db: Session, db_publication: Publication,
               reviewSchema: ReviewSchema, user_id: str):
    review = get_review_by_user(db, db_publication, user_id)
    if review is None:
        review = Review(user_id=user_id, publication_id=db_publication.id)
    review.rating = reviewSchema.rating
    review.description = reviewSchema.description
    db.merge(review)
    db.commit()

    db_publication.rating = (sum([p.rating for p in db_publication.reviews
                                  ])) / len(db_publication.reviews)
    db.merge(db_publication)
    db.commit()
    return review
