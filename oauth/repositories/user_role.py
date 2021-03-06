from repositories.base import BaseRepository
from models.user_role import UserRole
from models.role import Role
from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError

from gateway.db import session_scope


class UserRoleRepository(BaseRepository):
    Model = UserRole
    ModelName = "user_role"
    validator = None

    def __init__(self):
        pass

    def get(self, **kwargs):
        try:
            with session_scope() as session:
                data = []
                for value in session.query(Role.id).join(self.Model).filter_by(**kwargs).all():
                    data.append(value.id)
                return data
        except SQLAlchemyError as err:
            raise err
        except ValidationError as err:
            raise err
        except DataError as err:
            err.message = err.to_primitive()
            raise err
        except Exception as err:
            raise err
