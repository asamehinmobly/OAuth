from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound

from gateway.db import session_scope
from repositories.repository import IRepository


class BaseRepository(IRepository):
    Model = None
    ModelName = ""

    def create(self, **kwargs):
        try:
            with session_scope() as session:
                row = self.Model(**kwargs)
                session.add(row)
                session.flush()
                session.refresh(row)
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

    def list(self, app_id):
        try:
            with session_scope() as session:
                data = session.query(self.Model).filter_by(app_id=app_id).all()
                data = map(lambda row: row.as_dict(), data)
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

    def get(self, app_id, **kwargs):
        try:
            with session_scope() as session:
                data = session.query(self.Model).filter_by(app_id=app_id, **kwargs).all()
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

    def delete(self, model_id, app_id):
        try:
            with session_scope() as session:
                query = session.query(self.Model).filter_by(id=model_id, app_id=app_id)
                row = query.first()
                if row is None:
                    raise NoResultFound(
                        "{model_name} with id: {model_id}, app_id: {app_id} not found ".format(
                            model_name=self.ModelName,
                            model_id=model_id,
                            app_id=app_id))
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

    def update(self, model_id, app_id, **kwargs):
        try:
            with session_scope() as session:
                row = session.query(self.Model).filter_by(id=model_id, app_id=app_id).first()
                if row is None:
                    raise NoResultFound(
                        "{model_name} with id: {model_id}, app_id: {app_id} not found ".format(
                            model_name=self.ModelName,
                            model_id=model_id,
                            app_id=app_id))
                for (key, value) in kwargs.items():
                    setattr(row, key, value)
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

    def is_duplicated_data(self, app_id, data, obj_id=None):
        obj = self.get(app_id, name=data['name'])
        if obj:
            if not obj_id or obj_id != obj[0].get('id'):
                return True, 'name must be unique'
        return False, ''
