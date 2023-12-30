from flask import Blueprint,jsonify
from app.database import create_db_session
from app.Services import paymentService
from flask import Blueprint
otpBlueprint = Blueprint('payment', __name__,url_prefix='/api/order')

@otpBlueprint.route('/create')
@create_db_session
def createNewOrder():
    response = paymentService.createOrder().__dict__
    return jsonify(response)


@otpBlueprint.route('/placed')
@create_db_session
def placeOrder():
    response = paymentService.placeOrder().__dict__
    return jsonify(response)


@otpBlueprint.route('/confirm')
@create_db_session
def confirmOrder():
    response = paymentService.confirmOrder().__dict__
    return jsonify(response)