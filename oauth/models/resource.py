from sqlalchemy import Column, String, DateTime, func, Integer
from oauth.models import Base


class Resource(Base):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    app_id = Column(String(256), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())

