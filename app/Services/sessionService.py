from app.Contract.Response.sendSessionResponse import sendSessionResponse
from app.Contract.Request.sendSessionRequest import sendSessionRequest
from app.Contract.Response.verifySessionResponse import verifySessionResponse
from app.Contract.Request.verifySessionRequest import verifySessionRequest
from app.Contract.Response.cancelSessionResponse import cancelSessionResponse
from app.Contract.Request.cancelSessionRequest import cancelSessionRequest
from app.Models.DAO import sessionDao


def sendSessionRequest(request : sendSessionRequest) -> sendSessionResponse:
    session_type = null

    try:
        session_type=request.session_type
        if session_type == None:
            session_type = 'chat'
    except:
        session_type = 'chat'

    user = userService.getUser() #Todo by Gavy
    sessionDao.createRequest(request.listener_id,session_type,user.id)
    #Todo return session Id which is cretaed above in respose

def cancelSessionRequest(request : cancelSessionRequest) -> cancelSessionResponse:
    try:
        sessionDao.cancelSessionById(request.session_request_id)
        response = cancelSessionResponse(status="Success", message="Session request cancelled.")
        return response
    except:
        response = cancelSessionResponse(status="Error", message="Error in cancelling request")
        return response

def verifySessionRequest(request : verifySessionRequest) -> verifySessionResponse:
    verifiedSessionRequestId= sessionDao.findSessionRequestById(request.session_request_id)

    if verifiedSessionRequestId==None:
        response = verifySessionResponse(status=False)
        return response


    response = verifySessionResponse(status=True)
    return response

def fetchSessionRequest():
    user = userService.getUser()  # Todo by Gavy
    verifiedSessionRequest= sessionDao.fetchSessionRequestByUserId(user.id)
    customerId = verifiedSessionRequest.userId
    customer= userService.getUserById(customerId)  # Todo by Gavy
