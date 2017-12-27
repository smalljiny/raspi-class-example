# coding=utf-8
from flask import json, Response

# 결과 코드
RESULT_OK = 0
ERR_NO_USER = 1
ERR_INVALID_PASSWORD = 2
ERR_INVALID_PARAMS = 3
ERR_INVALID_SESSION = 4

ERR_DB = 1000
ERR_DB_DUPLICATE = 1001

# MySQL 에러 코드
PYMYSQL_DUPLICATE_ERROR = 1062

# 응답 - 성공
def success(body):
    data = {
        'code': RESULT_OK,
        'body': body
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

def error(status_code, code, debug_message):
    data = {
        'code': code,
        'debug': debug_message
    }

    js = json.dumps(data)
    resp = Response(js, status=status_code, mimetype='application/json')
    return resp

def db_error(e):
    if e.args[0] == PYMYSQL_DUPLICATE_ERROR:
        return error(400, ERR_DB_DUPLICATE, 'Duplicated')
    else:
        return error(500, ERR_DB, 'DB Error')

# 응답 - 패스워드 오류
def invalid_password():
    return error(400, ERR_INVALID_PASSWORD, 'Invalid password')

def no_user():
    return error(400, ERR_NO_USER, 'No user')

def invalid_param(message='Invalid params'):
    return error(400, ERR_INVALID_PARAMS, message)

def invalid_session():
    return error(400, ERR_INVALID_SESSION, 'Invalid session')

def session_exp():
    return error(400, ERR_INVALID_SESSION, 'Session expired')
