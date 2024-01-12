import logging

from flask import g, request
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


def format_request_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        content_type = request.headers.get('Content-Type', '').lower()
        if 'multipart/form-data' in content_type:
            request.json_data = request.form.to_dict()
        else:
            try:
                request.json_data = request.get_json()
            except:
                request.json_data = None

        return func(*args, **kwargs)

    return wrapper
