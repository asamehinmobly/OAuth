from oauth.models.permissions import Permission
from oauth.repositories.base import BaseRepository


class PermissionRepository(BaseRepository):
    Model = Permission
    ModelName = "permission"
    validator = None

    def __init__(self):
        pass
