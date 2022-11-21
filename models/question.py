from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.db import Base


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    publication_id = Column(Integer, ForeignKey("publications.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(String)
    question_datetime = Column(DateTime)
    answer = Column(String)
    answer_datetime = Column(DateTime)

    publications = relationship("Publication", back_populates="questions")
    user = relationship("User", back_populates="questions")