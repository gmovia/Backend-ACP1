from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import controllers.controller as controller
from config.db import get_db
from schemas.user_login_schema import UserLoginSchema

access = APIRouter()


@access.post("/users/", status_code=201)
def create_user(user: UserLoginSchema, db: Session = Depends(get_db)):
    """Crea un usuario"""
    return controller.create_user(user)


@access.get('/users/login', status_code=200)
def login_user(user: UserLoginSchema):
    """ Devuelve un usuario por su email y contraseña """
    return controller.login(user)

