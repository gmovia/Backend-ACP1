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
    #link = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="propertys")
    publication = relationship("Publication", back_populates="property_", uselist=False)

class Publication(Base):
    __tablename__ = 'publications'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    property_id = Column(Integer, ForeignKey("propertys.id"))
    property_ = relationship("Property", back_populates="publication")
    price = relationship("Price", back_populates="publication")

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(String)
    end_date = Column(String)
    price_per_day = Column(Integer)
    publication_id = Column(Integer, ForeignKey("publications.id"))
    publication = relationship("Publication", back_populates="price")