from app.Contract.Response.allPsychologistResponse import allPsychologistResponse
from app.Models.DAO import psychologistDao

def getAllPsychologist()-> allPsychologistResponse:
    response= psychologistDao.getAllPsychologist()
    return response