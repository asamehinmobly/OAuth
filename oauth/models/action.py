from sqlalchemy import Column, String, DateTime, func, inspect, Integer
from oauth.models import Base


class Action(Base):
    __tablename__ = 'action'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
