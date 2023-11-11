import sessionEntity.sessionEntityDao as sessionDao
import user.userService as userService
from flask import  jsonify

def getSessionHistoryForUser():
    user= userService.getUser()
    sessionList= sessionDao.sessionHistoryList(user.id)
    if len(sessionList) !=0 :
        return jsonify({
            "sessionList": (sessionList)
        })
    else:
        return jsonify({
            "sessionList": {}
        })
