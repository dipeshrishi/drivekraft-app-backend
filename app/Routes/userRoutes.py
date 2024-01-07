from flask import Blueprint,jsonify,request
from app.Models.mysql import user
from app.Services import userService
from app.util import create_db_session,format_request_data
from flask import Blueprint
from app.Contract.Request import userUpdateFirebaseDetailsRequest,checkUsernameRequest,confirmUsernameRequest
from ..authenticate import authenticate_user


userBlueprint = Blueprint('user', __name__,url_prefix='/api')


@userBlueprint.route('/user/firebase',methods=['GET','POST'])
@format_request_data
@create_db_session
@authenticate_user
def updateUserFirebaseData():
    userRequest = userUpdateFirebaseDetailsRequest.userUpdateFirebaseDetail(**request.json_data)
    response = userService.updateUserFirebaseDetails(userRequest).__dict__
    return jsonify(response)

@userBlueprint.route('/user')
@format_request_data
@create_db_session
@authenticate_user
def getUserDetails():
    response = userService.getUserDetails().__dict__
    return jsonify(response)

@userBlueprint.route('/check/user/bal')
@format_request_data
@create_db_session
@authenticate_user
def fetchUserRoleDetails():
    response = userService.getUserBalance().__dict__
    return jsonify(response)

@userBlueprint.route('/username/check')
@format_request_data
@create_db_session
@authenticate_user
def checkForUsername():
    requestData = checkUsernameRequest.CheckUsernameRequest(**request.json_data)
    response = userService.checkUsername(requestData).__dict__
    return jsonify(response)

@userBlueprint.route('/username/check/confirm')
@format_request_data
@create_db_session
@authenticate_user
def confirmUsername():
    requestConfirm = confirmUsernameRequest.ConfirmUsernameRequest(**request.json_data)
    response = userService.confirmUsername(requestConfirm).__dict__
    return jsonify(response)
