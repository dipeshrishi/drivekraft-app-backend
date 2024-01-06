from app.utils import currentTime
from flask import g
from datetime import  timedelta
from app.Models.mysql.sessionRequest import SessionRequest
from app.Models.mysql.sessionRequestStatusMapping import SessionRequestStatusMapping
from sqlalchemy import and_

def createRequest(listener_id,session_type,user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    expiredTime= now + timedelta(minutes = 2)
    try:
        newsessionRequest= SessionRequest(psychologistId=listener_id,userId=user_id,mode=session_type,expired = expiredTime )
        session.add(newsessionRequest)
        session.commit()
    except:
        newsessionRequest = None
    return newsessionRequest



def cancelSessionById(sessionId):
    session =g.session
    now = currentTime.getCurrentTime()
    userSession = session.query(SessionRequest).filter_by(id=sessionId).first()
    userSession.sessionRequestStatusId = findSessionRequestIdByName('CANCELLED')
    userSession.updated = now

    session.commit()
    return True
    # sql = f"Update sessionRequest set is_cancelled ='1' , updated_at =now() where id ='{sessionRequestId}'"


def findSessionRequestIdByName(name):
    id = g.session.query(SessionRequestStatusMapping).filter(SessionRequestStatusMapping.status==name).one()
    return id

def findSessionRequestById(sessionId):
    session = g.session
    verifiedSessionRequest = session.query(SessionRequest).filter(and_(SessionRequest.id==sessionId,SessionRequest.sessionRequestStatusId=='CREATED')).one()

    return verifiedSessionRequest

def fetchSessionRequestByUserId(user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    verifiedSessionRequest = session.query(SessionRequest).filter(and_(SessionRequest.psychologistId==user_id,
                                                                     SessionRequest.sessionRequestStatus=='CREATED',SessionRequest.expired >now)).one()    
    return verifiedSessionRequest

def isExpiredOrCancelled(sessionRequestId):
    session = g.session
    now = currentTime.getCurrentTime()
    sessionStatus = session.query(SessionRequest).filter_by(and_(SessionRequest.id==sessionRequestId,SessionRequest.sessionRequestStatus=='CREATED',SessionRequest.expired >now)).one()    
    if sessionStatus ==None:
        return True

    return False