import json
from repositories.base import BaseRepository
from models.role import Role
from utils.redis import RedisCash
from utils.database_util import DataBaseUtils


class RoleRepository(BaseRepository):
    Model = Role
    ModelName = "role"
    validator = None

    def __init__(self):
        pass

    def get_permissions(self, app_id, role_id):
        redis = RedisCash()
        permission_data = redis.app_prefix_get(role_id, app_id)
        if permission_data is None:
            permission_data = DataBaseUtils.exec_procedure("sp_get_permissions", [app_id, role_id])
            if permission_data:
                permission_data = permission_data[0][0]
                try:
                    permission_data = json.loads(permission_data)
                    redis.app_prefix_set(role_id, permission_data, app_id)
                    return permission_data
                except ValueError as err:
                    raise err
            else:
                return []
        else:
            return permission_data

