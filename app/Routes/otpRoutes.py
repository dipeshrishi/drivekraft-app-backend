from flask import Blueprint,jsonify,g,request
from app.Models.mysql import otp
from app.Services import otpGenerateService,otpVerificationService
from app.Contract.Request import otpGenerateRequest
from app.util import create_db_session
from flask import Blueprint

otpBlueprint = Blueprint('otp', __name__,url_prefix='/otp')

@otpBlueprint.route('/generate',methods=['GET','POST'])
@create_db_session
def generateNewOtp():
    otpRequest = otpGenerateRequest.otpGenerateRequest(request.get_json())
    response = otpGenerateService.generateOtp(otpRequest).__dict__
    return jsonify(response)

@otpBlueprint.route('/verify',methods=['GET','POST'])
@create_db_session
def verifyOtp():
    response = otpVerificationService.verifyOtp().__dict__
    return jsonify(response)