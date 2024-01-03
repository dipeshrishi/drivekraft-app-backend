from app.Contract.Response.sendSessionResponse import sendSessionResponse
from app.Contract.Request.sendSessionRequest import sendSessionRequest
from app.Contract.Response.verifySessionResponse import verifySessionResponse
from app.Contract.Request.verifySessionRequest import verifySessionRequest
from app.Contract.Response.cancelSessionResponse import cancelSessionResponse
from app.Contract.Request.cancelSessionRequest import cancelSessionRequest
from app.Contract.Response.confirmSessionResponse import confirmSessionResponse
from app.Contract.Request.confirmSessionRequest import confirmSessionRequest
from app.Models.DAO import sessionDao

SESSION_REQUEST_STATUS= 0
SESSION_REQUEST_ISCANCELLED =0
SESSION_REQUEST_EXPIRED_STATUS=False
SESSION_REQUEST_VaLID_STATUS=True

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
    SessionRequest= sessionDao.fetchSessionRequestByUserId(user.id)
    customerId = SessionRequest.userId
    customer= userService.getUserById(customerId)  # Todo by Gavy

    return createVerifySessionRequest(SessionRequest,customer)


def createVerifySessionRequest(sessionRequest : SessionRequest,customer: user):
    response = verifySessionResponse( id=sessionRequest.id, listener_id= sessionRequest.psychologistId, customer_id=user.id , status= SESSION_REQUEST_STATUS, session_type =sessionRequest.mode, customer_firebase_id = user.firebaseId, username= user.name,
                 is_cancelled = SESSION_REQUEST_ISCANCELLED, expiry_at = sessionRequest.expired))
    return response
    #todo need to fix response at android side as well--> need to remove list , created and updated as well

def confirmSessionRequest(request : confirmSessionRequest) -> confirmSessionResponse:

    if sessionDao.isExpiredOrCancelled(request.session_request_id):
        response = confirmSessionRequest(status ="Error", message ="Session request either expired or cancelled.", sessionStatus =SESSION_REQUEST_EXPIRED_STATUS)
        return response

    response = confirmSessionRequest(status="Success", message="Session Confirmed",
                                     sessionStatus=SESSION_REQUEST_VaLID_STATUS)
    return response
#TODO need to change repsonse at android side as well
