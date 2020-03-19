from unicodedata import name

from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from oauth.models.resource import Resource
from oauth.models.action import Action
from oauth.models.role import Role
from oauth.models import Base


class RolePermission(Base):
    __tablename__ = 'role_permission'
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey(f"{Role.__tablename__}.id", ondelete='CASCADE'), nullable=False)
    action_id = Column(Integer, ForeignKey(f"{Action.__tablename__}.id", ondelete='CASCADE'), nullable=False)
    resource_id = Column(Integer, ForeignKey(f"{Resource.__tablename__}.id", ondelete='CASCADE'), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
