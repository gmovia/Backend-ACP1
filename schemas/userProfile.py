from pydantic import BaseModel
from typing import Optional

class UserProfile(BaseModel):
    email: str
    name: Optional[str]
    bio: Optional[str]
    ocupation: Optional[str]
    location: Optional[str]
    pic: Optional[str]

    class Config:
        orm_mode = True