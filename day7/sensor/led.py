import RPi.GPIO as GPIO
import time

def ctrlLed():
    # GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    print("Setup LED pins as outputs")

    GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)

    GPIO.output(4, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)

    time.sleep(1)

    GPIO.output(4, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)

    input('press enter to exit program')

    GPIO.cleanup()

ctrlLed()
