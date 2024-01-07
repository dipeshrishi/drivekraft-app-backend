from flask import Blueprint,jsonify,g,request
from app.Models.mysql import psychologist, psychologistData
from app.Services import psychologistService
from app.util import format_request_data
from app.authenticate import authenticate_user
from app.util import create_db_session
from flask import Blueprint
from ..Contract.Request import setPsychologistBusyRequest,updatePsychologistBusyStatusRequest

psychologistBlueprint = Blueprint('api', __name__,url_prefix='/api')

@psychologistBlueprint.route('/psychologist',methods=['GET','POST'])
@create_db_session
@format_request_data
def getAllPsychologist():
    response = psychologistService.getAllPsychologist().__dict__
    return jsonify(response)

@psychologistBlueprint.route('/check/user/busy',methods=['GET','POST'])
@create_db_session
@authenticate_user
@format_request_data
def setPsychologistAsBusy():
    requestData = setPsychologistBusyRequest.setPsychologistBusyRequest(**request.json_data)
    response = psychologistService.setPsychologistBusy(requestData).__dict__
    return jsonify(response)

@psychologistBlueprint.route('/check/user/busy',methods=['GET','POST'])
@create_db_session
@authenticate_user
@format_request_data
def updatePsychologistBusyStat():
    requestData = updatePsychologistBusyStatusRequest.updatePsychologistBusyStatusRequest(**request.json_data)
    response = psychologistService.updatePsychologistBusyStatus(requestData).__dict__
    return jsonify(response)