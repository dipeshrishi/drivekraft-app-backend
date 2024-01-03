from flask import Blueprint,jsonify,g,request
from app.util import create_db_session
from app.Contract.Request import sendSessionRequest
from app.Services import sessionService



sessionBlueprint = Blueprint('session', __name__,url_prefix='api/session')

@sessionBlueprint.route('/book/request', methods =['POST'])
@create_db_session
def sendSessionRequest():
    sessionCreationRequest = sendSessionRequest.sendSessionRequest(request.get_json())
    response = sessionService.sendSessionRequest(sessionCreationRequest).__dict__
    return jsonify(response)
#todo will change repsonse in android side


@sessionBlueprint.route('/book/request/cancel', methods =['POST'])
@create_db_session
def cancelSessionRequest():
    sessionCancellationRequest = sendSessionRequest.cancelSessionRequest(request.get_json())
    response = sessionService.cancelSessionRequest(sessionCancellationRequest).__dict__
    return jsonify(response)


@sessionBlueprint.route('/book/request/verify', methods =['POST'])
@create_db_session
def verifySessionRequest():
    sessionVerifyRequest = verifySessionRequest.verifySessionRequest(request.get_json())
    response = sessionService.verifySessionRequest(sessionVerifyRequest).__dict__
    return jsonify(response)

@sessionBlueprint.route('/book/request/fetch', methods =['GET'])
@create_db_session
def fetchSessionRequest():
    sessionFetchRequest = fetchSessionRequest.fetchSessionRequest(request.get_json())
    response = sessionService.fetchSessionRequest().__dict__
    return jsonify(response)