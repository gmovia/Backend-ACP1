from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserLogin):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True