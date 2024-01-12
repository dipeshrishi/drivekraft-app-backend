from flask import Blueprint,jsonify,g,request
from app.util import create_db_session
from app.Contract.Response.versionResponse import versionResponse



versionBlueprint = Blueprint('version', __name__,url_prefix='/api')

@versionBlueprint.route('/app/ver', methods =['GET'])
def getVersion():
    response = versionResponse("1", "version", "102.0", "2023-08-02T11:40:20.000000", "2023-08-02T11:40:20.000000").__dict__
    return jsonify(response)

