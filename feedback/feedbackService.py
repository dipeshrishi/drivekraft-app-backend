from pickle import FALSE, TRUE
from flask import jsonify, request
import feedback.feedbackDao as feedbackDao
import sessionRequest.sessionRequestDao as sessionRequestDao


def addFeedback():
    sessionId = request.form.get('session_request_id')
    if(isValidSessionId(sessionId)):
        feedback = request.form.get('feedback')
        rating = request.form.get('rating')
        feedbackDao.addFeedback(sessionId,feedback,rating)
        return jsonify({
            "message": "feedback submitted successfully",
            "feedbacck":feedback,
            "rating":rating
        })
    return jsonify({
        "message":"feedback submission failed"
    })

def isValidSessionId(sessionId):
    sessionRequest = sessionRequestDao.verifySessionRequestBySessionId(sessionId)
    if(sessionRequest!=None):
        return True
    return False


    
