from app.utils import currentTime
from app.Models.mysql.token import Token
from flask import g  

def addToken(userId, tokenValue):
    now = currentTime.getCurrentTime()

    session = g.session  

    newToken = Token(userId=userId, value=tokenValue, created=now)
   
    session.add(newToken)
    session.commit()

    return "Value updated in the database"
