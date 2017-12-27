import sys
import time
import datetime
import threading

import Adafruit_DHT
import RPi.GPIO as GPIO

DTH_SENSOR = 11
DHT_PIN = 27

LED_ALARM_PIN = 4

class MeasureThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            now = int(time.time())
            if (now % 5) != 0:
                continue
            print(now)
            humidity, temperature = Adafruit_DHT.read(DTH_SENSOR, DHT_PIN)
            if humidity is not None and temperature is not None:
                timestamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
                print('[{0:s}]  Temp={1:0.1f}*  Humidity={2:0.1f}%'.format(timestamp, temperature, humidity))
                if (temperature > 25.0):
                    GPIO.output(4, GPIO.HIGH)
                else:
                    GPIO.output(4, GPIO.LOW)

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

    # while True:
    #     cmd = input()

    # while(True):
        # humidity, temperature = Adafruit_DHT.read(DTH_SENSOR, DHT_PIN)
        #
        # if humidity is not None and temperature is not None:
        #     now = time.time()
        #     timestamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
        #     print('[{0:s}]  Temp={1:0.1f}*  Humidity={2:0.1f}%'.format(timestamp, temperature, humidity))
        #     if (temperature > 25.0):
        #         GPIO.output(4, GPIO.HIGH)
        #     else:
        #         GPIO.output(4, GPIO.LOW)
        #     time.sleep(5)
        # else:
        #     print('Failed to get reading. Try again!')
        #     GPIO.cleanup()
        #     sys.exit(1)

main()
