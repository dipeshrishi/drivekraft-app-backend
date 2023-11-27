import logging

from flask import request,jsonify
import user.userDao as userDao
import json
import otp.otpService as otpService
import psychologist.psychologistService as psychologistService

def createUser(contactNumber):
    return userDao.addUser(contactNumber)

def UserByContact(contactNumber):
    return userDao.getUserByContact(contactNumber)

def firebaseUser():
    logging.info("obtaining user from token")
    tokenValue =getTokenFromRequest()
    token=otpService.getTokenFromTokenValue(tokenValue)
    userDao.updateUserFirebaseData(token.userId)

    user = userDao.getUserById(token.userId)
    logging.info("user obtained successfully  from token")

    return jsonify({
        "msg": "Successfully Updated.",
        "status" :"Success",
        "user" : (user.__dict__)
    })


def updateBusyStatus():
    user = getUser()
    status = request.form.get('busy')
    userDao.updateUsetStatus(user.id,status)

    return jsonify({
        "msg": "Successfully Updated",
        "user": (getUser().__dict__)
    })


def getUser():
    logging.info("user obtained token from request")
    tokenValue = getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)
    if token==None:
        return None
    user = userDao.getUserById(token.userId)
    logging.info(f"token value {tokenValue} successfully from request")
    return user



def getTokenFromRequest():
    headers = request.headers
    bearer = headers.get('Authorization')  # Bearer YourTokenHere
    token = bearer.split()[1]  # YourTokenHere
    logging.info(f"Assigned token for user is {token}")
    return token

def checkUsername():
    username = request.form.get('username')
    id = userDao.getUserByUserName(username)
    if id ==None:
        return jsonify({
            "status": True,
             "message": "Username is available.",
        })

    return jsonify({
        "status": False,
        "message": "Username is not available",
    })         


def getUserRoleID():
    tokenValue = getTokenFromRequest()
    token = otpService.getTokenFromTokenValue(tokenValue)

    user = userDao.getUserById(token.userId)
    return user.role_id


def addUserCredit(amt):
    user = getUser()
    userDao.updateUserBalance(user.id,amt+ user.credits)
    return


def setUserOnline():
    user = getUser()
    status = request.form.get('online_status')
    userDao.updateUserAvailStatus(user.id, status)

    psychologistService.updateStatus(user.email,status)
    print("status is " + str(status))

    return jsonify({
        "msg": "Successfully Updated.",
        'status' : 'Success',
        "user": (getUser().__dict__)
    })

def checkUserBusy():
    psyId = request.form.get('psychologist_id')
    psychologist = psychologistService.getPsychologistById(psyId)
    user= userDao.getUserById(psychologist.user_id)

    return jsonify({
        "is_busy": user.is_busy,
        'is_online': user.online

    })



def checkUserBalance():
    user = getUser()

    return jsonify({
        "credits": user.credits
    })

def getUserById(id):
    return userDao.getUserById(id)


def confirmUsername():
    username = request.form.get('username')
    id = userDao.getUserByUserName(username)
    if id != None:
        return jsonify({
            "status": False,
            "message": "Username is not available.",
        })

    user = getUser()
    userDao.updateUsername(user.id,username)
    return jsonify({
        "status": True,
        "message": "Username registered.",
    })

def updatingSessionType():
    user = getUser()
    is_chat = request.form.get('chat')
    is_call = request.form.get('call')

    userDao.updateAvailableSessionTypeByUserId(user.id,is_chat,is_call)

    return jsonify({
        "status": 'Success',
        "message": "Session type call updated.",
    })


def updateCallStatusByUserId(id,is_call):
    userDao.updateCallStatusByUserId(id,is_call)


def updateChatStatusByUserId(user_id,is_chat):
    userDao.updateChatStatusByUserId(user_id, is_chat)