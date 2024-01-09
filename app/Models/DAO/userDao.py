from flask import g
from app.Models.mysql.user import User
from app.Models.mysql.userRole import UserRole
from app.utils.currentTime import getCurrentTime
from sqlalchemy.orm.exc import NoResultFound


def addUser(contactNumber):
    now = getCurrentTime()
    session = g.session
    new_user = User(contactNumber=contactNumber, created=now, updated=now, roleId=1)
    session.add(new_user)
    session.commit()

    return new_user

def addUser(contactNumber):
    now = getCurrentTime()
    session = g.session
    new_user = User(contactNumber=contactNumber, created=now, updated=now, roleId=1)
    session.add(new_user)
    session.commit()

    return new_user
def findUserByUsername(username):
    session = g.session
    return session.query(User).filter_by(username=username).count() == 0

def assignUsername(newUsername,userId):
    session = g.session
    user = session.query(User).filter_by(id=userId).first()
    print(user.id)
    user.username = newUsername
    session.commit()

    return True



def getUserByContact(contactNumber):
    session = g.session
    try:
        user = session.query(User).filter_by(contactNumber=contactNumber).one()
        return user
    except NoResultFound:
        return None


def getUserById(userId):
    session = g.session
    try:
        user = session.query(User).filter_by(id=userId).one()
        return user
    except NoResultFound:
        return None


def updateUserFirebaseData(firebaseData,userDetails):
    session = g.session
    user = session.query(User).filter_by(id=userDetails.id).first()
    user.firebaseId = firebaseData.firebaseId
    user.firebasePassword = firebaseData.firebasePassword
    user.firebaseEmail = firebaseData.firebaseEmail
    user.firebaseName = firebaseData.firebaseName

    session.commit()
    return True

def getUserRole(userRoleId):
    session = g.session
    role = session.query(UserRole).filter_by(id=userRoleId).one()
    return role

def updateBalance(userId,newBalance):
    session = g.session
    user = session.query(User).filter_by(id=userId).one()
    user.balance = newBalance
    session.commit()
    return True

def addCredits(credits,userId):
    session = g.session
    user = session.query(User).filter_by(id=userId).one()
    user.balance += credits
    session.commit()
    return True




