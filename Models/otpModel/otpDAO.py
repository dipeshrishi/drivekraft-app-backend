from datetime import datetime, timedelta
from otp import otp
from flask import g

def addOtp(userId,otpValue):
    session = g.session
    now = datetime.utcnow()+timedelta(hours=5,minutes=30)
    new_otp = otp(otp=otpValue,userId=userId, created=now)

    session.add(new_otp)

    session.commit()

    return "Value updated in the database"
    