# coding=utf-8
from flask import json, Response

# 결과 코드
RESULT_OK = 0

INVALID_STATUS = 1

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

def invalid_status():
    return error(400, INVALID_STATUS, 'Invalid Status')
