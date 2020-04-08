from models.role_permission import RolePermission
from repositories.base import BaseRepository
from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from gateway.db import session_scope


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

    def delete(self, model_id):
        try:
            with session_scope() as session:
                query = session.query(self.Model).filter_by(id=model_id)
                row = query.first()
                if row is None:
                    raise NoResultFound(
                        "{model_name} with id: {model_id} not found ".format(
                            model_name=self.ModelName,
                            model_id=model_id,
                        ))
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
