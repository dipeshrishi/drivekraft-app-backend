
from db import connect,disconnect
import  configuration.currentTime as currentTime
import logging
from flask import  g

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
