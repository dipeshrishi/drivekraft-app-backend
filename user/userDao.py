from flask import request
from db import connect,disconnect
import logging
import  configuration.currentTime as currentTime
import  user.user as user
from flask import  g

def addUser(contactNumber):
    now=currentTime.getCurrentTimeInIst()
    # connection_pool,obj=connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql= f"Insert into user(contact,created,updated) values('{contactNumber}','{now}','{now}')"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj,mycursor)
    logging.info(f"user with contact number {contactNumber} created")
    return "user is created"

def getUserByContact(contactNumber):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,name, username ,emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,role_id,is_online,is_busy,is_call,is_chat from user where contact='{contactNumber}'"
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return None
    return user.user(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15])


def getUserById(userId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id,name,username, emailId,contact,totalSessions,firebase_id,firebase_name,firebase_email,firebase_password,credits,role_id,is_online,is_busy,is_call,is_chat from user where id='{userId}'"
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return None
    return user.user(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15])




def updateUserFirebaseData(userId):
    now = currentTime.getCurrentTimeInIst()
    firebase_id = request.form.get('firebase_id')
    firebase_name = request.form.get('firebase_name')
    firebase_email = request.form.get('firebase_email')
    firebase_password = request.form.get('mobile')
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set  firebase_id ='{firebase_id}' , firebase_name ='{firebase_name}' , firebase_email ='{firebase_email}' , firebase_password = '{firebase_password}' , updated ='{now}' where id ='{userId}'"
    mycursor.execute(sql)
    # obj.commit()
    g.db.commit()

    sql = f"Update psychologist set  firebase_id ='{firebase_id}' , firebase_name ='{firebase_name}' , firebase_email ='{firebase_email}' , firebase_password = '{firebase_password}' , updated_at ='{now}' where user_id ='{userId}'"
    mycursor.execute(sql)
    #obj.commit()
    g.db.commit()

    # disconnect(connection_pool,obj, mycursor)
    logging.info(f"user with user id {userId} updated")
    return "user is updated"


def getUserByUserName(username):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"select id from user where username='{username}'"
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return None
    return data[0]


def updateUserBalance(id,bal):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set credits ='{bal}',updated =now() where id ='{id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"Balance updated to  {bal} for user {id}")
    return

def updateUsetStatus(user_id,status):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set is_busy ='{status}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    #obj.commit()
    sql = f"Update psychologist set is_busy ='{status}',updated_at =now() where user_id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)
    logging.info(f"user status  updated to  {status} for user {user_id}")
    return

def updateOrderStatus(razorpay_order_id,status):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update paymentorder set is_busy ='{status}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"user status  updated to  {status} for user {user_id}")
    return


def updateUserAvailStatus(user_id,status):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set is_online ='{status}', is_chat='{status}',is_call ='{status}',updated =now() where id ='{user_id}'"
    print(sql)
    mycursor.execute(sql)
    g.db.commit()
    #obj.commit()
    sql = f"Update psychologist set online ='{status}',updated_at =now() where user_id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    #obj.commit()
    #disconnect(connection_pool,obj, mycursor)

    logging.info(f"user status  updated_at to  {status} for user {user_id}")
    return


def updateUsername(user_id,username):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set username ='{username}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool,obj, mycursor)

    logging.info(f"usermane  updated to  {username} for user {user_id}")
    return


def updateAvailableSessionTypeByUserId(user_id,is_chat,is_call):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set is_call ='{is_call}',is_chat='{is_chat}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)

    logging.info(f"Session type updated  for user {user_id}")
    return


def updateCallStatusByUserId(user_id,is_call):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set is_call ='{is_call}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)

    logging.info(f"Session type updated  for user {user_id}")
    return


def updateChatStatusByUserId(user_id,is_chat):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    sql = f"Update user set is_chat='{is_chat}',updated =now() where id ='{user_id}'"
    mycursor.execute(sql)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)

    logging.info(f"Session type updated  for user {user_id}")
    return