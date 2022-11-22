from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.queryPublicationSchema import QueryPublicationSchema
from config.db import get_db, engine
from controller import recommendationController
from models import queryPublication

queryPublication.Base.metadata.create_all(bind=engine)

recommendation = APIRouter()

@recommendation.post("/saveQueryPublication/")
def save_query(query: QueryPublicationSchema, db: Session = Depends(get_db)):
    return recommendationController.save_query(query, db)

@recommendation.post("/getRecommendationByLocation/")
def get_recommendation_by_location(user_email: str, db: Session = Depends(get_db)):
    return recommendationController.get_recommendation_by_location(user_email, db)