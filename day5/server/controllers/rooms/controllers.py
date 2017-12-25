from flask import Blueprint, abort, request, json, Response

rooms = Blueprint('rooms', __name__)

# 방(센서 노드) 목록 조회, 방 추가
@rooms.route('', methods=['GET', 'POST'])
def route_rooms():
    abort(501)

# 방 상세 정보 조회, 변경, 삭제
@rooms.route('/<int:room_id>', methods=['GET', 'PUT', 'DELETE'])
def route_room_id(room_id):
    abort(501)

# 방별 계측 정보 조회, 계측 정보 저장
@rooms.route('/<int:room_id>/measurements', methods=['GET', 'POST'])
def route_measurements1(room_id):
    abort(501)

# 방별 알람 리스트 조회
@rooms.route('/<int:room_id>/alarms', methods=['GET'])
def route_alarms(room_id):
    abort(501)

# 알람 해제
@rooms.route('/<int:room_id>/alarms/<int:alarm_id>', methods=['PUT'])
def route_alarm_id(room_id, alarm_id):
    abort(501)

# 보일러 상태 변경
@rooms.route('/<int:room_id>/boiler', methods=['PUT'])
def route_boiler(room_id):
    abort(501)

# 제습기 상태 변경
@rooms.route('/<int:room_id>/humidifier ', methods=['PUT'])
def route_humidifier(room_id):
    abort(501)
