
from db import connect,disconnect
import  configuration.currentTime as currentTime
import logging
from flask import  g
import feedback.feedback as feedback

def addFeedback(sessionId,feedback,rating):
    now = currentTime.getCurrentTimeInIst()
    mycursor = g.cursor
    sql = f"Insert into sessionFeedback(sessionId,feedback,rating,created_at,updated_at) values('{sessionId}','{feedback}','{rating}','{now}','{now}')"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    logging.info(f"sessionFeedback with for session  {sessionId} created")
    return "feedback updated"


def getFeedbackFromPsychologist(psychologistId):
    mycursor = g.cursor
    sql =f"select sf.id,feedback,rating from sessionFeedback sf left join sessionRequest sr on sf.sessionId= sr.id where sr.listener_id ={psychologistId}"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    feedbackList=list()
    for feeedback in data:
        feedback.feedback(feeedback[0],feeedback[1],feeedback[2],feeedback[3])
        feedbackList.append(feedbackList)

    return feedbackList