# coding=utf-8
import time
import jwt

from flask import Blueprint, abort, request, json, Response
from pymysql.err import IntegrityError

from models import db
from models import user_model
from models import session_model

from encryption import password
from encryption import session_token

from common.response import success
from common.response import db_error
from common.response import no_user
from common.response import invalid_password
from common.response import invalid_param
from common.response import invalid_session
from common.response import session_exp

sessions = Blueprint('sessions', __name__)

# 로그인, 자동 로그인, 로그아웃
@sessions.route('', methods=['POST', 'PUT', 'DELETE'])
def user_id():
        if request.method == 'POST':
            return create_session()
        elif request.method == 'PUT':
            return update_session()
        else:
            return delete_session()

def create_session():
    connection = db.get_connection()

    data = request.json
    email = data["email"]
    passwd = data["password"]

    # 사용자 패스워드 조회
    try:
        result = user_model.get_password(email, connection)

        if (result):
            if password.valid(result[1], passwd):
                token = session_token.encode(result[0])
                session_model.insert(token, connection)
                connection.commit()
                return success({'uid':result[0], 'token': token})
            else:
                return invalid_password()
    except IntegrityError as e:
        connection.rollback()
        return db_error.response(e)
    finally:
        connection.close()

    return no_user()

def update_session():
    # 토큰의 uid와 입력된 uid가 일지하는지 검사한다.
    try:
        auth_token = request.headers['Authorization']
        decoded = session_token.decode(auth_token)
        data = request.json
        uid = data['uid']
        if (decoded['uid'] != uid):
            return invalid_param('Invalid User')
        elif decoded['exp'] < int(time.time()):
            return session_exp()
    except KeyError:
        return invalid_session()
    except jwt.exceptions.DecodeError:
        return invalid_session()

    # 새로운 토근을 발급한다
    connection = db.get_connection()
    try:
        new_token = session_token.encode(uid)
        session_model.update(auth_token, new_token, connection)
        connection.commit()
    except IntegrityError as e:
        connection.rollback()
        return db_error.response(e)
    finally:
        connection.close()

    return success({'uid':uid, 'token': new_token})

def delete_session():
    # 토큰의 uid와 입력된 uid가 일지하는지 검사한다.
    try:
        auth_token = request.headers['Authorization']
        decoded = session_token.decode(auth_token)
        uid = request.args.get('uid')
        if (decoded['uid'] != uid):
            return invalid_param('Invalid User')
        elif decoded['exp'] < int(time.time()):
            return session_exp()
    except KeyError:
        return invalid_session()

    # 세션 레코드를 삭제한다.
    connection = db.get_connection()
    try:
        result = session_model.delete(auth_token, connection)
        connection.commit()
    except IntegrityError as e:
        connection.rollback()
        return db_error.response(e)
    finally:
        connection.close()

    return success('OK')
