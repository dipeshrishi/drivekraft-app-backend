from flask import Blueprint,jsonify,g,request
from app.Models.mysql import otp
from app.Services import otpGenerateService,otpVerificationService
from app.Contract.Request import otpGenerateRequest,otpVerficationRequest
from app.util import create_db_session,format_request_data
from flask import Blueprint
from functools import wraps
import logging
otpBlueprint = Blueprint('otp', __name__,url_prefix='/api')

@otpBlueprint.route('/login-send-otp',methods=['GET','POST'])
@create_db_session
@format_request_data
def generateNewOtp():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    logging.info(request.json_data);
    otpRequest = otpGenerateRequest.otpGenerateRequest(**request.json_data)
    response = otpGenerateService.generateOtp(otpRequest).__dict__
    return jsonify(response)

@otpBlueprint.route('/login',methods=['GET','POST'])
@create_db_session
@format_request_data
def verifyOtp():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    otpVerifyRequest = otpVerficationRequest.otpVerificationRequest(**request.json_data)
    response = otpVerificationService.verifyOtp(otpVerifyRequest).__dict__
    return jsonify(response)