from app.Contract.Response.placeRazorpayOrderResponse import placeRazorpayOrderResponse
from app.Contract.Request.createRazorpayOrderRequest import createRazorpayOrderRequest
from app.Contract.Response.createRazorpayOrderResponse import createRazorpayOrderResponse
from app.Contract.Request.placeRazorpayOrderRequest import placeRazorpayOrderRequest
from app.Contract.Response.createRazorpayOrderResponse import confirmRazorpayOrderResponse
from app.Contract.Request.placeRazorpayOrderRequest import confirmRazorpayOrderRequest
import json
from ..Configurations.razorpay import ORDER_URL,ORDER_RECEIPT,ORDER_AUTHORIZATION,ORDER_CURRENCY
import requests
from app.Models.DAO import paymentDao


def createOrder(request : createRazorpayOrderRequest) -> createRazorpayOrderResponse:
    amountInPaisa = int(request.amount)*100
    payload = getPayloadForOrder(amountInPaisa)
    headers = getHeaderForOrder()

    response = requests.request("POST", ORDER_URL, headers=headers, data=payload)

    userId = userService.getUser().id # ToDo need to get function from Gavy

    responseDict = json.loads(response.text)
    paymentDao.storePaymentOrder(responseDict, userId)

    response = createRazorpayOrderResponse(order_id=responseDict['id'],currency=ORDER_CURRENCY,amount= responseDict['amount']/100)

    return response



def placeOrder(request : placeRazorpayOrderRequest) -> placeRazorpayOrderResponse:
    user = userService.getUser()

    if user.credits < 5:
        response = placeRazorpayOrderResponse(user_credits=user.credits,
                                              status="Error",msg ="Insufficient credits",credits_availablility=False,
                                              credits_sufficient_for_five_minutes=False)
        return response

    transactional = paymentDao.getTransactionaByTransId(request.transaction_id)
    cost = int((int(request.seconds_chatted) + 60) / 60) * 5
    sessionRequest = sessionRequestService.getSessionByRequestId(request.session_request_id)

    if transactional == None:
         paymentDao.createTranaction(userId = user.id,razorpayOrderRequest = request,cost=cost, sessionType = sessionRequest.session_type )

    else:
        paymentDao.updateTranaction(razorpayOrderRequest = request, cost=cost)

    userDao.updateUserBalance(user.id, user.credits - 5) #Todo create this function in user dao
    sufficent_balance = True
    availability = True

    if user.credits <25:
        sufficent_balance = False

    if user.credits <5:
        availability = False

    response = placeRazorpayOrderResponse(user_credits=user.credits,
                                          status="Success", msg="Sufficient credits", credits_availablility=availability,
                                          credits_sufficient_for_five_minutes=sufficent_balance)
    return response

    # Todo need to make changes in android as well


def confirmOrder(request : confirmRazorpayOrderRequest) -> confirmRazorpayOrderResponse:
    response_string = request.response
    payload = json.loads(response_string)
    if 'razorpay_payment_id' in payload:
        paymentDao.updatePamentOrder(order_id=payload['razorpay_order_id'],payment_id= payload['razorpay_payment_id'],
                                     signature=payload['razorpay_signature'], gateway='razorpay')

        url= getRazorpayURl(payload['razorpay_order_id'])
        payload = {}
        headers = getHeaderForOrder()

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            responseDict = json.loads(response.text)
            if responseDict['status'] == 'paid':
                # paymentDao.updateOrderStatus(payload['razorpay_order_id'],True) #will add filed in future and do this
                userService.addUserCredit(responseDict['amount'] / 100) #Todo create this in user service

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