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
    
    class Config:
        orm_mode = True