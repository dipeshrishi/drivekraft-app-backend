from flask import g
from functools import wraps
from app.database import db

def create_db_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        endpoint_name = func.__name__
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