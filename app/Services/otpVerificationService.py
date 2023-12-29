from app.Contract.Request.otpVerficationRequest import otpVerificationRequest
from app.Contract.Response.otpVerificationResponse import otpVerificationResponse
from app.Models.DAO import otpDAO,tokenDAO
from app.utils import validateContactNumber
from app.Services import userService
from app.utils import currentTime
import random,string


def verifyOtp(request : otpVerificationRequest) -> otpVerificationResponse:
    validate = validateContactNumber(request.phoneNo)
    if(validate):
        user = userService.getUserByContact(contactNumber=request.contactNumber)
        otp = otpDAO.getOtpbyUserId(userId=user.userId)
        if otp != str(otp.otp):
            response = otpVerificationResponse(successful="false",error="{'message':'OTP does not match.'}", status=401)
            return response
        tokenValue= getToken()
        tokenDAO.addToken(user.userId,tokenValue)
        response  = otpVerificationResponse(successful="true",authToken=tokenValue,tokenType="Bearer")
        return response
    


def getToken():
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=50))
    return res
