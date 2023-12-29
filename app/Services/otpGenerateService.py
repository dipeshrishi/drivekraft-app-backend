from app.Contract.Request.otpGenerateRequest import otpGenerateRequest
from app.Contract.Response.otpGenerateResponse import otpGenerateResponse
from app.Contract.Response.otpVerificationResponse import otpVerificationResponse
from app.Contract.Request.otpVerficationRequest import otpVerificationRequest
from random import randint
from app.utils import validateContactNumber
from app.Services import userService
from app.utils import currentTime
from app.Models.DAO import otpDAO

def generateOtp(request : otpGenerateRequest) -> otpGenerateResponse:
    validate = validateContactNumber(otpGenerateRequest.phoneNo)
    if(validate):
        user = userService.getUserByContact(contactNumber=request.contactNumber)
        if user is None:
            user = userService.createUser(contactNumber=request.contactNumber)
        created = currentTime()
        otp = generateOtpInternal()
        otpDAO.addOtp(user.id,otp)
        response = otpGenerateResponse(successful=True,otp=otp,created=created)
        return response
    else:
        response = otpGenerateResponse(successful="false",error="Invalid Phone Number")

# def verifyOtp(request:otpVerificationRequest) ->otpVerificationResponse:
    


def generateOtpInternal():
    otp = randint(10,99)+randint(10,99)*100+randint(10,99)*(10000)
    return otp



