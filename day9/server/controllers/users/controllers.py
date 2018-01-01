# coding=utf-8
import time
import jwt
from flask import Blueprint, abort, request, json, Response
from pymysql.err import IntegrityError

from models import db
from models import user_model
from encryption import session_token
from common.response import success
from common.response import db_error
from common.response import invalid_session
from common.response import session_exp

users = Blueprint('users', __name__)

# 사용자 리스트 조회, 사용자 추가
@users.route('', methods=['GET', 'POST'])
def route_user():
    if request.method == 'POST':
        return create_new_user()
    else:
        return get_users()

# 신규 사용자 가입
def create_new_user():
    data = request.json
    email = data["email"]
    pwd = data["password"]
    confirm = data["confirm"]

    if (pwd != confirm):
        return invalid_password()

    connection = db.get_connection()
    try:
        user_model.insert(email, pwd, connection)
        connection.commit()
    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    return success('OK')

# 사용자 리스트
def get_users():
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
        user_list = user_model.get_users(connection)
    except IntegrityError as e:
        return db_error(e)
    finally:
        connection.close()

    return success(user_list)
