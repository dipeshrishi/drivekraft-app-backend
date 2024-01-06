from flask import Blueprint,jsonify,request
from app.Models.mysql import user
from app.Services import userService
from app.util import create_db_session,format_request_data
from flask import Blueprint
from app.Contract.Request import userUpdateFirebaseDetailsRequest
from ..authenticate import authenticate_user


userBlueprint = Blueprint('user', __name__,url_prefix='api')


@userBlueprint.route('/user/firebase',methods=['GET','POST'])
@format_request_data
@create_db_session
@authenticate_user
def updateUserFirebaseData():
    userRequest = userUpdateFirebaseDetailsRequest.userUpdateFirebaseDetail(**request.json_data)
    response = userService.updateUserFirebaseDetails(userRequest).__dict__
    return jsonify(response)

@userBlueprint.route('/role')
@format_request_data
@create_db_session
@authenticate_user
def getUserDetails():
    response = userService.getUserDetails().__dict__
    return jsonify(response)

@userBlueprint.route('/user')
@format_request_data
@create_db_session
@authenticate_user
def getUserRoleDetails():
    response = userService.getUserRole().__dict__
    return jsonify(response)

@userBlueprint.route('/check/user/balance')
@format_request_data
@create_db_session
@authenticate_user
def getUserRoleDetails():
    response = userService.getUserBalance().__dict__
    return jsonify(response)
