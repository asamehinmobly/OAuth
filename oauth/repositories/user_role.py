from repositories.base import BaseRepository
from models.user_role import UserRole
from models.role import Role
from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError


class UserRoleRepository(BaseRepository):
    Model = UserRole
    ModelName = "user_role"
    validator = None

    def __init__(self):
        pass

    def get(self, session, **kwargs):
        try:
            data = session.query(Role).join(self.Model).all()
            data = map(lambda row: row._asdict(), data)
            print(data)
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
