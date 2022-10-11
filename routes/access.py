from fastapi import APIRouter, HTTPException, Depends
from schemas.schemas import User
from sqlalchemy.orm import Session

from models import  models
from schemas import schemas
from config import crud
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


@access.get('/users/{user_id}')
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Devuelve un usuario por su id
    """
    db_user = crud.get_user(db, user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    return db_user
    

@access.get('/user')
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Devuelve un usuario por su email y contraseña
    """
    db_user = crud.get_user_by_email(db, email = user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.hashed_password != user.password:
        raise HTTPException(status_code=404, detail="Incorrect password")
    return db_user


@access.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    """
    Crea un usuario
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



