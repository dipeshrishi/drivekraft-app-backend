import user.userService as userService
import externalAPIs.whatsappApi.sendNormalMessage as snm
import externalAPIs.whatsappApi.messages as msg



def nortifyMissedMessage(userId):
    user =userService.getUserById(userId)
    sendMissedSessionMSgToLisnter(user.contact)
    sendMissedSessionMSgToAdmin(user.name)

    return


def sendMissedSessionMSgToLisnter(contact):
    return snm.sendMessage(contact,msg.listnerMsgOnSessionMiss())

def sendMissedSessionMSgToAdmin(name):
     snm.sendMessage('917889085355', msg.adminMsgOnSessionMiss(name))
     snm.sendMessage('919717707445', msg.adminMsgOnSessionMiss(name))
     return
