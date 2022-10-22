from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import models
from schemas.userLogin import UserLogin
from config.db import SessionLocal, engine
from controller import accessController

models.Base.metadata.create_all(bind=engine)

access = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@access.post('/user/login', status_code=200)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    return accessController.login(user, db)


@access.post("/users/", status_code=201)
def create_user(user: UserLogin, db: Session = Depends(get_db)):
    return accessController.register(user, db)
