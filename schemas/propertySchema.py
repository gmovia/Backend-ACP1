from pydantic import BaseModel

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