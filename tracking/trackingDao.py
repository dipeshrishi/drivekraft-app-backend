from flask import  g


def gettingLastMrktDateUpdate():

    mycursor = g.cursor
    query = f"select value from environmentProperties where name ='lastLastMarketingDateUpdatemail' "
    mycursor.execute(query)
    data = mycursor.fetchone()
    return data[0]


def gettingDailySpend():

    mycursor = g.cursor
    query = f"select value from environmentProperties where name ='gettingDailySpend'"
    mycursor.execute(query)
    data = mycursor.fetchone()
    return data[0]

def noOfUsersAcquiredInAGivenDay(current_date):
    # connection_pool,obj = connect()
    # mycursor = obj.cursor(buffered=True)

    mycursor = g.cursor
    query = f"select count(*) from user where created rlike '{current_date}' "
    mycursor.execute(query)
    data = mycursor.fetchone()
    # disconnect(connection_pool, obj, mycursor)
    if data==None:
        return 0
    return data[0]


def noOfSessionsByNewUsers(current_date):

    mycursor = g.cursor
    query = f"select group_concat(id) from user where created rlike '{current_date}' "
    data = mycursor.fetchone()
    if data==None:
        return 0

    userIdConcat = data[0]
    query = f" select count(*) from sessionRequest where created_at rlike '{current_date}' and status ='1' and customer_id in ({userIdConcat})"
    mycursor.execute(query)
    data = mycursor.fetchone()
    if data==None:
        return 0
    dataCount= data[0];
    return dataCount


def insertIntomarketingDashboard(current_date,getDailySpend,websiteVisits,dailyAppDownloads,noOfUsersAcquird,noOfSessions):
    mycursor = g.cursor
    sql = f"Insert into marketingDashboard values(null,'{current_date}','{getDailySpend}','{websiteVisits}','{dailyAppDownloads}','{noOfUsersAcquird}','{noOfSessions}')"
    mycursor.execute(sql)
    g.db.commit()
    return


def getDataForDashBoard():
    mycursor = g.cursor
    query = f"select * from marketingDashboard order by id desc "
    mycursor.execute(query)
    data = mycursor.fetchall()

    return data

def updateLateTrackingData(todaysDate):
    mycursor = g.cursor
    sql = f"Update environmentProperties set  value ='{todaysDate}'  where name ='lastLastMarketingDateUpdatemail' "
    mycursor.execute(sql)
    g.db.commit()

    return

def getActiveListnersDetails():
    mycursor = g.cursor
    query = f"select count(*) from psychologist where online =1"
    mycursor.execute(query)
    dataCount = mycursor.fetchone()

    query = f"select group_concat(name) from psychologist where online =1"
    mycursor.execute(query)
    dataNameList = mycursor.fetchone()

    return dataCount[0],dataNameList[0]


def updateActiveListnerData(dataCount,dataNameList,current_date,current_time):
    mycursor = g.cursor
    sql = f"Insert into activeListnerCount values(null,'{current_date}','{current_time}','{dataCount}','{dataNameList}')"
    mycursor.execute(sql)
    g.db.commit()
    return

def getListnerCountPerHour():
    mycursor = g.cursor
    query = f"select dateValue,currentTime,countOfActiveListner,nameList from activeListnerCount order by id desc"
    mycursor.execute(query)
    dataCount = mycursor.fetchall()

    return dataCount