from flask import Blueprint, abort, request, json, Response
import RPi.GPIO as GPIO
import time

from common.response import success
from common.response import invalid_status

boiler = Blueprint('boiler', __name__)

# System 전체의 알람 리스트를 반환한다.
@boiler.route('', methods=['PUT'])
def route_boiler():
    data = request.json
    status = data["status"]

    if (status == 'ON'):
        GPIO.output(4, GPIO.HIGH)
        return success('ON')
    elif (status == 'OFF'):
        GPIO.output(4, GPIO.LOW)
        return success('OFF')

    return invalid_status()
