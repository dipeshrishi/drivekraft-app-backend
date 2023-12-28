from app.utils import validateContactNumber
from app.Models.DAO import userDao


def createUser(contactNumber):
    validate = validateContactNumber(contactNumber)
    if(validate):
        user = createUserInternal(contactNumber=contactNumber)
        return user
    return ""


def createUserInternal(contactNumber):
    validate = validateContactNumber(contactNumber)
    if(validate):
        return userDao.addUser(contactNumber)


def getUserByContact(contactNumber):
    return userDao.getUser(contactNumber)

