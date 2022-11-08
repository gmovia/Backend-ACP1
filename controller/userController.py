from fastapi import HTTPException
from schemas.userProfile import UserProfile
from config import userCrud
from sqlalchemy.orm import Session

def update_profile(profileSchema: UserProfile, db: Session):
    db_user = userCrud.get_user(db, profileSchema.email)

    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    profile = profileSchema.dict(exclude_unset=True,
                                 exclude_none=True,
                                 exclude={'email'})

    userCrud.update_user(db, db_user, profile)

    return "Profile updated successfully"


def get_profile(user_email: str, db: Session):
    db_user = userCrud.get_user(db, user_email)

    if db_user is None:
        raise HTTPException(status_code=400, detail="User not exist.")

    return db_user
