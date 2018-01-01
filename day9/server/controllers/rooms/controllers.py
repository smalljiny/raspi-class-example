# coding=utf-8
from flask import Blueprint, abort, request, json, Response

from controllers.rooms.func_rooms import get_rooms
from controllers.rooms.func_rooms import create_new_room
from controllers.rooms.func_measurements import report_measurement
from controllers.rooms.func_measurements import get_measurements
from controllers.rooms.func_sensor import update_boiler
from controllers.rooms.func_sensor import update_humidifier

rooms = Blueprint('rooms', __name__)

# 방(센서 노드) 목록 조회, 방 추가
@rooms.route('', methods=['GET', 'POST'])
def route_rooms():
    if request.method == 'POST':
        return create_new_room()
    else:
        return get_rooms()


# 방 상세 정보 조회, 변경, 삭제
@rooms.route('/<int:room_id>', methods=['GET', 'PUT', 'DELETE'])
def route_room_id(room_id):
    abort(501)

# 방별 계측 정보 조회, 계측 정보 저장
@rooms.route('/<int:room_id>/measurements', methods=['GET', 'POST'])
def route_measurements1(room_id):
    if request.method == 'POST':
        return report_measurement(room_id)
    else:
        return get_measurements(room_id)

# 보일러 상태 변경
@rooms.route('/<int:room_id>/boiler', methods=['PUT'])
def route_boiler(room_id):
    return update_boiler(room_id)

# 제습기 상태 변경
@rooms.route('/<int:room_id>/humidifier', methods=['PUT'])
def route_humidifier(room_id):
    return update_humidifier(room_id)
