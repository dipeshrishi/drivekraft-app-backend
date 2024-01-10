from app.Contract.Request.otpVerficationRequest import otpVerificationRequest
from app.Contract.Response.otpVerificationResponse import otpVerificationResponse
from app.Models.DAO import otpDAO,tokenDAO
from app.utils.validateContactNumber import validateContactNumber
from app.Services import userService
from app.utils import currentTime
import random,string


def verifyOtp(request : otpVerificationRequest) -> otpVerificationResponse:
    validate = validateContactNumber(request.mobile)
    if(validate):
        user = userService.getUserByContact(request.mobile)
        otp = otpDAO.getOtp(userId=user.id)
        if str(otp) != request.otp:
            response = otpVerificationResponse(successful="false",error="{'message':'OTP does not match.'}", statusCode=401)
            return response
        tokenValue= getToken()
        tokenDAO.addToken(user.id,tokenValue)
        response = otpVerificationResponse(successful="true",authToken=tokenValue,tokenType="Bearer")
        return response
    


def getToken():
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=50))
    return res
