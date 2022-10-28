from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from config.db import Base

class Reserve(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True)
    publication_id = Column(Integer, ForeignKey("publications.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    price = Column(Integer)
    publication = relationship("Publication", back_populates="reserve")
    user = relationship("User", back_populates="reserve")