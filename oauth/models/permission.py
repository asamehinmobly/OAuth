from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    role_id = Column(Integer)
    resource_id = Column(Integer)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
