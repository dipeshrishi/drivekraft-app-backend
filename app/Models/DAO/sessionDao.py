from app.utils import currentTime
from flask import g
from datetime import  timedelta
from app.Models.mysql.sessionRequest import sessionRequest

def createRequest(listener_id,session_type,user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    expiredTime= now + timedelta(minutes = 2)
    newsessionRequest= sessionRequest(psychologistId=listener_id,userId=user_id,mode=session_type,expired = expiredTime )
    session.add(newsessionRequest)
    session.commit()
    return "Session has been created in db"



def cancelSessionById(sessionId):
    #TODO  sql = f"Update sessionRequest set is_cancelled ='1' , updated_at =now() where id ='{sessionRequestId}'"


def findSessionRequestById(sessionId):
    session = g.session
    verifiedSessionRequest = session.query(sessionRequest).filter_by(id=sessionId,sessionRequestStatusId='CREATED').one()

    return verifiedSessionRequest

def fetchSessionRequestByUserId(user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    verifiedSessionRequest = session.query(sessionRequest).filter_by(psychologistId=user_id,
                                                                     sessionRequestStatus='CREATED',expired >now).one()    #todo kindly fix this expiry issue
    return verifiedSessionRequest

def isExpiredOrCancelled(sessionRequestId):
    session = g.session
    sessionStatus = session.query(sessionRequest).filter_by(id=sessionRequestId,sessionRequestStatus='CREATED',expired >now).one()    #todo kindly fix this expiry issue

    if sessionStatus ==None:
        return True

    return False