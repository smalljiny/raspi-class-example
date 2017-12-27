from flask import Blueprint, abort, request, json, Response
import RPi.GPIO as GPIO
import time

from common.response import success
from common.response import invalid_status

humidifier = Blueprint('humidifier', __name__)

# 로그인, 자동 로그인, 로그아웃
@humidifier.route('', methods=['PUT'])
def user_humidifier():
    data = request.json
    status = data["status"]

    if (status == 'ON'):
        GPIO.output(17, GPIO.HIGH)
        return success('ON')
    elif (status == 'OFF'):
        GPIO.output(17, GPIO.LOW)
        return success('OFF')

    return invalid_status()
