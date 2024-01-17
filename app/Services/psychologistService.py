from app.Contract.Response.allPsychologistResponse import allPsychologistResponse
from ..Contract.Response.setPsychologistBusyResponse import setPsychologistBusyResponse
from ..Contract.Response.updatePsychologistStatusResponse import updatePsychologistStatusResponse
from ..Contract.Request.createPsychologistRequest import createPsychologistRequest
from ..Contract.Response.createPsychologistResponse import createPsychologistResponse
from ..Models.mysql.psychologist import Psychologist
from ..Models.mysql.psychologistData import PsychologistData
from app.Models.DAO import psychologistDao
from app.Services import userService
from ..utils.currentTime import getCurrentTime


def getAllPsychologist() -> allPsychologistResponse:
    response = psychologistDao.getAllPsychologist()
    return response


def setPsychologistBusy(requestData) -> setPsychologistBusyResponse:
    result = psychologistDao.setStatusBusy(requestData.psychologist_id)
    if (result):
        response = setPsychologistBusyResponse(is_busy=1, is_Online=0)
    else:
        response = setPsychologistBusyResponse(error="couldn't set user busy")
    return response


def updatePsychologistBusyStatus(requestData) -> updatePsychologistStatusResponse:
    user = userService.getUserDetails()
    data = psychologistDao.updateBusyStatus(requestData.busy, user.id)
    if data is not None:
        response = updatePsychologistStatusResponse(successful=True, user=data)
    else:
        response = updatePsychologistStatusResponse(error="couldn't set user busy")
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

