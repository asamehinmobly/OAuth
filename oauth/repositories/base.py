from schematics.exceptions import ValidationError, DataError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound


class BaseRepository(object):
    Model = None
    ModelName = ""

    def create(self, session, **kwargs):
        try:
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

    def list(self, session, app_id):
        try:
            data = session.query(self.Model).filter_by(app_id=app_id).all()
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

    def get(self, session, **kwargs):
        try:
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

    def delete(self, session, model_id, app_id):
        try:
            query = session.query(self.Model).filter_by(id=model_id, app_id=app_id)
            row = query.first()
            if row is None:
                raise NoResultFound(
                    "{model_name} with id: {model_id}, app_id: {app_id} not found ".format(model_name=self.ModelName,
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

    def update(self, session, model_id, app_id, **kwargs):
        try:
            row = session.query(self.Model).filter_by(id=model_id, app_id=app_id).first()
            if row is None:
                raise NoResultFound(
                    "{model_name} with id: {model_id}, app_id: {app_id} not found ".format(model_name=self.ModelName,
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
