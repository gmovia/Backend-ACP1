from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class Publications(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(String)
    property = relationship("Property", back_populates="publication")
    price = relationship("Price", back_populates="publication")