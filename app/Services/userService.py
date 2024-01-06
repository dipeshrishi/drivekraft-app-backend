from app.utils.validateContactNumber import validateContactNumber
from app.Models.DAO import userDao
from app.Contract.Request.userUpdateFirebaseDetailsRequest import userUpdateFirebaseDetail
from app.Contract.Response.serviceResponse import serviceResponse
from app.Contract.Response.getUserRoleResponse import UserRoleDetailResponse
from app.Models.DAO.tokenDAO import getToken
from app.cache import cache
from flask import g

def updateUserFirebaseDetails(request : userUpdateFirebaseDetail) -> serviceResponse:
    user = getUserDetails()
    result = userDao.updateUserFirebaseData(request,user)
    if(result):
        response = serviceResponse(successful = True,statusCode=200)
    else:
        response = serviceResponse(successful= False,error="User Details not updated")
    return response

def getUserRole () -> UserRoleDetailResponse :
    user = getUserDetails()
    if user is None:
        response = UserRoleDetailResponse(successful=False, error="User Details not found")
    else:
        role = userDao.getUserRole(user.roleId)
        response = UserRoleDetailResponse(successful=True,user_role=role)
    return response



def updateUserBalance(userId,newBalance):
    result = userDao.updateBalance(userId,newBalance)
    return result

def getUserBalance():
    user = getUserDetails()
    return user.balance
def addUserCredit(credits):
    user =getUserDetails()
    result = userDao.addCredits(credits,user.id)

def createUser(contactNumber):
    validate = validateContactNumber(contactNumber)
    if(validate):
        user = createUserInternal(contactNumber=contactNumber)
        return user
    return ""

def createUserInternal(contactNumber):
    validate = validateContactNumber(contactNumber)
    if(validate):
        return userDao.addUser(contactNumber)
    
def getUserByContact(contactNumber):
    return userDao.getUserByContact(contactNumber)

@cache.memoize(timeout=600)
def getUserByToken(tokenValue):
    token = getToken(tokenValue)
    if token is None:
        return None
    else:

        return userDao.getUserById(token.userId)

def getUserDetails():
    return getUserByToken(g.tokenValue)

def getUserById(userId):
    user = userDao.getUserById(userId)
    return user



