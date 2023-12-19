from Contract.Request import otpGenerateRequest
from Contract.Response import otpGenerateResponse
from random import randint
from utils import validateContactNumber
from UserService import userService
from utils import currentTime
from Models.otpModel import otpDAO

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



