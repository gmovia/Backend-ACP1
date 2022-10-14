from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    propertys = relationship("Property", back_populates="user")

class Property(Base):
    __tablename__ = "propertys"

    id = Column(Integer, primary_key=True, index=True)
    direction = Column(String)
    province = Column(String)
    location = Column(String)
    country = Column(String)
    toilets = Column(Integer)
    rooms = Column(Integer)
    people = Column(Integer)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="propertys")