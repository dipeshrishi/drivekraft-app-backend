from app.Contract.Request.otpGenerateRequest import otpGenerateRequest
from app.Contract.Response.otpGenerateResponse import otpGenerateResponse
from ..Configurations.constants import GOOGLE_OTP,GOOGLE_CONTACT_NUMBER
from app.Contract.Response.otpVerificationResponse import otpVerificationResponse
from app.Contract.Request.otpVerficationRequest import otpVerificationRequest
from ..Services import sendTemplateService
from random import randint
from app.utils.validateContactNumber import validateContactNumber
from app.Services import userService
from app.utils.currentTime import getCurrentTime
from app.Models.DAO import otpDAO
import logging

def generateOtp(request : otpGenerateRequest) -> otpGenerateResponse:
    logging.info("inside otp generation")
    validate = validateContactNumber(request.mobile)
    created = getCurrentTime()
    print(validate)
    if(validate):
        if googleVerificationOtp(request.mobile):
           #userService.addGoogleContact(contactNumber=request.mobile)
            otp = GOOGLE_OTP
            otpDAO.addOtp(1, otp)
        else:
            user = userService.getUserByContact(contactNumber=request.mobile)
            if user is None:
                user = userService.createUser(contactNumber=request.mobile)
                otp = generateOtpInternal()
                otpDAO.addOtp(user.id,otp)
            else:
                otp = otpDAO.getOtp(user.id)
                if otp == None :
                    otp = generateOtpInternal()
                    otpDAO.addOtp(user.id,otp)

        sendTemplateService.sendTemplate('otp', [otp],[], request.mobile)
        response = otpGenerateResponse(successful=True,otp=otp,created=created)
        return response
    else:
        response = otpGenerateResponse(successful=False,error="Invalid Phone Number")
        return response


def generateOtpInternal():
    otp = randint(10,99)+randint(10,99)*100+randint(10,99)*(10000)
    return otp

def googleVerificationOtp(contactNumber):
    logging.info("inside otp verification")
    if contactNumber == GOOGLE_CONTACT_NUMBER:
        return True



