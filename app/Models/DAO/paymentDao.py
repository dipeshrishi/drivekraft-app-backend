from app.utils import currentTime
from app.Models.mysql.paymentOrder import PaymentOrder
from app.Models.mysql.transaction import Transaction
from flask import g


def storePaymentOrder(responseDict, userId):
    now = currentTime.getCurrentTime()

    session = g.session

    newPaymentOrder = PaymentOrder(orderId=responseDict['id'], amount=(responseDict['amount'] / 100), userId=userId,
                                   paymentGateway="Razorpay", created=now, updated=now)

    session.add(newPaymentOrder)
    session.commit()

    return "New order created in the database"


def getTransactionaByTransId(transactionId):
    session = g.session
    transaction = session.query(PaymentOrder).filter_by(contactNumber=transactionId).one()

    return transaction


def createTranaction(userId, razorpayOrderRequest, cost, sessionType):
    now = currentTime.getCurrentTime()

    session = g.session

    newTransaction = Transaction(userId=userId,
                                 transactionId=razorpayOrderRequest.transaction_id,
                                 psychologistId=razorpayOrderRequest.psychologist_id,
                                 sessionRequestId=razorpayOrderRequest.session_request_id,
                                 secondsChatted=razorpayOrderRequest.seconds_chatted,
                                 amountDeducted=cost, sessionType=sessionType, created=now, updated=now)

    session.add(newTransaction)
    session.commit()

    return "New transaction created in the database"


def updateTransaction(razorpayOrderRequest, cost):
    session = g.session

    transaction = session.query(Transaction).filter_by(transactionId=razorpayOrderRequest.transaction_id)
    transaction.amountDeducted = cost

    session.commit()



def updatePaymentOrder(order_id, payment_id, signature, gateway):
    session = g.session
    paymentOrder = session.query(PaymentOrder).filter_by(orderId=order_id)
    paymentOrder.paymentId = payment_id
    paymentOrder.signature = signature
    paymentOrder.paymentGateway = gateway

    session.commit()


# f"Update paymentOrder set payment_id ='{razorpay_payment_id}' ,signature ='{razorpay_signature}',paymentGateway ='{gateway}',updated_at =now() where order_id ='{razorpay_order_id}'"
