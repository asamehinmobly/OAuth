from sqlalchemy.exc import SQLAlchemyError
from schematics.exceptions import ValidationError, DataError
from oauth.models.role_permission import Permission
from oauth.repositories.base import BaseRepository
from oauth.models.role import Role


class RoleRepository(BaseRepository):
    Model = Role
    ModelName = "role"
    validator = None

    def __init__(self):
        pass
