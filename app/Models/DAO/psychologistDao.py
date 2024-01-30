from flask import g
from app.Models.mysql.psychologist import Psychologist
from app.Models.mysql.psychologistData import PsychologistData
from sqlalchemy.orm.exc import NoResultFound


def getAllPsychologist():
    session = g.session
    psychologist_entire_details_obj = session.query(Psychologist, PsychologistData). \
        join(Psychologist, PsychologistData.psychologistId == Psychologist.id). \
        filter(Psychologist.enabled == True). \
        order_by(PsychologistData.online.desc(), PsychologistData.isBusy). \
        all()

    result_list = [
        {**psychologist.as_dict(), **data.as_dict()}
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
         psychologistData = session.query(PsychologistData.isBusy).filter_by(psychologistId=psychologist.id).first()
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
        psychologist_id, email = session.query(Psychologist.id, Psychologist.emailId).filter_by(userId=user_id).first()
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


