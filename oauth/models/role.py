from sqlalchemy import Column, String, DateTime, func, inspect, Integer

from oauth.models import Base


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    app_id = Column(String(256))
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())