from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from models import Base


class RolePermission(Base):
    __tablename__ = 'role_permission'
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey(f"{'role'}.id", ondelete='CASCADE'), nullable=False)
    action_id = Column(Integer, ForeignKey(f"{'action'}.id", ondelete='CASCADE'), nullable=False)
    resource_id = Column(Integer, ForeignKey(f"{'resource'}.id", ondelete='CASCADE'), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())
