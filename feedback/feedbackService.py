from pickle import FALSE, TRUE
import json
from flask import jsonify, request
import feedback.feedbackDao as feedbackDao
import sessionRequest.sessionRequestDao as sessionRequestDao
import logging


def addFeedback():
    sessionId = request.form.get('session_request_id')
    if(isValidSessionId(sessionId)):
        feedback = request.form.get('feedback')
        rating = request.form.get('rating')
        feedbackDao.addFeedback(sessionId,feedback,rating)
        return jsonify({
            "message": "feedback submitted successfully",
            "feedback":feedback,
            "rating":rating
        })
    return jsonify({
        "message":"feedback submission failed"
    })

def getFeedback():
    # obj = json.loads(request.data)
    # psychologistId = obj['psychologist_id']
    psychologistId = request.args.get('psychologist_id')
    logging.info(f"fetching feedbacks for {psychologistId}")
    feedback= feedbackDao.getFeedbackFromPsychologist(psychologistId)
    return jsonify({
            "feedback":feedback
        })


def isValidSessionId(sessionId):
    sessionRequest = sessionRequestDao.verifySessionRequestBySessionId(sessionId)
    if(sessionRequest!=None):
        return True
    return False


    
