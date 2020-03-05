from contextlib import contextmanager
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

engine_url = URL(drivername=current_app.config['DATABASE_DRIVER'],
                 host=current_app.config['DATABASE_HOST'],
                 username=current_app.config['DATABASE_USERNAME'],
                 password=current_app.config['DATABASE_PASSWORD'],
                 database=current_app.config['DATABASE_NAME'])

engine = create_engine(engine_url, echo=True, convert_unicode=True,
                       pool_size=200, pool_recycle=170, isolation_level="READ COMMITTED")

Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session(autocommit=True)
    session.begin()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


__all__ = ["session_scope"]
