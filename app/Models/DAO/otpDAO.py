from datetime import datetime, timedelta
from app.utils import currentTime
from app.Models.mysql.otp import Otp
from flask import g
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import desc


def addOtp(userId,otpValue):
    session = g.session
    now = currentTime.getCurrentTime()
    new_otp = Otp(otp=otpValue,userId=userId, created=now)

    session.add(new_otp)

    session.commit()

    return "Value updated in the database"

def getOtpbyUserId(userId):
    session = g.session
    otp = session.query(Otp).filter_by(userId=userId).order_by(desc(Otp.id)).first()
    print(otp)
    return otp

def getOtp(userId):
    session = g.session
    now = currentTime.getCurrentTime()
    try:
        otp = session.query(Otp).filter(
            and_(Otp.userId == userId, Otp.created >= now - timedelta(minutes=10))
        ).one()
        return otp.otp
    except NoResultFound:
        return None
