from fastapi import APIRouter, HTTPException
from models.user import User
from config.db import connection

access = APIRouter()

@access.post('/login')
def login(user: User):
    registeredUser = connection.databaseUsers.users.find_one({"username": user.username})
    
    if(registeredUser == None):
        raise HTTPException(status_code=404, detail='The user is not registered.')
    
    if(registeredUser["password"] != user.password):
        raise HTTPException(status_code=404, detail='Incorrect password.')
    
    return {"detail": 'The user logged in successfully.'}


@access.post('/register')
def register(user: User):
    if(connection.databaseUsers.users.find_one({"username": user.username}) != None):
        raise HTTPException(status_code=404, detail='The user has already been registered.')
    
    connection.databaseUsers.users.insert_one({"username": user.username, "password": user.password})
    return {"detail": 'The user is successfully registered.'}