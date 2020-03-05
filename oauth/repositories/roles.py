from oauth.repositories.base import BaseRepository
from oauth.models.roles import Role


class RoleRepository(BaseRepository):
    Model = Role
    ModelName = "role"
    validator = None

    def __init__(self):
        pass
