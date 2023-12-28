from datetime import datetime, timedelta
from app.utils import currentTime
from app.Models.mysql.otp import otp
from flask import g

def addOtp(userId,otpValue):
    session = g.session
    now = currentTime.getCurrentTime()
    new_otp = otp(otp=otpValue,userId=userId, created=now)

    session.add(new_otp)

    session.commit()

    return "Value updated in the database"
    
def getOtpbyUserId(userId):
    session = g.session
    otp = session.query(otp).filter_by(userId=userId).one()

    return otp