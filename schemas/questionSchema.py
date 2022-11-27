from pydantic import BaseModel


class QuestionSchema(BaseModel):
    user_email: str
    publication_id: int
    question: str


class AnswerSchema(BaseModel):
    question_id: int
    answer: str
