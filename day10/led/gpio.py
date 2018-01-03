import RPi.GPIO as GPIO

LED_0 = 17
LED_1 = 27
LED = (17, 27)
ON = GPIO.HIGH
OFF = GPIO.LOW

def init():
    print("GPIO init!")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED[0], GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(LED[1], GPIO.OUT, initial=GPIO.LOW)
    INIT = True

def clean():
    print("GPIO clean up!")
    GPIO.cleanup()

def get_led_status():
    return {
        "led0": GPIO.input(LED[0]),
        "led1": GPIO.input(LED[1]),
    }

def set_led_status(led, status):
    GPIO.output(LED[led], status)
    return {
        "led0": GPIO.input(LED[0]),
        "led1": GPIO.input(LED[1]),
    }
