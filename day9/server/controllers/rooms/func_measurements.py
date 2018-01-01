import time
import jwt
from flask import request, json
from pymysql.err import IntegrityError

from models import db
from models import measurement_model
from models import room_model
from encryption import session_token
from encryption import access_key
from common.response import success
from common.response import invalid_session
from common.response import invalid_param
from common.response import session_exp

def report_measurement(room_id):
    # 토큰의 uid와 입력된 uid가 일치하는지 검사한다.
    try:
        access_token = request.headers['Authorization']
    except KeyError:
        return invalid_session()

    connection = db.get_connection()
    try:
        room_info = room_model.get_room(room_id, connection)

        # if access_key.valid(access_token, room_info['ip'], room_info['id']) == False:
        #     return invalid_session()

        data = request.json
        datetime = data["datetime"]
        temperature = data["temperature"]
        humidity = data["humidity"]

        measurement_model.insert((room_id, datetime, temperature, humidity), connection)
        connection.commit()
    except IntegrityError as e:
        connection.rollback()
        return db_error(e)
    except KeyError:
        connection.rollback()
        return invalid_param()
    finally:
        connection.close()

    return success('OK')

def get_measurements(room_id):
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

    data = request.json

    try:
        start = request.args.get('start')
    except KeyError:
        start = int(time.time()) - (60 * 60 * 24)

    try:
        end = request.args.get('end')
    except KeyError:
        end = start + (60 * 60 * 24)

    connection = db.get_connection()
    try:
        user_list = measurement_model.get_measurements(room_id, start, end, connection)
    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    return success(user_list)
