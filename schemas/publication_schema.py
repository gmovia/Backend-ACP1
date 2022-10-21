from pydantic import BaseModel

from schemas.property_schema import PropertySchema


class PublicationSchema(BaseModel):
    title: str
    description: str
    property: PropertySchema
    user_email: str

    class Config:
        orm_mode = True
