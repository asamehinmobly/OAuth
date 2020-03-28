from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from models.role import Role
from models import Base


class UserRole(Base):
    __tablename__ = 'user_role'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, ForeignKey(f"{Role.__tablename__}.id", ondelete='CASCADE'), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
