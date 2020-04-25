from sqlalchemy import Column, String, DateTime, func, Integer
from models import Base
from sqlalchemy.orm import relationship
from models.resource import Resource
from models.role_permission import RolePermission


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    app_id = Column(String(256), nullable=False)
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    resources = relationship(Resource, backref="roles", secondary=RolePermission.__tablename__)
    role_resources = relationship(RolePermission, backref="role")

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def role_resources_as_dict(self):
        permissions = {}
        for resource in self.resources:
            permissions[resource.name] = [action.name for action in resource.actions]
        return permissions
