from sqlalchemy.orm import Session

from models.question import Question
from models.user import User
from schemas.questionSchema import QuestionSchema, AnswerSchema
from datetime import datetime


def add_question(db: Session, question: QuestionSchema):
    db_question = Question(
        publication_id=question.publication_id,
        user_id=question.user_id,
        question=question.question,
        question_datetime=datetime.now(),
        answer=None)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question_id):
    db_question = db.query(Question).filter(Question.id == question_id).first()
    return db_question


def add_answer(db: Session, answer: AnswerSchema):
    db_question: Question = get_question(db, answer.question_id)
    if not db_question:
        return None
    db_question.answer = answer.answer
    db_question.answer_datetime = datetime.now()
    db.add(db_question)
    db.commit()
    return db_question


def get_questions(db: Session, publication_id):
    return db.query(Question, User.name, User.email).filter(
        Question.publication_id == publication_id).join(User).all()
