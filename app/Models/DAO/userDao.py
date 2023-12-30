from flask import g
from app.Models.mysql.user import User
from app.utils import currentTime


def addUser(contactNumber):
    now = currentTime()
    session = g.session
    new_user = User(contactNumber=contactNumber, created=now, updated=now)
    session.add(new_user)
    session.commit()

    return True


def getUser(contactNumber):

    session = g.session
    user = session.query(User).filter_by(contactNumber=contactNumber).one()

    return user