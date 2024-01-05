from flask import g
from app.Models.mysql.psychlogist import Psychologist
from app.Models.mysql.psychologistData import PsychologistData


def getAllPsychologist():
    session = g.session
    psychologist_entire_details_obj = session.query(Psychologist, PsychologistData).\
        join(Psychologist, PsychologistData.psychologistId == Psychologist.id).\
        filter(Psychologist.enabled == True).\
        order_by(PsychologistData.online.desc(), PsychologistData.isBusy).\
        all()

    return psychologist_entire_details_obj