from db import connect,disconnect
import logging
import payment.transaction as transaction
import uuid
from flask import  g

def storePaymentOrder(responseDict, userId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Insert into paymentOrder(order_id, payment_id,signature,amount,userId," \
          f"paymentGateway,created_at,updated_at) values('{responseDict['id']}','none','none'," \
          f"'{responseDict['amount']/100}','{userId}' ,'Razorpay',now(),now())"
    mycursor.execute(sql)
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    g.db.commit()
    logging.info(f"order for user {userId} created for amount {responseDict['amount']/100}")
    return "order created is created"


def getTransactionaByTransId(transId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,transaction_id, userId,psychologist_id,session_request_id,seconds_chatted,amount_deducted,session_type,created_at,updated_at from transaction where transaction_id='{transId}'"
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)
    if data == None:
        return None
    return transaction.transaction(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],data[9])


def createTranaction(user_id,psychologist_id,session_request_id,seconds_chatted,cost,session_type):
    tranactionalId= str(uuid.uuid4())
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Insert into transaction(transaction_id, userId,psychologist_id," \
          f"session_request_id,seconds_chatted,amount_deducted,session_type,created_at,updated_at)" \
          f" values('{tranactionalId}','{user_id}','{psychologist_id}','{session_request_id}'," \
          f"'{seconds_chatted}','{cost}','{session_type}', now(), now() )"
    mycursor.execute(sql)
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    g.db.commit()
    logging.info(f"transaction created with {tranactionalId} id")
    return tranactionalId

def updateTranaction(transId,seconds_chatted,cost):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update transaction set seconds_chatted ='{seconds_chatted}' ,amount_deducted ='{cost}' ,updated_at =now() where id ='{transId}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"transaction upated with {transId} id")
    return

def updatePamentOrder(razorpay_order_id,razorpay_payment_id,razorpay_signature,gateway):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update paymentOrder set payment_id ='{razorpay_payment_id}' ,signature ='{razorpay_signature}',paymentGateway ='{gateway}',updated_at =now() where order_id ='{razorpay_order_id}'"
    mycursor.execute(sql)
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    g.db.commit()

    logging.info(f"payment order  upated with {razorpay_order_id} id")
    return


