from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import models
from schemas import schemas
from config import userCrud
from config.db import SessionLocal, engine

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
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Devuelve un usuario por su email y contraseña
    """
    db_user = userCrud.get_user(db, email=user.email)
    if db_user is None or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return "Login exitoso"


@access.post("/users/", status_code=201)
def create_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Crea un usuario
    """
    db_user = userCrud.get_user(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    userCrud.create_user(db=db, email=user.email, password=user.password)

    return "Ok"
