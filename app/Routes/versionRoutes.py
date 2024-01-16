from flask import Blueprint,jsonify,g,request
from app.util import create_db_session
from app.Contract.Response.versionResponse import versionResponse
from app.util import format_request_data
import logging


versionBlueprint = Blueprint('version', __name__,url_prefix='/api')

@versionBlueprint.route('/app/ver', methods =['GET'])
@format_request_data
def getVersion():
    content_type = request.headers.get('Content-Type', '').lower()
    logging.info(str(content_type))
    response = versionResponse("1", "version", "102.0").__dict__
    return jsonify(response)

