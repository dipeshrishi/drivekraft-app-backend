from flask import Flask
import logging
import configuration.logfileConfigs as logfileConfigs
import otp.otpService as otpService
import user.userService as userService





app = Flask(__name__)
logfileConfigs.logFileCongig()


@app.route("/")
def index():
    logging.info("testt")
    return "test"


@app.route("/api/login-send-otp",methods=['POST'])
def sendOtp():
    return otpService.sendOtpInternally()

@app.route("/api/login",methods=['POST'])
def generateToken():
    return otpService.generateTokenInternally()


@app.route("/api/user/firebase", methods =['POST'])
def getUSerForFirebase():
    return userService.firebaseUser()

@app.route("/api/username/check", methods =['POST'])
def checkUserNameIfExists():
    return userService.checkUsername()

app.run(debug=True)


