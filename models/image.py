from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Image(Base): 
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    property_id = Column(Integer, ForeignKey('propertys.id'), index=True)
    property = relationship("Property", back_populates="images")
