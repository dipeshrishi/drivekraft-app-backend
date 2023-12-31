from db import connect,disconnect
import  psychologist.psychologist as psychologist
from flask import g
import json


def getPsychologistInOrder():
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = '''select p.id,p.name,p.profile_image,p.is_busy,p.firebase_id,p.firebase_name,p.firebase_email,p.firebase_password,p.uuid,
      p.user_id, p.description,p.session_count,p.rating,
               p.yrs_of_exp,p.education,p.short_desc,p.status,order_,p.created_at
               ,p.updated_at,p.gender,p.age,p.interests,p.languages,p.`online` , u.contact,u.is_call,u.is_chat,p.delta,p.lastSeen from psychologist p left join user u on p.user_id = u.id where p.enable ='1' order by p.`online` desc , p.is_busy '''
    mycursor.execute(query)
    psyData = mycursor.fetchall()

    # disconnect(connection_pool, obj, mycursor)

    psychologistList= list()

    for data in psyData:
        psy=psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     int(data[11]) + int(data[28]), data[12], data[13],data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24],data[25],data[26],data[27],data[28],data[29])

        psychologistList.append(psy.__dict__)

    return psychologistList


def getPsychologistById(psyId):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f'''select p.id,p.name,p.profile_image,p.is_busy,p.firebase_id,p.firebase_name,p.firebase_email,p.firebase_password,p.uuid,
      p.user_id, p.description,p.session_count,p.rating,
               p.yrs_of_exp,p.education,p.short_desc,p.status,order_,p.created_at
               ,p.updated_at,p.gender,p.age,p.interests,p.languages,p.`online` , u.contact,u.is_call,u.is_chat,p.lastSeen from psychologist p left join user u on p.user_id = u.id  where u.id ='{psyId}' '''
    print("here" +  str(query))
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)

    if data == None:
        return None
    return psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     data[11], data[12], data[13],data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24],data[25],data[26],data[27],data[29])



def updatingLastSeenInternally(listner_email,currentTime):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor

    query1 = f"update psychologist set lastSeen ='{currentTime}' where user_id in (select id from user where emailId= '{listner_email}' )"
    print(query1)
    mycursor.execute(query1)
    g.db.commit()

    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)

    return



def getIdAndActivesFromPsyEmail(email):
        # connection_pool, obj = connect()
        # mycursor = obj.cursor(buffered=True)
        mycursor = g.cursor
        query = f"select id,todayCurrentActiveTime from psychologist where user_id in ( select id from user where emailId ='{email}') limit 1"
        print(query)
        mycursor.execute(query)
        data = mycursor.fetchone()
        # disconnect(connection_pool, obj, mycursor)
        id = data[0]
        activeTimes = data[1]

        return id, activeTimes

def turnStatusOff(listner_id,endTime,endEpoch,activeTimes):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f"Select id, startEpoch from activeTimes where psyId='{listner_id}' and endTime='0' order by id desc limit 1"
    mycursor.execute(query)
    data = mycursor.fetchone()
    print("dta check", data)

    if data == None:
        # disconnect(connection_pool, obj, mycursor)
        return

    id = data[0]
    duration = endEpoch - int(data[1])

    query1 = f"update activeTimes set endTime ='{endTime}' , endEpoch ='{endEpoch}' , duration='{duration}' where id ='{id}'"
    print(query1)
    mycursor.execute(query1)

    updatedActiveTime = int(duration) + int(activeTimes)
    query2 = f"update psychologist set todayCurrentActiveTime = '{updatedActiveTime}'  where id='{listner_id}'"
    print("here", query2)
    mycursor.execute(query2)

    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)
    return

def turnStatusOn(listner_id, startTime, startEpoch, activeTimes):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor

    query1 = f"Insert into activeTimes(psyId,startTime,startEpoch) values('{listner_id}','{startTime}','{startEpoch}')"
    print(query1)
    mycursor.execute(query1)
    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)
    return


