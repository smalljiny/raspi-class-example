import requests
import time
import jwt
from flask import request, json
from pymysql.err import IntegrityError

from models import db
from models import room_model
from encryption import session_token
from common.response import success
from common.response import db_error
from common.response import invalid_session
from common.response import session_exp
from common.response import invalid_param

SENSOR_URL = "http://{0:s}:5001/{1:s}"

def update_boiler(room_id):
    # 토큰의 uid와 입력된 uid가 일지하는지 검사한다.
    try:
        auth_token = request.headers['Authorization']
        decoded = session_token.decode(auth_token)
        if decoded == False:
            return invalid_session()
        elif decoded['exp'] < int(time.time()):
            return session_exp()
    except KeyError:
        return invalid_session()
    except jwt.exceptions.DecodeError:
        return invalid_session()

    connection = db.get_connection()

    try:
        ip = room_model.get_room_ip(room_id, connection)
        url = SENSOR_URL.format(ip, 'boiler')
        headers = {'content-type': 'application/json'}
        data = request.json
        payload = {
            "status": data["status"]
        }
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        if (response.status_code == 200 and data["status"] == 'ON'):
            print ('ON')
        else:
            print ('OFF')

    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    if (response.status_code == 200):
        return success('OK')
    elif (response.status_code == 400):
        return invalid_param()

def update_humidifier(room_id):
    # 토큰의 uid와 입력된 uid가 일지하는지 검사한다.
    try:
        auth_token = request.headers['Authorization']
        decoded = session_token.decode(auth_token)
        if decoded == False:
            return invalid_session()
        elif decoded['exp'] < int(time.time()):
            return session_exp()
    except KeyError:
        return invalid_session()
    except jwt.exceptions.DecodeError:
        return invalid_session()

    connection = db.get_connection()

    try:
        ip = room_model.get_room_ip(room_id, connection)
        url = SENSOR_URL.format(ip, 'humidifier')
        headers = {'content-type': 'application/json'}
        data = request.json
        payload = {
            "status": data["status"]
        }
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        if (response.status_code == 200 and data["status"] == 'ON'):
            print ('ON')
        else:
            print ('OFF')

    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    if (response.status_code == 200):
        return success('OK')
    elif (response.status_code == 400):
        return invalid_param()
