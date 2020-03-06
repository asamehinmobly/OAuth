from sqlalchemy import Column, String, DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Resource(Base):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())

