from flask import Blueprint,jsonify,g,request
from app.Models.mysql import psychologist, psychologistData
from app.Services import psychologistService
from app.util import create_db_session
from flask import Blueprint

psychologistBlueprint = Blueprint('api', __name__,url_prefix='/api')

@psychologistBlueprint.route('/psychologist',methods=['GET','POST'])
@create_db_session
def getAllPsychologist():
    response = psychologistService.getAllPsychologist().__dict__
    return jsonify(response)