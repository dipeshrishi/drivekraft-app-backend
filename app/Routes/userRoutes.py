from flask import Blueprint,jsonify,request
from app.Models.mysql import user
from app.Services import userService
from app.Services import psychologistService
from app.util import create_db_session,format_request_data
from flask import Blueprint
from app.Contract.Request import userUpdateFirebaseDetailsRequest,checkUsernameRequest,confirmUsernameRequest
from ..authenticate import authenticate_user
import logging

userBlueprint = Blueprint('user', __name__,url_prefix='/api')


@userBlueprint.route('/user/firebase',methods=['GET','POST'])
@format_request_data
@create_db_session
@authenticate_user
def updateUserFirebaseData():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    userRequest = userUpdateFirebaseDetailsRequest.userUpdateFirebaseDetail(**request.json_data)
    psychologistService.updateFirebaseDetails(userRequest)
    response = userService.updateUserFirebaseDetails(userRequest).__dict__
    return jsonify(response)

@userBlueprint.route('/user')
@format_request_data
@create_db_session
@authenticate_user
def getUserDetails():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    response = userService.getUserDetails().as_dict()
    return response

@userBlueprint.route('/check/user/bal')
@format_request_data
@create_db_session
@authenticate_user
def fetchUserBalanceDetails():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    response = userService.getUserBalance().__dict__
    return jsonify(response)

@userBlueprint.route('/username/check',methods=['GET','POST'])
@format_request_data
@create_db_session
@authenticate_user
def checkForUsername():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    requestData = checkUsernameRequest.CheckUsernameRequest(**request.json_data)
    response = userService.checkUsername(requestData).__dict__
    return jsonify(response)

@userBlueprint.route('/username/check/confirm',methods=['GET','POST'])
@format_request_data
@create_db_session
@authenticate_user
def confirmUsername():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    requestConfirm = confirmUsernameRequest.ConfirmUsernameRequest(**request.json_data)
    response = userService.confirmUsername(requestConfirm).__dict__
    return jsonify(response)
