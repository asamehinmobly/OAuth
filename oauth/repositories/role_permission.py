from models.role_permission import RolePermission
from repositories.base import BaseRepository


class RolePermissionRepository(BaseRepository):
    Model = RolePermission
    ModelName = "role_permission"
    validator = None

    def __init__(self):
        pass
