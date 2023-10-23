import sessionRequest.sessionRequestDao as sessionRequestDao
import json
from flask import request,jsonify
import user.userService as userService
import otp.otpService as otpService
import sessionRequest.sessionRequestDao as sessionRequestDao
import psychologist.psychologistDao as psychologistDao
import psychologist.psychologistService as psychologistService
from datetime import datetime, timedelta

def sendSessionRequest():
    listnersId = request.form.get('listener_id')

    tokenValue = userService.getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    sessionRequestDao.createRequest(listnersId,token.userId)

    sessionRequest=sessionRequestDao.getLastRequestByUserId(token.userId)

    return jsonify({
        'data': sessionRequest.__dict__
    })

def cancelSessionRequest():
    sessionRequestId = request.form.get('session_request_id')
    sessionRequestDao.cancelSessionRequestBySessionId(sessionRequestId)

    return jsonify({
        'status' : 'Success',
        'message': "Session request cancelled.",
    })

def verifySessionRequest():
    #obj = json.loads(request.data)
    sessionRequestId = request.form.get('session_request_id')

    sessionRequest=sessionRequestDao.verifySessionRequestBySessionId(sessionRequestId)

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

        return jsonify({
            "status": "Success",
            "message": "Session request successfully confirmed.",
            'sessions': sessionRequest.__dict__
        })

def fetchSessionRequest():
    user= userService.getUser()
    return sessionRequestDao.getValidSessionRequest(user.id)


def updateSessionRequestStatus():
    obj = json.loads(request.data)
    contact = obj['phone']
    status = obj['status']
    now = datetime.now() + timedelta(minutes=30, hours=5)
    sessionRequest=sessionRequestDao.getLastSessionRequestByUserContact(contact)

    psychologistDao.updatePsychologistSessionData(sessionRequest.listener_id,status)

    return "updated"




