# coding=utf-8
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

def get_rooms():
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
        room_list = room_model.get_rooms(connection)
    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    return success(room_list)

def create_new_room():
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
        return invalid_sessio

    params = get_room_info_from_request()

    connection = db.get_connection()
    try:
        room_id = room_model.create_room(params, connection)
        room_model.update_ip(room_id, params[1], connection)
        connection.commit()
        room_info = room_model.get_room(room_id, connection)
    except IntegrityError as e:
        connection.rollback()
        return db_error(e)
    finally:
        connection.close()

    return success(room_info)

def get_room_info_from_request():
    data = request.json
    try:
        name = data["name"]
        ip = data["ip"]
    except KeyError:
        return invalid_param()

    try:
        max_temperature = data["max_temperature"]
    except KeyError:
        max_temperature = 26.00

    try:
        min_temperature = data["min_temperature"]
    except KeyError:
        max_temperature = 28.00

    try:
        max_humidity = data["max_humidity"]
    except KeyError:
        max_humidity = 60.00

    try:
        min_humidity = data["min_humidity"]
    except KeyError:
        min_humidity = 30.00

    return (name, ip, max_temperature, min_temperature, max_humidity, min_humidity)
