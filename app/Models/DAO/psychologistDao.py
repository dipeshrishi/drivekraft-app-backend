from flask import g
from app.Models.mysql.psychologist import Psychologist
from app.Models.mysql.psychologistData import PsychologistData
from sqlalchemy.orm.exc import NoResultFound


def getAllPsychologist():
    session = g.session
    psychologist_entire_details_obj = session.query(Psychologist, PsychologistData).\
        join(Psychologist, PsychologistData.psychologistId == Psychologist.id).\
        filter(Psychologist.enabled == True).\
        order_by(PsychologistData.online.desc(), PsychologistData.isBusy).\
        all()

    result_list = [
        {**psychologist.as_dict(), **data.as_dict()}
        for psychologist, data in psychologist_entire_details_obj
    ]

    return result_list

def setStatusBusy(psychologist_id):
    session = g.session
    try:
        psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist_id).first()
        psychologistData.isBusy = True
    except NoResultFound:
        return False
    return True

def updateBusyStatus(busy,id):
    session = g.session
    try:
        psychologist = session.query(Psychologist).filter_by(userId=id).first()
    except NoResultFound:
        return None
    try:
        psychologistData = session.query(PsychologistData).filter_by(psychologistId=psychologist.id).first()
        psychologistData.isBusy = busy
    except NoResultFound:
        return None
    return psychologistData

