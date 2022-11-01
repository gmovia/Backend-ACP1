from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="reviews")
    rating = Column(Integer, nullable=False)
    description = Column(String(500))
    publication_id = Column(Integer, ForeignKey('publications.id'), index=True)
    publication = relationship("Publication", back_populates="reviews")
