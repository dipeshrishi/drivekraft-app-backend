url="https://api.chat-api.com/{}/sendMessage?token={}"
url_for_templates="https://api.chat-api.com/{}/sendTemplate?token={}"
api_token = "bfllgpii7xqb42zq"
api_instance = "instance294124"
nameSpace="73376c2d_a5cc_4aea_a5f8_fcde0de1be47"


def getTemplateName(name):
    switcher = {
        "dailyMessageNortification": "daily_nortification_msg",
        "sendToDNP": "sendtodnp",
        "sessionCompletion": "session_completed_5",
        "feedback": "feedback",
        "nextSessionBookingText": "next_session_booking",
        "nextSessionBookingText_2": "next_session_booking_5",
        "opeiningMsg": "first_opeining_msg",
        "SessionBookingWithLink": "session_booking_link",
        "otp": "otp"
    }
    return switcher.get(name, "nothing")
