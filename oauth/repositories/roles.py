from repositories.base import BaseRepository
from models.role import Role


class RoleRepository(BaseRepository):
    Model = Role
    ModelName = "role"
    validator = None

    def __init__(self):
        pass
