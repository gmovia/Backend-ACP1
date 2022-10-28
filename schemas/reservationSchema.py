from datetime import date
from pydantic import BaseModel

class ReserveSchema(BaseModel):
    start_date: str
    end_date: str
    email_user: str
    publication_id: int
    price_per_day: int

    class Config:
        orm_mode = True