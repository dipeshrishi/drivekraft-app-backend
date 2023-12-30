from flask import Blueprint,jsonify
from app.Models.mysql import user
from app.Services import userService
from app.util import create_db_session
from flask import Blueprint


userBlueprint = Blueprint('user', __name__,url_prefix='/user')


@userBlueprint.route('/firebase')
def getUserForFirebase():
    response = userService.getUserFirebase().__dict__
    return jsonify(response)
