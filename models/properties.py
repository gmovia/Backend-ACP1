from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db import Base


class Properties(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    direction = Column(String)
    province = Column(String)
    location = Column(String)
    country = Column(String)
    toilets = Column(Integer)
    rooms = Column(Integer)
    people = Column(Integer)
    description = Column(String)
    publication = relationship("Publication", back_populates="property_", uselist=False)