def fetchDataForPsychologist():
    #connection_pool, obj = connect()
    mycursor = g.cursor
    #mycursor = obj.cursor(buffered=True)

    query1 = "select name,session_count,round(round(yesterDayActiveTime/60)/60,2),session_count,TotalRequestsRecieved,missedRequests, delta from psychologist where enable= true"
    print(query1)
    mycursor.execute(query1)
    data = mycursor.fetchall()

    query2 = "select count(*) from transaction "
    print(query2)
    mycursor.execute(query2)
    data2 = mycursor.fetchone()

    #disconnect(connection_pool, obj, mycursor)

    return data, data2


def updatePsychologistSessionData(listener_id,status):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor

    query = f"select missedRequests,TotalRequestsRecieved,session_count from psychologist where user_id = '{listener_id}' "
    print(query)
    mycursor.execute(query)
    data2 = mycursor.fetchone()
    missedRequests = int(data2[0])
    TotalRequestsRecieved = int(data2[1])
    session_count = int(data2[2])

    # i guess REQUEST_ACCEPTED doesnt work ... haha
    if status == 'REQUEST_ACCEPTED':
        query2 = f"update psychologist set session_count = {session_count} +1 , TotalRequestsRecieved ={TotalRequestsRecieved} +1   where user_id='{listener_id}'"
        print("here", query2)
        mycursor.execute(query2)

    if status == 'REQUEST_MISSED':
        query2 = f"update psychologist set missedRequests = {missedRequests} +1 , TotalRequestsRecieved ={TotalRequestsRecieved} +1   where user_id='{listener_id}'"
        print("here", query2)
        mycursor.execute(query2)

    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)

    return "updated"

def updateSessionCountById(user_id):
    # connection_pool, obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor

    query = f"select session_count,TotalRequestsRecieved from psychologist where user_id = '{user_id}' "
    print(query)
    mycursor.execute(query)
    data2 = mycursor.fetchone()
    count = int(data2[0])
    requestCount = int(data2[1])

    query2 = f"update psychologist set session_count = {count} +1 ,TotalRequestsRecieved= {requestCount} +1  where user_id='{user_id}'"
    print("here", query2)
    mycursor.execute(query2)

    g.db.commit()
    # obj.commit()
    # disconnect(connection_pool, obj, mycursor)
    return count


def getPsychologistByDescription(description):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f'''select p.id,p.name,p.profile_image,p.is_busy,p.firebase_id,p.firebase_name,p.firebase_email,p.firebase_password,p.uuid,
      p.user_id, p.description,p.session_count,p.rating,
               p.yrs_of_exp,p.education,p.short_desc,p.status,order_,p.created_at
               ,p.updated_at,p.gender,p.age,p.interests,p.languages,p.`online` , u.contact,u.is_call,u.is_chat,p.delta,p.lastSeen from psychologist p left join user u on p.user_id = u.id where (p.description rlike '{description}' or p.short_desc rlike '{description}' or p.interests rlike '{description}' or p.name rlike '{description}') '''
    mycursor.execute(query)
    psyData = mycursor.fetchall()

    # disconnect(connection_pool, obj, mycursor)

    psychologistList= list()

    for data in psyData:
        psy=psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                     data[11], data[12], data[13],data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24],data[25],data[26],data[27],data[28],data[29])

        psychologistList.append(psy.__dict__)

    return psychologistList

def psyListForSearchPage():
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)
    mycursor = g.cursor
    query = f'''select p.id,p.name,p.profile_image,p.is_busy,p.firebase_id,p.firebase_name,p.firebase_email,p.firebase_password,p.uuid,
         p.user_id, p.description,p.session_count,p.rating,
                  p.yrs_of_exp,p.education,p.short_desc,p.status,order_,p.created_at
                  ,p.updated_at,p.gender,p.age,p.interests,p.languages,p.`online` , u.contact,u.is_call,u.is_chat,p.lastSeen from psychologist p left join user u on p.user_id = u.id where p.enable ='1' order by p.`online` desc , p.is_busy limit 4'''
    mycursor.execute(query)
    psyData = mycursor.fetchall()

    # disconnect(connection_pool, obj, mycursor)

    psychologistList = list()

    for data in psyData:
        psy = psychologist.psychologist(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],
                                        data[9], data[10],
                                        data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18],
                                        data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26],
                                        data[27],data[29])

        psychologistList.append(psy.__dict__)

    return psychologistList
