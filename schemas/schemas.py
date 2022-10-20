from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class PropertySchema(BaseModel): 
    direction: str
    province: str
    location: str
    country: str
    toilets: int
    rooms: int
    people: int
    description: str
    email_user: str
    
    class Config:
        orm_mode = True
    
class PublicationSchema(BaseModel):
    title: str
    price: int
    property_id: int
    email_user: str
    
    class Config:
        orm_mode = True