from app.Contract.Response.placeRazorpayOrderResponse import placeRazorpayOrderResponse
from app.Contract.Request.createPaymentOrderRequest import createRazorpayOrderRequest
from app.Contract.Response.createRazorpayOrderResponse import createRazorpayOrderResponse
from app.Contract.Request.placePaymentOrderRequest import placeRazorpayOrderRequest
from app.Contract.Request.confirmPaymentOrderRequest import confirmPaymentOrderRequest
from app.Contract.Response.confirmRazorpayOrderResponse import confirmRazorpayOrderResponse
from app.Contract.Request.placePaymentOrderRequest import placeRazorpayOrderRequest
import json
from ..Configurations.razorpay import ORDER_URL,ORDER_RECEIPT,ORDER_AUTHORIZATION,ORDER_CURRENCY
import requests
from app.Models.DAO import paymentDao
from app.Services import sessionService
from app.Services import userService
import logging
import json


def createOrder(request : createRazorpayOrderRequest) -> createRazorpayOrderResponse:
    amountInPaisa = int(request.amount)
    payload = getPayloadForOrder(amountInPaisa)
    headers = getHeaderForOrder()

    response = requests.request("POST", ORDER_URL, headers=headers, data=payload)

    user = userService.getUserDetails()

    responseDict = json.loads(response.text)
    paymentDao.storePaymentOrder(responseDict, user.id)

    response = createRazorpayOrderResponse(order_id=responseDict['id'],currency=ORDER_CURRENCY,amount= responseDict['amount']/100)

    return response



def placeOrder(request : placeRazorpayOrderRequest) -> placeRazorpayOrderResponse:
    user = userService.getUserDetails()

    if user.balance < 5:
        response = placeRazorpayOrderResponse(transaction_id=request['transaction_id'],user_credits=user.balance,
                                              status="Error",msg ="Insufficient credits",credits_availablility=False,
                                              credits_sufficient_for_five_minutes=False)
        return response
    #print("printing request",request.session_request_id,request.transaction_id,request.seconds_chatted)
    transactional = paymentDao.getTransactionaByTransId(request['transaction_id'])
    cost = int((int(request['seconds_chatted']) + 60) / 60) * 5
    sessionRequest = sessionService.getSessionByRequestId(request['session_request_id']) # needs clarification

    if transactional == None:
         transactional=paymentDao.createTranaction(userId = user.id,razorpayOrderRequest = request,cost=cost, sessionType = sessionRequest.mode )

    else:
        paymentDao.updateTransaction(razorpayOrderRequest = request, cost=cost)

    userService.updateUserBalance(user.id, user.balance - 5)
    sufficent_balance = True
    availability = True

    if user.balance <25:
        sufficent_balance = False

    if user.balance <5:
        availability = False

    response = placeRazorpayOrderResponse(transaction_id=transactional.transactionId,user_credits=user.balance,
                                          status="Success", msg="Sufficient credits", credits_availablility=availability,
                                          credits_sufficient_for_five_minutes=sufficent_balance)
    return response

    # Todo need to make changes in android as well


def confirmOrder(request : confirmPaymentOrderRequest) -> confirmRazorpayOrderResponse:
    response_string = request.response
    payload_ = response_string
    payload = json.loads(payload_)
    logging.info("datatype of payload" + str(type(payload)))
    logging.info("datatype of payload" + str((payload)))
    logging.info("datatype of payload" + str(payload.keys()))
    if 'razorpay_payment_id' in payload:
        paymentDao.updatePaymentOrder(order_id=payload['razorpay_order_id'], payment_id= payload['razorpay_payment_id'],
                                      signature=payload['razorpay_signature'], gateway='razorpay')

        url= getRazorpayURl(payload['razorpay_order_id'])
        payload = {}
        headers = getHeaderForOrder()

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            responseDict = json.loads(response.text)
            if responseDict['status'] == 'paid':
                # paymentDao.updateOrderStatus(payload['razorpay_order_id'],True) #will add filed in future and do this
                userService.addUserCredit(responseDict['amount'] / 100)

                response = confirmRazorpayOrderResponse(msg ='Your payment id is ' + payload['razorpay_order_id'] + '.',status= 'success',title ="Session Booked")
                return response

        else:
            response = confirmRazorpayOrderResponse(msg='Payment Failed',
                                                    status='error', title="Error")
            return response

def getPayloadForOrder(amountInPaisa):
    payload = json.dumps({
        "amount": int(amountInPaisa) * 100,
        "currency": ORDER_CURRENCY,
        "receipt": ORDER_RECEIPT
    })

    return payload


def getHeaderForOrder():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': ORDER_AUTHORIZATION
    }

    return headers

def getRazorpayURl(order_id):
    url = f"https://api.razorpay.com/v1/orders/{order_id}"
    return url