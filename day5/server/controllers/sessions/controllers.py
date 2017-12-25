from flask import Blueprint, abort, request, json, Response

sessions = Blueprint('sessions', __name__)

# 로그인, 자동 로그인, 로그아웃
@sessions.route('', methods=['POST', 'PUT', 'DELETE'])
def user_id():
    abort(501)
