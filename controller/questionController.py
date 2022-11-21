from sqlalchemy.orm import Session

from config import questionCrud
from schemas.questionSchema import QuestionSchema, AnswerSchema


def add_question(db: Session, question: QuestionSchema):
    return questionCrud.add_question(db, question)


def add_answer(db: Session, answer: AnswerSchema):
    question = questionCrud.add_answer(db, answer)
    if not question:
        return "La pregunta no existe"
    return "Respuesta agregada con exito"


def get_questions(db: Session, publication_id):
    return questionCrud.get_questions(db, publication_id)
