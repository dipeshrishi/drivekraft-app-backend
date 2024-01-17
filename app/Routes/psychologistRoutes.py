from flask import Blueprint,jsonify,g,request
from app.Models.mysql import psychologist, psychologistData
from app.Services import psychologistService
from app.util import format_request_data
from app.authenticate import authenticate_user
from app.util import create_db_session
from flask import Blueprint
from ..Contract.Request import checkPsychologistBusyRequest,updatePsychologistBusyStatusRequest
import logging

psychologistBlueprint = Blueprint('api', __name__,url_prefix='/api')

@psychologistBlueprint.route('/psychologists',methods=['GET','POST'])
@create_db_session
@format_request_data
def getAllPsychologist():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    response = psychologistService.getAllPsychologist()
    return jsonify(response)


@psychologistBlueprint.route('/users/status/busy',methods=['GET','POST'])
@create_db_session
@authenticate_user
@format_request_data
def setPsychologistAsBusy():
    requestData = updatePsychologistBusyStatusRequest.updatePsychologistBusyStatusRequest(**request.json_data)
    response = psychologistService.setPsychologistBusy(requestData).__dict__
    return jsonify(response)

@psychologistBlueprint.route('/check/user/busy',methods=['GET','POST'])
@create_db_session
@authenticate_user
@format_request_data
def checkPsychologistStatus():
    requestData = checkPsychologistBusyRequest.checkPsychologistBusyRequest(**request.json_data)
    response = psychologistService.checkPsychologistBusyStatus(requestData).__dict__
    return jsonify(response)

@psychologistBlueprint.route('/psychologist/create',methods=['POST'])
@create_db_session
@format_request_data
def createPsychologist():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    requestData = createPsychologistRequest.createPsychologistRequest(**request.json_data)
    response = psychologistService.createPsychologist(requestData).__dict__
    return jsonify(response)