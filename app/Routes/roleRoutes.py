from flask import Blueprint,jsonify,g,request
from app.util import create_db_session,format_request_data
from app.authenticate import authenticate_user
from app.Services import roleService



roleBlueprint = Blueprint('role', __name__,url_prefix='/api')

@roleBlueprint.route('/role', methods =['GET'])
@create_db_session
@authenticate_user
@format_request_data
def getRole():
    response = roleService.getUserRole().to_dict()
    return jsonify(response)