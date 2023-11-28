import tracking.trackingDao as trackingDao
from datetime import date, timedelta,datetime


def getDataForMarketingDashBoard():
    lastUpdatedDate= trackingDao.gettingLastMrktDateUpdate()
    getDailySpend =trackingDao.gettingDailySpend()

    todaysDate = date.today()

    current_date = (datetime.strptime(lastUpdatedDate, "%Y-%m-%d") + timedelta(days=1)).date()
    while current_date <= todaysDate:
        print(current_date)
        dateinReqFormat=currentDateinyyyymmddFormat(current_date)
        updateMrktDataForGivenDate(dateinReqFormat,getDailySpend)
        current_date += timedelta(days=1)

    data= trackingDao.getDataForDashBoard()
    trackingDao.updateLateTrackingData(todaysDate)
    return data


def currentDateinyyyymmddFormat(current_date):
    date_object = datetime.strptime(str(current_date), "%Y-%m-%d")
    formatted_date = date_object.strftime("%Y-%m-%d")
    return formatted_date



def updateMrktDataForGivenDate(current_date,getDailySpend):
    noOfUsersAcquird =trackingDao.noOfUsersAcquiredInAGivenDay(current_date)
    noOfSessions = trackingDao.noOfSessionsByNewUsers(current_date)
    trackingDao.insertIntomarketingDashboard(current_date,getDailySpend,"-","-",noOfUsersAcquird,noOfSessions)
    return


def countActiveListnersCron():
    dataCount,dataNameList = trackingDao.getActiveListnersDetails()
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    trackingDao.updateActiveListnerData(dataCount,dataNameList,current_date,current_time)
    return


def activelistnerCountDashboard():
    data= trackingDao.getListnerCountPerHour()
    return data