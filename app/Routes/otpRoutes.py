from flask import Blueprint,jsonify
from app.Models.mysql import otp
from app.Services import otpGenerateService,otpVerificationService
from app.database import create_db_session
from flask import Blueprint
otpBlueprint = Blueprint('otp', __name__,url_prefix='/otp')

@otpBlueprint.route('/generate')
@create_db_session
def generateNewOtp():
    response = otpGenerateService.generateOtp().__dict__
    return jsonify(response)

@otpBlueprint.route('/verify')
@create_db_session
def verifyOtp():
    response = otpVerificationService.verifyOtp().__dict__
    return jsonify(response)