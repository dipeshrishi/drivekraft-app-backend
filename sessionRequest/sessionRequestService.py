import logging

import sessionRequest.sessionRequestDao as sessionRequestDao
import json
from flask import request,jsonify
import user.userService as userService
import otp.otpService as otpService
import sessionRequest.sessionRequestDao as sessionRequestDao
import psychologist.psychologistDao as psychologistDao
import psychologist.psychologistService as psychologistService
import nortificationMessage.nortificationMessageService as nortificationService
from datetime import datetime, timedelta

def sendSessionRequest():
    listnersId = request.form.get('listener_id')
    try:
        session_type =request.form.get('session_type')
        if session_type== None:
            session_type = 'chat'
    except:
        session_type= 'chat'

    logging.info(f"trying to send session request to listner with id :{listnersId}")

    tokenValue = userService.getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    sessionRequestDao.createRequest(listnersId,session_type,token.userId)
    sessionRequest=sessionRequestDao.getLastRequestByUserId(token.userId)

    logging.info(f"request successfully send to listner with id :{listnersId}")

    return jsonify({
        'data': sessionRequest.__dict__
    })

def cancelSessionRequest():
    sessionRequestId = request.form.get('session_request_id')
    sessionRequestDao.cancelSessionRequestBySessionId(sessionRequestId)
    logging.info(f"request with session id {sessionRequestId} has been cancelled")

    return jsonify({
        'status' : 'Success',
        'message': "Session request cancelled.",
    })

def verifySessionRequest():
    #obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')
    sessionRequest=sessionRequestDao.verifySessionRequestBySessionId(sessionRequestId)

    logging.info(f"request with session id {sessionRequestId} has been verified")
    return jsonify({
        'session': (sessionRequest.__dict__)
    })

def confirmSessionRequest():
    #obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')

    if sessionRequestDao.isExpiredOrCancelled(sessionRequestId)== True:
        return jsonify({
            "status": "Error",
            "message": "Session request either expired or cancelled."
        })
    else:
        sessionRequestDao.confirmSessionById(sessionRequestId)
        sessionRequest = sessionRequestDao.verifySessionRequestBySessionId(sessionRequestId)
        psychologistService.incrementSessionCount(sessionRequest.listener_id)
        logging.info(f"request with session id {sessionRequestId} has been confirmed")
        return jsonify({
            "status": "Success",
            "message": "Session request successfully confirmed.",
            'sessions': sessionRequest.__dict__
        })

def fetchSessionRequest():
    user= userService.getUser()
    rqst= sessionRequestDao.getValidSessionRequest(user.id)
    return jsonify({
        "sessions": (rqst)
    })


def updateSessionRequestStatus():
    obj = json.loads(request.data)
    contact = obj['phone']
    status = obj['status']
    now = datetime.now() + timedelta(minutes=30, hours=5)
    sessionRequest=sessionRequestDao.getLastSessionRequestByUserContact(contact)

    psychologistDao.updatePsychologistSessionData(sessionRequest.listener_id,status)
    if status == 'REQUEST_MISSED':
        nortificationService.nortifyMissedMessage(sessionRequest.listener_id)
        psychologistService.updateStatus(user.email, "off")
        logging.info(f"Turning status off forcefully for {user.email}")
        logging.info(f"Session Request Missed")
        user = userService.UserByContact(contact)
        nortificationService.nortifyMissedMessage(sessionRequest.listener_id)
        psychologistService.updateStatus(user.email, "off")
        logging.info(f"Turning status off forcefully for {user.email}")


    return "updated"




