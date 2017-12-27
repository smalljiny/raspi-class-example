# coding=utf-8
import jwt
import datetime

SECRET = 'raspi-class-session'

def encode(uid):
    return jwt.encode({
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'uid': uid}, SECRET, algorithm='HS256')

def decode(encded):
    return jwt.decode(encded, SECRET, algorithm=['HS256'])
