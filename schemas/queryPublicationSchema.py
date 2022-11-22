from pydantic import BaseModel

class QueryPublicationSchema(BaseModel):
    user_email: str
    publication_id: int
    