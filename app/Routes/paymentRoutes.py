from flask import Blueprint,jsonify,request
from ..util import create_db_session,format_request_data
from ..authenticate import authenticate_user
from ..Contract.Request import createPaymentOrderRequest
from app.Services import paymentService
from flask import Blueprint

paymentBlueprint = Blueprint('payment', __name__,url_prefix='/api/order')

@paymentBlueprint.route('/create')
@create_db_session
@format_request_data
@authenticate_user
def createNewOrder():
    createPayRequest = createPaymentOrderRequest.createRazorpayOrderRequest(**request.json_data)
    response = paymentService.createOrder(createPayRequest).__dict__
    return jsonify(response)


@paymentBlueprint.route('/placed')
@create_db_session
@format_request_data
@authenticate_user
def placeOrder():
    # request.header
    response = paymentService.placeOrder(request.json_data).__dict__
    return jsonify(response)


@paymentBlueprint.route('/confirm')
@create_db_session
@format_request_data
def confirmOrder():
    response = paymentService.confirmOrder(request.json_data).__dict__
    return jsonify(response)