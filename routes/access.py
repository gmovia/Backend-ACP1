from fastapi import APIRouter, HTTPException
from models.user import User
from config.db import connection

access = APIRouter()

@access.post('/login')
def login(user: User):
    user = connection.databaseUsers.users.find_one(dict(user))
    if(user == None):
        raise HTTPException(status_code=404, detail='The user is not registered.')
    return {"detail": 'The user logged in successfully.'}

@access.post('/register')
def register(user: User):
    connection.databaseUsers.users.insert_one(dict(user))
    return {"detail": 'The user is successfully registered.'}