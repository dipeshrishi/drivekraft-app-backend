from flask import Blueprint,jsonify,g,request
from app.util import create_db_session
from app.Services import roleService



roleBlueprint = Blueprint('role', __name__,url_prefix='api')

@roleBlueprint.route('/role', methods =['GET'])
@create_db_session
def getRole():
    response = roleService.getUserRole().__dict__
    return jsonify(response)