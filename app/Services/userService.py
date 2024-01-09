import logging

from app.utils.validateContactNumber import validateContactNumber
from app.Models.DAO import userDao
from app.Contract.Request.userUpdateFirebaseDetailsRequest import userUpdateFirebaseDetail
from app.Contract.Response.serviceResponse import serviceResponse
from app.Contract.Response.checkUsernameResponse import CheckUsernameResponse
from app.Contract.Request.checkUsernameRequest import CheckUsernameRequest
from app.Contract.Request.confirmUsernameRequest import ConfirmUsernameRequest
from app.Contract.Response.confirmUsernameResponse import ConfirmUsernameResponse
from app.Contract.Response.userBalanceResponse import userBalanceResponse
from app.Models.DAO.tokenDAO import getToken
from app.cache import cache
from flask import g


def updateUserFirebaseDetails(request: userUpdateFirebaseDetail) -> serviceResponse:
    user = getUserDetails()
    result = userDao.updateUserFirebaseData(request, user)
    if (result):
        response = serviceResponse(successful=True, statusCode=200)
        logging.info("firebase details updated ")
    else:
        response = serviceResponse(successful=False, error="User Details not updated")
        logging.info("cannot update user details")
    return response


def checkUsername(request: CheckUsernameRequest) -> CheckUsernameResponse:
    if (len(request.username) < 4):
        response = CheckUsernameResponse(message="Username must be greater than 4 characters", status=False)
        logging.info("username length is less than 4")
    else:
        result = userDao.findUserByUsername(request.username)
        if (result):
            response = CheckUsernameResponse(message="Username is available", status=True)
        else:
            response = CheckUsernameResponse(message="Username is not available", status=False)
    return response

def confirmUsername(request: ConfirmUsernameRequest) -> ConfirmUsernameResponse:
    user = getUserDetails()
    if (len(request.username) < 4):
        response = CheckUsernameResponse(message="Username must be greater than 4 characters", status=False)
    else:
        result = userDao.assignUsername(request.username,user.id)
        if (result):
            response = CheckUsernameResponse(message="Username is available", status=True)
        else:
            response = CheckUsernameResponse(message="Username is not available", status=False)
    return response

def updateUserBalance(userId, newBalance):
    result = userDao.updateBalance(userId, newBalance)
    return result


def getUserBalance():
    user = getUserDetails()
    response = userBalanceResponse(successful=True , balance=user.balance)
    return response


def addUserCredit(credits):
    user = getUserDetails()
    result = userDao.addCredits(credits, user.id)


def createUser(contactNumber):
    validate = validateContactNumber(contactNumber)
    if (validate):
        user = createUserInternal(contactNumber=contactNumber)
        return user
    return ""


def createUserInternal(contactNumber):
    validate = validateContactNumber(contactNumber)
    if (validate):
        return userDao.addUser(contactNumber)


def getUserByContact(contactNumber):
    return userDao.getUserByContact(contactNumber)


def getUserByToken(tokenValue):
    token = getToken(tokenValue)
    if token is None:
        return None
    else:

        return userDao.getUserById(token.userId)


def getUserDetails():
    user = getUserByToken(g.tokenValue)
    return user

def getUserById(userId):
    user = userDao.getUserById(userId)
    return user
