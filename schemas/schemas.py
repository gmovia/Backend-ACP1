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
    link: str
    email_user: str
    
    class Config:
        orm_mode = True
    
class PublicationSchema(BaseModel):
    title: str
    description: str
    property_id: int
    email_user: str
    price_per_day: int
    start_day: str
    end_day: str
    
    class Config:
        orm_mode = True
