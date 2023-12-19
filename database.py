from flask import  g
from sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

db = SQLAlchemy()
scoped_session = scoped_session(sessionmaker(bind=db.engine))

def db_session(func):
    def wrapper(*args, **kwargs):
        g.session = scoped_session()

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

