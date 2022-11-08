from pydantic import BaseModel
from typing import Optional

class PublicationSchema(BaseModel):
    title: str
    description: str
    price: int
    property_id: int
    email_user: str
    
    class Config:
        orm_mode = True
        

class PublicationFilter(BaseModel):
    email_user: Optional[str]
    price_max: Optional[int]
    price_min: Optional[int]
    rating: Optional[float]
    people: Optional[int]
    country: Optional[str]
    province: Optional[str]
    location: Optional[str]
    
    class Config:
        orm_mode = True