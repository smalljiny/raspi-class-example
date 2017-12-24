import requests
import json

def send_request():
    # Request
    # GET http://127.0.0.1:5000

    try:
        response = requests.get(
            url = "http://127.0.0.1:5000",
            headers = {
                "Content-Type":"application/json; charset=utf-8"
            }
        )

        print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format( content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()
