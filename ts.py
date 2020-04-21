#!/usr/bin/env python3

TOKEN='my-token'
CHATID='my-chatid'

import requests
import urllib
import sys

def send_telegram(message):
    message = urllib.parse.quote(message) 
    url = "https://api.telegram.org/bot" + TOKEN + \
        "/sendMessage?chat_id=" + CHATID + \
        "&text=" + message

    response = requests.get(url)

if __name__ == "__main__":
    message = (str(sys.stdin.read()))
    if len(message) != 0 :
      send_telegram(message)

