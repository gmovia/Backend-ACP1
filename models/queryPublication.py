from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class QueryPublication(Base): 
    __tablename__ = "queryPublication"
    id = Column(Integer, primary_key=True)
    user_email = Column(String)
    publication_id = Column(Integer)
