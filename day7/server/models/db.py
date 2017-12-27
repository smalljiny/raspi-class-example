from pymysql import connect

# DB 연결
def get_connection():
    return connect(host='192.168.25.60',
            user='pi',
            password='Wkddmsgk0613!',
            db='raspi',
            charset='utf8')
