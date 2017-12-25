from flask import Blueprint, abort, request, json, Response
import pymysql.cursors
from pymysql.err import IntegrityError
from encryption import password
from error import db_error

users = Blueprint('users', __name__)

# 사용자 리스트 조회, 사용자 추가
@users.route('', methods=['GET', 'POST'])
def route_user():
    if request.method == 'POST':
        return create_new_user()
    else:
        return get_users()
# DB 연결
def get_db_connection():
    conn = pymysql.connect(host='192.168.25.60',
            user='pi',
            password='Wkddmsgk0613!',
            db='raspi',
            charset='utf8')
    return conn;

# 응답 - 패스워드 오류
def invalid_password():
    data = {
        'code': 400,
        'debug': 'Invalid password'
    }
    js = json.dumps(data)
    resp = Response(js, status=400, mimetype='application/json')
    return resp

# 응답 - 성공
def send_response(body):
    data = {
        'code': 200,
        'body': body
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

# 신규 사용자 가입
def create_new_user():
    data = request.json
    email = data["email"]
    passwd = data["password"]
    confirm = data["confirm"]

    if (passwd != confirm):
        return invalid_password()

    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO `users` (`email`, `password`) VALUES (%s, %s);'
            cursor.execute(sql, (email, password.get(passwd)))
        conn.commit()
    except IntegrityError as e:
        return db_error.response(e)
    finally:
        conn.close()

    return send_response('OK')

# 사용자 리스트
def get_users():
    conn = get_db_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT `email` FROM users;'
            cursor.execute(sql)
            db_result = cursor.fetchall()
    except IntegrityError as e:
        return db_error.response(e)
    finally:
        conn.close()

    result = [];
    for row in db_result:
        result.append({'email':row[0]})

    return send_response(result)
