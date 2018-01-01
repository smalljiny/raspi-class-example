import hashlib
import hmac
import base64

def get(password):
    key = bytes('raspi-class-password', 'UTF-8')
    message = bytes(password, 'UTF-8')
    digester = hmac.new(key, message, hashlib.sha1)
    signature = base64.urlsafe_b64encode(digester.digest())

    return str(signature, 'UTF-8')

def valid(token, password):
    return token == get(password)
