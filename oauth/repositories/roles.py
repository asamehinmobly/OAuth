import json
from repositories.base import BaseRepository
from models.role import Role
from sqlalchemy.exc import SQLAlchemyError
from utils.redis import RedisCash
from utils.database_util import DataBaseUtils

from gateway.db import session_scope


class RoleRepository(BaseRepository):
    Model = Role
    ModelName = "role"
    validator = None

    def __init__(self):
        pass

    def get_permissions(self, app_id, role_id):
        try:
            redis = RedisCash()
            permission_data = redis.app_prefix_get(role_id, app_id)
            if permission_data is None:
                with session_scope() as session:
                    permission_data = session.query(self.Model).filter_by(id=role_id, app_id=app_id).first()
                    permission_data = permission_data.role_resources_as_dict()
                    redis.app_prefix_set(role_id, permission_data, app_id)
            return permission_data
        except SQLAlchemyError as err:
            raise err
        except Exception as err:
            raise err
