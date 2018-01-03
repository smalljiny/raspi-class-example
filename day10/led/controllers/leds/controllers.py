from flask import Blueprint, Response, json, request
#, jsonify,
import gpio

HTTP_STATUS_OK = 200
HTTP_INVALID_REQUEST = 400

SUCCESS = 0
INVALID_LED_ID = 1
INVALID_LED_STATUS = 2

leds = Blueprint('leds', __name__)

def response(result):
    resp = {
        "code": SUCCESS,
        "body": result
    }
    return Response(
        json.dumps(resp),
        status = HTTP_STATUS_OK,
        mimetype = 'application/json'
    )

def error(http_status, code, debug):
    resp = {
        "code": code,
        "debug": debug
    }
    return Response(
        json.dumps(resp),
        status = http_status,
        mimetype = 'application/json'
    )

@leds.route('', methods=['GET'])
def get_led_status():
    result = gpio.get_led_status()

    return response(result)

@leds.route('/<int:led_id>', methods=['PUT'])
def set_led_status(led_id):
    if (led_id < 0 or led_id > 1):
        return error(HTTP_INVALID_REQUEST, INVALID_LED_ID, 'Invalid LED ID!')

    data = request.json
    status = data["status"]

    if (status < 0 or status > 1):
        return error(HTTP_INVALID_REQUEST, INVALID_LED_STATUS, 'Invalid LED status!')

    result = gpio.set_led_status(led_id, status)

    return response(result)
