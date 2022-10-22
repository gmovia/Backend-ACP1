from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import models
from schemas.userLogin import UserLogin
from config.db import engine, get_db
from controller import accessController

models.Base.metadata.create_all(bind=engine)

access = APIRouter()

@access.post('/user/login', status_code=200)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    return accessController.login(user, db)


@access.post("/users/", status_code=201)
def create_user(user: UserLogin, db: Session = Depends(get_db)):
    return accessController.register(user, db)
