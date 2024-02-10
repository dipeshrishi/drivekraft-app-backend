from app.utils import currentTime
from flask import g
from datetime import  timedelta
from app.Models.mysql.sessionRequest import SessionRequest
from app.Models.mysql.sessionRequestStatusMapping import SessionRequestStatusMapping
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
import logging

def createRequest(listener_id,session_type,user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    expiredTime= now + timedelta(minutes = 2)
    try:
        newsessionRequest= SessionRequest(psychologistId=listener_id,userId=user_id,mode=session_type,expired = expiredTime,sessionRequestStatusId=1 )
        session.add(newsessionRequest)
        session.commit()
    except Exception as e:
        print(f"Couldn't add sessionRequest object. Exception: {e}")
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
    # sql = f"Update sessionRequest set is_cancelled ='1' , updated_at =now() where id ='{sessioxnRequestId}'"

def confirmSession(sessionId):
    session = g.session
    now = currentTime.getCurrentTime()
    sessionRequest = session.query(SessionRequest).filter_by(id=sessionId).first()
    sessionRequest.sessionRequestStatusId = 2
    session.commit()
    logging.error("confirming session  : {}".format(sessionId))
    return True

def findSessionRequestIdByName(name):
    id = g.session.query(SessionRequestStatusMapping).filter(SessionRequestStatusMapping.status==name).one()
    return id

def findSessionRequestById(sessionId):
    session = g.session
    try:
        verifiedSessionRequest = session.query(SessionRequest).filter(
            and_(SessionRequest.id == sessionId, SessionRequest.sessionRequestStatusId == 2)).one()
        return verifiedSessionRequest
    except NoResultFound:
        # Handle the case when no row is found
        return None

def fetchSessionRequestByUserId(user_id):
    session = g.session
    now = currentTime.getCurrentTime()
    print("user id is " + str(user_id))
    print(str(now))

    try:
        verifiedSessionRequest = session.query(SessionRequest).filter(
            and_(
                SessionRequest.psychologistId == user_id,
                SessionRequest.sessionRequestStatusId == 1,
                SessionRequest.expired > now
            )
        ).first()
        return verifiedSessionRequest
    except NoResultFound:
        # Handle the case where no result is found
        return None

def isExpiredOrCancelled(sessionRequestId):
    session = g.session
    now = currentTime.getCurrentTime()
    sessionStatus = session.query(SessionRequest).filter(and_(SessionRequest.id==sessionRequestId,SessionRequest.sessionRequestStatusId==1,SessionRequest.expired >now)).one()
    if sessionStatus ==None:
        return True

    return False