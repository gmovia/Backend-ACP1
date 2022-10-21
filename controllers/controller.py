from fastapi import HTTPException

from schemas.user_login_schema import UserLoginSchema
from schemas.publication_schema import PublicationSchema
from dao import user_dao, publications_dao


def create_user(user: UserLoginSchema):
    db_user = user_dao.get_user(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = user_dao.create_user(user)
    return user.id


def login(user: UserLoginSchema):
    db_user = user_dao.get_user(email=user.email)
    if db_user is None or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return "Login exitoso"


def create_publication(publication: PublicationSchema):
    db_user = user_dao.get_user(email=publication.user_email)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

    return publications_dao.create_publication(PublicationSchema, db_user.id)
