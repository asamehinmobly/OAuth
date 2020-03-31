from flask import current_app
from sqlalchemy import create_engine

engine = create_engine(current_app.config['DATABASE_URL'] + "?charset=utf8", echo=True, convert_unicode=True,
                       pool_size=200, pool_recycle=170, isolation_level="READ COMMITTED")


class DataBaseUtils(object):
    @staticmethod
    def exec_procedure(proc_name, params):
        connection = engine.raw_connection()
        try:
            cursor = connection.cursor()
            results = cursor.callproc(proc_name, params)
            results = []
            results = list(cursor.fetchall())
            cursor.close()
            connection.commit()
            return results
        finally:
            connection.close()
