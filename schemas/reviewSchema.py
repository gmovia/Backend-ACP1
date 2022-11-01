from pydantic import BaseModel, Field
from typing import Optional

class ReviewSchema(BaseModel):
    email_user: str
    rating: int = Field(..., ge=1, le=5)
    description: Optional[str] = Field(None, max_length=500)

    class Config:
        orm_mode = True

    

class ReviewSchemaOut(BaseModel):
    user_id: int
    rating: int
    description: str

    class Config:
        orm_mode = True