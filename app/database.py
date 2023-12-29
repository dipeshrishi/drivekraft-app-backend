# database.py

from flask import g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()

def create_db_session(func):
    def wrapper(*args, **kwargs):
        g.session = db.session()

        try:
            # Call the decorated function
            result = func(*args, **kwargs)
            g.session.commit()
            return result

        except Exception as e:
            g.session.rollback()
            raise e

        finally:
            g.session.close()

    return wrapper


