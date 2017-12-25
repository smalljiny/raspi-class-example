from flask import json, Response

PYMYSQL_DUPLICATE_ERROR = 1062

def response(e):
    if e.args[0] == PYMYSQL_DUPLICATE_ERROR:
        data = {
            'code': 400,
            'debug': 'Duplicated user'
        }
        js = json.dumps(data)
        resp = Response(js, status=400, mimetype='application/json')
    else:
        data = {
            'code': 500,
            'debug': 'DB Error'
        }
        js = json.dumps(data)
        resp = Response(js, status=500, mimetype='application/json')

    return resp
