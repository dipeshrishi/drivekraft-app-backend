import tracking.trackingDao as trackingDao
from datetime import date, timedelta,datetime


def getDataForMarketingDashBoard():
    lastUpdatedDate= trackingDao.gettingLastMrktDateUpdate()
    getDailySpend =trackingDao.gettingDailySpend()

    todaysDate = date.today()

    current_date = (datetime.strptime(lastUpdatedDate, "%Y-%m-%d") + timedelta(days=1)).date()
    while current_date < todaysDate:
        print(current_date)
        current_date += timedelta(days=1)
        dateinReqFormat=currentDateinyyyymmddFormat(current_date)
        updateMrktDataForGivenDate(dateinReqFormat,getDailySpend)

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
