from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from config.db import Base


class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Integer)
    property_id = Column(Integer, ForeignKey("propertys.id"))
    property_ = relationship("Property", back_populates="publication")
    reservations = relationship("Reservation", back_populates="publication")
    rating = Column(Float)
    reviews = relationship("Review",
                           back_populates="publication",
                           cascade="all, delete, delete-orphan")
    questions = relationship("Question", back_populates="publications")