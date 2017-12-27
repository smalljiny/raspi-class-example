from flask import Flask, json, jsonify, Response

from controllers.boiler.controllers import boiler
from controllers.humidifier.controllers import humidifier

app = Flask(__name__)
app.debug = True

# 에러 핸들러 등록
@app.errorhandler(404)
def page_not_found(error):
    data = {
        'code'  : 404,
        'debug' : 'Not Found'
    }
    js = json.dumps(data)
    resp = Response(js, status=404, mimetype='application/json')
    return resp

@app.errorhandler(405)
def page_not_found(error):
    data = {
        'code'  : 405,
        'debug' : 'Not Allowed'
    }
    js = json.dumps(data)
    resp = Response(js, status=405, mimetype='application/json')
    return resp

@app.errorhandler(501)
def page_not_found(error):
    data = {
        'code'  : 501,
        'debug' : 'Not Implemented'
    }
    js = json.dumps(data)
    resp = Response(js, status=501, mimetype='application/json')
    return resp

# blueprint 등록
app.register_blueprint(boiler, url_prefix='/boiler')
app.register_blueprint(humidifier, url_prefix='/humidifier')
