from flask import Flask,jsonify,request,render_template
import logging
import json
import configuration.logfileConfigs as logfileConfigs
import otp.otpService as otpService
import user.userService as userService
import role.roleService as roleService
import psychologist.psychologistService as psychologistService
import sessionRequest.sessionRequestService as sessionRequestService
import payment.paymentService as paymentService


app = Flask(__name__)
#logfileConfigs.logFileCongig()


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
def sendOtp():
    return otpService.sendOtpInternally()

@app.route("/api/login",methods=['POST'])
def generateToken():
    return otpService.generateTokenInternally()


@app.route("/api/user/firebase", methods =['POST'])
def getUSerForFirebase():
    return userService.firebaseUser()


@app.route("/api/user", methods =['GET'])
def getUSer():
    user=userService.getUser()
    return jsonify({
        "user": (user.__dict__)
    })


@app.route("/api/username/check", methods =['POST'])
def checkUserNameIfExists():
    return userService.checkUsername()

@app.route("/api/username/check/confirm", methods =['POST'])
def confirmUserName():
    return userService.confirmUsername()

@app.route("/api/users/status/busy", methods =['POST'])
def updateBusyStatus():
    return userService.updateBusyStatus()


@app.route("/api/check/user/busy", methods =['POST'])
def checkBusyStatus():
    return userService.checkUserBusy()


@app.route("/api/user/online", methods =['POST'])
def setUserOnline():
    return userService.setUserOnline()



@app.route("/api/check/user/bal", methods =['GET'])
def checkUserBalance():
    return userService.checkUserBalance()




@app.route("/api/session/book/request", methods =['POST'])
def bookRequest():
        return sessionRequestService.sendSessionRequest()


@app.route("/api/session/book/request/cancel", methods =['POST'])
def cancelSessionRequest():
        return sessionRequestService.cancelSessionRequest()

@app.route("/api/session/book/request/verify", methods =['POST'])
def verifySessionRequest():
        return sessionRequestService.verifySessionRequest()


@app.route("/api/session/request/fetch" , methods =['GET'])
def fetchSessionRequest():
    rqst= sessionRequestService.fetchSessionRequest()

    return jsonify({
        "sessions": (rqst)
    })



@app.route("/api/session/request/confirm", methods =['POST'])
def confirmSessionRequestInternal():
        return sessionRequestService.confirmSessionRequest()


@app.route("/api/role", methods =['GET'])
def getRole():
        return roleService.getUserRole()


@app.route("/api/psychologists", methods =['GET'])
def getPsychologist():
        data= psychologistService.getPsychologistList()
        return ({
            "data": data
        })

@app.route("/api/order/create", methods =['POST'])
def createRazorpayOrder():
    response= paymentService.createRazorpayOrder()
    return jsonify({
        "order_id": response['id'],
        "currency" : "INR" ,
        "amount" : response['amount']/100
    })


@app.route("/api/app/ver", methods =['GET'])
def appVersion():
    return ({
         "id": 1,
         "key": "version",
         "value": "102.0",
         "created_at": "2023-08-02T11:40:20.000000Z",
         "updated_at": "2023-08-02T11:40:20.000000Z"
    })


@app.route("/api/order/placed", methods =['POST'])
def placeRazorpayOrder():
    return paymentService.placeRazorpayOrder()

@app.route("/api/order/confirm", methods =['POST'])
def confirmRazorpayOrder():
    return paymentService.confirmRazorpayOrder()


@app.route("/lastSeen", methods =['POST'])
def lastSeen():
    return psychologistService.updateLastSeen()

@app.route("/trackListners/<name>/<status>",methods=['POST','GET'])
def trackListners(name,status):
        response=dict()
        try:
            psychologistService.updateStatus(name,status)
            response['success'] = True
            response['message'] = 'Psychologist status has been updated Successfully'
            json_object = json.dumps(response)
            return json_object
        except Exception as error:
            response['success'] = False
            response['message'] = error
            json_object = json.dumps(response)
            return json_object


@app.route("/admin/dashboard/listner")
def getListnersData():
    data,data2=psychologistService.fetchDataofPsyDashboard()
    print(data,data2)
    return render_template("psychologistDashboard.html",data=data, data2= data2[0])

#app.run(debug=True)


