from pydantic import BaseModel
from typing import List


class Image(BaseModel):
    link: str

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
    images: List[Image]
    email_user: str

    class Config:
        orm_mode = True


class PropertySchemaOut(BaseModel):
    id: int
    direction: str
    province: str
    location: str
    country: str
    toilets: int
    rooms: int
    people: int
    description: str

    class Config:
        orm_mode = True
