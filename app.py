from flask import Flask,jsonify,request,render_template,g
import logging
import json
from flask_caching import Cache
from functools import wraps
from db import connect, disconnect
import configuration.logfileConfigs as logfileConfigs
import otp.otpService as otpService
import user.userService as userService
import role.roleService as roleService
import psychologist.psychologistService as psychologistService
import sessionRequest.sessionRequestService as sessionRequestService
import payment.paymentService as paymentService
import admin.adminService as adminService
import feedback.feedbackService as feedbackService
import sessionEntity.sessionEntityService as sessionEntityService



app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
logfileConfigs.logFileCongig()


# Create the database connection pool
connection_pool, _ = connect()


def database_connection(view):
    @wraps(view)
    def decorated_view(*args, **kwargs):
        connection_object = connection_pool.get_connection()
        cursor = connection_object.cursor()
        g.db = connection_object
        g.cursor = cursor
        logging.info("trying to accquire db connection")

        try:
            result = view(*args, **kwargs)
            logging.info("db connection acquired")
        except Exception as e:
            # Handle database-related errors here
            result = "An error occurred while processing the request."
            logging.error(result)
        finally:
            if 'db' in g:
                cursor = g.pop('cursor', None)
                if cursor:
                    cursor.close()
                connection_object = g.pop('db', None)
                if connection_object:
                    connection_object.close()
                logging.info("db connection released")
        return result

    return decorated_view

@app.route("/drivekraft-next")
def newUI():
     return render_template(".next/index.html")

@app.route("/")
def index():
    logging.info("testt")
    return "test"

@app.route("/home")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/blog.html")
def blog():
    return render_template("blog.html")

@app.route("/api/login-send-otp",methods=['POST'])
@database_connection
def sendOtp():
    return otpService.sendOtpInternally()

@app.route("/api/login",methods=['POST'])
@database_connection
def generateToken():
    return otpService.generateTokenInternally()


@app.route("/api/user/firebase", methods =['POST'])
@database_connection
def getUSerForFirebase():
    headers = request.headers.get('Authorization')
    cache_key = f'data_{headers}'
    data = cache.get(cache_key)
    if data is None:
        data = userService.firebaseUser()
        cache.set(cache_key, data, timeout=60)
    else:
        logging.info("/api/user/firebase served by cache layer")
    return data


@app.route("/api/user", methods =['GET'])
@database_connection
def getUSer():
    headers = request.headers.get('Authorization')
    cache_key = f'data_{headers}'
    data = cache.get(cache_key)
    if data is None:
        user = userService.getUser()
        data = jsonify({
        "user": (user.__dict__)
    })
    else:
        logging.info("/api/user served by cache layer")
    cache.set(cache_key, data, timeout=60)
    return data


@app.route("/api/username/check", methods =['POST'])
@database_connection
def checkUserNameIfExists():
    return userService.checkUsername()

@app.route("/api/username/check/confirm", methods =['POST'])
@database_connection
def confirmUserName():
    return userService.confirmUsername()

@app.route("/api/users/status/busy", methods =['POST'])
@database_connection
def updateBusyStatus():
    return userService.updateBusyStatus()


@app.route("/api/check/user/busy", methods =['POST'])
@database_connection
def checkBusyStatus():
    return userService.checkUserBusy()


@app.route("/api/user/online", methods =['POST'])
@database_connection
def setUserOnline():
    return userService.setUserOnline()



@app.route("/api/check/user/bal", methods =['GET'])
@database_connection
def checkUserBalance():
    return userService.checkUserBalance()




@app.route("/api/session/book/request", methods =['POST'])
@database_connection
def bookRequest():
        return sessionRequestService.sendSessionRequest()


@app.route("/api/session/book/request/cancel", methods =['POST'])
@database_connection
def cancelSessionRequest():
        return sessionRequestService.cancelSessionRequest()

@app.route("/api/session/book/request/verify", methods =['POST'])
@database_connection
def verifySessionRequest():
        return sessionRequestService.verifySessionRequest()


@app.route("/api/session/request/fetch" , methods =['GET'])
@database_connection
def fetchSessionRequest():
    return sessionRequestService.fetchSessionRequest()


@app.route("/api/session/request/confirm", methods =['POST'])
@database_connection
def confirmSessionRequestInternal():
        return sessionRequestService.confirmSessionRequest()


@app.route("/api/role", methods =['GET'])
@database_connection
def getRole():
        return roleService.getUserRole()


@app.route("/api/psychologists", methods =['GET'])
@database_connection
def getPsychologist():
        return psychologistService.getPsychologistList()

@app.route("/api/order/create", methods =['POST'])
@database_connection
def createRazorpayOrder():
    return paymentService.createRazorpayOrder()

@app.route("/api/app/ver", methods =['GET'])
@database_connection
def appVersion():
    return ({
         "id": 1,
         "key": "version",
         "value": "102.0",
         "created_at": "2023-08-02T11:40:20.000000Z",
         "updated_at": "2023-08-02T11:40:20.000000Z"
    })


@app.route("/api/order/placed", methods =['POST'])
@database_connection
def placeRazorpayOrder():
    return paymentService.placeRazorpayOrder()

@app.route("/api/order/confirm", methods =['POST'])
@database_connection
def confirmRazorpayOrder():
    return paymentService.confirmRazorpayOrder()

@app.route("/api/search/psychologist", methods =['POST'])
@database_connection
def searchPsychologistByDescription():
    return  psychologistService.getPsychologistByDescription()

@app.route("/api/get/psychologistforSearch", methods =['Get'])
@database_connection
def imagesForSearchPage():
    return psychologistService.getPsychologistForSearchPage()

@app.route("/lastSeen", methods =['POST'])
@database_connection
def lastSeen():
    return psychologistService.updateLastSeen()

@app.route("/trackListners/<name>/<status>",methods=['POST','GET'])
@database_connection
def trackListners(name,status):
            return psychologistService.updateStatus(name,status)


@app.route("/admin/dashboard/listner")
@database_connection
def getListnersData():
    data,data2=psychologistService.fetchDataofPsyDashboard()
    return render_template("psychologistDashboard.html",data=data, data2= data2[0])

@app.route("/admin/dashboard/secretKey/adminboard")
@database_connection
def adminBoard():
    data=adminService.fetchDataofAdminDashboard()
    return render_template("adminDashboard.html", data=data)


@app.route('/requestStatusUpdate', methods = ['POST'])
@database_connection
def requestStatusUpdate():
        return sessionRequestService.updateSessionRequestStatus()

@app.route('/api/reviews', methods = ['POST'])
@database_connection
def addFeedbackForSessionRequest():
        return feedbackService.addFeedback()

@app.route('/api/get/reviews', methods = ['GET'])
@database_connection
def getFeedbacks():
        return feedbackService.getFeedback()

@app.route('/psychologists/session-type', methods = ['POST'])
@database_connection
def updatePsychologistSessionType():
        return userService.updatingSessionType()


@app.route('/user/sessionhistory', methods = ['POST'])
@database_connection
def getUserSessionHistory():
        return sessionEntityService.getSessionHistoryForUser()

#app.run(debug=True)


