import sys
import time
import datetime
import threading
import json
import requests
import Adafruit_DHT
import RPi.GPIO as GPIO

DTH_SENSOR = 11
DHT_PIN = 27

LED_ALARM_PIN = 4

SERVER_URL = 'http://192.168.25.61:5000/rooms/{0:d}/measurements'
ROOM_ID = 1
ACCESS_KEY = '1gypuuHnafHMqJbR4kDMgD4DcxA='

def report_to_server(timestamp, temperature, humidity):
    url = SERVER_URL.format(ROOM_ID)
    headers = {
        'authorization': ACCESS_KEY,
        'content-type': 'application/json'
    }
    payload = {
        "datetime": timestamp,
        "temperature": temperature,
        "humidity": humidity
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

class MeasureThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            now = int(time.time())
            if (now % 5) != 0:
                continue
            humidity, temperature = Adafruit_DHT.read(DTH_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                timestamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
                print('[{0:s}]  Temp={1:0.1f}*  Humidity={2:0.1f}%'.format(timestamp, temperature, humidity))
                report_to_server(now, temperature, humidity)

            time.sleep(1000.0 / 1000.0)

def init():
    GPIO.cleanup(LED_ALARM_PIN)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

def main():
    init()

    thread = MeasureThread()
    thread.start()
    thread.join()

main()
