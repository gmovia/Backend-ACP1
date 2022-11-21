from pydantic import BaseModel


class QuestionSchema(BaseModel):
    user_id: int
    publication_id: int
    question: str


class AnswerSchema(BaseModel):
    question_id: int
    answer: str
