from flask import Blueprint,jsonify
from Models.otpModel import otp
from Services.OtpService import otpGenerateService

otpBlueprint = Blueprint('otp', __name__)

@otp.route('/otp/generate')
def generateNewOtp():
    response = otpGenerateService().__dict__
    return jsonify(response)