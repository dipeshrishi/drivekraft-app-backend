
from db import connect, disconnect
from psychologist import psychologistService
from admin import adminService

def dailyCron():
    # new new entry for all active listners
    connection_pool,obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"Select distinct u.emailId from activeTimes at join psychologist p on p.id= at.psyId join user u on u.id= p.user_id	where at.endTime='0'"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchall()
    disconnect(connection_pool, obj, mycursor)
    print("dta", data)

    for name in data:
        toggleStatus(name[0])

    copyTodayCurrentTimeToYst()
    adminService.updateDataForAdminDashboard()
    return


def toggleStatus(name):
    psychologistService.updateStatus(name, 'off')
    psychologistService.updateStatus(name, 'on')
    return


def copyTodayCurrentTimeToYst():
    connection_pool,obj = connect()
    mycursor = obj.cursor(buffered=True)
    query = f"Select id,todayCurrentActiveTime  from psychologist "
    mycursor.execute(query)
    dataList = mycursor.fetchall()

    for data in dataList:
        query1 = f"update psychologist set todayCurrentActiveTime ='0' , yesterDayActiveTime ='{data[1]}'  where id ='{data[0]}'"
        print("bla", query1)
        mycursor.execute(query1)
    obj.commit()
    disconnect(connection_pool, obj, mycursor)

    return


dailyCron()

#     obj = connect()
#     mycursor = obj.cursor(buffered=True)
#     query=f"Select id, startEpoch from activeTimes where name='{psyName}' order by id desc limit 1"
#     mycursor.execute(query)
#     data=mycursor.fetchone()
#     print("dta",data)

#     if data == None:
#             disconnect(obj,mycursor)
#             return

#     id= data[0]
#     endTime = datetime.now()  + timedelta(hours=5, minutes=30)
#     endEpoch = int(time.time())
#     duration = endEpoch-int(data[1])

#     query1 = f"update activeTimes set endTime ='{endTime}' , endEpoch ='{endEpoch}' , duration='{duration}' where id ='{id}'"
#     print(query1)
#     mycursor.execute(query1)

#     updatedActiveTime = int(duration) + int(activeTimes)
#     query2 =f"update listners set todayCurrentActiveTime = '{updatedActiveTime}' where id='{listner_id}'"
#     print(query2)
#     mycursor.execute(query2)

#     obj.commit()
#     disconnect(obj,mycursor)

#     return "done"

