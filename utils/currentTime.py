from datetime import datetime,timedelta
def getCurrentTime():
    currentTime = datetime.utcnow()+timedelta(hours=5,minutes=30)
    return currentTime