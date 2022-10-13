from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class PropertySchema(BaseModel):
    title: str
    direction: str
    location: str
    province: str
    country: str
    floors: int
    rooms: int
    toilets: int
    beds: int
    
    class Config:
        orm_mode = True