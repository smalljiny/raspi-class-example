# coding=utf-8

from flask import Flask, json, jsonify, Response

from controllers.users.controllers import users
from controllers.rooms.controllers import rooms
from controllers.alarms.controllers import alarms
from controllers.sessions.controllers import sessions

app = Flask(__name__, static_folder='../views', static_url_path='/views')
app.debug = True

# views/index.html
@app.route('/views/')
def index():
    return app.send_static_file('index.html')

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
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(rooms, url_prefix='/rooms')
app.register_blueprint(alarms, url_prefix='/alarms')
app.register_blueprint(sessions, url_prefix='/sessions')
