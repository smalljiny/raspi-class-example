from pymysql import connect

# DB 연결
def get_connection():
    return connect(host='192.168.25.61',
            user='pi',
            password='1qazxsw2!',
            db='raspi',
            charset='utf8')
