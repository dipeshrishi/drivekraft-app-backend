from app.Contract.Response.allPsychologistResponse import allPsychologistResponse
from ..Contract.Response.setPsychologistBusyResponse import setPsychologistBusyResponse
from ..Contract.Response.updatePsychologistStatusResponse import updatePsychologistStatusResponse
from app.Models.DAO import psychologistDao
from app.Services import userService

def getAllPsychologist()-> allPsychologistResponse:
    response = psychologistDao.getAllPsychologist()
    return response

def setPsychologistBusy(requestData) ->setPsychologistBusyResponse:
    result = psychologistDao.setStatusBusy(requestData.psychologist_id)
    if(result):
        response = setPsychologistBusyResponse(is_busy=1,is_Online=0)
    else:
        response = setPsychologistBusyResponse(error="couldn't set user busy")
    return response

def updatePsychologistBusyStatus(requestData) ->updatePsychologistStatusResponse:
    user = userService.getUserDetails()
    data = psychologistDao.updateBusyStatus(requestData.busy,user.id)
    if data is not None:
        response = updatePsychologistStatusResponse(successful=True , user=data)
    else:
        response = updatePsychologistStatusResponse(error="couldn't set user busy")
    return response
