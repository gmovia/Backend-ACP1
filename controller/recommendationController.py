from fastapi import HTTPException
from schemas.publicationSchema import PublicationSchema, PublicationFilter
from config.userCrud import *
from config.propertyCrud import *
from config.publicationCrud import *
from config.recommendationCrud import*
from schemas.queryPublicationSchema import QueryPublicationSchema
from sqlalchemy.orm import Session

def save_query(query: QueryPublicationSchema, db: Session):
    user_db = get_user(db, query.user_email)

    if user_db is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    publication_db = get_publication(db, query.publication_id)

    if publication_db is None:
        raise HTTPException(status_code=400, detail="Publication not exist.")
    
    return add_query(query, db)

def get_recommendation_by_location(user_email: str, db: Session):
    user_db = get_user(db, user_email)

    if user_db is None:
        raise HTTPException(status_code=400, detail="User not exist.")
    
    return get_propertys_by_more_frequent_location(user_email, db)

    