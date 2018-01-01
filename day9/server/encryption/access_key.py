import hashlib
import hmac
import base64

def get(ip, id):
    key = bytes('raspi-class-rooms', 'UTF-8')
    message = bytes("{0:s}{1:d}%".format(ip, id), 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature = base64.urlsafe_b64encode(digester.digest())

    return str(signature, 'UTF-8')

def valid(token, ip, id):
    return token == get(ip, id)
