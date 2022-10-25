from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from routes import access
from schemas.userProfile import UserProfile
from controller import userController

user = APIRouter()


@user.put('/updateProfile/', status_code=200)
def update_profile(profileSchema: UserProfile,
                   db: Session = Depends(access.get_db)):
    return userController.update_profile(profileSchema, db)


@user.get('/getProfile/', status_code=200, response_model=UserProfile)
def get_profile(user_email: str, db: Session = Depends(access.get_db)):
    return userController.get_profile(user_email, db)
