from functools import wraps
from flask import request,g
from .Models.DAO.tokenDAO import getToken

def authenticate_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            tokenValue = request.headers.get('Authorization', '').split(' ')[1]
        except:
            tokenValue = None
        if tokenValue:
            if verify_token(tokenValue):
                g.tokenValue = tokenValue
                return func(*args, **kwargs)
            else:
                return {'error': 'Invalid token'}, 401
        else:
            return {'error': 'Authorization header missing'}, 400

    return wrapper
def verify_token(tokenValue):
    if tokenValue is not None:
        token = getToken(tokenValue=tokenValue)

        if token is not None:
            return True
        return False
    return False
    
