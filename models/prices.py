from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from config.db import Base


class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(String)
    end_date = Column(String)
    price = Column(Numeric)
    publication_id = Column(Integer, ForeignKey("publications.id"))

