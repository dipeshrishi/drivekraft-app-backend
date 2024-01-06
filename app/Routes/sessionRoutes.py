from flask import Blueprint,jsonify,g,request
from app.util import create_db_session,format_request_data
from app.Contract.Request import sendSessionRequest
from app.Services import sessionService
from app.authenticate import authenticate_user


sessionBlueprint = Blueprint('session', __name__,url_prefix='api/session')

@sessionBlueprint.route('/book/request', methods =['POST'])
@create_db_session
@format_request_data
@authenticate_user
def sendSessionRequest():
    sessionCreationRequest = sendSessionRequest.sendSessionRequest(**request.json_data)
    response = sessionService.send_Session_Request(sessionCreationRequest).__dict__
    return jsonify(response)
#todo will change repsonse in android side


@sessionBlueprint.route('/book/request/cancel', methods =['POST'])
@create_db_session
@format_request_data
@authenticate_user
def cancelSessionRequest():
    sessionCancellationRequest = sendSessionRequest.cancelSessionRequest(**request.json_data)
    response = sessionService.cancelSessionRequest(sessionCancellationRequest).__dict__
    return jsonify(response)


@sessionBlueprint.route('/book/request/verify', methods =['POST'])
@create_db_session
@format_request_data
@authenticate_user
def verifySessionRequest():
    sessionVerifyRequest = verifySessionRequest.verifySessionRequest(**request.json_data)
    response = sessionService.verifySessionRequest(sessionVerifyRequest).__dict__
    return jsonify(response)

@sessionBlueprint.route('/book/request/fetch', methods =['GET'])
@create_db_session
@format_request_data
@authenticate_user
def fetchSessionRequest():
    # token -> cached, generate, 
    sessionFetchRequest = fetchSessionRequest.fetchSessionRequest(**request.json_data)
    response = sessionService.fetchSessionRequest().__dict__
    return jsonify(response)

@sessionBlueprint.route('/book/request/confirm', methods =['POST'])
@create_db_session
@format_request_data
@authenticate_user
def confirmSessionRequest():
    sessionConfirmRequest = confirmSessionRequest.confirmSessionRequest(**request.json_data)
    response = sessionService.confirmSessionRequest(sessionConfirmRequest).__dict__
    return jsonify(response)