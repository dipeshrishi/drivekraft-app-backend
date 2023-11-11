from flask import g
import sessionEntity.sessionEntity as sessionEntity
from datetime import datetime

def sessionHistoryList(userId):


    mycursor = g.cursor
    query = f'''select t.id,t.userId,p.name,t.created_at,round((t.seconds_chatted)/60,0), p.profile_image from transaction t left join psychologist p on p.user_id = t.psychologist_id  where t.userId ={userId} order by id desc'''
    mycursor.execute(query)
    sessionList = mycursor.fetchall()

    sessionHistroyData= list()

    for session in sessionList:
        date_str= str(session[3])
        date_format = '%Y-%m-%d %H:%M:%S'
        date_obj = datetime.strptime(date_str, date_format)
        reqFormat = ' %I:%M:%p %d-%b'
        reqDateFormat=date_obj.strftime(reqFormat)
        ses=sessionEntity.sessionEntity(session[0],session[1],session[2],reqDateFormat,session[4], session[5])
        sessionHistroyData.append(ses.__dict__)


    return sessionHistroyData