from sqlalchemy import Column, String, DateTime, func, Integer, ForeignKey
from models import Base
from sqlalchemy.orm import relationship, backref
from models.action import Action
from models.role_permission import RolePermission


class Resource(Base):
    __tablename__ = 'resource'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    app_id = Column(String(256), nullable=False)
    # parent_id = Column(Integer, ForeignKey('resource.id'))
    creation_date = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now())

    actions = relationship(Action, backref="resources", secondary=RolePermission.__tablename__)
    resource_actions = relationship(RolePermission, backref="resource")
    # children = relationship("Resource", backref=backref('parent', remote_side=[id]))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def resource_actions_as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'actions': [action.name for action in self.actions]
        }