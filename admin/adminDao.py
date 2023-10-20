from datetime import date

from db import connect, disconnect
def updateDataForAdminDashboard():
    connection_pool, obj = connect()
    mycursor = obj.cursor(buffered=True)

    query = f"select total_requestRecieved,total_requestMissed,total_requestCancelled,total_sessionCount from admindata  order by id desc limit 1"
    print(query)
    mycursor.execute(query)
    data = mycursor.fetchone()
    disconnect(connection_pool, obj, mycursor)
    total_requestRecieved_yesterday,total_requestMissed_yesterday,total_requestCancelled_yesterday,total_sessionCount_yesterday = data[0],data[1],data[2],data[3]

    query = f"select sum(session_count), sum(TotalRequestsRecieved), sum(missedRequests), sum(yesterDayActiveTime) from psychologist"
    print(query)
    mycursor.execute(query)
    data2 = mycursor.fetchone()

    total_session = int(data2[0])
    total_requestRecieved = int(data2[1])
    total_requestMissed = int(data2[2])
    today_activeTime =  round(round(int(data2[3]) /60)/60,2)
    total_requestCancelled= total_requestRecieved - total_session-total_requestMissed
    today_requestRecieved =total_requestRecieved- total_requestRecieved_yesterday
    today_requestMissed = total_requestMissed- total_requestMissed_yesterday
    today_requestCancelled= total_requestCancelled- total_requestCancelled_yesterday
    today_requestAccepted= total_session-total_sessionCount_yesterday
    tdate= date.today()

    query2 = f'''INSERT INTO admindata (today_Date, total_sessionCount, total_requestMissed, total_requestRecieved, total_requestCancelled, today_activeTime,today_requestRecieved,today_requestMissed,today_requestCancelled,today_requestAccepted)
VALUES ('{tdate}', {total_session}, {total_requestMissed}, {total_requestRecieved}, {total_requestCancelled}, {today_activeTime},{today_requestRecieved},{today_requestMissed},{today_requestCancelled},{today_requestAccepted})'''

    mycursor.execute(query2)
    obj.commit()
    disconnect(connection_pool, obj, mycursor)

    return


def fetchadminBoardData():
    connection_pool, obj = connect()
    mycursor = obj.cursor(buffered=True)

    query1 = "select today_Date,today_requestRecieved,today_requestMissed,today_requestAccepted,today_requestCancelled,today_activeTime,total_requestRecieved,total_requestMissed,total_requestCancelled,total_sessionCount,total_counsellingTime from admindata order by id desc"
    print(query1)
    mycursor.execute(query1)
    data = mycursor.fetchall()

    disconnect(connection_pool, obj, mycursor)

    return data