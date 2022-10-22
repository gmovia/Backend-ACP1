from fastapi import HTTPException
from schemas.userLogin import UserLogin
from config.userCrud import get_user, create_user
from sqlalchemy.orm import Session

def login(user: UserLogin, db: Session):
    db_user = get_user(db, email=user.email)
    
    if (db_user is None) or (db_user.password != user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
   
    return "OK"

def register(user: UserLogin, db: Session):
    db_user = get_user(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = create_user(db, email=user.email, password=user.password)

    return db_user.id