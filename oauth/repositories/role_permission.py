from models.role_permission import RolePermission
from repositories.base import BaseRepository
from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from gateway.db import session_scope
from utils.redis import RedisCash


class RolePermissionRepository(BaseRepository):
    Model = RolePermission
    ModelName = "role_permission"
    validator = None

    def __init__(self):
        pass

    def get(self, **kwargs):
        try:
            with session_scope() as session:
                data = session.query(self.Model).filter_by(**kwargs).all()
                data = map(lambda row: row._asdict(), data)
                return list(data)
        except SQLAlchemyError as err:
            raise err
        except ValidationError as err:
            raise err
        except DataError as err:
            err.message = err.to_primitive()
            raise err
        except Exception as err:
            raise err

    def create(self, app_id, **kwargs):
        try:
            with session_scope() as session:
                redis = RedisCash()
                row = self.Model(**kwargs)
                session.add(row)
                session.flush()
                session.refresh(row)
                redis.app_prefix_clear(kwargs['role_id'], app_id)
                return row._asdict()
        except SQLAlchemyError as err:
            raise err
        except ValidationError as err:
            raise err
        except DataError as err:
            err.message = err.to_primitive()
            raise err
        except Exception as err:
            raise err

    def delete(self, app_id, role_id, permission_id):
        try:
            with session_scope() as session:
                redis = RedisCash()
                query = session.query(self.Model).filter_by(id=permission_id)
                row = query.first()
                if row is None:
                    raise NoResultFound(
                        "{model_name} with id: {model_id} not found ".format(
                            model_name=self.ModelName,
                            model_id=permission_id,
                        ))
                redis.app_prefix_clear(role_id, app_id)
                query.delete()
                return row._asdict()
        except SQLAlchemyError as err:
            raise err
        except ValidationError as err:
            raise err
        except DataError as err:
            err.message = err.to_primitive()
            raise err
        except Exception as err:
            raise err
