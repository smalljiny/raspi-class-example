# coding=utf-8
from flask import Blueprint, abort, request, json, Response

alarms = Blueprint('alarms', __name__)


# System 전체의 알람 리스트를 반환한다.
@alarms.route('', methods=['GET'])
def route_alarms():
    abort(501)

# System 선택된 알람을 해제한다.
@alarms.route('/<int:alarm_id>', methods=['PUT'])
def route_alarm_id(alarm_id):
    abort(501)
