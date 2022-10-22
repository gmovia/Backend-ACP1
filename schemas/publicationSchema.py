from pydantic import BaseModel

class PublicationSchema(BaseModel):
    title: str
    description: str
    price: int
    property_id: int
    email_user: str
    
    class Config:
        orm_mode = True
        