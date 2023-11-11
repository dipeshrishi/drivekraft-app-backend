from flask import request, jsonify
from datetime import datetime,timedelta
import psychologist.psychologistDao as psychologistDao
import json
import time

def getPsychologistList():
    data= psychologistDao.getPsychologistInOrder()
    return ({
        "data": data
    })


def getPsychologistById(psyId):
    return psychologistDao.getPsychologistById(psyId)


def getPsychologistByDescription():
    obj = json.loads(request.data)
    description = obj['value']
    psy= psychologistDao.getPsychologistByDescription(description)
    return jsonify({
        "psyologistList": (psy)
    })

def updateLastSeen():
    response = dict()
    try:
        obj = json.loads(request.data)
        listner_email = obj['email']
        currentTime = datetime.now() + timedelta(hours=5, minutes=30)

        psychologistDao.updatingLastSeenInternally(listner_email,currentTime)
        response['success'] = True
        response['message'] = 'lastSeen Updated Successfully'
        json_object = json.dumps(response)
        return json_object
    except Exception as error:
        response['success'] = False
        response['message'] = error
        json_object = json.dumps(response)
        return json_object


def updateStatus(email,status):
    try:
        if status == "on" or status =='1':
            turnStatusOff(email)
            turnStatusOn(email)

        if status == "off" or status =='0':
            turnStatusOff(email)

        response= dict()

        response['success'] = True
        response['message'] = 'Psychologist status has been updated Successfully'
        json_object = json.dumps(response)
        return json_object
    except Exception as error:
        response = dict()
        response['success'] = False
        response['message'] = error
        json_object = json.dumps(response)
        return json_object


def turnStatusOff(email):
    listner_id, activeTimes = psychologistDao.getIdAndActivesFromPsyEmail(email)
    endTime = datetime.now() + timedelta(hours=5, minutes=30)
    endEpoch = int(time.time())
    psychologistDao.turnStatusOff(listner_id,endTime,endEpoch,activeTimes)

    return

def turnStatusOn(email):
    listner_id, activeTimes = psychologistDao.getIdAndActivesFromPsyEmail(email)
    startTime = datetime.now() + timedelta(hours=5, minutes=30)
    startEpoch = int(time.time())
    psychologistDao.turnStatusOn(listner_id, startTime, startEpoch, activeTimes)

    return


def fetchDataofPsyDashboard():
    return psychologistDao.fetchDataForPsychologist();

def incrementSessionCount(user_id):
    psychologistDao.updateSessionCountById(user_id)

def getPsychologistForSearchPage():
    psy= psychologistDao.psyListForSearchPage()
    return jsonify({
        "psyologistList": (psy)
    })

