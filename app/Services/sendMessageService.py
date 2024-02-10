import requests
import json
import time
import logging
from ..Configurations.chatApi import url as apiUrl,api_instance,api_token
import logging

def sendMessage(phonenumber, msg):
    logging.info("inside send message")
    url = apiUrl.format(api_instance, api_token)

    payload = json.dumps({
        "body": msg,
        "phone": phonenumber
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    strResult = json.loads(response.text)
    logging.info(f"Chat Api response for {phonenumber} is {strResult} ")
    if response.status_code==200:
        logging.info('Message Send to {} and value is {}'.format(phonenumber, msg))
    else:
        logging.error("API resposne : {}".format(response.text))

    time.sleep(1)

    return response.text