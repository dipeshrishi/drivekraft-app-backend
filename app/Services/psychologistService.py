from app.Contract.Response.allPsychologistResponse import allPsychologistResponse
from ..Contract.Response.setPsychologistBusyResponse import setPsychologistBusyResponse
from ..Contract.Response.updatePsychologistStatusResponse import updatePsychologistStatusResponse
from ..Contract.Request.createPsychologistRequest import createPsychologistRequest
from ..Contract.Response.checkPsychologistOnlineStatusResponse import checkPsychologistOnlineStatusResponse
from ..Contract.Response.createPsychologistResponse import createPsychologistResponse
from ..Contract.Response.checkPsychologistBusyResponse import checkPsychologistBusyResponse
from ..Models.mysql.psychologist import Psychologist
from ..Models.mysql.psychologistData import PsychologistData
from app.Models.DAO import psychologistDao
from app.Services import userService
from app.Services.userService import getUserDetails
from ..utils.currentTime import getCurrentTime


def getAllPsychologist() -> allPsychologistResponse:
    response = psychologistDao.getAllPsychologist()
    return response


def setPsychologistBusy(requestData) -> setPsychologistBusyResponse:
    user = getUserDetails()
    busyStatus = True if requestData.busy == 1 else False
    result = psychologistDao.updateBusyStatus(user.id,busyStatus)
    if (result):
        response = setPsychologistBusyResponse(is_busy=requestData.busy)
    else:
        response = setPsychologistBusyResponse(error="couldn't set user busy")
    return response


def checkPsychologistBusyStatus(requestData) ->updatePsychologistStatusResponse:

    busy,online= psychologistDao.getPsychologistStatus(requestData.psychologistId)
    if busy is not None:
        response = checkPsychologistBusyResponse(is_busy=busy,is_Online=online)
    else:
        response = updatePsychologistStatusResponse(error="couldn't set user busy")
    return response

def checkPsychologistOnlineStatus() ->checkPsychologistOnlineStatusResponse:

    user = getUserDetails()
    result = psychologistDao.getPsychologistOnlineStatus(user.id)
    if result is not None:
        email, online = result
        response = checkPsychologistOnlineStatusResponse(is_Online=online,email=email)
    else:
        response = updatePsychologistStatusResponse(error="couldn't find psychologist online status")
    return response

def createPsychologist(requestData: createPsychologistRequest) -> createPsychologistResponse:

    user = userService.getUserByContact(requestData.contactNumber)
    if user is None:
        user = userService.createUser(requestData.contactNumber)

        if user is not None:
            # create psychologist from request and user
            psychologist = Psychologist()
            psychologist.userId = user.id
            psychologist.name = requestData.name
            psychologist.contactNumber = requestData.contactNumber
            psychologist.profile_image = requestData.profile_image
            psychologist.emailId = requestData.emailId
            psychologist.description = requestData.description
            psychologist.yearsOfExp = requestData.yearsOfExp
            psychologist.education = requestData.education
            psychologist.gender = requestData.gender
            psychologist.age = requestData.age
            psychologist.interest = requestData.interest
            psychologist.language = requestData.language

            # create psychologistData object from request
            psychologistData = PsychologistData()
            psychologistData.firebaseId = user.firebaseId
            psychologistData.firebaseName = user.firebaseName
            psychologistData.firebaseEmail = user.firebaseEmail
            psychologistData.firebasePassword = user.firebasePassword
            psychologistData.sessionCount = requestData.sessionCount
            psychologistData.rating = requestData.rating
            psychologistData.preferenceOrder = requestData.preferenceOrder
            psychologistData.lastSeen = getCurrentTime()

            result = psychologistDao.createPsychologist(psychologist)

            if result is not None:
                psychologistData.psychologistId = result
                resultantDataId = psychologistDao.createPsychologistData(psychologistData)
                if resultantDataId is not None:
                    response = createPsychologistResponse(successful=True,psychologistId=result,psychologistDataId=resultantDataId)
                else:
                    response = createPsychologistResponse(error="Not able to create data for psychologist but profile was created")
            else:
                response = createPsychologistResponse(error="Not able to create psychologist profile")
        else:
            response = createPsychologistResponse(error="Cannot create user for psychologist")

    else:
        response = createPsychologistResponse(error="User already exists for the contact number")
    return response

