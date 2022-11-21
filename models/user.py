from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    propertys = relationship("Property", back_populates="user")
    reservations = relationship("Reservation", back_populates="user")
    reviews = relationship("Review", back_populates="user",
                               cascade="all, delete, delete-orphan")
    name = Column(String)
    bio = Column(String)
    ocupation = Column(String)
    location = Column(String)
    pic = Column(String)

    questions = relationship("Question", back_populates="user")