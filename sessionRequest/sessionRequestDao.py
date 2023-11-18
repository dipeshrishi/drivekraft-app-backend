from db import connect, disconnect
import logging
import configuration.currentTime as currentTime
import sessionRequest.sessionRequest as sessionRequest
import sessionRequest.sessionFetchObject as sessionFetchObject
import user.userService as userService
from flask import  g


def createRequest(listnerId,session_type, userId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Insert into sessionRequest(listener_id,customer_id,session_type, expiry_at, updated_at,created_at) values('{listnerId}','{userId}','{session_type}',DATE_ADD(now(),INTERVAL 2 MINUTE), now(), now())"
    print(sql)
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    logging.info(f"request created with useId : {userId} and listnerId : {listnerId}")
    return "session request  is created"


def getLastRequestByUserId(userId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,listener_id,is_cancelled,customer_id,status,session_type,expiry_at,updated_at,created_at from sessionRequest where customer_id='{userId}' order by id desc limit 1"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)
    if data == None:
        return None
    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] , data[8])


def cancelSessionRequestBySessionId(sessionRequestId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update sessionRequest set is_cancelled ='1' , updated_at =now() where id ='{sessionRequestId}'"
    print(sql)
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"session with id  {sessionRequestId} has been cancelled")
    return "session has been cancelled"


def verifySessionRequestBySessionId(sessionRequestId):
    print(sessionRequestId)
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,listener_id,is_cancelled,customer_id,status,session_type, expiry_at,updated_at,created_at from sessionRequest where id='{sessionRequestId}' "
    mycursor.execute(query)
    data = mycursor.fetchone()
    print(query)
    # disconnect(connection_pool, obj, mycursor)
    if data == None:
        return None
    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], True, data[5], data[6], data[7], data[8])


def isExpiredOrCancelled(sessionRequestId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id from sessionRequest  where id='{sessionRequestId}' and (expiry_at >= now() or is_cancelled =1 )"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return True
    else:
        return False


def confirmSessionById(sessionRequestId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update sessionRequest set status ='1' , updated_at =now() where id ='{sessionRequestId}'"
    print(sql)
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"session with id  {sessionRequestId} has been confirmed")
    return "session has been confirmed"


# id,listener_id,is_cancelled,customer_id,status, expiry_at,updated_at,created_at
def getValidSessionRequest(listner_Id):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,listener_id,is_cancelled,customer_id,status,session_type, expiry_at,updated_at,created_at from sessionRequest where listener_id='{listner_Id}' and now() < expiry_at and status ='false'  and is_cancelled ='false'"
    print(query)
    mycursor.execute(query)
    requestList = mycursor.fetchall()
    print(query)
    # disconnect(connection_pool, obj, mycursor)

    sessionRequestList = list()

    if len(requestList) ==0:
        return sessionRequestList

    for data in requestList:
        SessionRqst = sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                                                    data[7], data[8])
        user = userService.getUserById(SessionRqst.customer_id)

        rqst = sessionFetchObject.sessionFetchObject(SessionRqst.id, SessionRqst.listener_id, SessionRqst.customer_id,
                                                     user.username, SessionRqst.is_cancelled,SessionRqst.session_type ,SessionRqst.updated_at,
                                                     SessionRqst.created_at)
        sessionRequestList.append(rqst.__dict__)

    # print(sessionRequest.__dict__)
    return sessionRequestList


def getLastSessionRequestByUserContact(contact):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,listener_id,is_cancelled,customer_id,status,session_type, expiry_at,updated_at,created_at from sessionRequest  where customer_id in (select id from user where contact = '{contact}') order by created_at desc limit 1"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

def getSessionByRequestId(Id):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,listener_id,is_cancelled,customer_id,status,session_type,expiry_at,updated_at,created_at from sessionRequest where id='{Id}'"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)
    if data == None:
        return None
    return sessionRequest.sessionRequest(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] , data[8])
