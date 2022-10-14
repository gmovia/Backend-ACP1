from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class PropertySchema(BaseModel): 
    title: str
    direction: str
    province: str
    country: str
    price: int
    email_user: str
    
    class Config:
        orm_mode = True