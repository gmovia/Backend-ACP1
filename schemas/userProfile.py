from pydantic import BaseModel, EmailStr
from typing import Optional

class UserProfile(BaseModel):
    email: EmailStr
    name: Optional[str]
    bio: Optional[str]
    ocupation: Optional[str]
    location: Optional[str]

    class Config:
        orm_mode = True