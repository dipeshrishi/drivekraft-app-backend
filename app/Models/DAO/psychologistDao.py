from flask import g
from app.Models.mysql.psychologist import Psychologist
from app.Models.mysql.psychologistData import PsychologistData
from sqlalchemy.orm.exc import NoResultFound
import logging


def getAllPsychologist():
    session = g.session
    psychologist_entire_details_obj = session.query(Psychologist, PsychologistData). \
        join(Psychologist, PsychologistData.psychologistId == Psychologist.id). \
        filter(Psychologist.enabled == True). \
        order_by(PsychologistData.online.desc(), PsychologistData.isBusy). \
        all()

    result_list = [
        {**psychologist.as_dict(), **data.as_dict(), 'user_id': psychologist.userId,
         'firebase_id':data.firebaseId,'firebase_name' :data.firebaseName,
         'firebase_email': data.firebaseEmail,'firebase_password': data.firebasePassword ,'mobile': psychologist.contactNumber} # hack to fix data user issue
        for psychologist, data in psychologist_entire_details_obj
    ]

    return result_list


def setStatusBusy(psychologist_id,busyStatus):
    session = g.session
    try:
        psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist_id).first()
        psychologistData.isBusy = busyStatus
        session.add(psychologistData)
        session.commit()
    except NoResultFound:
        return False
    return True


def updateBusyStatus(user_id,busy):
    session = g.session
    try:
        psychologist = session.query(Psychologist).filter_by(userId=user_id).first()
    except NoResultFound:
        return None
    try:
         psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist.id).first()
    except NoResultFound:
        return None
    psychologistData.isBusy = busy
    session.commit()
    return psychologistData


def createPsychologist(psychologist: Psychologist):
    session = g.session
    try:
        session.add(psychologist)
        session.commit()
    except:
        return None
    return psychologist.id


def createPsychologistData(psychologistData: PsychologistData):
    session = g.session
    try:
        session.add(psychologistData)
        session.commit()
    except:
        return None
    return psychologistData.id

def getPsychologistStatus(psychologist_id):
    session = g.session
    try:
        psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist_id).first()
        return psychologistData.isBusy,psychologistData.online
    except NoResultFound:
        return False
    return True

def getPsychologistOnlineStatus(user_id):
    session = g.session
    try:
        psychologist_id, email = session.query(Psychologist.id, Psychologist.emailId).filter_by(user_id=user_id).first()
        if psychologist_id is None:
            return None
        online = session.query(PsychologistData.online).filter_by(psychologistId=psychologist_id).scalar()

        return email, online
    except NoResultFound:
        return None


def getPsychologistIdFromUserID(UserId):
    session = g.session
    try:
        psychologistData = session.query(Psychologist).filter_by(userId=UserId).first()
        print("psyho " + str(psychologistData))
        return psychologistData.id
    except NoResultFound:
        return False
    return True

def updateFirebaseDetails(firebaseData,userDetails):
    session = g.session
    logging.info("userId" + str(userDetails.id))
    psychologist = session.query(Psychologist).filter_by(userId=userDetails.id).first()
    logging.info("psychologist" + str(psychologist.id))
    psychologistData= session.query(PsychologistData).filter_by(psychologistId=psychologist.id).first()
    psychologistData.firebaseId=firebaseData.firebaseId
    psychologistData.firebasePassword= firebaseData.firebasePassword
    psychologistData.firebaseEmail= firebaseData.firebaseEmail
    psychologistData.firebaseName = firebaseData.firebaseName
    logging.error("updating psychologistData id : {}".format(psychologist.id))
    logging.error("updating psychologistData firebasePassword : {}".format(firebaseData.firebasePassword))

    session.commit()
    return True

def changeOnlineStatus(userId,onlineStatus):
    session = g.session
    try:
        logging.info("userId" + str(userId))
        psychologist = session.query(Psychologist).filter_by(userId=userId).first()
        logging.info("psychologist" + str(psychologist.id))
        psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist.id).first()
        psychologistData.online = onlineStatus
        session.add(psychologistData)
        session.commit()
    except NoResultFound:
        return False
    return  True




