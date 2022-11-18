from datetime import date
from pydantic import BaseModel

class ReservationSchema(BaseModel):
    start_date: date
    end_date: date
    email_user: str
    publication_id: int
    paid: bool

    class Config:
        orm_mode = True

class ReservationSchemaByDateRange(BaseModel):
    start_date: date
    end_date: date
    publication_id: int

    class Config:
        orm_mode = True
