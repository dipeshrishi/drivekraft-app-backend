from app.utils import currentTime
from datetime import timedelta
from app.Models.mysql.token import Token
from flask import g
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from app.cache import cache


def addToken(userId, tokenValue):
    now = currentTime.getCurrentTime()

    session = g.session

    newToken = Token(userId=userId, value=tokenValue, created=now)

    session.add(newToken)
    session.commit()

    return "Value updated in the database"


@cache.memoize(timeout=600)
def getToken(tokenValue):
    now = currentTime.getCurrentTime()
    try:
        token = g.session.query(Token).filter(
            and_(Token.value == tokenValue, Token.created >= now - timedelta(hours=24))).one()
    except NoResultFound:
        token = None

    return token
